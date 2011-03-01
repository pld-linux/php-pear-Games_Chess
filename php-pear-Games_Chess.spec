%include	/usr/lib/rpm/macros.php
%define		_class		Games
%define		_subclass	Chess
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - construct and validate a logical chess game, does not display
Summary(pl.UTF-8):	%{_pearname} - konstruowanie i sprawdzanie poprawności logicznej gry w szachy
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	3
Epoch:		0
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f531ee3c5600a1713f41b3a4c2b6b09f
URL:		http://pear.php.net/package/Games_Chess/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Obsoletes:	php-pear-Games_Chess-tests
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

%description -l pl.UTF-8
Ten moduł obsługuje logikę obsługi szachownicy i analizy standardu
notacji FEN (Farnsworth-Edwards Notation) do opisu pozycji, a także
notacji SAN (Standard Algebraic Notation) do opisu poszczególnych
ruchów. Klasa może być używana jako backend do gry w szachy lub do
sprawdzania poprawności albo tworzenia plików PGN przy użyciu pakietu
File_ChessPGN.

Mimo że ten pakiet jest w stanie alpha, jest w pełni przetestowany.
Kod działa, ale API jest nie ustabilizowane i może się zmienić
drastycznie, jeśli znajdą się ku temu powody. Kiedy API się
ustabilizuje, zwiększy się stabilność całej klasy.

Ta klasa ma w PEAR status: %{_status}.

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
