Summary:	HarfBuzz - internationalized text shaping library - MinGW32 cross version
Summary(pl.UTF-8):	Rasteryzer fontów TrueType - wersja skrośna dla MinGW32
Name:		crossmingw32-harfbuzz
Version:	7.0.0
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	https://github.com/harfbuzz/harfbuzz/releases/download/%{version}/harfbuzz-%{version}.tar.xz
# Source0-md5:	5c7a6750760e4d6c098436a43542a7d0
URL:		https://harfbuzz.github.io/
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.13.0
BuildRequires:	crossmingw32-w32api >= 5.0.2-8
BuildRequires:	crossmingw32-cairo >= 1.8.0
BuildRequires:	crossmingw32-freetype >= 2.11
BuildRequires:	crossmingw32-glib2 >= 2.38
BuildRequires:	crossmingw32-gcc-c++ >= 1:4.7
BuildRequires:	crossmingw32-pthreads-w32
BuildRequires:	gtk-doc >= 1.15
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig >= 1:0.28
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	crossmingw32-freetype >= 2.11
Requires:	crossmingw32-glib2 >= 2.38
Requires:	crossmingw32-gcc-c++ >= 1:4.7
Requires:	crossmingw32-pthreads-w32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# see <harfbuzz/internal/ftserv.h>, the real horror
%define		specflags	-fno-strict-aliasing

%define		no_install_post_strip	1
%define		_enable_debug_packages	0

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32

%define		_sysprefix		/usr
%define		_prefix			%{_sysprefix}/%{target}
%define		_libdir			%{_prefix}/lib
%define		_pkgconfigdir		%{_prefix}/lib/pkgconfig
%define		_dlldir			/usr/share/wine/windows/system
%define		__cc			%{target}-gcc
%define		__cxx			%{target}-g++
%define		__pkgconfig_provides	%{nil}
%define		__pkgconfig_requires	%{nil}

%ifnarch %{ix86}
# arch-specific flags (like alpha's -mieee) are not valid for i386 gcc
%define		optflags	-O2 -march=i486
%endif
# -z options are invalid for mingw linker, most of -f options are Linux-specific
%define		filterout_ld	-Wl,-z,.*
%define		filterout_c	-f[-a-z0-9=]*
%define		filterout_cxx	-f[-a-z0-9=]*

%description
Internationalized OpenType text layout and rendering library.

This package contains the cross version for Win32.

%description -l pl.UTF-8
Biblioteka rozmieszczająca i rysująca tekst z fontów OpenType,
obsługująca wiele języków.

Ten pakiet zawiera wersję skrośną dla Win32.

%package static
Summary:	Static harfbuzz library (cross MinGW32 version)
Summary(pl.UTF-8):	Statyczna biblioteka harfbuzz (wersja skrośna MinGW32)
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static harfbuzz library (cross MinGW32 version).

%description static -l pl.UTF-8
Statyczna biblioteka harfbuzz (wersja skrośna MinGW32).

%package dll
Summary:	DLL harfbuzz library for Windows
Summary(pl.UTF-8):	Biblioteka DLL harfbuzz dla Windows
Group:		Applications/Emulators
Requires:	crossmingw32-freetype-dll >= 2.11
Requires:	crossmingw32-glib2-dll >= 2.38
Requires:	wine

%description dll
DLL harfbuzz library for Windows.

%description dll -l pl.UTF-8
Biblioteka DLL harfbuzz dla Windows.

%package cairo
Summary:	HarfBuzz text shaping library - cairo integration - MinGW32 cross version
Summary(pl.UTF-8):	Biblioteka HarfBuzz do rysowania tekstu - integracja z cairo - wersja skrośna dla MinGW32
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	crossmingw32-cairo >= 1.8.0

%description cairo
HarfBuzz text shaping library - cairo integration.

This package contains the cross version for Win32.

%description cairo -l pl.UTF-8
Biblioteka HarfBuzz do rysowania tekstu - integracja z cairo.

Ten pakiet zawiera wersję skrośną dla Win32.

%package cairo-static
Summary:	Static HarfBuzz cairo library (cross MinGW32 version)
Summary(pl.UTF-8):	Biblioteka statyczna HarfBuzz cairo (wersja skrośna MinGW32)
Group:		Development/Libraries
Requires:	%{name}-cairo-devel = %{version}-%{release}

%description cairo-static
Static HarfBuzz cairo library (cross MinGW32 version).

%description cairo-static -l pl.UTF-8
Biblioteka statyczna HarfBuzz cairo (wersja skrośna MinGW32).

%package cairo-dll
Summary:	DLL harfbuzz cairo library for Windows
Summary(pl.UTF-8):	Biblioteka DLL harfbuzz cairo dla Windows
Group:		Applications/Emulators
Requires:	%{name}-dll = %{version}-%{release}
Requires:	crossmingw32-cairo-dll >= 1.8.0
Requires:	wine

%description cairo-dll
DLL harfbuzz cairo library for Windows.

%description cairo-dll -l pl.UTF-8
Biblioteka DLL harfbuzz cairo dla Windows.

%package subset
Summary:	HarfBuzz text shaping library - font subsetter - MinGW32 cross version
Summary(pl.UTF-8):	Biblioteka HarfBuzz do rysowania tekstu - font subsetter - wersja skrośna dla MinGW32
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description subset
HarfBuzz text shaping library - font subsetter.

This package contains the cross version for Win32.

%description subset -l pl.UTF-8
Biblioteka HarfBuzz do rysowania tekstu - font subsetter.

Ten pakiet zawiera wersję skrośną dla Win32.

