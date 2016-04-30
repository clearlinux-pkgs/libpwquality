#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libpwquality
Version  : 1.3.0
Release  : 9
URL      : https://fedorahosted.org/releases/l/i/libpwquality/libpwquality-1.3.0.tar.bz2
Source0  : https://fedorahosted.org/releases/l/i/libpwquality/libpwquality-1.3.0.tar.bz2
Summary  : A library for password generation and password quality checking
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: libpwquality-bin
Requires: libpwquality-python
Requires: libpwquality-lib
Requires: libpwquality-locales
Requires: libpwquality-doc
BuildRequires : Linux-PAM-dev
BuildRequires : cracklib-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
This is a library for password quality checks and generation
of random passwords that pass the checks.
This library uses the cracklib and cracklib dictionaries
to perform some of the checks.

%package bin
Summary: bin components for the libpwquality package.
Group: Binaries

%description bin
bin components for the libpwquality package.


%package dev
Summary: dev components for the libpwquality package.
Group: Development
Requires: libpwquality-lib
Requires: libpwquality-bin

%description dev
dev components for the libpwquality package.


%package doc
Summary: doc components for the libpwquality package.
Group: Documentation

%description doc
doc components for the libpwquality package.


%package lib
Summary: lib components for the libpwquality package.
Group: Libraries

%description lib
lib components for the libpwquality package.


%package locales
Summary: locales components for the libpwquality package.
Group: Default

%description locales
locales components for the libpwquality package.


%package python
Summary: python components for the libpwquality package.
Group: Default

%description python
python components for the libpwquality package.


%prep
%setup -q -n libpwquality-1.3.0

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang libpwquality

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pwmake
/usr/bin/pwscore

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
/usr/lib64/security/pam_pwquality.so

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*

%files locales -f libpwquality.lang 
%defattr(-,root,root,-)

