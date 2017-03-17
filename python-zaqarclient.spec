#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB9069B1335700CDC (infra-root@openstack.org)
#
Name     : python-zaqarclient
Version  : 1.4.0
Release  : 15
URL      : http://tarballs.openstack.org/python-zaqarclient/python-zaqarclient-1.4.0.tar.gz
Source0  : http://tarballs.openstack.org/python-zaqarclient/python-zaqarclient-1.4.0.tar.gz
Source99 : http://tarballs.openstack.org/python-zaqarclient/python-zaqarclient-1.4.0.tar.gz.asc
Summary  : Client Library for OpenStack Zaqar Messaging API
Group    : Development/Tools
License  : Apache-2.0
Requires: python-zaqarclient-python
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
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
========================
Team and repository tags
========================
.. image:: http://governance.openstack.org/badges/python-zaqarclient.svg
:target: http://governance.openstack.org/reference/tags/index.html

%package python
Summary: python components for the python-zaqarclient package.
Group: Default

%description python
python components for the python-zaqarclient package.


%prep
%setup -q -n python-zaqarclient-1.4.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489787422
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1489787422
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
