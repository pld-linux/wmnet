Summary: 	Applet that monitors the network
Summary(fr): 	Applette qui surveille le réseau
Summary(pl):	Aplet monitoruj±cy sieæ
Name:		wmnet
Version:	1.04
Release:	2
Copyright:      GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	%{name}-%{version}.tar.gz
Source1:	wmnet.desktop
Icon: 		wmnet.gif
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix /usr/X11R6
%define _mandir %{_prefix}/man

%description 
Wmnet uses ip accounting in the Linux kernel to monitor your network.

%description -l fr
Wmnet utilise "l'ip accounting" dans le kernel de Linux pour surveiller 
le réseau.

%description -l pl
Wmnet u¿ywa "ip accounting" w j±drze Linuxa do monitorowania sieci.

%prep
%setup -q

%build
xmkmf -a
make CFLAGS="$RPM_OPT_FLAGS -Wall -I/usr/X11R6/include"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT/etc/X11/applnk/DockApplets 

install -s wmnet $RPM_BUILD_ROOT%{_bindir}
install wmnet.man $RPM_BUILD_ROOT%{_mandir}/man1/wmnet.1x
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/applnk/DockApplets

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	TODO README Changelog

%post
if [ ! -e /proc/net/ip_acct ]; then
        echo "You must have IP accounting enabled in your kernel !"
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {TODO,README,Changelog}.gz

%attr(755,root,root) %{_bindir}/wmnet
%{_mandir}/man1/*

/etc/X11/applnk/DockApplets/wmnet.desktop

%changelog
* Sun Jul 11 1999 Piotr Czerwiñski <pius@pld.org.pl> 
  [1.04-2]
- spec rewritten for PLD use,
- based on spec file by Jesse B. Off <joff@iastate.edu>.
