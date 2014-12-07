# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/yfonts
# catalog-date 2007-03-01 23:46:20 +0100
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-yfonts
Version:	1.3
Release:	9
Summary:	Support for old German fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/yfonts
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yfonts.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yfonts.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yfonts.source.tar.xz
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
%{_texmfdistdir}/tex/latex/yfonts/yfonts.sty
%doc %{_texmfdistdir}/doc/latex/yfonts/frktest.tex
%doc %{_texmfdistdir}/doc/latex/yfonts/liesmich
%doc %{_texmfdistdir}/doc/latex/yfonts/readme
#- source
%doc %{_texmfdistdir}/source/latex/yfonts/yfonts.dtx
%doc %{_texmfdistdir}/source/latex/yfonts/yfonts.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3-2
+ Revision: 757743
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3-1
+ Revision: 719964
- texlive-yfonts
- texlive-yfonts
- texlive-yfonts

