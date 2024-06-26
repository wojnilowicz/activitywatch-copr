%bcond_without check
%global srcname aw-client
%global commit 5c49cb2c6ed31d7c903b46f8c18ec2b317df24fb
%global short_commit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{srcname}
Version:        0.5.13^20240506.%{short_commit}
Release:        %autorelease
Summary:        Client library for ActivityWatch in Python

License:        MPL-2.0
URL:            https://github.com/ActivityWatch/%{srcname}
Source:         %{url}/archive/%{commit}/%{srcname}-%{short_commit}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Client library for ActivityWatch in Python.}

%description %{_description}

%package -n python3-%{srcname}
Summary:    %{summary}

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{commit}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i '/^[[:blank:]]*pytest-cov\b/d' pyproject.toml
sed -r -i '/^[[:blank:]]*pylint\b/d' pyproject.toml
sed -r -i '/^[[:blank:]]*black\b/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files aw_client

%check
# skip test_client.py due to a http connection error
# skip test_failqueue.py due to missing aw_server dependency
%pytest --ignore=tests/test_client.py \
        --ignore=tests/test_failqueue.py

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE.txt
%{_bindir}/%{srcname}

%changelog
%autochangelog
