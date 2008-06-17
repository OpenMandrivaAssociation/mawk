Summary:	An interpreter for the awk programming language
Name:		mawk
Version:	1.3.3
Release: 	%mkrel 9
License:	GPL
Group:		Development/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.math.fu-berlin.de/~leitner/mawk/
Source:		mawk1.3.3.tar.bz2
Patch:		mawk1.2.2-prefix.patch

%description
Mawk is a version of the awk programming language.  Awk interprets a 
special-purpose programming language to do quick text pattern matching
and reformatting.  Mawk improves on awk in certain ways and can 
sometimes outperform gawk, the standard awk program for Linux.  Mawk
conforms to the POSIX 1003.2 (draft 11.3) definition of awk.

You should install mawk if you use awk.

%prep

%setup -q
%patch -p1
chmod -R a+r .

%build
# (Dadou) Don't use configure macro, it doesn't work
# no need for --libdir, since there is only binary and man
MATHLIB=-lm ./configure

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


