%global tl_name aichej
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Bibliography style file for the AIChE Journal
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/misc/aichej.bst
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aichej.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The style was generated using custom-bib, and implements the style of
the American Institute of Chemical Engineers Journal (or AIChE Journal
or AIChE J or AIChEJ).

