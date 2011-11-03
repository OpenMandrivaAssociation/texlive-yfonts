# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/yfonts
# catalog-date 2007-03-01 23:46:20 +0100
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-yfonts
Version:	1.3
Release:	1
Summary:	Support for old German fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/yfonts
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yfonts.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yfonts.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yfonts.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A LaTeX interface to the old-german fonts designed by Yannis
Haralambous: Gothic, Schwabacher, Fraktur and the baroque
initials.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
