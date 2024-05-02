# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate figment

Name:           rust-figment
Version:        0.10.18
Release:        %autorelease
Summary:        Configuration library so con-free, it's unreal

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/figment
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A configuration library so con-free, it's unreal.}

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

%package     -n %{name}+env-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+env-devel %{_description}

This package contains library source intended for building other packages which
use the "env" feature of the "%{crate}" crate.

%files       -n %{name}+env-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+json-devel %{_description}

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%files       -n %{name}+json-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+parking_lot-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+parking_lot-devel %{_description}

This package contains library source intended for building other packages which
use the "parking_lot" feature of the "%{crate}" crate.

%files       -n %{name}+parking_lot-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+parse-value-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+parse-value-devel %{_description}

This package contains library source intended for building other packages which
use the "parse-value" feature of the "%{crate}" crate.

%files       -n %{name}+parse-value-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pear-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pear-devel %{_description}

This package contains library source intended for building other packages which
use the "pear" feature of the "%{crate}" crate.

%files       -n %{name}+pear-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde_json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_json-devel %{_description}

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%files       -n %{name}+serde_json-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde_yaml-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_yaml-devel %{_description}

This package contains library source intended for building other packages which
use the "serde_yaml" feature of the "%{crate}" crate.

%files       -n %{name}+serde_yaml-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tempfile-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tempfile-devel %{_description}

This package contains library source intended for building other packages which
use the "tempfile" feature of the "%{crate}" crate.

%files       -n %{name}+tempfile-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+test-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+test-devel %{_description}

This package contains library source intended for building other packages which
use the "test" feature of the "%{crate}" crate.

%files       -n %{name}+test-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+toml-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+toml-devel %{_description}

This package contains library source intended for building other packages which
use the "toml" feature of the "%{crate}" crate.

%files       -n %{name}+toml-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+yaml-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+yaml-devel %{_description}

This package contains library source intended for building other packages which
use the "yaml" feature of the "%{crate}" crate.

%files       -n %{name}+yaml-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -a

%build
%cargo_build -a

%install
%cargo_install -a

%if %{with check}
%check
%cargo_test -a
%endif

%changelog
%autochangelog
