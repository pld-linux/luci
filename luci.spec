# http://jsautret.free.fr/luci/luci-0.2.2.tar.gz
Summary:	LUCI is a Universal Configuration Interface
Summary(pl):	LUCI to Universalny Configurator Interfejsu 
Name:		luci
Version:	0.2.2
Release:	1
Epoch:		1
License:	GPL
Group:		
Vendor:		Jerome@SAUTRET.org
Icon:		
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	-
#Source1:	-
# Source1-md5:	-
#Patch0:		%{name}-what.patch
URL:		http://jsautret.free.fr/luci/
#BuildRequires:	-
#PreReq:		-
#Requires:	-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires(postun):	-
#Provides:	-
#Obsoletes:	-
#Conflicts:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LUCI provides a way to edit any configuration file by using a graphical interface instead of a text editor. 
     
%description -l pl

%package subpackage
Summary:	-
Summary(pl):	-
Group:		-

%description subpackage

%description subpackage -l pl

%prep
%setup -q -n %{name}-%{version}.orig -a 1
%patch0 -p1

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

%files subpackage
%defattr(644,root,root,755)
%doc extras/*.gz
%{_datadir}/%{name}-ext
