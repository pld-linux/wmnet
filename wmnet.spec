Summary:	Applet that monitors the network
Summary(fr):	Applette qui surveille le réseau
Summary(pl):	Aplet monitoruj±cy sieæ
Name:		wmnet
Version:	1.04
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	%{name}-%{version}.tar.gz
Source1:	wmnet.desktop
Icon:		wmnet.gif
URL:		http://isufug.ee.iastate.edu/~joff/wmnet.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix 	/usr/X11R6
%define 	_mandir 	%{_prefix}/man

%description 
Wmnet uses ip accounting in the Linux kernel to monitor your network.

%description -l fr
Wmnet utilise "l'ip accounting" dans le kernel de Linux pour
surveiller le réseau.

%description -l pl
Wmnet u¿ywa "ip accounting" w j±drze Linuxa do monitorowania sieci.

%prep
%setup -q

%build
xmkmf -a
%{__make} CFLAGS="$RPM_OPT_FLAGS -Wall -I%{_includedir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_applnkdir}/DockApplets

install -s wmnet $RPM_BUILD_ROOT%{_bindir}
install wmnet.man $RPM_BUILD_ROOT%{_mandir}/man1/wmnet.1x
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

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

%{_applnkdir}/DockApplets/wmnet.desktop
