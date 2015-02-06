%define upstream_name    Text-CSV-Slurp
%define upstream_version 1.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Convert CSV into an array of hashes, or an array of hashes into CSV
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/Text-CSV-Slurp-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(Test::Most)
BuildRequires:	perl(Text::CSV)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Differences)
BuildRequires:	perl(Test::Deep)
BuildArch:	noarch

%description
Convert CSV into an array of hashes, or an array of hashes into CSV.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml README Changes LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 24 2011 Funda Wang <fwang@mandriva.org> 0.900.0-2mdv2011.0
+ Revision: 658195
- add more br
- rebuild for updated spec-helper

* Mon Feb 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.900.0-1
+ Revision: 636686
- new version

* Thu May 06 2010 Michael Scherer <misc@mandriva.org> 0.800.0-1mdv2011.0
+ Revision: 542849
- import perl-Text-CSV-Slurp


* Thu May 06 2010 cpan2dist 0.8-1mdv
- initial mdv release, generated with cpan2dist

