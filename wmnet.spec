Summary:	Applet that monitors the network
Summary(fr.UTF-8):	Applette qui surveille le réseau
Summary(pl.UTF-8):	Aplet monitorujący sieć
Name:		wmnet
Version:	1.06
Release:	4
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.digitalkaos.net/linux/wmnet/download/%{name}-%{version}.tar.gz
# Source0-md5:	64e74c37c0cb5fd4fb81cfb0f5c4a264
Source1:	%{name}.desktop
URL:		http://www.digitalkaos.net/linux/wmnet/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wmnet uses ip accounting in the Linux kernel to monitor your network.

%description -l fr.UTF-8
Wmnet utilise "l'ip accounting" dans le kernel de Linux pour
surveiller le réseau.

%description -l pl.UTF-8
Wmnet używa "ip accounting" w jądrze Linuksa do monitorowania sieci.

%prep
%setup -q

%build
xmkmf -a
%{__make} CFLAGS="%{rpmcflags} -Wall -I%{_includedir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_desktopdir}/docklets

install wmnet $RPM_BUILD_ROOT%{_bindir}
install wmnet.man $RPM_BUILD_ROOT%{_mandir}/man1/wmnet.1x
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ ! -e /proc/net/ip_acct ]; then
	echo "You must have IP accounting enabled in your kernel!"
fi

%files
%defattr(644,root,root,755)
%doc README Changelog

%attr(755,root,root) %{_bindir}/wmnet
%{_mandir}/man1/*
%{_desktopdir}/docklets/wmnet.desktop
