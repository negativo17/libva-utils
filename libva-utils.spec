Name:       libva-utils
Epoch:      1
Version:    2.22.0
Release:    1%{?dist}
Summary:    Collection of tests for VA-API (VIdeo Acceleration API)
License:    MIT and BSD
URL:        https://01.org/linuxmedia/vaapi

Source0:    https://github.com/intel/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson >= 0.42.0
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libva) >= 1.1.0
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libva-wayland)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(wayland-client) >= 1.0.0
BuildRequires:  pkgconfig(x11)

%description
%{name} is a collection of utilities and examples to exercise VA-API in
accordance with the libva project. A driver implementation is necessary to
properly operate.

%prep
%autosetup -p1

%build
%meson \
  -D drm=true \
  -D wayland=true \
  -D x11=true

%meson_build

%install
%meson_install

%files
%license COPYING
%doc NEWS
%{_bindir}/av1encode
%{_bindir}/avcenc
%{_bindir}/avcstreamoutdemo
%{_bindir}/h264encode
%{_bindir}/hevcencode
%{_bindir}/jpegenc
%{_bindir}/loadjpeg
%{_bindir}/mpeg2vaenc
%{_bindir}/mpeg2vldemo
%{_bindir}/putsurface
%{_bindir}/putsurface_wayland
%{_bindir}/sfcsample
%{_bindir}/vacopy
%{_bindir}/vainfo
%{_bindir}/vavpp
%{_bindir}/vp8enc
%{_bindir}/vp9enc
%{_bindir}/vpp3dlut
%{_bindir}/vppblending
%{_bindir}/vppchromasitting
%{_bindir}/vppdenoise
%{_bindir}/vpphdr_tm
%{_bindir}/vppscaling_csc
%{_bindir}/vppscaling_n_out_usrptr
%{_bindir}/vppsharpness

%changelog
* Tue Jun 25 2024 Simone Caronni <negativo17@gmail.com> - 1:2.22.0-1
- Update to 2.22.0.

* Wed Mar 20 2024 Simone Caronni <negativo17@gmail.com> - 1:2.21.0-1
- Update to 2.21.0.

* Wed Dec 13 2023 Simone Caronni <negativo17@gmail.com> - 1:2.20.1-1
- Update to 2.20.1.

* Fri Sep 29 2023 Simone Caronni <negativo17@gmail.com> - 1:2.20.0-1
- Update to 2.20.0.

* Thu Jul 13 2023 Simone Caronni <negativo17@gmail.com> - 1:2.19.0-1
- Update to 2.19.0.

* Wed Apr 19 2023 Simone Caronni <negativo17@gmail.com> - 1:2.18.2-1
- Update to 2.18.2.

* Thu Apr 13 2023 Simone Caronni <negativo17@gmail.com> - 1:2.18.1-1
- Update to 2.18.1.

* Thu Jan 26 2023 Simone Caronni <negativo17@gmail.com> - 1:2.17.1-1
- Update to 2.17.1.

* Tue Oct 04 2022 Simone Caronni <negativo17@gmail.com> - 1:2.16.0-1
- Update to 2.16.0.

* Mon Jul 04 2022 Simone Caronni <negativo17@gmail.com> - 1:2.15.0-1
- Update to 2.15.0.

* Wed Mar 02 2022 Simone Caronni <negativo17@gmail.com> - 1:2.14.0-1
- Update to 2.14.0.
- Switch to meson.

* Mon Oct 25 2021 Simone Caronni <negativo17@gmail.com> - 1:2.13.0-1
- Update to 2.13.0.

* Wed Jun 23 2021 Simone Caronni <negativo17@gmail.com> - 1:2.12.0-1
- Update to 2.12.0.

* Sun Apr 04 2021 Simone Caronni <negativo17@gmail.com> - 1:2.11.1-1
- Update to 2.11.1.

* Tue Jan  5 2021 Simone Caronni <negativo17@gmail.com> - 1:2.10.0-1
- Update to 2.10.0.

* Fri Oct 30 2020 Simone Caronni <negativo17@gmail.com> - 1:2.9.1-1
- Update to 2.9.1.

* Sat May 02 2020 Simone Caronni <negativo17@gmail.com> - 1:2.7.1-1
- First build.
