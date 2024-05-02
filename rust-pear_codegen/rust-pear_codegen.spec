# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate pear_codegen

Name:           rust-pear_codegen
Version:        0.2.9
Release:        %autorelease
Summary:        (codegen) pear is a fruit

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pear_codegen
Source0:        %{crates_source}
Source1:        LICENSE-APACHE
Source2:        LICENSE-MIT

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
(codegen) pear is a fruit}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
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
install -Dm 0644 %{SOURCE1} -t %{buildroot}%{crate_instdir}
install -Dm 0644 %{SOURCE2} -t %{buildroot}%{crate_instdir}

%if %{with check}
%check
# * failed to resolve: use of undeclared crate or module `pear`
%cargo_test -- -- --skip 'src/lib.rs'
%endif

%changelog
%autochangelog