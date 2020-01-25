%define		_class		Crypt
%define		_subclass	Xtea
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - the Tiny Encryption Algorithm (TEA) (New Variant)
Summary(pl.UTF-8):	%{_pearname} - Tiny Encryption Algorithm (TEA) (nowy wariant)
Name:		php-pear-%{_pearname}
Version:	1.1.0
Release:	2
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	32fa48dcbd8f6f4bb9f386334a946a4a
URL:		http://pear.php.net/package/Crypt_Xtea/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-12
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Obsoletes:	php-pear-Crypt_Xtea-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A class that implements the Tiny Encryption Algorithm (TEA) (New
Variant). This class does not depend on mcrypt. Encryption is
relatively fast, decryption relatively slow. Original code from
http://vader.brad.ac.uk/tea/source.shtml#new_ansi

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa implementująca Tiny Encryption Algorithm (TEA) (nowy wariant).
Ta klasa nie zależy od mcrypt. Szyfrowanie jest stosunkowo szybkie,
rozkodowanie relatywnie wolne. Oryginalny kod:
http://vader.brad.ac.uk/tea/source.shtml#new_ansi

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

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

%{php_pear_dir}/data/%{_pearname}
