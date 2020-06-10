%define major 5
%define libname %mklibname KF5KGeoMap %{major}
%define devname %mklibname KF5KGeoMap -d

Summary:	Library for browsing and arranging photos on a map
Name:		libkgeomap
Version:	20.04.2
Release:	1
Epoch:		2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Source1:	%{name}.rpmlintrc
BuildRequires:	cmake(ECM)
#BuildRequires:	cmake(Marble)
BuildRequires:	marble-devel
BuildRequires:	cmake(KF5KExiv2)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Test)

%description
Library for browsing and arranging photos on a map.

#----------------------------------------------------------------------------

%package common
Summary:	Data files for browsing and arranging photos on a map library
Group:		Graphical desktop/KDE

%description common
Data files for browsing and arranging photos on a map library.

%files common -f %{name}.lang
%dir %{_datadir}/libkgeomap
%{_datadir}/libkgeomap/*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library for browsing and arranging photos on a map
Group:		System/Libraries
Requires:	%{name}-common = %{EVRD}
Obsoletes:	%{mklibname kgeomap 2} < 2:15.12.0

%description -n %{libname}
Library for browsing and arranging photos on a map.

%files -n %{libname}
%{_libdir}/libKF5KGeoMap.so.%{major}*
%{_libdir}/libKF5KGeoMap.so.10*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{mklibname kgeomap -d} < 2:15.12.0

%description -n %{devname}
Development files for %{name}.

%files -n %{devname}
%{_includedir}/KF5/KGeoMap
%{_includedir}/KF5/libkgeomap_version.h
%{_libdir}/cmake/KF5KGeoMap
%{_libdir}/*.so

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

# (tpg) not needed for now
rm -rf %{buildroot}%{_bindir}/libkgeomap_demo
%find_lang libkgeomap
