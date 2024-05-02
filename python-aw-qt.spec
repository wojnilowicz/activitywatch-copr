%bcond_without check

%global srcname aw-qt
%global commit0 d20a9419c5d94479a633c611c68138886a3ff135
%global short_commit0 %(c=%{commit0}; echo ${c:0:7})

%global url1 https://github.com/ActivityWatch/media
%global commit1 ae8d3737a4984cc891076dc830ad117b13288a9f
%global short_commit1 %(c=%{commit1}; echo ${c:0:7})

Name:           python-%{srcname}
Version:        0^20240507.%{short_commit0}
Release:        %autorelease
Summary:        Client library for ActivityWatch in Python

License:        MPL-2.0
URL:            https://github.com/ActivityWatch/%{srcname}
Source0:        %{url}/archive/%{commit0}/%{srcname}-%{short_commit0}.tar.gz
Source1:        %{url1}/archive/%{commit1}/media-%{short_commit1}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  help2man
BuildRequires:  desktop-file-utils

%global _description %{expand:
Client library for ActivityWatch in Python.}

%description %{_description}

%package -n python3-%{srcname}
Summary:    %{summary}

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
mkdir -p %{buildroot}%{_mandir}/man1
help2man --no-discard-stderr %{buildroot}%{_bindir}/%{srcname} -o %{buildroot}%{_mandir}/man1/%{srcname}.1
desktop-file-install -m 0644 --dir=%{buildroot}%{_datadir}/applications %{_builddir}/%{srcname}-%{commit0}/resources/%{srcname}.desktop
install -Dm 644 media/logo/logo-128.png %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/activitywatch.png
install -Dm 644 media/logo/logo.png %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/activitywatch.png

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE.txt
%{_mandir}/man1/%{srcname}.1*
%{_bindir}/%{srcname}
%{_datadir}/icons/hicolor/128x128/apps/activitywatch.png
%{_datadir}/icons/hicolor/512x512/apps/activitywatch.png
%{_datadir}/applications/%{srcname}.desktop

%changelog
%autochangelog
