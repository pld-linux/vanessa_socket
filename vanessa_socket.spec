Summary:	Simplify TCP/IP socket operations
Summary(pl.UTF-8):	Biblioteka upraszczająca operacje na gniazdach TCP/IP
Name:		vanessa_socket
Version:	0.0.10
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.vergenet.net/linux/vanessa/download/%{name}/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	6cf9c167650808f0626fbe4967e4bbcb
URL:		http://www.vergenet.net/linux/vanessa/
BuildRequires:	autoconf
BuildRequires:	popt-devel
BuildRequires:	vanessa_logger-devel >= 0.0.8
Requires:	vanessa_logger >= 0.0.8
Obsoletes:	libtcp_socket
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library to simplify TCP/IP socket operations. Includes code to open a
socket to a server as a client, to listen on socket for clients as a
server and to pipe information between sockets.

%description -l pl.UTF-8
Biblioteka upraszczająca operacje na gniazdach TCP/IP. Zawiera kod
otwierający gniazda do serwera jako klient, do słuchania jako serwer
oraz do przekazywania informacji między gniazdami.

%package devel
Summary:	Headers for vanessa_socket development
Summary(pl.UTF-8):	Pliki nagłówkowe vanessa_socket
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	vanessa_logger-devel >= 0.0.4

%description devel
Headers required to develop against vanessa_socket.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do tworzenia programów z użyciem
vanessa_socket.

%package static
Summary:	Static libraries for vanessa_socket development
Summary(pl.UTF-8):	Statyczne biblioteki vanessa_socket
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static vanessa_socket library.

%description static -l pl.UTF-8
Statyczna biblioteka vanessa_socket.

%package pipe
Summary:	Trivial TCP/IP pipe build using vanessa_socket
Summary(pl.UTF-8):	Prosta rurka TCP/IP stworzona przy użyciu vanessa_socket
License:	GPL
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description pipe
A TCP/IP pipe is a user space programme that listens for TCP/IP
connections on port on the local host and when a client connects makes
a connection to a TCP/IP port, possibly on another host. Once both
connections are established data sent on one connection is relayed to
the other, hence forming a bi-directional pipe.

Uses include enabling connections to specific ports on hosts behind a
packet filter.

This code is intended primarily as an example of how many of the
features of libvanessa_socket work.

%description pipe -l pl.UTF-8
Rurka TCP/IP to program w przestrzeni użytkownika, który oczekuje na
połączenia TCP/IP na lokalnym porcie, po czym łączy się jako klient na
inny port TCP/IP, który może być na innej maszynie. Po ustanowieniu
obu połączeń dane wysłane na jedno połączenie są przekazywane na
drugie, tworząc dwukierunkową rurkę.

Ten kod służy głównie jako przykład możliwości libvanessa_socket.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/vanessa_gethostbyname
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvanessa_socket.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files pipe
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vanessa_socket_pipe
%{_mandir}/man1/*.1*
