%define commit 924fb6f
%define tag 60df687

Name:		cakephp
Version:	1.3.13
Release:	1

Summary:	MVC rapid application development framework for PHP
License:	MIT
Group:		Development/PHP
URL:		http://cakephp.org/
		# https://github.com/cakephp/cakephp/tarball/%{version}:
Source0:	%{name}-%{name}-%{version}-0-g%{commit}.tar.gz
		# Fix the path to launch the console php script to an
		# absolute path:
Patch0:		%{name}-%{version}-mdv-fix-lib-path.patch

BuildArch:	noarch

Requires:	apache-mod_php
Requires:	php-pdo
Suggests:	cakephp-cli


%description
CakePHP is a free, open-source, model-view-controller rapid development
framework for PHP. It's a foundational structure for programmers to create
web applications. CakePHP reduces development costs and helps developers
write less code, making it swiftly and with the least amount of hassle:

* Compatible with versions 4 and 5 of PHP
* Integrated CRUD for database interaction
* Application scaffolding
* Code generation
* MVC architecture
* Request dispatcher with clean, custom URLs and routes
* Built-in validation
* Fast and flexible templating (PHP syntax, with helpers)
* View Helpers for AJAX, JavaScript, HTML Forms and more
* Email, Cookie, Security, Session, and Request Handling Components
* Flexible ACL
* Data Sanitization
* Flexible Caching
* Localization
* Works from any web site directory, with little to no Apache configuration
  involved


%package cli
Summary:	CakePHP console client
Group:	 	Development/PHP

Requires:	%{name}
Requires:	php-cli


%description cli
CakePHP is a free, open-source, model-view-controller rapid development
framework for PHP. It's a foundational structure for programmers to create
web applications.

This package contains the console command-line interface to CakePHP. It
features a number of console applications that are used in concert with
other CakePHP features (like ACL or i18n) and for general use in getting you
to launch quicker.


%prep
%setup -q -n %{name}-%{name}-%{tag}
%patch0 -p1


%build
# Remove unnecessary 'empty' files and directories.  These were added
# by upstream to workaround braindead MacOS X extracting utilities
# that would silently not create empty directories:
find ./ -type f -name empty -size 0 -print0 | xargs -0 rm -f
# We don't need the msdos command launcher:
CAKEBAT=cake/console/cake.bat
[[ -f ${CAKEBAT} ]] && rm -f ${CAKEBAT}


%install
mkdir -p %{buildroot}%{_datadir}/php/%{name}/cake/console
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_docdir}/%{name}

cp -r cake/libs \
    cake/tests \
    cake/config \
    cake/*.php \
    %{buildroot}%{_datadir}/php/%{name}/cake
cp -r cake/console/libs \
    cake/console/*.php \
    %{buildroot}%{_datadir}/php/%{name}/cake/console
cp -r cake/console/cake %{buildroot}%{_bindir}/cake

cp README %{buildroot}%{_docdir}/%{name}
cp cake/*.txt %{buildroot}%{_docdir}/%{name}


%files
%defattr(-,root,root)
%{_datadir}/php/%{name}/cake/libs
%{_datadir}/php/%{name}/cake/tests
%{_datadir}/php/%{name}/cake/config
%{_datadir}/php/%{name}/cake/*.php
%doc %{_docdir}/%{name}/README
%doc %{_docdir}/%{name}/VERSION.txt
%doc %{_docdir}/%{name}/LICENSE.txt


%files cli
%{_bindir}/cake
%{_datadir}/php/%{name}/cake/console


%changelog
* Sat Nov 05 2011 Joao Victor Duarte Martins <jvdm@mandriva.com.br> 1.3.13-1
+ Revision: 717754
- New version 1.3.13

* Thu Sep 29 2011 Sergey Zhemoitel <serg@mandriva.org> 1.3.12-1
+ Revision: 702038
- new version 1.3.12

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.6-2mdv2011.0
+ Revision: 610094
- rebuild

* Fri Mar 19 2010 Joao Victor Martins <jvictor@mandriva.com> 1.2.6-1mdv2010.1
+ Revision: 525266
- Imported to cooker
- Created package structure for cakephp.

