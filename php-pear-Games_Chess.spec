%include	/usr/lib/rpm/macros.php
%define		_class		Games
%define		_subclass	Chess
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - construct and validate a logical chess game, does not display
Summary(pl):	%{_pearname} - konstruowanie i sprawdzanie poprawno¶ci logicznej gry w szachy
Name:		php-pear-%{_pearname}
Version:	0.8.1
Release:	1
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e4cc13476fa86e53038eec658039c6ac
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

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{tests,examples}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
