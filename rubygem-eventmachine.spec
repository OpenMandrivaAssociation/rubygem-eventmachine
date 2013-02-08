%define	oname	eventmachine

Summary:	A fast, single-threaded engine for arbitrary network communications
Name:		rubygem-%{oname}
Version:	1.0.0
Release:	2
License:	MIT
Group:		Development/Ruby
URL:		http://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRequires:	ruby-RubyGems ruby-devel

%description
EventMachine implements a fast, single-threaded engine for arbitrary network
communications. It's extremely easy to use in Ruby. EventMachine wraps all
interactions with IP sockets, allowing programs to concentrate on the
implementation of network protocols. It can be used to create both network
servers and clients. To create a server or client, a Ruby program only needs
to specify the IP address and port, and provide a Module that implements the
communications protocol. Implementations of several standard network protocols
are provided with the package, primarily to serve as examples. The real goal of
EventMachine is to enable programs to easily interface with other programs
using TCP/IP, especially if custom protocols are required.

%prep

%build

%install
gem install -E -n %{buildroot}%{_bindir} --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}
rm -rf %{buildroot}%{ruby_gemdir}/{cache,gems/%{oname}-%{version}/ext}

mkdir -p %{buildroot}%{ruby_sitearchdir}
mv %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/lib/*.so  %{buildroot}%{ruby_sitearchdir}

%files
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
%{ruby_sitearchdir}/fastfilereaderext.so
%{ruby_sitearchdir}/rubyeventmachine.so



%changelog
* Sat Sep 18 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.12.10-1mdv2011.0
+ Revision: 579427
- import rubygem-eventmachine


* Sat Sep 18 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.12.10-1
- initial release
