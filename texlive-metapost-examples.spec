%global tl_name metapost-examples
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Example drawings using MetaPost
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/metapost/examples
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/metapost-examples.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/metapost-examples.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
These are a few (hundred) example pictures drawn with MetaPost, ranging
from very simple (lines and circles) to rather intricate (uncommon
geometric transformations, fractals, bitmap, etc).

