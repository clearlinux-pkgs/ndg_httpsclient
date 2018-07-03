#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ndg_httpsclient
Version  : 0.4.4
Release  : 31
URL      : http://pypi.debian.net/ndg_httpsclient/ndg_httpsclient-0.4.4.tar.gz
Source0  : http://pypi.debian.net/ndg_httpsclient/ndg_httpsclient-0.4.4.tar.gz
Summary  : Provides enhanced HTTPS support for httplib and urllib2 using PyOpenSSL
Group    : Development/Tools
License  : BSD-3-Clause
Requires: ndg_httpsclient-bin
Requires: ndg_httpsclient-python3
Requires: ndg_httpsclient-python
Requires: pyasn1
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pyOpenSSL
BuildRequires : pyasn1

BuildRequires : python3-dev
BuildRequires : setuptools

%description
A HTTPS client implementation for
         * ``httplib`` (Python 2), ``http.client`` (Python 3) and
         * ``urllib2`` (Python 2) and ``urllib`` (Python 3)
        
        ... based on PyOpenSSL.  PyOpenSSL provides a more fully featured SSL implementation
        over the default provided with Python and importantly enables full verification
        of the SSL peer using ``pyasn1``.
        
        Releases
        ========
        0.4.4
        -----
         * Update test certificate files.
        
        0.4.3
        -----

%package bin
Summary: bin components for the ndg_httpsclient package.
Group: Binaries

%description bin
bin components for the ndg_httpsclient package.


%package python
Summary: python components for the ndg_httpsclient package.
Group: Default
Requires: ndg_httpsclient-python3

%description python
python components for the ndg_httpsclient package.


%package python3
Summary: python3 components for the ndg_httpsclient package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ndg_httpsclient package.


%prep
%setup -q -n ndg_httpsclient-0.4.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523292283
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ndg_httpclient

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
