%global tl_name quran-bn
%global tl_revision 74830

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.21
Release:	%{tl_revision}.1
Summary:	Bengali translations to the quran package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/unicodetex/latex/quran-bn
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/quran-bn.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/quran-bn.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is prepared for typesetting some Bengali translations of the
Holy Quran. It adds two Bengali translations to the quran package.

