%global debug_package %{nil}

Name:           exim_exporter
Version:        1.6.1
Release:        1%{?dist}
Summary:        Exim Exporter for Prometheus

License:        MIT
URL:            https://github.com/gvengel/exim_exporter
Source0:        https://github.com/gvengel/exim_exporter/archive/refs/tags/v%{version}.tar.gz
Source1:        exim_exporter.service
Source2:        exim_exporter-sysconfig

BuildRequires:  golang >= 1.17
BuildRequires:  systemd-rpm-macros

%description
Exim Exporter for Prometheus

%prep
%setup -q -n %{name}-%{version}

%build
export GO111MODULE=on
go build .

%install
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}

%changelog
* Thu Nov  2 2023 Cody Robertson <cody@nerdymuffin.com> - 1.6.1-1
- Initial package

