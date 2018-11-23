#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Number-Compare
Version  : 0.03
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Number-Compare-0.03.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Number-Compare-0.03.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libn/libnumber-compare-perl/libnumber-compare-perl_0.03-1.debian.tar.gz
Summary  : ~
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Number-Compare-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
No detailed description available

%package dev
Summary: dev components for the perl-Number-Compare package.
Group: Development
Provides: perl-Number-Compare-devel = %{version}-%{release}

%description dev
dev components for the perl-Number-Compare package.


%package license
Summary: license components for the perl-Number-Compare package.
Group: Default

%description license
license components for the perl-Number-Compare package.


%prep
%setup -q -n Number-Compare-0.03
cd ..
%setup -q -T -D -n Number-Compare-0.03 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Number-Compare-0.03/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Number-Compare
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Number-Compare/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/Number/Compare.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Number::Compare.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Number-Compare/deblicense_copyright
