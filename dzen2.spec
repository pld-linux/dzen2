Summary:	A general purpose messaging and notification program
Name:		dzen2
Version:	0.8.5
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	5978620c2124c8a8ad52d7f17ce94fd7
Patch0:		%{name}-config.patch
Patch1:		%{name}-verbose.patch
URL:		https://sites.google.com/site/gotmor/dzen/
#BuildRequires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dzen is a general purpose messaging, notification and menuing program
for X11. It was designed to be scriptable in any language and
integrate well with window managers like dwm, wmii and xmonad, though
it will work with any windowmanger.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}" \
	PLD_LDFLAGS="%{rpmldflags}" \
	PREFIX="%{_prefix}" \
	LIBDIR="%{_libdir}"

%{__make} -C gadgets \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}" \
	PLD_LDFLAGS="%{rpmldflags}" \
	LIBDIR="%{_libdir}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX="%{_prefix}"

%{__make} -C gadgets install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX="%{_prefix}"

# append dzen2- prefix to binaries
for gadget in dbar gcpubar gdbar textwidth
do
mv $RPM_BUILD_ROOT%{_bindir}/{,dzen2-}"${gadget}"
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS README README.dzen gadgets/README.*
%attr(755,root,root) %{_bindir}/dzen2
%attr(755,root,root) %{_bindir}/dzen2-dbar
%attr(755,root,root) %{_bindir}/dzen2-gcpubar
%attr(755,root,root) %{_bindir}/dzen2-gdbar
%attr(755,root,root) %{_bindir}/dzen2-textwidth
