Summary:	An interpreter for the awk programming language
Name:		mawk
Version:	1.3.3
Release:	23
License:	GPLv2+
Group:		Development/Other
Url:		http://www.math.fu-berlin.de/~leitner/mawk/
Source0:	mawk1.3.3.tar.bz2
Patch0:		mawk1.2.2-prefix.patch
Patch1:		mawk1.3.3-LDFLAGS.diff

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
mkdir -p %{buildroot}{%{_bindir},%{_mandir}/man1}
%makeinstall

%files
%doc ACKNOWLEDGMENT CHANGES INSTALL README
%{_bindir}/mawk
%{_mandir}/man1/*

