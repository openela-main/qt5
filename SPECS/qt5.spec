
Name: qt5
Version: 5.15.3
Release: 1%{?dist}
Summary: Qt5 meta package
License: GPLv3
URL: https://getfedora.org/
Source0: macros.qt5
Source1: qmake-qt5.sh
BuildArch: noarch

Requires: qt5-qdbusviewer
Requires: qt5-qt3d
Requires: qt5-qtbase
Requires: qt5-qtbase-gui
Requires: qt5-qtbase-mysql
Requires: qt5-qtbase-postgresql
Requires: qt5-qtconnectivity
Requires: qt5-qtdeclarative
Requires: qt5-qtdoc
Requires: qt5-qtgraphicaleffects
Requires: qt5-qtimageformats
Requires: qt5-qtlocation
Requires: qt5-qtmultimedia
Requires: qt5-qtquickcontrols
Requires: qt5-qtquickcontrols2
Requires: qt5-qtscript
Requires: qt5-qtsensors
Requires: qt5-qtserialport
Requires: qt5-qtsvg
Requires: qt5-qttools
Requires: qt5-qtwayland
Requires: qt5-qtwebchannel
## qtwebengine is not available on all archs, omit for now
## else, need to make qt5 arch'd and deps conditional (on arch)
#Requires: qt5-qtwebengine
%if 0%{?fedora}
Requires: qt5-qtwebkit
%endif
Requires: qt5-qtwebsockets
Requires: qt5-qtx11extras
Requires: qt5-qtxmlpatterns

%description
%{summary}.

%package devel
Summary: Qt5 meta devel package
Requires: qt5-rpm-macros
Requires: qt5-qttools-static
Requires: qt5-qtdeclarative-static
Requires: qt5-qtbase-static
Requires: qt5-designer
Requires: qt5-qdoc
Requires: qt5-qhelpgenerator
Requires: qt5-linguist
Requires: qt5-qt3d-devel
Requires: qt5-qtbase-devel
Requires: qt5-qtconnectivity-devel
Requires: qt5-qtdeclarative-devel
Requires: qt5-qtlocation-devel
Requires: qt5-qtmultimedia-devel
Requires: qt5-qtscript-devel
Requires: qt5-qtsensors-devel
Requires: qt5-qtserialport-devel
Requires: qt5-qtsvg-devel
Requires: qt5-qttools-devel
Requires: qt5-qtwayland-devel
Requires: qt5-qtwebchannel-devel
%if 0%{?fedora}
#Requires: qt5-qtwebengine-devel
Requires: qt5-qtwebkit-devel
%endif
Requires: qt5-qtwebsockets-devel
Requires: qt5-qtx11extras-devel
Requires: qt5-qtxmlpatterns-devel

%description devel
%{summary}.

%package rpm-macros
Summary: RPM macros for building Qt5 and KDE Frameworks 5 packages
Conflicts: qt5-qtbase-devel < 5.6.0-0.23
%if 0%{?fedora} || 0%{?rhel} > 7
Requires: cmake >= 3
%endif
%if 0%{?epel}
Requires: cmake3
%endif
Requires: gcc-c++
%description rpm-macros
%{summary}.

%package srpm-macros
Summary: RPM macros for source Qt5 packages
%description srpm-macros
%{summary}.

%install
install -Dpm644 %{SOURCE0} %{buildroot}%{_rpmconfigdir}/macros.d/macros.qt5
install -Dpm755 %{SOURCE1} %{buildroot}%{_bindir}/qmake-qt5.sh
mkdir -p %{buildroot}%{_datadir}/qt5/wrappers
ln -s %{_bindir}/qmake-qt5.sh %{buildroot}%{_datadir}/qt5/wrappers/qmake-qt5
ln -s %{_bindir}/qmake-qt5.sh %{buildroot}%{_datadir}/qt5/wrappers/qmake

# substitute custom flags, and the path to binaries: binaries referenced from
# macros should not change if an application is built with a different prefix.
# %_libdir is left as /usr/%{_lib} (e.g.) so that the resulting macros are
# architecture independent, and don't hardcode /usr/lib or /usr/lib64.
sed -i \
  -e "s|@@QT5_CFLAGS@@|%{?qt5_cflags}|g" \
  -e "s|@@QT5_CXXFLAGS@@|%{?qt5_cxxflags}|g" \
  -e "s|@@QT5_RPM_LD_FLAGS@@|%{?qt5_rpm_ld_flags}|g" \
  -e "s|@@QT5_RPM_OPT_FLAGS@@|%{?qt5_rpm_opt_flags}|g" \
  -e "s|@@QMAKE@@|%{_prefix}/%%{_lib}/qt5/bin/qmake|g" \
  -e "s|@@QMAKE_QT5_WRAPPER@@|%{_bindir}/qmake-qt5.sh|g" \
  %{buildroot}%{_rpmconfigdir}/macros.d/macros.qt5

mkdir -p %{buildroot}%{_docdir}/qt5
mkdir -p %{buildroot}%{_docdir}/qt5-devel
echo "- Qt5 meta package" > %{buildroot}%{_docdir}/qt5/README
echo "- Qt5 devel meta package" > %{buildroot}%{_docdir}/qt5-devel/README

