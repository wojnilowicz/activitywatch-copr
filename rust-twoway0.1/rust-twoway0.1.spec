# Generated by rust2rpm 26
# * missing and outdated dev-dependencies
%bcond_with check
%global debug_package %{nil}

%global crate twoway

Name:           rust-twoway0.1
Version:        0.1.8
Release:        %autorelease
Summary:        Fast substring search for strings and byte strings. Optional SSE4.2 acceleration

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/twoway
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Fast substring search for strings and byte strings. Optional SSE4.2
acceleration (requires nightly and cargo feature flag pcmp) using
pcmpestri. Memchr is the only mandatory dependency. The two way
algorithm is also used by rust's libstd itself, but here it is exposed
both for byte strings, using memchr, and optionally using a SSE4.2
accelerated version.}

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
%doc %{crate_instdir}/README.rst
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pcmp-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pcmp-devel %{_description}

This package contains library source intended for building other packages which
use the "pcmp" feature of the "%{crate}" crate.

%files       -n %{name}+pcmp-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unchecked-index-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unchecked-index-devel %{_description}

This package contains library source intended for building other packages which
use the "unchecked-index" feature of the "%{crate}" crate.

%files       -n %{name}+unchecked-index-devel
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
