%bcond_with check
%global srcname aw-qt
%global commit0 a25960878bbaab9afb37a11cb0a7ee72c6be9dd3
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global url1 https://github.com/ActivityWatch/media
%global commit1 ae8d3737a4984cc891076dc830ad117b13288a9f
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

Name:           python-%{srcname}
Version:        %{shortcommit0}
Release:        %autorelease
Summary:        Client library for ActivityWatch in Python.

License:        MPL-2.0
URL:            https://github.com/ActivityWatch/%{srcname}

Source0:        %{url}/archive/%{commit0}/%{srcname}-%{shortcommit0}.tar.gz
Source1:        %{url1}/archive/%{commit1}/media-%{shortcommit1}.tar.gz
BuildArch:      noarch

# BuildRequires:  python3dist(pyqt6)
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils

%global _description %{expand:
Client library for ActivityWatch in Python.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{commit0}
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -ri '/^[[:blank:]]*flake8\b/d' pyproject.toml

tar -xf %{SOURCE1} --strip-components 1 -C ./media
# the build process somehow doesn't bundle the logo.png icon
sed -ri 's/\("icons:logo.png"\)/.fromTheme("activitywatch")/' aw_qt/trayicon.py

# dependency generator seems to not harvest following mandatory
# dependencies from tool.poetry.group.pyqt.dependencies
sed -ri '/^[[:blank:]]*aw-core\b/a PyQt6 = "^6.5.3"' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files aw_qt
desktop-file-install -m 0644 --dir=%{buildroot}%{_datadir}/applications %{_builddir}/%{srcname}-%{commit0}/resources/%{srcname}.desktop
install -Dm 644 media/logo/logo-128.png %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/activitywatch.png
install -Dm 644 media/logo/logo.png %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/activitywatch.png

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%{_bindir}/%{srcname}
%{_datadir}/icons/hicolor/128x128/apps/activitywatch.png
%{_datadir}/icons/hicolor/512x512/apps/activitywatch.png
%{_datadir}/applications/%{srcname}.desktop
%doc README.md
%license LICENSE.txt

%changelog
%autochangelog
