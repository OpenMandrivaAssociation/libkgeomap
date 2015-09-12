%define major 2
%define libname %mklibname kgeomap %{major}
%define devname %mklibname kgeomap -d

Summary:	Library for browsing and arranging photos on a map
Name:		libkgeomap
Version:	15.08.0
Release:	2
Epoch:		2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel
BuildRequires:	marble-devel
BuildRequires:	pkgconfig(libkexiv2)

%description
Library for browsing and arranging photos on a map.

#----------------------------------------------------------------------------

%package common
Summary:	Data files for browsing and arranging photos on a map library
Group:		Graphical desktop/KDE
BuildArch:	noarch

%description common
Data files for browsing and arranging photos on a map library.

%files common
%dir %{_kde_appsdir}/libkgeomap/
%{_kde_appsdir}/libkgeomap/*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library for browsing and arranging photos on a map
Group:		System/Libraries
Requires:	%{name}-common

%description -n %{libname}
Library for browsing and arranging photos on a map.

%files -n %{libname}
%{_kde_libdir}/libkgeomap.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development files for %{name}.

%files -n %{devname}
%{_kde_appsdir}/cmake/modules/FindKGeoMap.cmake
%dir %{_kde_includedir}/libkgeomap/
%{_kde_includedir}/libkgeomap/*.h
%{_kde_libdir}/libkgeomap.so
%{_kde_libdir}/pkgconfig/libkgeomap.pc

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build

# Seems to be useless
rm -f %{buildroot}%{_kde_bindir}/libkgeomap_demo

