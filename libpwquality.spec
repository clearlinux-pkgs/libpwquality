#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libpwquality
Version  : 1.4.4
Release  : 50
URL      : https://github.com/libpwquality/libpwquality/releases/download/libpwquality-1.4.4/libpwquality-1.4.4.tar.bz2
Source0  : https://github.com/libpwquality/libpwquality/releases/download/libpwquality-1.4.4/libpwquality-1.4.4.tar.bz2
Summary  : A library for password generation and password quality checking
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: libpwquality-bin = %{version}-%{release}
Requires: libpwquality-lib = %{version}-%{release}
Requires: libpwquality-license = %{version}-%{release}
Requires: libpwquality-locales = %{version}-%{release}
Requires: libpwquality-man = %{version}-%{release}
Requires: libpwquality-python = %{version}-%{release}
Requires: libpwquality-python3 = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : buildreq-distutils3
BuildRequires : cracklib-dev

%description
This is a library for password quality checks and generation
of random passwords that pass the checks.
This library uses the cracklib and cracklib dictionaries
to perform some of the checks.

%package bin
Summary: bin components for the libpwquality package.
Group: Binaries
Requires: libpwquality-license = %{version}-%{release}

%description bin
bin components for the libpwquality package.


%package dev
Summary: dev components for the libpwquality package.
Group: Development
Requires: libpwquality-lib = %{version}-%{release}
Requires: libpwquality-bin = %{version}-%{release}
Provides: libpwquality-devel = %{version}-%{release}
Requires: libpwquality = %{version}-%{release}

%description dev
dev components for the libpwquality package.


%package lib
Summary: lib components for the libpwquality package.
Group: Libraries
Requires: libpwquality-license = %{version}-%{release}

%description lib
lib components for the libpwquality package.


%package license
Summary: license components for the libpwquality package.
Group: Default

%description license
license components for the libpwquality package.


%package locales
Summary: locales components for the libpwquality package.
Group: Default

%description locales
locales components for the libpwquality package.


%package man
Summary: man components for the libpwquality package.
Group: Default

%description man
man components for the libpwquality package.


%package python
Summary: python components for the libpwquality package.
Group: Default
Requires: libpwquality-python3 = %{version}-%{release}

%description python
python components for the libpwquality package.


%package python3
Summary: python3 components for the libpwquality package.
Group: Default
Requires: python3-core

%description python3
python3 components for the libpwquality package.


%prep
%setup -q -n libpwquality-1.4.4
cd %{_builddir}/libpwquality-1.4.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635748898
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1635748898
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libpwquality
cp %{_builddir}/libpwquality-1.4.4/COPYING %{buildroot}/usr/share/package-licenses/libpwquality/a01b717e0f402c7a4edeeec8e2afbc961ec72c18
%make_install
%find_lang libpwquality
## Remove excluded files
rm -f %{buildroot}*/etc/security/pwquality.conf

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pwmake
/usr/bin/pwscore

%files dev
%defattr(-,root,root,-)
/usr/include/pwquality.h
/usr/lib64/libpwquality.so
/usr/lib64/pkgconfig/pwquality.pc
/usr/share/man/man3/pwquality.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpwquality.so.1
/usr/lib64/libpwquality.so.1.0.2
/usr/lib64/security/pam_pwquality.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libpwquality/a01b717e0f402c7a4edeeec8e2afbc961ec72c18

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pwmake.1
/usr/share/man/man1/pwscore.1
/usr/share/man/man5/pwquality.conf.5
/usr/share/man/man8/pam_pwquality.8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f libpwquality.lang
%defattr(-,root,root,-)

