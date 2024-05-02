# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate slice-deque

Name:           rust-slice-deque0.2
Version:        0.2.4
Release:        %autorelease
Summary:        Double-ended queue that Deref's into a slice

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/slice-deque
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          slice-deque-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A double-ended queue that Deref's into a slice.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/license-apache.md
%license %{crate_instdir}/license-mit.md
%license %{crate_instdir}/license.md
%doc %{crate_instdir}/readme.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unix_sysv-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unix_sysv-devel %{_description}

This package contains library source intended for building other packages which
use the "unix_sysv" feature of the "%{crate}" crate.

%files       -n %{name}+unix_sysv-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+use_std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+use_std-devel %{_description}

This package contains library source intended for building other packages which
use the "use_std" feature of the "%{crate}" crate.

%files       -n %{name}+use_std-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog