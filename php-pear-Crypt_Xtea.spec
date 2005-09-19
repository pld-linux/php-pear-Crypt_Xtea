%include	/usr/lib/rpm/macros.php
%define		_class		Crypt
%define		_subclass	Xtea
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - the Tiny Encryption Algorithm (TEA) (New Variant)
Summary(pl):	%{_pearname} - Tiny Encryption Algorithm (TEA) (nowy wariant)
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	3.2
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	77a3221bdae2bfa6d5c5b69ef9c52de2
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/Crypt_Xtea/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	sed >= 4.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A class that implements the Tiny Encryption Algorithm (TEA) (New
Variant). This class does not depend on mcrypt. Encryption is
relatively fast, decryption relatively slow. Original code from
http://vader.brad.ac.uk/tea/source.shtml#new_ansi

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa implementuj±ca Tiny Encryption Algorithm (TEA) (nowy wariant).
Ta klasa nie zale¿y od mcrypt. Szyfrowanie jest stosunkowo szybkie,
rozkodowanie relatywnie wolne. Oryginalny kod:
http://vader.brad.ac.uk/tea/source.shtml#new_ansi

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description tests
Tests for PEAR::%{_pearname}.

%prep
%pear_package_setup

# this should be in tests.
cd ./%{php_pear_dir}
install -d tests/%{_pearname}
sed -i 's,Xtea.php,Crypt/Xtea.php,' %{_class}/%{_subclass}Test.php
mv %{_class}/%{_subclass}Test.php tests/%{_pearname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
