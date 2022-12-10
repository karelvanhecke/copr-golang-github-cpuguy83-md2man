%global goipath github.com/cpuguy83/go-md2man
Version: 2.0.2
%global shortname go-md2man

%gometa

Name: %{goname}
Release: 1%{?dist}
Summary: Converts markdown into roff (man pages)
License: MIT
URL: %{gourl}
Source0: %{gosource}

Provides: %{shortname} = %{version}-%{release}

%description
Converts markdown into roff (man pages).

%prep
%goprep -k

%build
%gobuild -o %{gobuilddir}/bin/%{shortname} %{goipath}

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%files
%license LICENSE.md
%doc README.md go-md2man.1.md
%{_bindir}/*

%changelog
* Sat Dec 10 2022 Karel Van Hecke <copr@karelvanhecke.com> - 2.0.2-1
- Initial build
