Summary:	A MPD client focusing on low footprint for Xfce
Name:		xfmpc
Version:	0.0.6
Release:	%mkrel 1
License:	BSD-like
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/applications/%{name}
Source0:	http://goodies.xfce.org/releases/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	libxfcegui4-devel
BuildRequires:	libmpd-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A MPD client focusing on low footprint for Xfce desktop environment.

%prep
%setup -q

%build
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor

%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%{_bindir}/xfmpc
%{_datadir}/applications/*.desktop
