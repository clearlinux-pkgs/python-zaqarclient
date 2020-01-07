#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xFC43F0EE211DFED8 (infra-root@openstack.org)
#
Name     : python-zaqarclient
Version  : 1.12.0
Release  : 27
URL      : http://tarballs.openstack.org/python-zaqarclient/python-zaqarclient-1.12.0.tar.gz
Source0  : http://tarballs.openstack.org/python-zaqarclient/python-zaqarclient-1.12.0.tar.gz
Source1 : http://tarballs.openstack.org/python-zaqarclient/python-zaqarclient-1.12.0.tar.gz.asc
Summary  : Client Library for OpenStack Zaqar Messaging API
Group    : Development/Tools
License  : Apache-2.0
Requires: python-zaqarclient-license = %{version}-%{release}
Requires: python-zaqarclient-python = %{version}-%{release}
Requires: python-zaqarclient-python3 = %{version}-%{release}
Requires: jsonschema
Requires: keystoneauth1
Requires: osc-lib
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.utils
Requires: pbr
Requires: requests
Requires: six
Requires: stevedore
BuildRequires : buildreq-distutils3
BuildRequires : jsonschema
BuildRequires : keystoneauth1
BuildRequires : osc-lib
BuildRequires : oslo.i18n
BuildRequires : oslo.log
BuildRequires : oslo.utils
BuildRequires : pbr
BuildRequires : requests
BuildRequires : six
BuildRequires : stevedore

%description
========================
Team and repository tags
========================
.. image:: http://governance.openstack.org/tc/badges/python-zaqarclient.svg
:target: http://governance.openstack.org/tc/reference/tags/index.html

%package license
Summary: license components for the python-zaqarclient package.
Group: Default

%description license
license components for the python-zaqarclient package.


%package python
Summary: python components for the python-zaqarclient package.
Group: Default
Requires: python-zaqarclient-python3 = %{version}-%{release}

%description python
python components for the python-zaqarclient package.


%package python3
Summary: python3 components for the python-zaqarclient package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-zaqarclient package.


%prep
%setup -q -n python-zaqarclient-1.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567736970
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-zaqarclient
cp LICENSE %{buildroot}/usr/share/package-licenses/python-zaqarclient/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-zaqarclient/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
