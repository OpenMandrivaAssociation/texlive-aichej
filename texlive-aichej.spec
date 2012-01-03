# revision 15878
# category Package
# catalog-ctan /biblio/bibtex/contrib/misc/aichej.bst
# catalog-date 2008-08-16 20:32:59 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-aichej
Version:	20080816
Release:	2
Summary:	Bibliography style file for the AIChE Journal
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/misc/aichej.bst
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aichej.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The style was generated using custom-bib, and implements the
style of the American Institute of Chemical Engineers Jounal
(or AIChE Journal or AIChE J or AIChEJ).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/aichej/aichej.bst

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex %{buildroot}%{_texmfdistdir}
