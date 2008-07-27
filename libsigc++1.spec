Summary:	The Typesafe Signal Framework for C++
Summary(pl.UTF-8):	Środowisko sygnałów z kontrolą typów dla C++
Name:		libsigc++1
Version:	1.0.4
Release:	9
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libsigc/libsigc++-%{version}.tar.gz
# Source0-md5:	88d34840acc1cc5d47b347726e4a09e0
Patch0:		%{name}-remove_stupid_install-data-hook_targets.patch
Patch1:		%{name}-ac25x.patch
Patch2:		%{name}-link.patch
Patch3:		%{name}-am18.patch
URL:		http://libsigc.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
Obsoletes:	libsigc++ < 1.1
Obsoletes:	libsigc++-examples
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library implements a full callback system for use in widget
libraries, abstract interfaces, and general programming. Originally
part of the Gtk-- widget set, %{name} is now a seperate library to
provide for more general use. It is the most complete library of its
kind with the ablity to connect an abstract callback to a class
method, function, or function object. It contains adaptor classes for
connection of dissimilar callbacks and has an ease of use unmatched by
other C++ callback libraries.

%description -l pl.UTF-8
Ta biblioteka jest implementacją pełnego systemu callbacków do
używania w bibliotekach widgetów, interfejsach abstrakcyjnych i
ogólnym programowaniu. Oryginalnie była to część zestawu widgetów
Gtk--, ale jest teraz oddzielną biblioteką ogólniejszego
przeznaczenia. Jest to kompletna biblioteka tego typu z możliwością
łączenia abstrakcyjnych callbacków z metodami klas, funkcjami lub
obiektami funkcji. Zawiera klasy adapterów do łączenia różnych
callbacków.

%package devel
Summary:	Development tools for the Typesafe Signal Framework for C++
Summary(pl.UTF-8):	Narzędzia programistyczne do środowiska libsig++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	m4
Obsoletes:	libsigc++-devel < 1.1

%description devel
Development tools for the Typesafe Signal Framework for C++.

%description devel -l pl.UTF-8
Narzędzia programistyczne do środowiska libsigc++ - sygnałów z
kontrolą typów.

%package static
Summary:	Static Typesafe Signal Framework for C++ libraries
Summary(pl.UTF-8):	Statyczna biblioteka libsigc++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libsigc++-static < 1.1

%description static
Static Typesafe Signal Framework for C++ libraries.

%description static -l pl.UTF-8
Statyczna biblioteka libsigc++ - środowiska sygnałów z kontrolą typów.

%prep
%setup -q -n libsigc++-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
CXXFLAGS="%{rpmcflags} -fno-exceptions"
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

mv -f $RPM_BUILD_ROOT%{_aclocaldir}/{sigc++.m4,sigc++1.m4}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FEATURES IDEAS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/sigc-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/sigc++-*
%{_libdir}/sigc++-*
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
