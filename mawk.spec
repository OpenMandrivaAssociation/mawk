Summary:	An interpreter for the awk programming language
Name:		mawk
Version:	1.3.3
Release: 	%mkrel 16
License:	GPLv2+
Group:		Development/Other
URL:		http://www.math.fu-berlin.de/~leitner/mawk/
Source0:	mawk1.3.3.tar.bz2
Patch0:		mawk1.2.2-prefix.patch
Patch1:		mawk1.3.3-LDFLAGS.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Mawk is a version of the awk programming language.  Awk interprets a 
special-purpose programming language to do quick text pattern matching
and reformatting.  Mawk improves on awk in certain ways and can 
sometimes outperform gawk, the standard awk program for Linux.  Mawk
conforms to the POSIX 1003.2 (draft 11.3) definition of awk.

You should install mawk if you use awk.

%prep

%setup -q
%patch0 -p1
%patch1 -p0 -b .LDFLAGS
chmod -R a+r .

%build
# (Dadou) Don't use configure macro, it doesn't work
# no need for --libdir, since there is only binary and man
MATHLIB="-lm" LDFLAGS="%{ldflags}" ./configure

OPT_FLAGS=`echo "$RPM_OPT_FLAGS" | sed -e "s/-ffast-math//g"`
make CFLAGS="$OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/mawk
%{_mandir}/man1/*
%doc ACKNOWLEDGMENT CHANGES INSTALL README




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.3-15mdv2011.0
+ Revision: 666394
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.3-14mdv2011.0
+ Revision: 606632
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.3-13mdv2010.1
+ Revision: 519038
- rebuild

  + Sandro Cazzaniga <kharec@mandriva.org>
    - fix licence

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.3.3-11mdv2010.0
+ Revision: 426079
- rebuild

* Sun Dec 21 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.3-10mdv2009.1
+ Revision: 317075
- use %%ldflags (P1)

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.3.3-9mdv2009.0
+ Revision: 223225
- rebuild
- fix no-buildroot-tag

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.3.3-8mdv2008.1
+ Revision: 129783
- kill re-definition of %%buildroot on Pixel's request


* Wed Mar 07 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3.3-8mdv2007.0
+ Revision: 134436
- Import mawk

* Wed Mar 07 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3.3-8mdv2007.1
- use the %%mkrel macro

* Fri Oct 14 2005 Pixel <pixel@mandriva.com> 1.3.3-7mdk
- rebuild

