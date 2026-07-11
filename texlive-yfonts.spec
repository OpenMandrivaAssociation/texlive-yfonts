%global tl_name yfonts
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	Support for old German fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/yfonts
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yfonts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yfonts.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yfonts.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A LaTeX interface to the old-german fonts designed by Yannis
Haralambous: Gothic, Schwabacher, Fraktur and the baroque initials.

