%define name hipo
%define version 0.6.99
%define release %mkrel 11
Summary: GTK interface to iPod
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://download.gnome.org/sources/Hipo/%{name}-%{version}.tar.bz2
Patch: hipo-0.6.1-desktopentry.patch
Patch1: hipo-0.6.99-build.patch
License: GPLv2+ and GFDL
Group: Sound
Url: https://www.gnome.org/~pvillavi/hipo/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: desktop-file-utils
BuildRequires: mono-devel
BuildRequires: gnome-sharp2-devel
BuildRequires: ipod-sharp-devel
BuildRequires: ndesk-dbus-glib-devel
BuildRequires: taglib-sharp-devel
BuildRequires: glib2-devel
BuildRequires: gnome-doc-utils
BuildRequires: perl-XML-Parser

%description
Hipo is an application that allows you to manage the data of your iPod.


%prep
%setup -q -n %name-%version
%patch -p1 -b .desktopentry
%patch1 -p1

%build
./configure --prefix=%_prefix --libdir=%_prefix/lib --sysconfdir=%_sysconfdir
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %name --with-gnome
for omf in %buildroot%_datadir/omf/*/*-??.omf;do
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed s!%buildroot!!)" >> %name.lang
done


ln -sf %_prefix/lib/ipod-sharp/* %buildroot%_prefix/lib/%name/

%clean
rm -rf $RPM_BUILD_ROOT

%preun
%preun_uninstall_gconf_schemas hipo

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS TODO
%_sysconfdir/gconf/schemas/hipo.schemas
%_bindir/%name
%_prefix/lib/%name
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/*/apps/*
%dir %_datadir/omf/%name
%_datadir/omf/%name/%name-C.omf


