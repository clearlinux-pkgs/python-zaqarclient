#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC12B8E73B30F2FC8 (infra-root@openstack.org)
#
Name     : python-zaqarclient
Version  : 2.0.1
Release  : 33
URL      : http://tarballs.openstack.org/python-zaqarclient/python-zaqarclient-2.0.1.tar.gz
Source0  : http://tarballs.openstack.org/python-zaqarclient/python-zaqarclient-2.0.1.tar.gz
Source1  : http://tarballs.openstack.org/python-zaqarclient/python-zaqarclient-2.0.1.tar.gz.asc
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
Team and repository tags
        ========================

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
Provides: pypi(python_zaqarclient)
Requires: pypi(jsonschema)
Requires: pypi(keystoneauth1)
Requires: pypi(osc_lib)
Requires: pypi(oslo.i18n)
Requires: pypi(oslo.log)
Requires: pypi(oslo.utils)
Requires: pypi(pbr)
Requires: pypi(requests)
Requires: pypi(six)
Requires: pypi(stevedore)

%description python3
python3 components for the python-zaqarclient package.


%prep
%setup -q -n python-zaqarclient-2.0.1
cd %{_builddir}/python-zaqarclient-2.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1599848205
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-zaqarclient
cp %{_builddir}/python-zaqarclient-2.0.1/LICENSE %{buildroot}/usr/share/package-licenses/python-zaqarclient/57aed0b0f74e63f6b85cce11bce29ba1710b422b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-zaqarclient/57aed0b0f74e63f6b85cce11bce29ba1710b422b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
