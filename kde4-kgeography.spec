%define		_state		stable
%define		orgname		kgeography

Summary:	K Desktop Environment - A geography learning program
Summary(pl_PL.UTF8):	K Desktop Environment - Program do nauki geografii
Name:		kgeography
Version:	4.7.1
Release:	2
License:	GPL
Group:		X11/Applications/Science
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	9600b1a5d788475fa38ebfdeee6536fc
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel
Obsoletes:	kde4-kdeedu-kgeography < 4.6.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A geography learning program.

%description -l pl.UTF-8
Program do nauki geografii.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kgeography
%{_datadir}/apps/kgeography
%{_datadir}/config.kcfg/kgeography.kcfg
%{_desktopdir}/kde4/kgeography.desktop
%{_iconsdir}/hicolor/scalable/apps/kgeography.svgz
%{_iconsdir}/hicolor/*x*/apps/kgeography.png
