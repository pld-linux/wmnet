%define name wmnet
%define version 1.04
%define release 1

%define builddir $RPM_BUILD_DIR/%{name}-%{version}

Summary: Applet that monitors the network
Summary(fr): Applette qui surveille le réseau

Name: %{name}
Version: %{version}
Release: %{release}
Group: X11/Utilities
Copyright: GPL
Packager: Jesse B. Off <joff@iastate.edu>
Source0: %{name}-%{version}.tar.gz
Source1: %{name}.wmconfig
BuildRoot:	/tmp/%{name}-%{version}-root
Icon: %{name}.gif
Exclusiveos: Linux

%changelog


%description 
Wmnet uses ip accounting in the Linux kernel
to monitor your network.

%description -l fr
Wmnet utilise "l'ip accounting" dans le kernel
de Linux pour surveiller le réseau.

%prep

%setup

%build
xmkmf
make CFLAGS="$RPM_OPT_FLAGS"

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT ; fi
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin $RPM_BUILD_ROOT/etc/X11/wmconfig $RPM_BUILD_ROOT/usr/X11R6/man/man1
strip %{builddir}/wmnet
cp %{builddir}/wmnet $RPM_BUILD_ROOT/usr/X11R6/bin
cp %{builddir}/wmnet.man $RPM_BUILD_ROOT/usr/X11R6/man/man1/wmnet.1x
cp $RPM_SOURCE_DIR/%{name}.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/%{name}

%files
%doc TODO README Changelog
%attr(644,root,root) %config(missingok) /etc/X11/wmconfig/wmnet
%attr(755,root,root) /usr/X11R6/bin/wmnet
%attr(644,root,root) /usr/X11R6/man/man1/wmnet.1x

%clean
rm -r $RPM_BUILD_ROOT
rm -r %{builddir}

%post
if [ ! -e /proc/net/ip_acct ]; then
	echo "You must have IP accounting enabled in your kernel !"
fi
