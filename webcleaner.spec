Summary:	WebCleaner - a filtering HTTP proxy
Summary(pl):	WebCleaner - filtrujace proxy HTTP
Name:		webcleaner
Version:	2.18
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/webcleaner/%{name}-%{version}.tar.gz
# Source0-md5:	6ba6161d75ff074a3c4ff33340e6dbd5
Patch0:		%{name}-python-path.patch
URL:		http://webcleaner.sourceforge.net/
BuildRequires:	python >= 2.3.1
Requires:	python-pyOpenSSL
Requires:	python-Crypto
Requires:	python-Imagin
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

%description -l pl
Mo¿liwo¶ci:
 - obs³uga HTTP/1.1
 - obs³uga proxy HTTPS CONNECT i opcjonalna bramki SSL
 - zintegrowany parser HTML, usuwaj±cy niechciany kod (reklamy, flash
   itp.)
 - zintegrowany silnik JavaScriptu, umo¿liwia filtrowanie popupów
 - wykrywanie i poprawianie w HTML-u znanych b³êdów bezpieczeñstwa
 - kompresja dokumentów w locie (przy u¿yciu gzipa)
 - wy³±czanie animowanych GIF-ów
 - filtrowanie obrazków po rozmiarze, usuwanie bannerów reklamowych
 - zmniejszanie obrazków na JPEG-i niewielkich rozmiarów
 - usuwanie/dodawanie/modyfikowanie dowolnych nag³ówków HTTP
 - wykorzystywanie czarnych list SquidGuarda
 - modu³ filtra antywirusowego
 - obs³uga uwierzytelniania proxy Basic, Digest i (nie testowana) NTLM
 - kontrola dostêpu na poziomie hosta
 - konfigurowalne przez interfejs WWW z mo¿liwo¶ci± zmiany motywu

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__python} setup.py install \
	--home $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
#%attr(755,root,root) /bin/*
#%attr(755,root,root) /lib/python/*
#%attr(755,root,root) %{_datadir}/*
#%attr(755,root,root) /share/*
