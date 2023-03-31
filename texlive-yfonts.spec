Name:		texlive-yfonts
Version:	50755
Release:	2
Summary:	Support for old German fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/yfonts
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yfonts.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yfonts.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yfonts.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A LaTeX interface to the old-german fonts designed by Yannis
Haralambous: Gothic, Schwabacher, Fraktur and the baroque
initials.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/yfonts
%doc %{_texmfdistdir}/doc/latex/yfonts
#- source
%doc %{_texmfdistdir}/source/latex/yfonts

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
