Summary:	An interpreter for the awk programming language
Name:		mawk
Version:	1.3.4_20230808
Release:	1
License:	GPLv2+
Group:		Development/Other
Url:		https://invisible-island.net/mawk/
Source0:	https://invisible-island.net/archives/mawk/mawk-%(echo %{version}|sed -e 's,_,-,g').tgz
BuildRequires:	byacc
BuildRequires:	bison
BuildRequires:	groff-base
BuildRequires:	ctags

%description
Mawk is a version of the awk programming language.  Awk interprets a 
special-purpose programming language to do quick text pattern matching
and reformatting.  Mawk improves on awk in certain ways and can 
sometimes outperform gawk, the standard awk program for Linux.  Mawk
conforms to the POSIX 1003.2 (draft 11.3) definition of awk.

You should install mawk if you use awk.

%prep
%autosetup -n %{name}-%(echo %{version}|sed -e 's,_,-,g') -p1
chmod -R a+r .

%build
%configure
%make_build

%install
mkdir -p %{buildroot}{%{_bindir},%{_mandir}/man1}
%make_install

%files
%doc ACKNOWLEDGMENT CHANGES README
%{_bindir}/mawk
%doc %{_mandir}/man1/*
%doc %{_mandir}/man7/*
