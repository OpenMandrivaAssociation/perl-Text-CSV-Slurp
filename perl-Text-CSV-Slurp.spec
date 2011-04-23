%define upstream_name    Text-CSV-Slurp
%define upstream_version 0.9

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Convert CSV into an array of hashes, or an array of hashes into CSV
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(IO::Handle)
BuildRequires: perl(Test::Most)
BuildRequires: perl(Text::CSV)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Convert CSV into an array of hashes, or an array of hashes into CSV.

%prep
%setup -q -n %{upstream_name}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml README Changes LICENSE
%{_mandir}/man3/*
%perl_vendorlib/*


