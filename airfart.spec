Name:		airfart
Summary:	Wireless network discovery tool
Version:	0.2.1
Release:	12
License:	GPLv2
Group:		Networking/Other
URL:		http://airfart.sourceforge.net/
Source:		%{name}-v%{version}.tar.bz2
Patch0:		airfart-v0.2.1-fix-gcc43.patch
Patch1:		airfart-v0.2.1-fix-link.patch
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(pangox)
BuildRequires:	pkgconfig(pangoxft)
Requires:	prism2-utils
Requires:	gksu

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
%make C_FLAGS="-g %{optflags}" LDFLAGS="%{ldflags}"

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datadir}/pixmaps/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
cp %{name} %{buildroot}%{_bindir}
bzip2 %{name}.1
cp %{name}.1.bz2 %{buildroot}%{_mandir}/man1
cp graphics/* %{buildroot}%{_datadir}/pixmaps/%{name}
cp manuf %{buildroot}%{_datadir}/%{name}

#menu

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{summary}
Exec=gksu %{_bindir}/%{name}
Icon=networking_section
Terminal=false
Type=Application
Categories=GTK;Settings;Network;
Encoding=UTF-8
EOF

%files
%doc README Authors ChangeLog TODO LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_mandir}/man1/*
%{_datadir}/pixmaps/%{name}
%{_datadir}/%{name}

