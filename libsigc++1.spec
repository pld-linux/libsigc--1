Summary:	The Typesafe Signal Framework for C++
Summary(pl):	�rodowisko sygna��w z kontrol� typ�w dla C++
Name:		libsigc++1
Version:	1.0.4
Release:	5
License:	LGPL
Vendor:		Karl E. Nelson <kenelson@ece.ucdavis.edu>
Group:		Libraries
Source0:	ftp://download.sourceforge.net/pub/sourceforge/libsigc/libsigc++-%{version}.tar.gz
Patch0:		libsigc++-remove_stupid_install-data-hook_targets.patch
Patch1:		%{name}-ac25x.patch
URL:		http://libsigc.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libsigc++-examples
Obsoletes:	libsigc++ < 1.1

%description
This library implements a full callback system for use in widget
libraries, abstract interfaces, and general programming. Originally
part of the Gtk-- widget set, %{name} is now a seperate library to
provide for more general use. It is the most complete library of its
kind with the ablity to connect an abstract callback to a class
method, function, or function object. It contains adaptor classes for
connection of dissimilar callbacks and has an ease of use unmatched by
other C++ callback libraries.

%description -l pl
Ta biblioteka jest implementacj� pe�nego systemu callback�w do
u�ywania w bibliotekach widget�w, interfejsach abstrakcyjnych i
og�lnym programowaniu. Oryginalnie by�a to cz�� zestawu widget�w
Gtk--, ale jest teraz oddzieln� bibliotek� og�lniejszego
przeznaczenia. Jest to kompletna biblioteka tego typu z mo�liwo�ci�
��czenia abstrakcyjnych callback�w z metodami klas, funkcjami lub
obiektami funkcji. Zawiera klasy adapter�w do ��czenia r�nych
callback�w.

%package devel
Summary:	Development tools for the Typesafe Signal Framework for C++
Summary(pl):	Narz�dzia programistyczne do �rodowiska libsig++
Group:		Development/Libraries
Requires:	m4
Requires:	%{name} = %{version}
Obsoletes:	libsigc++-devel < 1.1

%description devel
Development tools for the Typesafe Signal Framework for C++.

%description devel -l pl
Narz�dzia programistyczne do �rodowiska libsigc++ - sygna��w z
kontrol� typ�w.

%package static
Summary:	Static Typesafe Signal Framework for C++ libraries
Summary(pl):	Statyczna biblioteka libsigc++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Obsoletes:	libsigc++-static < 1.1

%description static
Static Typesafe Signal Framework for C++ libraries.

%description static -l pl
Statyczna biblioteka libsigc++ - �rodowiska sygna��w z kontrol� typ�w.

%prep
%setup -q -n libsigc++-%{version}
%patch0 -p1
%patch1 -p1

%build
CXXFLAGS="%{rpmcflags} -fno-exceptions"
rm -f scripts/missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

mv -f $RPM_BUILD_ROOT%{_aclocaldir}/sigc++.m4 $RPM_BUILD_ROOT%{_aclocaldir}/sigc++1.m4

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS README IDEAS NEWS ChangeLog TODO doc/*
%attr(755,root,root) %{_bindir}/sigc-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/sigc++-*
%{_libdir}/sigc++-*
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