%package subset-static
Summary:	Static HarfBuzz subset library (cross MinGW32 version)
Summary(pl.UTF-8):	Biblioteka statyczna HarfBuzz subset (wersja skrośna MinGW32)
Group:		Development/Libraries
Requires:	%{name}-subset = %{version}-%{release}

%description subset-static
Static HarfBuzz subset library (cross MinGW32 version).

%description subset-static -l pl.UTF-8
Biblioteka statyczna HarfBuzz subset (wersja skrośna MinGW32).

%package subset-dll
Summary:	DLL HarfBuzz subset library for Windows
Summary(pl.UTF-8):	Biblioteka DLL HarfBuzz subset dla Windows
Group:		Applications/Emulators
Requires:	%{name}-dll = %{version}-%{release}

%description subset-dll
DLL HarfBuzz subset library for Windows.

%description subset-dll -l pl.UTF-8
Biblioteka DLL HarfBuzz subset dla Windows.

%prep
%setup -q -n harfbuzz-%{version}

%build
%{__libtoolize}
%{__gtkdocize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
export PKG_CONFIG_LIBDIR=%{_pkgconfigdir}
# MingW32 headers require GNU extensions (-std=c++11 doesn't work)
%configure \
	CPPFLAGS="%{rpmcppflags} -D_GNU_SOURCE" \
	CXXFLAGS="%{rpmcxxflags} -std=gnu++11" \
	PTHREAD_LIBS="-lpthread" \
	--target=%{target} \
	--build=i686-pc-linux-gnu \
	--host=%{target} \
	--disable-gtk-doc \
	--disable-silent-rules \
	--enable-static \
	--with-cairo \
	--with-freetype \
	--with-glib \
	--without-graphite2 \
	--with-html-dir=%{_gtkdocdir} \
	--without-icu \
	--with-uniscribe

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_dlldir}
%{__mv} $RPM_BUILD_ROOT%{_prefix}/bin/*.dll $RPM_BUILD_ROOT%{_dlldir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

%if 0%{!?debug:1}
%{target}-strip --strip-unneeded -R.comment -R.note $RPM_BUILD_ROOT%{_dlldir}/*.dll
%{target}-strip -g -R.comment -R.note $RPM_BUILD_ROOT%{_libdir}/*.a
%endif

%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/cmake/harfbuzz
%{__rm} $RPM_BUILD_ROOT%{_bindir}/hb*.exe
%{__rm} -rf $RPM_BUILD_ROOT%{_gtkdocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README.md THANKS
%{_libdir}/libharfbuzz.dll.a
%dir %{_includedir}/harfbuzz
%{_includedir}/harfbuzz/hb.h
%{_includedir}/harfbuzz/hb-aat.h
%{_includedir}/harfbuzz/hb-aat-layout.h
%{_includedir}/harfbuzz/hb-blob.h
%{_includedir}/harfbuzz/hb-buffer.h
%{_includedir}/harfbuzz/hb-common.h
%{_includedir}/harfbuzz/hb-cplusplus.hh
%{_includedir}/harfbuzz/hb-deprecated.h
%{_includedir}/harfbuzz/hb-draw.h
%{_includedir}/harfbuzz/hb-face.h
%{_includedir}/harfbuzz/hb-font.h
%{_includedir}/harfbuzz/hb-ft.h
%{_includedir}/harfbuzz/hb-glib.h
%{_includedir}/harfbuzz/hb-map.h
%{_includedir}/harfbuzz/hb-ot-color.h
%{_includedir}/harfbuzz/hb-ot-deprecated.h
%{_includedir}/harfbuzz/hb-ot-font.h
%{_includedir}/harfbuzz/hb-ot-layout.h
%{_includedir}/harfbuzz/hb-ot-math.h
%{_includedir}/harfbuzz/hb-ot-meta.h
%{_includedir}/harfbuzz/hb-ot-metrics.h
%{_includedir}/harfbuzz/hb-ot-name.h
%{_includedir}/harfbuzz/hb-ot-shape.h
%{_includedir}/harfbuzz/hb-ot-var.h
%{_includedir}/harfbuzz/hb-ot.h
%{_includedir}/harfbuzz/hb-paint.h
%{_includedir}/harfbuzz/hb-set.h
%{_includedir}/harfbuzz/hb-shape-plan.h
%{_includedir}/harfbuzz/hb-shape.h
%{_includedir}/harfbuzz/hb-style.h
%{_includedir}/harfbuzz/hb-unicode.h
%{_includedir}/harfbuzz/hb-uniscribe.h
%{_includedir}/harfbuzz/hb-version.h
%{_pkgconfigdir}/harfbuzz.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libharfbuzz.a

%files dll
%defattr(644,root,root,755)
%{_dlldir}/libharfbuzz-0.dll

%files cairo
%defattr(644,root,root,755)
%{_libdir}/libharfbuzz-cairo.dll.a
%{_includedir}/harfbuzz/hb-cairo.h
%{_pkgconfigdir}/harfbuzz-cairo.pc

%files cairo-static
%defattr(644,root,root,755)
%{_libdir}/libharfbuzz-cairo.a

%files cairo-dll
%defattr(644,root,root,755)
%{_dlldir}/libharfbuzz-cairo-0.dll

%files subset
%defattr(644,root,root,755)
%{_libdir}/libharfbuzz-subset.dll.a
%{_includedir}/harfbuzz/hb-subset.h
%{_includedir}/harfbuzz/hb-subset-repacker.h
%{_pkgconfigdir}/harfbuzz-subset.pc

%files subset-static
%defattr(644,root,root,755)
%{_libdir}/libharfbuzz-subset.a

%files subset-dll
%defattr(644,root,root,755)
%{_dlldir}/libharfbuzz-subset-0.dll
