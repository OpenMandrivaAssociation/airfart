%define name	airfart
%define version	0.2.1
%define release %mkrel 9

Name: 	 	%{name}
Summary: 	Wireless network discovery tool
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-v%{version}.tar.bz2
Patch0:		airfart-v0.2.1-fix-gcc43.patch
Patch1:		airfart-v0.2.1-fix-link.patch
URL:		http://airfart.sourceforge.net/
License:	GPL
Group:		Networking/Other
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	gtk+2-devel
Requires:	prism2-utils gksu

%description
AirFart is a wireless tool created to detect wireless devices, calculate their
signal strengths, and present them to the user in an easy-to-understand
fashion. It is written in C/C++ with a GTK front end. Airfart supports all
wireless network cards supported by the linux-wlan-ng Prism2 driver that
provide hardware signal strength information in the "raw signal" format
(ssi_type 3). Airfart implements a modular n-tier architecture with the data
collection at the bottom tier and a graphical user interface at the top.

%prep
%setup -q -n %name
%patch0 -p0
%patch1 -p0 -b .link

%build
%make C_FLAGS="-g %optflags" LDFLAGS="%{ldflags}"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir
mkdir -p $RPM_BUILD_ROOT/%_mandir/man1
mkdir -p $RPM_BUILD_ROOT/%_datadir/pixmaps/%name
mkdir -p $RPM_BUILD_ROOT/%_datadir/%name
cp %name $RPM_BUILD_ROOT/%_bindir
bzip2 %name.1
cp %name.1.bz2 $RPM_BUILD_ROOT/%_mandir/man1
cp graphics/* $RPM_BUILD_ROOT/%_datadir/pixmaps/%name
cp manuf $RPM_BUILD_ROOT/%_datadir/%name

#menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{summary}
Exec=gksu %{_bindir}/%{name}
Icon=networking_section
Terminal=false
Type=Application
Categories=GTK;X-MandrivaLinux-System-Configuration-Networking;Settings;Network;
Encoding=UTF-8
EOF

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc README Authors ChangeLog TODO LICENSE
%{_bindir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
%{_mandir}/man1/*
%{_datadir}/pixmaps/%name
%{_datadir}/%name
