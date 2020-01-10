
%global group_id  org.apache.maven.plugins

Name:             maven-jarsigner-plugin
Version:          1.2
Release:          8%{?dist}
Summary:          Signs or verifies a project artifact and attachments using jarsigner
License:          ASL 2.0
Group:            Development/Libraries
URL:              http://maven.apache.org/plugins/%{name}/
# http://search.maven.org/remotecontent?filepath=org/apache/maven/plugins/maven-jarsigner-plugin/1.2/maven-jarsigner-plugin-1.2-source-release.zip
Source0:          http://search.maven.org/remotecontent?filepath=org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch:        noarch

BuildRequires:    java-devel
BuildRequires:    maven-local


%description
This plugin provides the capability to sign or verify
a project artifact and attachments using jarsigner.

If you need to sign a project artifact and all attached artifacts,
just configure the sign goal appropriately in your pom.xml
for the signing to occur automatically during the package phase.

If you need to verify the signatures of a project artifact
and all attached artifacts, just configure the verify goal
appropriately in your pom.xml for the verification to occur
automatically during the verify phase.


%package javadoc
Summary:          API documentation for %{name}
Group:            Documentation

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

%mvn_file :%{name} %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE DEPENDENCIES

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Aug 22 2013 Michal Srb <msrb@redhat.com> - 1.2-8
- Migrate away from mvn-rpmbuild (Resolves: #997477)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-7
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 11 2012 Jaromir Capik <jcapik@redhat.com> - 1.2-5
- Introducing NOTICE in the javadoc subpackage
- Minor spec file changes according to the latest guidelines

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed May 25 2011 Jaromir Capik <jcapik@redhat.com> - 1.2-2
- Missing runtime deps (maven, plexus-utils) added

* Wed May 18 2011 Jaromir Capik <jcapik@redhat.com> - 1.2-1
- Initial version of the package
