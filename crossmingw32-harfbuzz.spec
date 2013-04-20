Summary:	HarfBuzz - internationalized text shaping library - MinGW32 cross version
Summary(pl.UTF-8):	Rasteryzer fontów TrueType - wersja skrośna dla MinGW32
Name:		crossmingw32-harfbuzz
Version:	0.9.15
Release:	2
License:	MIT
Group:		Development/Libraries
Source0:	http://www.freedesktop.org/software/harfbuzz/release/harfbuzz-%{version}.tar.bz2
# Source0-md5:	f6075024947eb445dd3bec587b1753d1
Patch0:		harfbuzz-mingw32.patch
URL:		http://www.freedesktop.org/wiki/HarfBuzz
BuildRequires:	crossmingw32-cairo >= 1.8.0
BuildRequires:	crossmingw32-freetype >= 2.3.8
BuildRequires:	crossmingw32-glib2 >= 2.16
BuildRequires:	crossmingw32-gcc-c++
BuildRequires:	pkgconfig >= 1:0.20
Requires:	crossmingw32-cairo >= 1.8.0
Requires:	crossmingw32-freetype >= 2.3.8
Requires:	crossmingw32-glib2 >= 2.16
Requires:	crossmingw32-gcc-c++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# see <harfbuzz/internal/ftserv.h>, the real horror
%define		specflags	-fno-strict-aliasing

%define		no_install_post_strip	1

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

%ifnarch %{ix86}
# arch-specific flags (like alpha's -mieee) are not valid for i386 gcc
%define		optflags	-O2
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
Requires:	crossmingw32-cairo-dll >= 1.8.0
Requires:	crossmingw32-freetype-dll >= 2.3.8
Requires:	crossmingw32-glib2-dll >= 2.16
Requires:	wine

%description dll
DLL harfbuzz library for Windows.

%description dll -l pl.UTF-8
Biblioteka DLL harfbuzz dla Windows.

%prep
%setup -q -n harfbuzz-%{version}
%patch0 -p1

%build
export PKG_CONFIG_LIBDIR=%{_pkgconfigdir}
%configure \
	ICU_CONFIG=/none \
	--target=%{target} \
	--build=i686-pc-linux-gnu \
	--host=%{target} \
	--disable-silent-rules \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

# parallel install broken (hb-version.h both in pkginclude_HEADERS and
# nodist_pkginclude_HEADERS)
%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_dlldir}
mv -f $RPM_BUILD_ROOT%{_prefix}/bin/*.dll $RPM_BUILD_ROOT%{_dlldir}

%if 0%{!?debug:1}
%{target}-strip --strip-unneeded -R.comment -R.note $RPM_BUILD_ROOT%{_dlldir}/*.dll
%{target}-strip -g -R.comment -R.note $RPM_BUILD_ROOT%{_libdir}/*.a
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README TODO
%{_libdir}/libharfbuzz.dll.a
%{_libdir}/libharfbuzz.la
%{_includedir}/harfbuzz
%{_pkgconfigdir}/harfbuzz.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libharfbuzz.a

%files dll
%defattr(644,root,root,755)
%{_dlldir}/libharfbuzz-*.dll
