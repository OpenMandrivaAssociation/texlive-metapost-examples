Name:		texlive-metapost-examples
Version:	15878
Release:	2
Summary:	Example drawings using MetaPost
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/metapost/examples
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metapost-examples.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metapost-examples.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
These are a few (hundred) example pictures drawn with MetaPost,
ranging from very simple (lines and circles) to rather
intricate (uncommon geometric transformations, fractals,
bitmap, etc).

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/metapost/metapost-examples/Makefile
%doc %{_texmfdistdir}/doc/metapost/metapost-examples/README
%doc %{_texmfdistdir}/doc/metapost/metapost-examples/data1
%doc %{_texmfdistdir}/doc/metapost/metapost-examples/data2
%doc %{_texmfdistdir}/doc/metapost/metapost-examples/data3
%doc %{_texmfdistdir}/doc/metapost/metapost-examples/examples.mp
%doc %{_texmfdistdir}/doc/metapost/metapost-examples/mp2html.pl

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
