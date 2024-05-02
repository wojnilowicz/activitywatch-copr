%bcond_without check

%global commit 124192b2024c492dafde5aa6bb62030c201cea35
%global short_commit %(c=%{commit}; echo ${c:0:7})

Name:           aw-server-rust
Version:        0.12.3.b16^20240507.%{short_commit}
Release:        %autorelease
Summary:        A re-implementation of aw-server in Rust

License:        MPL-2.0

URL:            https://github.com/ActivityWatch/%{name}
Source:         %{url}/archive/%{commit}/%{name}-%{short_commit}.tar.gz

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  systemd-rpm-macros
BuildRequires:  help2man
BuildRequires:  nodejs-aw-webui

%description
%{summary}

%prep
%autosetup -n %{name}-%{commit} -p1
# drop unused, benchmark-only criterion dev-dependency to speed up builds
find -name "*.toml" | xargs sed -ri '/^[[:blank:]]*criterion\b/d'

# switch to SQLite available in Fedora
sed -ri 's/rusqlite = \{ version = "0.30", features = \["chrono", "serde_json", "bundled"\]  \}/rusqlite = \{ version = "0.31", features = \["chrono", "serde_json"\]  \}/' aw-datastore/Cargo.toml

# mimic what "make set-version" would do
sed -ri 's/version = "0.12.1"/version = "0.12.3-b16.dev+%{short_commit}"/' aw-server/Cargo.toml

# remove Android dependencies
sed -ri '/target_os="android"/,+4d' aw-server/Cargo.toml

# remove unused depndency
sed -ri '/^[[:blank:]]*multipart\b/d' aw-server/Cargo.toml

# jemallocator will not be packaged for Fedora, so remove it
sed -ri '/target_os="linux", target_arch="x86"/,+1d' aw-server/Cargo.toml
sed -ri '/target_os = "linux", target_arch = "x86"/,/static ALLOC: jemallocator::Jemalloc = jemallocator::Jemalloc;/d' aw-server/src/main.rs

%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
# no UI built without this
export AW_WEBUI_DIR="%{_datadir}/aw-webui/dist/"
%cargo_build
%cargo_license
%cargo_license_summary

%install
install -Dm 0755 %{_builddir}/%{name}-%{commit}/target/rpm/{aw-server,aw-sync} -t %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
help2man %{buildroot}%{_bindir}/aw-server -o %{buildroot}%{_mandir}/man1/aw-server.1
help2man %{buildroot}%{_bindir}/aw-sync -o %{buildroot}%{_mandir}/man1/aw-sync.1
install -Dm 0644 aw-server.service -t %{buildroot}%{_userunitdir}

%if %{with check}
%check
# tests report an error with EmbeddedAssets without this
export AW_WEBUI_DIR="%{_datadir}/aw-webui/dist/"
%cargo_test
%endif

%package     -n aw-sync
Summary:        %{summary}
Requires:       %{name} = %{version}-%{release}

%description -n aw-sync
%{summary}

%files       -n aw-sync
%doc README.md
%license LICENSE
%{_mandir}/man1/aw-sync.1*
%{_bindir}/aw-sync

%files
%doc README.md
%license LICENSE
%{_mandir}/man1/aw-server.1*
%{_bindir}/aw-server
%{_userunitdir}/aw-server.service

%changelog
%autochangelog
