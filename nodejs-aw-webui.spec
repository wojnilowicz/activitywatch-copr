%bcond_without check
%global npm_name aw-webui

%global commit0 cb83d124961affe2ae25f488eb14422ee35e66c8
%global short_commit0 %(c=%{commit0}; echo ${c:0:7})

%global url1 https://github.com/ActivityWatch/media
%global commit1 ae8d3737a4984cc891076dc830ad117b13288a9f
%global short_commit1 %(c=%{commit1}; echo ${c:0:7})

Name:           nodejs-%{npm_name}
Version:        0^20240507.%{short_commit0}
Release:        %autorelease
Summary:        A web-based UI for ActivityWatch, built with Vue.js

License:        MPL-2.0

URL:            https://github.com/ActivityWatch/%{npm_name}
Source0:        %{url}/archive/%{commit0}/%{npm_name}-%{short_commit0}.tar.gz
# prepared with "nodejs-packaging-bundler %%{npm_name} %%{short_commit0} %%{SOURCE0}"
Source1:        https://wojnilowicz.fedorapeople.org/%{npm_name}-%{short_commit0}-nm-prod.tgz
Source2:        https://wojnilowicz.fedorapeople.org/%{npm_name}-%{short_commit0}-nm-dev.tgz
Source3:        %{url1}/archive/%{commit1}/media-%{short_commit1}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch
BuildRequires:  nodejs-npm
BuildRequires:  nodejs-devel
BuildRequires:  fdupes

%description
%{summary}

%prep
%autosetup -n %{npm_name}-%{commit0} -p1

# unpack some icons
tar xfz %{SOURCE3} --strip-components 1 -C media
cp -pr media/logo/logo.{png,svg} -t static

# it's not a git repository, so querying git would fail
sed -ri 's/git rev-parse --short HEAD/echo %{short_commit0}/' vue.config.js

# unpack npm prod dependencies straight to node_modules, because
# building fails when symlinking from node_modules_prod to node_modules
mkdir -p node_modules
tar xfz %{SOURCE1} --strip-components 2 -C node_modules

# unpack npm dev dependencies too, because cannot find vue-cli-service
# when building
tar xfz %{SOURCE2} --strip-components 2 -C node_modules

%build
npm run build

%install
mkdir -p %{buildroot}%{_datadir}/%{npm_name}
cp -pr dist -t %{buildroot}%{_datadir}/%{npm_name}

%fdupes %{buildroot}%{_datadir}/%{npm_name}/dist/css

%if %{with check}
%check
npm test
%endif

%files
%license LICENSE.txt
%doc README.md
%{_datadir}/%{npm_name}

%changelog
%autochangelog
