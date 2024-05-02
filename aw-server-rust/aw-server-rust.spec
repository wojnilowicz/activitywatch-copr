%bcond_without check

%global commit c056e50646b45070c330de8a6dbd14042b3455e4
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           aw-server-rust
Version:        %{shortcommit}
Release:        %autorelease
Summary:        A reimplementation of aw-server in Rust.

License:        MPL-2.0

URL:            https://github.com/ActivityWatch/%{name}
Source:         %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch:          aw-server-rust-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  systemd-rpm-macros
BuildRequires:  npm(aw-webui)

%description
%{summary}

%prep
%autosetup -n %{name}-%{commit} -p1
# * drop unused, benchmark-only criterion dev-dependency to speed up builds
find -name "*.toml" | xargs sed -r -i '/^[[:blank:]]*criterion\b/d'

# * switch to sqlite available in Fedora
sed -ri 's/rusqlite = \{ version = "0.30", features = \["chrono", "serde_json", "bundled"\]  \}/rusqlite = \{ version = "0.31", features = \["chrono", "serde_json"\]  \}/' aw-datastore/Cargo.toml

# * mimic what "make set-version" would do
sed -ri 's/version = "0.12.1"/version = "0.12.3-b16.dev+%{shortcommit}"/' aw-server/Cargo.toml

%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
# * no UI built without this
export AW_WEBUI_DIR="%{nodejs_sitelib}/aw-webui/dist/"
%cargo_build

%install
install -Dm 0755 %{_builddir}/%{name}-%{commit}/target/rpm/aw-server -t %{buildroot}%{_bindir}
install -Dm 0755 %{_builddir}/%{name}-%{commit}/target/rpm/aw-sync -t %{buildroot}%{_bindir}
install -Dm 0644 aw-server.service -t %{buildroot}%{_userunitdir}

%if %{with check}
%check
# * tests report error with EmbeddedAssets without this
export AW_WEBUI_DIR="%{nodejs_sitelib}/aw-webui/dist/"
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
%{_bindir}/aw-sync

%files
%doc README.md
%license LICENSE
%{_bindir}/aw-server
%config %{_userunitdir}/aw-server.service

%changelog
%autochangelog
