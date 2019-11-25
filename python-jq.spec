# Created by pyp2rpm-3.3.3
%global pypi_name jq

Name:           python-%{pypi_name}
Version:        0.1.6
Release:        1%{?dist}
Summary:        jq is a lightweight and flexible JSON processor

License:        BSD 2-Clause
URL:            http://github.com/mwilliamson/jq.py
Source0:        https://files.pythonhosted.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python3-devel autoconf automake libtool gcc glibc-devel
BuildRequires:  python3dist(setuptools)

%description
jq.py: a lightweight and flexible JSON processor This project contains Python
bindings for jq < During installation, the source for jq 1.5 is downloaded over
HTTPS and built. Therefore, installation requires any programs required to
build jq. This includes:* Autoreconf* The normal C compiler toolchain, such as
gcc and make.* libtool* Python headers.Debian, Ubuntu or relatives If on
Debian,...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
jq.py: a lightweight and flexible JSON processor This project contains Python
bindings for jq < During installation, the source for jq 1.5 is downloaded over
HTTPS and built. Therefore, installation requires any programs required to
build jq. This includes:* Autoreconf* The normal C compiler toolchain, such as
gcc and make.* libtool* Python headers.Debian, Ubuntu or relatives If on
Debian,...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitearch}/%{pypi_name}.cpython-36m-x86_64-linux-gnu.so
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

