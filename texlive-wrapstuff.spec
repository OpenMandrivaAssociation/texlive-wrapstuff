Name:		texlive-wrapstuff
Version:	64058
Release:	2
Summary:	Wrapping text around stuff
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/wrapstuff
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wrapstuff.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wrapstuff.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/wrapstuff.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides another implementation of text wrapping.
Its implementation benefits from the paragraph hooks available
since LaTeX 2021-06-01.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/wrapstuff
%{_texmfdistdir}/tex/latex/wrapstuff
%doc %{_texmfdistdir}/doc/latex/wrapstuff

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
