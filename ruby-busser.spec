#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	busser
Summary:	Kitchen Busser - Runs tests for projects in test-kitchen
Name:		ruby-%{pkgname}
Version:	0.4.1
Release:	1
License:	Apache v2.0
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	f6271f37653d7ae8a322c7293bc4f6e8
URL:		https://github.com/fnichol/busser
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	ruby-aruba
BuildRequires:	ruby-bundler < 2
BuildRequires:	ruby-bundler >= 1.3
BuildRequires:	ruby-cane
BuildRequires:	ruby-chef
BuildRequires:	ruby-countloc
BuildRequires:	ruby-fakefs
BuildRequires:	ruby-guard-cane
BuildRequires:	ruby-guard-cucumber
BuildRequires:	ruby-guard-minitest
BuildRequires:	ruby-minitest
BuildRequires:	ruby-mocha
BuildRequires:	ruby-rake
BuildRequires:	ruby-simplecov
BuildRequires:	ruby-tailor
%endif
Requires:	ruby-thor
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kitchen Busser - Runs tests for projects in test-kitchen

%prep
%setup -q -n %{pkgname}-%{version}
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/busser
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
