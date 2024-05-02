# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate rocket_cors

Name:           rust-rocket_cors
Version:        0.6.0
Release:        %autorelease
Summary:        Cross-origin resource sharing (CORS) for Rocket.rs applications

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rocket_cors
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Cross-origin resource sharing (CORS) for Rocket.rs applications.}

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
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde_derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_derive-devel %{_description}

This package contains library source intended for building other packages which
use the "serde_derive" feature of the "%{crate}" crate.

%files       -n %{name}+serde_derive-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serialization-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serialization-devel %{_description}

This package contains library source intended for building other packages which
use the "serialization" feature of the "%{crate}" crate.

%files       -n %{name}+serialization-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unicase_serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicase_serde-devel %{_description}

This package contains library source intended for building other packages which
use the "unicase_serde" feature of the "%{crate}" crate.

%files       -n %{name}+unicase_serde-devel
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