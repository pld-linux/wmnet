Summary:	Applet that monitors the network
Summary(fr):	Applette qui surveille le réseau
Summary(pl):	Aplet monitoruj±cy sieæ
Name:		wmnet
Version:	1.04
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://www.digitalkaos.net/linux/wmnet/download/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Icon:		wmnet.gif
URL:		http://www.digitalkaos.net/linux/wmnet/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix 	/usr/X11R6
%define 	_mandir 	%{_prefix}/man

%description 
Wmnet uses ip accounting in the Linux kernel to monitor your network.

%description -l fr
Wmnet utilise "l'ip accounting" dans le kernel de Linux pour
surveiller le réseau.

%description -l pl
Wmnet u¿ywa "ip accounting" w j±drze Linuksa do monitorowania sieci.

%prep
%setup -q

%build
xmkmf -a
%{__make} CFLAGS="%{rpmcflags} -Wall -I%{_includedir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_applnkdir}/DockApplets

install wmnet $RPM_BUILD_ROOT%{_bindir}
install wmnet.man $RPM_BUILD_ROOT%{_mandir}/man1/wmnet.1x
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf TODO README Changelog

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ ! -e /proc/net/ip_acct ]; then
        echo "You must have IP accounting enabled in your kernel!"
fi

%files
%defattr(644,root,root,755)
%doc *.gz

%attr(755,root,root) %{_bindir}/wmnet
%{_mandir}/man1/*

%{_applnkdir}/DockApplets/wmnet.desktop