%files
%{_docdir}/qt5/README

%files devel
%{_docdir}/qt5-devel/README

%files rpm-macros
%{_rpmconfigdir}/macros.d/macros.qt5
%{_bindir}/qmake-qt5.sh
%{_datadir}/qt5/wrappers/

%files srpm-macros


%changelog
* Thu Mar 24 2022 Jan Grulich <jgrulich@redhat.com> - 5.15.3-1
- 5.15.3
  Resolves: bz#2061377

* Mon Mar 29 2021 Jan Grulich <jgrulich@redhat.com> - 5.15.2-1
- 5.15.2
  Resolves: bz#1928156

* Mon Mar 29 2021 Jan Grulich <jgrulich@redhat.com> - 5.15.1-1
- 5.15.1
  Resolves: bz#1928156

* Tue Oct 29 2019 Jan Grulich <jgrulich@redhat.com> - 5.12.5-3
- Re-add srpm macros, just leave them empty
  Resolves: bz#1733133

* Tue Oct 29 2019 Jan Grulich <jgrulich@redhat.com> - 5.12.5-2
- Drop srpm macros as we don't ship qtwebengine
  Resolves: bz#1733133

* Tue Oct 29 2019 Jan Grulich <jgrulich@redhat.com> - 5.12.5-1
- 5.12.5 + sync with Fedora
  Resolves: bz#1733133

* Mon Jul 09 2018 Jan Grulich <jgrulich@redhat.com> - 5.11.1-2
- drop dependency on qt5-qtenginio

* Thu Jun 28 2018 Jan Grulich <jgrulich@redhat.com> - 5.11.1-1
- 5.11.1
- sync with Fedora and enable CMake in buildroot for RHEL

* Mon May 14 2018 Jan Grulich <jgrulich@redhat.com> - 5.10.1-2
- Require qt5-qtwebkit only for Fedora

* Wed Mar 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.10.1-1
- 5.10.1
- rpm-macros: Requires: gcc-c++

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.10.0-4
- macros.qt5: fix path to qmake-qt5.sh wrapper

* Wed Jan 24 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.10.0-3
- use noarch-friendly paths for qmake-qt5.sh wrapper

* Wed Jan 24 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.10.0-2
- provide qmake-qt5.sh wrapper and new macro: %%qmake_qt5_wrapper

* Wed Jan 03 2018 Rex Dieter <rdieter@fedoraproject.org> 5.10.0-1
- 5.10.0

* Wed Jan 03 2018 Rex Dieter <rdieter@fedoraproject.org> 5.9.3-1
- 5.9.3

* Tue Oct 10 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.9.2-1
- 5.9.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.9.1-1
- 5.9.1

* Thu Jun 01 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.9.0-2
- drop -fno-delete-null-pointer-checks hack/workaround

* Sat Apr 15 2017 Helio Chissini de Castro <helio@kde.org> - 5.9.0-1
- Up to match upcoming 5.9.0

* Fri Mar 31 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.8.0-3
- rebuild

* Fri Jan 27 2017 Helio Chissini de Castro <helio@kde.org> - 5.8.0-1
- Tie to new upstream release

* Mon Jan 02 2017 Rex Dieter <rdieter@math.unl.edu> - 5.7.1-2
- drop Requires: qt5-gstreamer qt5-qtacountsservice qt5-qtconfiguration (not from qtproject.org)

* Wed Nov 09 2016 Helio Chissini de Castro <helio@kde.org> - 5.7.1-1
- Prepare for new release

* Tue Sep 27 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.0-10
- s/%%rhel/%%epel/ , cmake3 is only available in epel

* Wed Sep 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.0-9
- install the right macros.qt5-srpm file

* Wed Sep 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.0-8
- introduce -srpm-macros (initially defines %%qt5_qtwebengine_arches)
- -devel: drop Requires: qt5-qtwebengine-devel (since not all archs are supported)

* Sat Jul 23 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.0-7
- drop Requires: qt5-qtwebengine (not available on all archs)

* Tue Jul 12 2016 Helio Chissini de Castro <helio@kde.org> - 5.7.0-6
- Fix macros with invalid substitutions.

* Wed Jul 06 2016 Helio Chissini de Castro <helio@kde.org> - 5.7.0-5
- Fix typo. Thanks to Diego Herrera.
- Add macro qt5_includedir as more logical than headerdir. Old one still available

* Mon Jul 04 2016 Helio Chissini de Castro <helio@kde.org> - 5.7.0-4
- Clang is not default anymore. End of experimentation phase

* Wed Jun 15 2016 Helio Chissini de Castro <helio@kde.org> - 5.7.0-3
- Move package to be qt5 and create meta packages
- Add new macro for qml dir

* Mon Jun 13 2016 Helio Chissini de Castro <helio@kde.org> - 5.7.0-2
- Test repositories using clang by default


* Thu Jun 09 2016 Helio Chissini de Castro <helio@kde.org> - 5.7.0-1
- Decouple macros from main qtbase package
