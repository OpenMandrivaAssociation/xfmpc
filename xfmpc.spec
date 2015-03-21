%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A MPD client focusing on low footprint for Xfce
Name:		xfmpc
Version:	0.2.2
Release:	9
License:	BSD-like
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/applications/%{name}
Source0:	http://archive.xfce.org/src/apps/xfmpc/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.11
BuildRequires:	pkgconfig(libxfce4util-1.0) >= 4.11
BuildRequires:	pkgconfig(libmpd)

%description
A MPD client focusing on low footprint for Xfce desktop environment.

%prep
%setup -q

%build
%define Werror_cflags %nil
%configure2_5x

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README ChangeLog
%{_bindir}/xfmpc
%{_datadir}/applications/*.desktop
%{_mandir}/man1/%{name}*
