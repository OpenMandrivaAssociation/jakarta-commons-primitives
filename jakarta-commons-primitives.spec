# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define section free
%define shortname commons-primitives
%define gcj_support 1

Name:           jakarta-%{shortname}
Version:        1.0
Release:        3.0.7
Epoch:          0
Summary:        Jakarta Commons Primitives Component

License:        Apache Software License
Group:          Development/Java
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:            https://jakarta.apache.org/commons/primitives/
Source0:        http://archive.apache.org/dist/jakarta/commons/primitives/source/commons-primitives-1.0-src.tar.gz
Patch0:         %{name}-crosslink.patch

%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%else
BuildArch:      noarch
BuildRequires:  java-devel
%endif
BuildRequires:  java-rpmbuild >= 0:1.5
#BuildRequires:  java-javadoc
BuildRequires:  ant
BuildRequires:  junit
Provides:       %{shortname} = %{epoch}:%{version}-%{release}

%description
Apache Jakarta Commons Primitives provides a collection of types and
utilities optimized for working with Java primitives (boolean, byte,
char, double, float, int, long, short). Generally, the
Commons-Primitives classes are smaller, faster and easier to work with
than their purely Object based alternatives.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java

%description    javadoc
Javadoc for %{name}.


%prep
%setup -q -n %{shortname}-%{version}
%patch0 -p0


%build
# No unit tests yet, would require commons-collections snapshot.
%{ant} \
  -Dfinal.name=%{name}-%{version} \
  -Dj2se.apidoc=%{_javadocdir}/java \
  jar javadoc


%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 644 target/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{shortname}-%{version}.jar
ln -s %{shortname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{shortname}.jar
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pR target/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%clean
rm -rf $RPM_BUILD_ROOT


%if %{gcj_support}
%post
%{update_gcjdb}

%postun
%{clean_gcjdb}
%endif

%files
%defattr(0644,root,root,0755)
%doc LICENSE.txt
%{_javadir}/*.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*
%endif

%files javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0:1.0-3.0.6mdv2011.0
+ Revision: 619761
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0:1.0-3.0.5mdv2010.0
+ Revision: 429589
- rebuild

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 0:1.0-3.0.4mdv2009.0
+ Revision: 167951
- fix no-buildroot-tag
- kill re-definition of %%buildroot on Pixel's request

* Sun Dec 16 2007 Anssi Hannula <anssi@mandriva.org> 0:1.0-3.0.4mdv2008.1
+ Revision: 120918
- buildrequire java-rpmbuild, i.e. build with icedtea on x86(_64)

* Sat Sep 15 2007 Anssi Hannula <anssi@mandriva.org> 0:1.0-3.0.3mdv2008.0
+ Revision: 87417
- rebuild to filter out autorequires of GCJ AOT objects
- remove unnecessary Requires(post) on java-gcj-compat

* Sat Aug 04 2007 David Walluck <walluck@mandriva.org> 0:1.0-3.0.2mdv2008.0
+ Revision: 58798
- bump release

* Thu Aug 02 2007 David Walluck <walluck@mandriva.org> 0:1.0-3.0.1mdv2008.0
+ Revision: 58336
- Import jakarta-commons-primitives




* Mon Jul 09 2007 Alexander Kurtakov <akurtakov@active-lynx.com> - 0:1.0-3.0.1mdv2008.0
- Add gcj support
- Use mdv macros

* Mon May 29 2006 Fernando Nasser <fnasser@redhat.com> - 0:1.0-3jpp
- First JPP 1.7 build

* Sun Aug 23 2004 Randy Watler <rwatler at finali.com> - 0:1.0-2jpp
- Rebuild with ant-1.6.2

* Sun Dec 14 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.0-1jpp
- First build.
