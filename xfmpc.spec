%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A MPD client focusing on low footprint for Xfce
Name:		xfmpc
Version:	0.2.2
Release:	4
License:	BSD-like
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/applications/%{name}
Source0:	http://archive.xfce.org/src/apps/xfmpc/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	libxfce4ui-devel
BuildRequires:	libxfce4util-devel
BuildRequires:	libmpd-devel

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


%changelog
* Mon Apr 09 2012 Crispin Boylan <crisb@mandriva.org> 0.2.2-2mdv2012.0
+ Revision: 789963
- Rebuild

* Thu Oct 27 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.2-1
+ Revision: 707444
- update to new version 0.2.2
- fix url for source0

* Sun May 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.1-1
+ Revision: 672534
- update to new version 0.2.1
- add missing buildrequires

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0-4
+ Revision: 633062
- rebuild for new Xfce 4.8.0

* Sat Sep 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0-3mdv2011.0
+ Revision: 579668
- rebuild for new xfce 4.7.0

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0-2mdv2010.1
+ Revision: 543315
- rebuild for mdv 2010.1

* Mon Sep 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0-1mdv2010.0
+ Revision: 432952
- update to new version 0.2.0

* Mon May 25 2009 Funda Wang <fwang@mandriva.org> 0.1.0-1mdv2010.0
+ Revision: 379437
- rebuild for new mpd

* Mon Apr 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.0-1mdv2009.1
+ Revision: 364416
- update to new version 0.1.0

* Sun Mar 08 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.7-2mdv2009.1
+ Revision: 352876
- rebuild for xfce-4.6.0

* Tue Aug 26 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.7-1mdv2009.0
+ Revision: 276257
- update to new version 0.0.7

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 0.0.6-2mdv2009.0
+ Revision: 269797
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Apr 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.6-1mdv2009.0
+ Revision: 198091
- new version

* Tue Apr 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.5-1mdv2009.0
+ Revision: 192381
- new version

* Sun Feb 24 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.3-1mdv2008.1
+ Revision: 174137
- new release
- add desktop file
- add sources and spec file
- Created package structure for xfmpc.

