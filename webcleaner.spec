Summary:	WebCleaner - a filtering HTTP proxy
Summary(pl.UTF-8):	WebCleaner - filtrujące proxy HTTP
Name:		webcleaner
Version:	2.29
Release:	0.1
License:	GPL
Group:		Networking/Daemons/HTTP
Source0:	http://dl.sourceforge.net/webcleaner/%{name}-%{version}.tar.gz
# Source0-md5:	1b0b37c3722bb1e31f7eb496ce358963
Patch0:		%{name}-python-path.patch
URL:		http://webcleaner.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	python >= 2.3.1
Requires:	python-pyOpenSSL
Requires:	python-Crypto
Requires:	python-Imaging
Requires:	openssl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Features:
- HTTP/1.1 support
- HTTPS proxy CONNECT and optional SSL gateway support
- integrated HTML parser, removes unwanted HTML (adverts, flash, etc.)
- integrated JavaScript engine, allows popup filtering
- detection and correction of known HTML security flaws
- compress documents on-the-fly (with gzip)
- disable animated GIFs
- filter images by size, removes banner adverts
- reduce images to low-bandwidth JPEGs
- remove/add/modify arbitrary HTTP headers
- usage of SquidGuard blacklists
- antivirus filter module
- Basic, Digest and (untested) NTLM proxy authentication support
- per-host access control
- configurable over a themable web interface

%description -l pl.UTF-8
Możliwości:
- obsługa HTTP/1.1
- obsługa proxy HTTPS CONNECT i opcjonalna bramki SSL
- zintegrowany parser HTML, usuwający niechciany kod (reklamy, flash
  itp.)
- zintegrowany silnik JavaScriptu, umożliwia filtrowanie popupów
- wykrywanie i poprawianie w HTML-u znanych błędów bezpieczeństwa
- kompresja dokumentów w locie (przy użyciu gzipa)
- wyłączanie animowanych GIF-ów
- filtrowanie obrazków po rozmiarze, usuwanie bannerów reklamowych
- zmniejszanie obrazków na JPEG-i niewielkich rozmiarów
- usuwanie/dodawanie/modyfikowanie dowolnych nagłówków HTTP
- wykorzystywanie czarnych list SquidGuarda
- moduł filtra antywirusowego
- obsługa uwierzytelniania proxy Basic, Digest i (nie testowana) NTLM
- kontrola dostępu na poziomie hosta
- konfigurowalne przez interfejs WWW z możliwością zmiany motywu

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
#%%{__autoheader}
%{__automake}
%configure
%{__make}
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_prefix}/lib/python}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__python} setup.py install \
	--home $RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT/share/* 		$RPM_BUILD_ROOT%{_datadir}/
mv $RPM_BUILD_ROOT/bin/*		$RPM_BUILD_ROOT%{_bindir}/
mv $RPM_BUILD_ROOT/lib/python/* 	$RPM_BUILD_ROOT%{_prefix}/lib/python/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_prefix}/lib/python/*
%attr(755,root,root) %{_datadir}/*
