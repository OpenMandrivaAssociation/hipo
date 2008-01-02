%define name hipo
%define version 0.5
%define release %mkrel 1
Summary: GTK interface to iPod
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://download.gnome.org/sources/Hipo/%{name}-%{version}.tar.bz2
Patch: hipo-0.5-desktopentry.patch
License: GPL
Group: Sound
Url: http://www.gnome.org/~pvillavi/hipo/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: desktop-file-utils
BuildRequires: mono-devel
BuildRequires: gnome-sharp2
BuildRequires: ipod-sharp

%description
Hipo is an application that allows you to manage the data of your iPod.


%prep
%setup -q -n %name-%version
%patch -p1

%build
./configure --prefix=%_prefix --libdir=%_prefix/lib
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %name
ln -sf %_prefix/lib/ipod-sharp/* %buildroot%_prefix/lib/%name/

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%postun
%clean_icon_cache hicolor

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS TODO
%_bindir/%name
%_prefix/lib/%name
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/*/apps/*


