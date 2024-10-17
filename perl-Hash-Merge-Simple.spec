%define upstream_name    Hash-Merge-Simple
%define upstream_version 0.051

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Recursively merge two or more hashes, simply
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Hash/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Most)
BuildRequires:	perl(Test::Warn)
BuildArch:	noarch

%description
Hash::Merge::Simple will recursively merge two or more hashes and return
the result as a new hash reference. The merge function will descend and
merge hashes that exist under the same node in both the left and right
hash, but doesn't attempt to combine arrays, objects, scalars, or anything
else. The rightmost hash also takes precedence, replacing whatever was in
the left hash if a conflict occurs.

This code was pretty much taken straight from the Catalyst::Utils manpage,
and modified to handle more than 2 hashes at the same time.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.51.0-2mdv2011.0
+ Revision: 656930
- rebuild for updated spec-helper

* Wed Dec 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.51.0-1mdv2011.0
+ Revision: 616208
- update to new version 0.051

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 552321
- update to 0.05

* Fri May 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 381004
- adding missing buildrequires:
- import perl-Hash-Merge-Simple


* Fri May 29 2009 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist

