%bcond_without check
%global npm_name aw-webui

%global commit0 7de395b4b5d9097c2ee6fd2afcc9876bc969df66
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global url1 https://github.com/ActivityWatch/media
%global commit1 ae8d3737a4984cc891076dc830ad117b13288a9f
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

Name:           nodejs-%{npm_name}
Version:        %{shortcommit0}
Release:        %autorelease
Summary:        A web-based UI for ActivityWatch, built with Vue.js

License:        0BSD and Apache-2.0 and (Apache-2.0 OR MIT) and Artistic-2.0 and BSD-2-Clause and BSD-3-Clause and CC-BY-4.0 and ISC and MIT and MPL-2.0 and (MPL-2.0 OR Apache-2.0) and Unlicense and W3C-20150513"

URL:            https://github.com/ActivityWatch/%{npm_name}
Source0:        %{url}/archive/%{commit0}/%{npm_name}-%{shortcommit0}.tar.gz
Source1:        %{npm_name}-%{version}-nm-prod.tgz
Source2:        %{npm_name}-%{version}-nm-dev.tgz
Source3:        %{npm_name}-%{version}-bundled-licenses.txt
Source4:        %{url1}/archive/%{commit1}/media-%{shortcommit1}.tar.gz
Source5:        nodejs-aw-webui-package.json
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-devel
BuildRequires:  make

%description
%{summary}

%prep
%autosetup -n %{npm_name}-%{commit0} -p1

# unpack some icons
tar -xf %{SOURCE4} --strip-components 1 -C ./media

# replace version
grep -Rl 'git rev-parse' | xargs sed -i 's/$(git rev-parse HEAD)/%{commit0}/g'
grep -Rl 'git rev-parse' | xargs sed -i 's/git rev-parse --short HEAD/echo %{shortcommit0}/g'

# copy license
cp %{SOURCE3} .

# unpack npm dependencies
tar xfz %{SOURCE1}
# building fails when symlinking, so move instead
mv node_modules_prod node_modules

%build
make build
rm -r node_modules

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr dist -t %{buildroot}%{nodejs_sitelib}/%{npm_name}

# package.json with dependencies adds them to requires or wants to bundle them
cp -pr %{SOURCE5} %{buildroot}%{nodejs_sitelib}/%{npm_name}/package.json
%nodejs_symlink_deps

%if %{with check}
%check
tar xfz %{SOURCE2}
mv node_modules_dev node_modules
make test
rm -r node_modules
%endif

%files
%license LICENSE.txt %{npm_name}-%{version}-bundled-licenses.txt
%doc README.md
%{nodejs_sitelib}/%{npm_name}

%changelog
%autochangelog
