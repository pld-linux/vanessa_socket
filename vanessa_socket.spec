Summary:	Simplify TCP/IP socket operations
Name:		vanessa_socket
Version:	0.0.3
Release:	1
License:	LGPL
Group:		Libraries
Group(cs):	Knihovny
Group(da):	Biblioteker
Group(de):	Bibliotheken
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(is):	Aðgerðasöfn
Group(it):	Librerie
Group(ja):	¥é¥¤¥Ö¥é¥ê
Group(no):	Biblioteker
Group(pl):	Biblioteki
Group(pt):	Bibliotecas
Group(pt_BR):	Bibliotecas
Group(ru):	âÉÂÌÉÏÔÅËÉ
Group(sl):	Knji¾nice
Group(sv):	Bibliotek
Group(uk):	â¦ÂÌ¦ÏÔÅËÉ
Source0:	ftp://vergenet.net/pub/vanessa_socket/vanessa_socket/%{name}-%{version}.tar.gz
URL:		http://vanessa.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	popt
BuildRequires:	sed
BuildRequires:	vanessa_logger-devel
Obsoletes:	libtcp_socket
Provides:	%{name}-%{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Library to simplify TCP/IP socket operations. Includes code to open a
socket to a server as a client, to listen on socket for clients as a
server and to pipe information between sockets.


%package devel
Summary:	Headers and static libraries for development
Group:		Development/Libraries
Group(cs):	Vývojové prostøedky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(is):	Þróunartól/Aðgerðasöfn
Group(it):	Sviluppo/Librerie
Group(ja):	³«È¯/¥é¥¤¥Ö¥é¥ê
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(sl):	Razvoj/Knji¾nice
Group(sv):	Utveckling/Bibliotek
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
Requires:	%{name}-%{version}
Requires:	vanessa_logger-devel

%description devel
Headers and static libraries required to develop against
vanessa_socket.

%package pipe
Summary:	Trivial TCP/IP pipe build using libvanessa_adt
Group:		Applications/System
Group(cs):	Aplikace/Systém
Group(da):	Programmer/System
Group(de):	Applikationen/System
Group(es):	Aplicaciones/Sistema
Group(fr):	Applications/Système
Group(is):	Forrit/Kerfisforrit
Group(it):	Applicazioni/Sistema
Group(ja):	¥¢¥×¥ê¥±¡¼¥·¥ç¥ó/¥·¥¹¥Æ¥à
Group(no):	Applikasjoner/System
Group(pl):	Aplikacje/System
Group(pt):	Aplicações/Sistema
Group(pt_BR):	Aplicações/Sistema
Group(ru):	ðÒÉÌÏÖÅÎÉÑ/óÉÓÔÅÍÁ
Group(sl):	Programi/Sistem
Group(sv):	Tillämpningar/System
License:	GPL
Requires:	%{name}-%{version}
Provides:	%{name}-pipe-%{version}

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
CFLAGS="${RPM_OPT_FLAGS}"
%{__make}


%install
rm -rf $RPM_BUILD_ROOT
install -d ${RPM_BUILD_ROOT}/{etc,%{_prefix}/{lib,bin,doc}}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf README ChangeLog NEWS TODO

%clean
rm -rf $RPM_BUILD_DIR/%{name}-%{version}
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.*a
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.so.0
%attr(644,root,root) %{_includedir}/*.h
%doc *.gz

%files pipe
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vanessa_socket_pipe
%{_mandir}/man1/*.1*
