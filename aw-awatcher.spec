# * no tests available
%bcond_with check

%global commit0 be59315e8a7c7be3bbeafc60b68a06d1507b2a2a
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global url1 https://github.com/ActivityWatch/aw-server-rust
%global commit1 448312d410980d4a92a0fb4d4bb3fa3494cf6c89
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

Name:           aw-awatcher
Version:        %{shortcommit0}
Release:        %autorelease
Summary:        A window activity and idle watcher.

License:        MPL-2.0
URL:            https://github.com/2e3s/awatcher
Source0:        %{url}/archive/%{commit0}/awatcher-%{version}.tar.gz
Source1:        %{url1}/archive/%{commit1}/aw-server-rust-%{shortcommit1}.tar.gz

Requires:       aw-server-rust
BuildRequires:  cargo-rpm-macros >= 24

%description
%{summary}

%prep
%autosetup -n awatcher-%{commit0}
tar -xf %{SOURCE1} --strip-components 1 aw-server-rust-%{commit1}/{aw-client-rust,aw-models}

# don't download anything from the internet
sed -ri 's|git = "https://github.com/ActivityWatch/aw-server-rust", rev = "448312d"|path = "../aw-client-rust"|' watchers/Cargo.toml

# works with 0.24.7 too
sed -ri 's/image = \{ version = "0.25.1" \}/image = \{ version = "0.24.7" \}/' Cargo.toml

# aw-client-rust is just a dependency, so it doesn't need its dev dependencies
sed -ri '/dev-dependencies/,+4d' aw-client-rust/Cargo.toml
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install
# prefix with aw- in order to be detected a watcher in aw-qt
mv %{buildroot}%{_bindir}/{awatcher,%{name}}

%if %{with check}
%check
%cargo_test
%endif

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog
