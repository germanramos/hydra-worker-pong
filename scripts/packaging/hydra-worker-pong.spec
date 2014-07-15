Name: hydra-worker-pong
Version: 1
Release: 0
Summary: hydra-worker-pong
Source0: hydra-worker-pong-1.0.tar.gz
License: MIT
Group: custom
URL: https://github.com/innotech/hydra-worker-pong
BuildArch: x86_64
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: libzmq3
%description
Returns the same instances received in the same order.
%prep
%setup -q
%build
%install
install -m 0755 -d $RPM_BUILD_ROOT/usr/local/hydra
install -m 0755 hydra-worker-pong $RPM_BUILD_ROOT/usr/local/hydra/hydra-worker-pong

install -m 0755 -d $RPM_BUILD_ROOT/etc/init.d
install -m 0755 hydra-worker-pong-init.d.sh $RPM_BUILD_ROOT/etc/init.d/hydra-worker-pong

install -m 0755 -d $RPM_BUILD_ROOT/etc/hydra
install -m 0644 hydra.conf $RPM_BUILD_ROOT/etc/hydra/hydra-worker-pong.conf
%clean
rm -rf $RPM_BUILD_ROOT
%post
echo   You should edit config file /etc/hydra/hydra-worker-pong.conf
echo   When finished, you may want to run \"update-rc.d hydra-worker-pong defaults\"
%files
/usr/local/hydra/hydra-worker-pong
/etc/init.d/hydra-worker-pong
