Summary:	Universal Configuration Interface
Summary(pl):	Uniwersalny interfejs konfiguracyjny
Name:		luci
Version:	0.2.2
Release:	1
License:	GPL
Group:		X11/Aplications
Vendor:		Jerome@SAUTRET.org
Source0:	http://jsautret.free.fr/luci/%{name}-%{version}.tar.gz
# Source0-md5:	25fc7dae4fc0012674e2d75f80e32d2a
URL:		http://jsautret.free.fr/luci/
Requires:	python
Requires:	python-pygtk
BuildRequires:	python
BuildRequires:	python-modules
BuildRequires:	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LUCI provides a way to edit any configuration file by using 
a graphical interface instead of a text editor. 
     
%description -l pl
LUCI daje mo¿liwo¶æ edycji dowolnego pliku konfiguracyjnego przy
pomocy interfejsu graficznego.

%prep
%setup -q -n %{name}-%{version} 

%build
cp luci luci-fix
cp create_desc_file create_desc_file-fix
cat luci-fix | sed -e 's/\/usr\/local/\/usr/' > luci
cat create_desc_file-fix | sed -e 's/\/usr\/local/\/usr/' > create_desc_file
python -O gui.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/luci/{environement,system/network,system/users} $RPM_BUILD_ROOT%{_libdir}/luci $RPM_BUILD_ROOT%{_bindir}/
install create_desc_file $RPM_BUILD_ROOT%{_bindir}/
install luci $RPM_BUILD_ROOT%{_bindir}/
install *.py $RPM_BUILD_ROOT%{_libdir}/luci/
install *.pyo $RPM_BUILD_ROOT%{_libdir}/luci/
install examples/environement/* $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/environement
install examples/system/network/* $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/system/network
install examples/system/users/* $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/system/users

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc  BUGS COPIER COPYING INSTALL NEWS README THANKS TODO
#%{_datadir}/doc/%{name}-%{version}/*
%{_sysconfdir}/luci/environement/*
%{_sysconfdir}/luci/system/network/*
%{_sysconfdir}/luci/system/users/*
%{_libdir}/%{name}/*
%defattr(755,root,root)
%attr(755,root,root) %{_bindir}/*
