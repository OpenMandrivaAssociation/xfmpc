%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A MPD client focusing on low footprint for Xfce
Name:		xfmpc
Version:	0.2.2
Release:	%mkrel 2
License:	BSD-like
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/applications/%{name}
Source0:	http://archive.xfce.org/src/apps/xfmpc/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	libxfce4ui-devel
BuildRequires:	libxfce4util-devel
BuildRequires:	libmpd-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A MPD client focusing on low footprint for Xfce desktop environment.

%prep
%setup -q

%build
%define Werror_cflags %nil
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%{_bindir}/xfmpc
%{_datadir}/applications/*.desktop
%{_mandir}/man1/%{name}*
