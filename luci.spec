Summary:	LUCI is a Universal Configuration Interface
Summary(pl):	LUCI to Universalny Configurator Interfejsu 
Name:		luci
Version:	0.2.2
Release:	1
License:	GPL
Group:		X11/Aplications
Vendor:		Jerome@SAUTRET.org
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	25fc7dae4fc0012674e2d75f80e32d2a
URL:		http://jsautret.free.fr/luci/
#Patch0:		luci.etc-descdir.patch
Requires:	python
Requires:	python-pygtk
BuildRequires:	python
BuildRequires:	python-modules
BuildRequires:	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LUCI provides a way to edit any configuration file by using a graphical interface 
instead of a text editor. 
     
%description -l pl
LUCI daje mo¿liwo¶æ edycji dowolnego pliku konfiguracyjnego przez wykorzystanie 
graficznego interfejsu, zamiast edytora terkstowego.

#%package subpackage
#Summary:	-
#Summary(pl):	-
#Group:		-

#%description subpackage

#%description subpackage -l pl

%prep
%setup -q -n %{name}-%{version} 
#%patch0 -p1

%build
rm -f missing

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
mkdir ./dest/
python install.py PREFIX=$RPM_BUILD_ROOT/usr/
cp -fpr ./dest/* $RPM_BUILD_ROOT/

%clean
#rm -rf $RPM_BUILD_ROOT

#%pre

#%post

#%preun

#%postun

%files
%defattr(644,root,root,755)
%doc  BUGS COPIER COPYING INSTALL NEWS README THANKS TODO
#%{_datadir}/doc/%{name}-%{version}/*
%{_sysconfdir}/luci/environement/*
%{_sysconfdir}/luci/system/network/*
%{_sysconfdir}/luci/system/users/*
%{_libdir}/%{name}/*
%defattr(755,root,root)
%{_bindir}/*

#%files subpackage
#%defattr(644,root,root,755)
#%doc extras/*.gz
#%{_datadir}/%{name}-ext
