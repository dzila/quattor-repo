Name:           quattor-repo
Version:        13.9.1
Release:        1
Summary:        RPM Package containing quattor yum repository
Group: 		System Environment/Base
License:        Apache
Source0:	quattor.repo
URL:		http://yum.quattor.org
BuildArch: 	noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Installs the quattor yum repository


%prep
%setup -cT

%build


%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/yum.repos.d/
cp -p %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
/etc/yum.repos.d/quattor.repo

%changelog
* Tue Oct 01 2013 Dimitrios Zilaskos  <dimitrios.zilaskos@stfc.ac.uk> 13.9.1
- This is the rpm installing quattor yum repo
