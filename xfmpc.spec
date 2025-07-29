%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A MPD client focusing on low footprint for Xfce
Name:		xfmpc
Version:	0.4.0
Release:	1
License:	BSD-like
Group:		Graphical desktop/Xfce
Url:		https://goodies.xfce.org/projects/applications/%{name}
Source0:	https://archive.xfce.org/src/apps/xfmpc/%{url_ver}/%{name}-%{version}.tar.bz2

BuildRequires:  meson
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(libmpd)
BuildRequires:  pkgconfig(vapigen)
  
Requires:	mpd  

%description
A MPD client focusing on low footprint for Xfce desktop environment.

%prep
%autosetup -p1

%build
%define Werror_cflags %nil
%meson

%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README*
%{_bindir}/xfmpc
%{_datadir}/applications/*.desktop
%{_mandir}/man1/%{name}*
