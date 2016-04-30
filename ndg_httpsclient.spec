#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ndg_httpsclient
Version  : 0.4.0
Release  : 8
URL      : https://pypi.python.org/packages/source/n/ndg-httpsclient/ndg_httpsclient-0.4.0.tar.gz
Source0  : https://pypi.python.org/packages/source/n/ndg-httpsclient/ndg_httpsclient-0.4.0.tar.gz
Summary  : Provides enhanced HTTPS support for httplib and urllib2 using PyOpenSSL
Group    : Development/Tools
License  : BSD-3-Clause
Requires: ndg_httpsclient-bin
Requires: ndg_httpsclient-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
NDG HTTPS Client Unit tests directory
=====================================
The unit tests expect to connect to a simple HTTPS server listening on port
4443.  An OpenSSL script is provided for this purpose in scripts/.  To run,

%package bin
Summary: bin components for the ndg_httpsclient package.
Group: Binaries

%description bin
bin components for the ndg_httpsclient package.


%package python
Summary: python components for the ndg_httpsclient package.
Group: Default

%description python
python components for the ndg_httpsclient package.


%prep
%setup -q -n ndg_httpsclient-0.4.0

%build
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ndg_httpclient

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
