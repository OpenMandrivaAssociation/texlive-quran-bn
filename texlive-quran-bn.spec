Name:		texlive-quran-bn
Version:	68345
Release:	1
Summary:	Bengali translations to the quran package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/quran-bn
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quran-bn.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quran-bn.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is prepared for typesetting some Bengali
translations of the Holy Quran. It adds two Bengali
translations to the quran package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/quran-bn
%doc %{_texmfdistdir}/doc/latex/quran-bn

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
