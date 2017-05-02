#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xineramaproto
Version  : 1.2.1
Release  : 9
URL      : http://xorg.freedesktop.org/releases/individual/proto/xineramaproto-1.2.1.tar.bz2
Source0  : http://xorg.freedesktop.org/releases/individual/proto/xineramaproto-1.2.1.tar.bz2
Summary  : Xinerama extension headers
Group    : Development/Tools
License  : MIT-Opengroup
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(xorg-macros)

%description
X Xinerama Extension
This is an X extension that allows multiple physical screens controlled
by a single X server to appear as a single screen.

%package dev
Summary: dev components for the xineramaproto package.
Group: Development
Provides: xineramaproto-devel

%description dev
dev components for the xineramaproto package.


%package dev32
Summary: dev32 components for the xineramaproto package.
Group: Default

%description dev32
dev32 components for the xineramaproto package.


%prep
%setup -q -n xineramaproto-1.2.1
pushd ..
cp -a xineramaproto-1.2.1 build32
popd

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
%configure --disable-static  --libdir=/usr/lib32
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
pushd ../build32
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do mv $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/panoramiXproto.h
/usr/lib64/pkgconfig/xineramaproto.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/pkgconfig/32xineramaproto.pc
