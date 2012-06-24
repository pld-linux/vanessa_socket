Summary:	Simplify TCP/IP socket operations
Summary(pl):	Biblioteka upraszczaj�ca operacje na gniazdach TCP/IP
Name:		vanessa_socket
Version:	0.0.3
Release:	2
License:	LGPL
Group:		Libraries
Group(cs):	Knihovny
Group(da):	Biblioteker
Group(de):	Bibliotheken
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(is):	A�ger�as�fn
Group(it):	Librerie
Group(ja):	�饤�֥��
Group(no):	Biblioteker
Group(pl):	Biblioteki
Group(pt):	Bibliotecas
Group(pt_BR):	Bibliotecas
Group(ru):	����������
Group(sl):	Knji�nice
Group(sv):	Bibliotek
Group(uk):	��̦�����
Source0:	ftp://vergenet.net/pub/vanessa_socket/vanessa_socket/%{name}-%{version}.tar.gz
URL:		http://vanessa.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	popt-devel
BuildRequires:	vanessa_logger-devel
Obsoletes:	libtcp_socket
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library to simplify TCP/IP socket operations. Includes code to open a
socket to a server as a client, to listen on socket for clients as a
server and to pipe information between sockets.

%description -l pl
Biblioteka upraszczaj�ca operacje na gniazdach TCP/IP. Zawiera kod
otwieraj�cy gniazda do serwera jako klient, do s�uchania jako serwer
oraz do przekazywania informacji mi�dzy gniazdami.

%package devel
Summary:	Headers for vanessa_socket development
Summary(pl):	Pliki nag��wkowe vanessa_socket
Group:		Development/Libraries
Group(cs):	V�vojov� prost�edky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(is):	�r�unart�l/A�ger�as�fn
Group(it):	Sviluppo/Librerie
Group(ja):	��ȯ/�饤�֥��
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(sl):	Razvoj/Knji�nice
Group(sv):	Utveckling/Bibliotek
Group(uk):	��������/��̦�����
Requires:	%{name} = %{version}
Requires:	vanessa_logger-devel

%description devel
Headers required to develop against vanessa_socket.

%description devel -l pl
Pliki nag��wkowe potrzebne do tworzenia program�w z u�yciem
vanessa_socket.

%package static
Summary:	Static libraries for vanessa_socket development
Summary(pl):	Statyczne biblioteki vanessa_socket
Group:		Development/Libraries
Group(cs):	V�vojov� prost�edky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(is):	�r�unart�l/A�ger�as�fn
Group(it):	Sviluppo/Librerie
Group(ja):	��ȯ/�饤�֥��
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(sl):	Razvoj/Knji�nice
Group(sv):	Utveckling/Bibliotek
Group(uk):	��������/��̦�����
Requires:	%{name}-devel = %{version}

%description static
Static vanessa_socket library.

%description static -l pl
Statyczna biblioteka vanessa_socket.

%package pipe
Summary:	Trivial TCP/IP pipe build using vanessa_socket
Summary(pl):	Prosta rurka TCP/IP stworzona przy u�yciu vanessa_socket
License:	GPL
Group:		Applications/System
Group(cs):	Aplikace/Syst�m
Group(da):	Programmer/System
Group(de):	Applikationen/System
Group(es):	Aplicaciones/Sistema
Group(fr):	Applications/Syst�me
Group(is):	Forrit/Kerfisforrit
Group(it):	Applicazioni/Sistema
Group(ja):	���ץꥱ�������/�����ƥ�
Group(no):	Applikasjoner/System
Group(pl):	Aplikacje/System
Group(pt):	Aplica��es/Sistema
Group(pt_BR):	Aplica��es/Sistema
Group(ru):	����������/�������
Group(sl):	Programi/Sistem
Group(sv):	Till�mpningar/System
Requires:	%{name} = %{version}

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

%description pipe -l pl
Rurka TCP/IP to program w przestrzeni u�ytkownika, kt�ry oczekuje na
po��czenia TCP/IP na lokalnym porcie, po czym ��czy si� jako klient
na inny port TCP/IP, kt�ry mo�e by� na innej maszynie. Po ustanowieniu
obu po��cze� dane wys�ane na jedno po��czenie s� przekazywane na
drugie, tworz�c dwukierunkow� rurk�.

Ten kod s�u�y g��wnie jako przyk�ad mo�liwo�ci libvanessa_socket.

%prep
%setup -q

%build
sed -e s/AC_PROG_RANLIB/AC_PROG_LIBTOOL/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in

rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure
CFLAGS="%{rpmcflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_prefix}/{lib,bin,doc}}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf README ChangeLog NEWS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/*.la
%attr(755,root,root) %{_libdir}/*.so
%attr(644,root,root) %{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files pipe
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vanessa_socket_pipe
%{_mandir}/man1/*.1*
