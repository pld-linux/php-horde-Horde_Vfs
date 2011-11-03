# TODO
# - system locale dir
%define		status		stable
%define		pearname	Horde_Vfs
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Virtual File System API
Name:		php-horde-Horde_Vfs
Version:	1.0.7
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	69539548b7ebc8a66445980d5ab843d7
URL:		https://github.com/horde/horde/tree/master/framework/Vfs/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-horde-Horde_Translation < 2.0.0
Requires:	php-horde-Horde_Util < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
Suggests:	php-ftp
Suggests:	php-horde-Horde_Auth
Suggests:	php-horde-Horde_Core
Suggests:	php-horde-Horde_Db
Suggests:	php-horde-Horde_Kolab_Session
Suggests:	php-horde-Horde_Mime
Suggests:	php-horde-Horde_Perms
Suggests:	php-pear-PEAR
Suggests:	php-pecl-ssh2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	 pear(Horde/Auth.*) pear(Horde/Core.*) pear(Horde/Db.*) pear(Horde/Kolab/Session.*) pear(Horde/Mime.*) pear(Horde/Perms.*) pear(PEAR.*) pear(ssh2.*)

%description
This package provides a Virtual File System API, with backends for:
- SQL
- FTP
- Local filesystems
- Hybrid SQL and filesystem
- Samba
- SSH2/SFTP
- IMAP (Kolab)

Reading, writing and listing of files are all supported, and there are
both object-based and array-based interfaces to directory listings.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}}
install -p ./%{_bindir}/* $RPM_BUILD_ROOT%{_bindir}

%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%{php_pear_dir}/.registry/.channel.*/*.reg
%attr(755,root,root) %{_bindir}/horde-vfs
%{php_pear_dir}/Horde/Vfs
%{php_pear_dir}/Horde/Vfs.php
%{php_pear_dir}/data/Horde_Vfs
