%{?scl:%scl_package nodejs-json-schema}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global npm_name json-schema

Name:       %{?scl_prefix}nodejs-%{npm_name}
Version:    0.2.2
Release:    2%{?dist}
Summary:    JSON Schema validation and specifications
License:    BSD and AFL
URL:        http://github.com/kriszyp/json-schema
Source0:    http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Source1:    https://raw.githubusercontent.com/piotr1212/json-schema/ee0c11cc999e553809c517f08ceb3747d1b3aa1f/LICENSE
BuildRequires: %{?scl_prefix}nodejs-devel
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
JSON Schema validation and specifications

%prep
%setup -q -n package
cp -p %{SOURCE1} .

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr draft-00 draft-01 draft-02 draft-03 draft-04 lib package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
# If any binaries are included, symlink them to bindir here


%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
#not running tests in RHSCL
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc LICENSE
%doc README.md

%changelog
* Tue Sep 20 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.2.2-2
- Initial build

