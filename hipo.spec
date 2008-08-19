%define name hipo
%define version 0.6.1
%define release %mkrel 5
Summary: GTK interface to iPod
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://download.gnome.org/sources/Hipo/%{name}-%{version}.tar.bz2
Patch: hipo-0.6.1-desktopentry.patch
License: GPLv2+ and GFDL
Group: Sound
Url: http://www.gnome.org/~pvillavi/hipo/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: desktop-file-utils
BuildRequires: mono-devel
BuildRequires: gnome-sharp2
BuildRequires: ipod-sharp
BuildRequires: ndesk-dbus-glib
BuildRequires: taglib-sharp
BuildRequires: gnome-doc-utils
BuildRequires: perl-XML-Parser

%description
Hipo is an application that allows you to manage the data of your iPod.


%prep
%setup -q -n %name-%version
%patch -p1 -b .desktopentry

%build
./configure --prefix=%_prefix --libdir=%_prefix/lib
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

%post
%update_icon_cache hicolor
%update_desktop_database

%postun
%clean_icon_cache hicolor
%clean_desktop_database

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS TODO
%_bindir/%name
%_prefix/lib/%name
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/*/apps/*
%dir %_datadir/omf/%name
%_datadir/omf/%name/%name-C.omf


