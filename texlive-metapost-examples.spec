# revision 15878
# category Package
# catalog-ctan /info/metapost/examples
# catalog-date 2008-04-20 19:53:04 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-metapost-examples
Version:	20080420
Release:	5
Summary:	Example drawings using MetaPost
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/metapost/examples
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metapost-examples.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metapost-examples.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080420-2
+ Revision: 753916
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080420-1
+ Revision: 719001
- texlive-metapost-examples
- texlive-metapost-examples
- texlive-metapost-examples
- texlive-metapost-examples

