# -*- encoding: utf-8 -*-
# stub: arachni-rpc 0.2.1.4 ruby lib

Gem::Specification.new do |s|
  s.name = "arachni-rpc"
  s.version = "0.2.1.4"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib"]
  s.authors = ["Tasos Laskos"]
  s.date = "2017-01-06"
  s.description = "        Arachni::RPC is a simple and lightweight Remote Procedure Call protocol\n        used to provide the basis for Arachni's distributed infrastructure.\n"
  s.email = "tasos.laskos@arachni-scanner.com"
  s.extra_rdoc_files = ["README.md", "LICENSE.md", "CHANGELOG.md"]
  s.files = ["CHANGELOG.md", "LICENSE.md", "README.md"]
  s.homepage = "https://github.com/Arachni/arachni-rpc"
  s.rdoc_options = ["--charset=UTF-8"]
  s.rubygems_version = "2.4.5"
  s.summary = "The RPC protocol of the Arachni Framework."

  s.installed_by_version = "2.4.5" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<arachni-reactor>, ["~> 0.1.2"])
    else
      s.add_dependency(%q<arachni-reactor>, ["~> 0.1.2"])
    end
  else
    s.add_dependency(%q<arachni-reactor>, ["~> 0.1.2"])
  end
end
