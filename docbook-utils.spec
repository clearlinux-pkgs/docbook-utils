#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : docbook-utils
Version  : 0.6.14
Release  : 8
URL      : ftp://sources.redhat.com/pub/docbook-tools/new-trials/SOURCES/docbook-utils-0.6.14.tar.gz
Source0  : ftp://sources.redhat.com/pub/docbook-tools/new-trials/SOURCES/docbook-utils-0.6.14.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: docbook-utils-bin
Requires: docbook-utils-doc
Requires: docbook-utils-data
Patch1: build.patch

%description


%package bin
Summary: bin components for the docbook-utils package.
Group: Binaries
Requires: docbook-utils-data

%description bin
bin components for the docbook-utils package.


%package doc
Summary: doc components for the docbook-utils package.
Group: Documentation

%description doc
doc components for the docbook-utils package.


%package data
Summary: data components for the docbook-utils package.
Group: Data

%description data
data components for the docbook-utils package.


%prep
%setup -q -n docbook-utils-0.6.14
%patch1 -p1

%build
%configure --disable-static 
make V=1 %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/docbook2dvi
/usr/bin/docbook2html
/usr/bin/docbook2man
/usr/bin/docbook2pdf
/usr/bin/docbook2ps
/usr/bin/docbook2rtf
/usr/bin/docbook2tex
/usr/bin/docbook2texi
/usr/bin/docbook2txt
/usr/bin/jw
/usr/bin/sgmldiff

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man7/*

%files data
%defattr(-,root,root,-)
/usr/share/sgml/docbook/utils-0.6.14/backends/dvi
/usr/share/sgml/docbook/utils-0.6.14/backends/html
/usr/share/sgml/docbook/utils-0.6.14/backends/man
/usr/share/sgml/docbook/utils-0.6.14/backends/pdf
/usr/share/sgml/docbook/utils-0.6.14/backends/ps
/usr/share/sgml/docbook/utils-0.6.14/backends/rtf
/usr/share/sgml/docbook/utils-0.6.14/backends/tex
/usr/share/sgml/docbook/utils-0.6.14/backends/texi
/usr/share/sgml/docbook/utils-0.6.14/backends/txt
/usr/share/sgml/docbook/utils-0.6.14/docbook-utils.dsl
/usr/share/sgml/docbook/utils-0.6.14/frontends/docbook
/usr/share/sgml/docbook/utils-0.6.14/helpers/docbook2man-spec.pl
/usr/share/sgml/docbook/utils-0.6.14/helpers/docbook2texi-spec.pl