#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ndg_httpsclient
Version  : 0.5.1
Release  : 37
URL      : https://files.pythonhosted.org/packages/b9/f8/8f49278581cb848fb710a362bfc3028262a82044167684fb64ad068dbf92/ndg_httpsclient-0.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/b9/f8/8f49278581cb848fb710a362bfc3028262a82044167684fb64ad068dbf92/ndg_httpsclient-0.5.1.tar.gz
Summary  : Provides enhanced HTTPS support for httplib and urllib2 using PyOpenSSL
Group    : Development/Tools
License  : BSD-3-Clause
Requires: ndg_httpsclient-bin
Requires: ndg_httpsclient-python3
Requires: ndg_httpsclient-license
Requires: ndg_httpsclient-python
Requires: pyOpenSSL
Requires: pyasn1
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pyOpenSSL
BuildRequires : pyasn1
BuildRequires : python3-dev
BuildRequires : setuptools

%description
* ``httplib`` (Python 2), ``http.client`` (Python 3) and 
         * ``urllib2`` (Python 2) and ``urllib`` (Python 3)
        
        ... based on PyOpenSSL.  PyOpenSSL provides a more fully featured SSL implementation 
        over the default provided with Python and importantly enables full verification 
        of the SSL peer using ``pyasn1``.
        
        Releases
        ========
        0.5.1
        -----
         * Clean up handling for description file - pull in content from this file into setup()
         * Allows the nightly build to fail
         * Add Trove version classifiers to make it explicit what is supported
         * Add python_requires to help pip
         * Drop support for EOL Python 2.6 and 3.3  
          
        Thanks to @hugovk for contributions
        
        0.5.0
        -----
         * Fix to Subject Alternative Name handling to allow for certificates with
           more than 64 names (max now 1024).  Thanks to Matt Pegler
         * Fix to subjectAltName string to use byte type for correct matching 
         * Updated SSL Context objects to default to TLS 1.2
        
        0.4.4
        -----
         * Updated test certificates
        
        0.4.3
        -----

%package bin
Summary: bin components for the ndg_httpsclient package.
Group: Binaries
Requires: ndg_httpsclient-license

%description bin
bin components for the ndg_httpsclient package.


%package license
Summary: license components for the ndg_httpsclient package.
Group: Default

%description license
license components for the ndg_httpsclient package.


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
%setup -q -n ndg_httpsclient-0.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532392570
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/ndg_httpsclient
cp ndg/httpsclient/LICENSE %{buildroot}/usr/share/doc/ndg_httpsclient/ndg_httpsclient_LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ndg_httpclient

%files license
%defattr(-,root,root,-)
/usr/share/doc/ndg_httpsclient/ndg_httpsclient_LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
