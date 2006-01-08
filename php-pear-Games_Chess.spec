%include	/usr/lib/rpm/macros.php
%define		_class		Games
%define		_subclass	Chess
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - construct and validate a logical chess game, does not display
Summary(pl):	%{_pearname} - konstruowanie i sprawdzanie poprawno¶ci logicznej gry w szachy
Name:		php-pear-%{_pearname}
Version:	0.9.0
Release:	2
Epoch:		0
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	113d29fe28e965212668acb57f8cef8f
URL:		http://pear.php.net/package/Games_Chess/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# included in tests
%define		_noautoreq 'pear(HTML_TestListener.php)' 'pear(TestUnit.php)'

%description
The logic of handling a chessboard and parsing standard FEN
(Farnsworth-Edwards Notation) for describing a position as well as SAN
(Standard Algebraic Notation) for describing individual moves is
handled. This class can be used as a backend driver for playing chess,
or for validating and/or creating PGN files using the File_ChessPGN
package.

Although this package is alpha, it is fully unit-tested. The code
works, but the API is fluid, and may change dramatically as it is put
into use and better ways are found to use it. When the API stabilizes,
the stability will increase.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten modu³ obs³uguje logikê obs³ugi szachownicy i analizy standardu
notacji FEN (Farnsworth-Edwards Notation) do opisu pozycji, a tak¿e
notacji SAN (Standard Algebraic Notation) do opisu poszczególnych
ruchów. Klasa mo¿e byæ u¿ywana jako backend do gry w szachy lub do
sprawdzania poprawno¶ci albo tworzenia plików PGN przy u¿yciu pakietu
File_ChessPGN.

Mimo ¿e ten pakiet jest w stanie alpha, jest w pe³ni przetestowany.
Kod dzia³a, ale API jest nie ustabilizowane i mo¿e siê zmieniæ
drastycznie, je¶li znajd± siê ku temu powody. Kiedy API siê
ustabilizuje, zwiêkszy siê stabilno¶æ ca³ej klasy.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

rm -f ./%{php_pear_dir}/data/Games_Chess/LICENSE # PHP 3.0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/examples
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
