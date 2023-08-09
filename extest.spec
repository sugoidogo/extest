Name:           extest
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        X11 XTEST reimplementation primarily for Steam Controller on Wayland 

License:        MIT
URL:            https://github.com/Supreeeme/extest
VCS:            {{{ git_dir_vcs }}}
Source:        	{{{ git_dir_pack }}}     

BuildRequires:  rust-packaging >= 21
BuildRequires:  systemd-rpm-macros

%description
Extest is a drop in replacement for the X11 XTEST extension. It creates a virtual device with the uinput kernel module. It's been primarily developed for allowing the desktop functionality on the Steam Controller to work while Steam is open on Wayland.

%prep
{{{ git_dir_setup_macro }}}
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%files
%license LICENSE
%doc README.md

%changelog
{{{ git_dir_changelog }}}
