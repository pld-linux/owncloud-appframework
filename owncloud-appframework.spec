%define		pkgname	appframework
Summary:	Framework for the ownCloud News app
Name:		owncloud-%{pkgname}
Version:	0.103
Release:	1
License:	AGPL
Group:		Development/Languages/PHP
Source0:	http://apps.owncloud.com/CONTENT/content-files/158433-appframework.zip
# Source0-md5:	a8b039aeee877ef21d194dad06d5456d
URL:		http://apps.owncloud.com/content/show.php/App+Framework?content=158433
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	owncloud >= 5.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/owncloud/apps/%{pkgname}

%description
Framework for the ownCloud News app

%prep
%setup -q -n %{pkgname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}

cp -a * $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
