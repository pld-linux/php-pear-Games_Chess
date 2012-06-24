%include	/usr/lib/rpm/macros.php
%define         _class          Games
%define         _subclass       Chess
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Construct and validate a logical chess game, does not display
Summary(pl):	%{_pearname} - Konstruowanie i sprawdzanie poprawno�ci logicznej gry w szachy
Name:		php-pear-%{_pearname}
Version:	0.5
Release:	0.alpha
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}alpha.tgz
# Source0-md5:	a07dd1348d143267be75effa6818a655
URL:		http://pear.php.net/package/Games_Chess/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

This class has in PEAR status: %{_status}.

%description -l pl
Ten modu� obs�uguje logik� obs�ugi szachownicy i analizy standardu
notacji FEN (Farnsworth-Edwards Notation) do opisu pozycji, a tak�e
notacji SAN (Standard Algebraic Notation) do opisu poszczeg�lnych
ruch�w. Klasa mo�e by� u�ywana jako backend do gry w szachy lub do
sprawdzania poprawno�ci albo tworzenia plik�w PGN przy u�yciu pakietu
File_ChessPGN.

Mimo �e ten pakiet jest w stanie alpha, jest w pe�ni przetestowany.
Kod dzia�a, ale API jest nie ustabilizowane i mo�e si� zmieni�
drastycznie, je�li znajd� si� ku temu powody. Kiedy API si�
ustabilizuje, zwi�kszy si� stabilno�� ca�ej klasy.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}alpha/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}alpha/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}alpha/{tests,examples}
%dir %{php_pear_dir}/%{_class}
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
