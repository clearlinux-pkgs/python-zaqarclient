#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-zaqarclient
Version  : 0.3.0
Release  : 5
URL      : http://tarballs.openstack.org/python-zaqarclient/python-zaqarclient-0.3.0.tar.gz
Source0  : http://tarballs.openstack.org/python-zaqarclient/python-zaqarclient-0.3.0.tar.gz
Summary  : Client Library for OpenStack Zaqar Messaging API
Group    : Development/Tools
License  : Apache-2.0
Requires: python-zaqarclient-python
BuildRequires : Jinja2
BuildRequires : PyYAML-python
BuildRequires : Pygments
BuildRequires : Sphinx-python
BuildRequires : colorama-python
BuildRequires : coverage-python
BuildRequires : ddt-python
BuildRequires : debtcollector-python
BuildRequires : demjson-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : flake8-python
BuildRequires : funcsigs-python
BuildRequires : hacking
BuildRequires : iso8601-python
BuildRequires : jsonschema-python
BuildRequires : linecache2-python
BuildRequires : lxml-python
BuildRequires : mccabe-python
BuildRequires : msgpack-python-python
BuildRequires : netaddr
BuildRequires : netifaces-python
BuildRequires : nose-exclude-python
BuildRequires : nose-python
BuildRequires : openstack-doc-tools-python
BuildRequires : openstack.nose_plugin
BuildRequires : oslo.config
BuildRequires : oslo.i18n-python
BuildRequires : oslo.serialization-python
BuildRequires : oslo.utils-python
BuildRequires : oslosphinx-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : prettytable
BuildRequires : py-python
BuildRequires : pyflakes-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-keystoneclient-python
BuildRequires : python-mimeparse-python
BuildRequires : python-mock-python
BuildRequires : python3-dev
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : stevedore
BuildRequires : termcolor-python
BuildRequires : testrepository-python
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv
BuildRequires : wrapt-python

%description
*******************
Python Zaqar Client
*******************
.. image:: https://img.shields.io/pypi/v/python-zaqarclient.svg
:target: https://pypi.python.org/pypi/python-zaqarclient/
:alt: Latest Version

%package python
Summary: python components for the python-zaqarclient package.
Group: Default
Requires: jsonschema-python
Requires: oslo.i18n-python
Requires: python-keystoneclient-python
Requires: requests-python
Requires: stevedore

%description python
python components for the python-zaqarclient package.


%prep
%setup -q -n python-zaqarclient-0.3.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
