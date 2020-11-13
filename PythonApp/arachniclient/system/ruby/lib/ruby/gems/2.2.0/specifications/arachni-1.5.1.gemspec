# -*- encoding: utf-8 -*-
# stub: arachni 1.5.1 ruby lib

Gem::Specification.new do |s|
  s.name = "arachni"
  s.version = "1.5.1"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib"]
  s.authors = ["Tasos Laskos"]
  s.date = "2017-03-29"
  s.description = "Arachni is a feature-full, modular, high-performance Ruby framework aimed towards\nhelping penetration testers and administrators evaluate the security of web applications.\n\nIt is smart, it trains itself by monitoring and learning from the web application's\nbehavior during the scan process and is able to perform meta-analysis using a number of\nfactors in order to correctly assess the trustworthiness of results and intelligently\nidentify (or avoid) false-positives.\n\nUnlike other scanners, it takes into account the dynamic nature of web applications,\ncan detect changes caused while travelling through the paths of a web application\u{2019}s\ncyclomatic complexity and is able to adjust itself accordingly. This way, attack/input\nvectors that would otherwise be undetectable by non-humans can be handled seamlessly.\n\nMoreover, due to its integrated browser environment, it can also audit and inspect\nclient-side code, as well as support highly complicated web applications which make\nheavy use of technologies such as JavaScript, HTML5, DOM manipulation and AJAX.\n\nFinally, it is versatile enough to cover a great deal of use cases, ranging from\na simple command line scanner utility, to a global high performance grid of\nscanners, to a Ruby library allowing for scripted audits, to a multi-user\nmulti-scan web collaboration platform.\n"
  s.email = "tasos.laskos@arachni-scanner.com"
  s.executables = ["arachni_rpcd", "arachni_restore", "arachni_console", "arachni_rpc", "arachni_rpcd_monitor", "arachni_reproduce", "arachni_reporter", "arachni_rest_server", "arachni_multi", "arachni_script", "arachni"]
  s.extra_rdoc_files = ["README.md", "LICENSE.md", "CHANGELOG.md"]
  s.files = ["CHANGELOG.md", "LICENSE.md", "README.md", "bin/arachni", "bin/arachni_console", "bin/arachni_multi", "bin/arachni_reporter", "bin/arachni_reproduce", "bin/arachni_rest_server", "bin/arachni_restore", "bin/arachni_rpc", "bin/arachni_rpcd", "bin/arachni_rpcd_monitor", "bin/arachni_script"]
  s.homepage = "https://www.arachni-scanner.com"
  s.licenses = ["Arachni Public Source License v1.0"]
  s.post_install_message = "\nThank you for installing Arachni, here are some resources which should\nhelp you make the best of it:\n\nHomepage           - http://arachni-scanner.com\nBlog               - http://arachni-scanner.com/blog\nDocumentation      - http://arachni-scanner.com/wiki\nSupport            - http://support.arachni-scanner.com\nGitHub page        - http://github.com/Arachni/arachni\nCode Documentation - http://rubydoc.info/github/Arachni/arachni\nLicense            - Arachni Public Source License v1.0\n                        (https://github.com/Arachni/arachni/blob/master/LICENSE.md)\nAuthor             - Tasos \"Zapotek\" Laskos (http://twitter.com/Zap0tek)\nTwitter            - http://twitter.com/ArachniScanner\nCopyright          - 2010-2017 Sarosys LLC (http://www.sarosys.com)\n\nPlease do not hesitate to ask for assistance (via the support portal)\nor report a bug (via GitHub Issues) if you come across any problem.\n\n"
  s.rdoc_options = ["--charset=UTF-8"]
  s.required_ruby_version = Gem::Requirement.new(">= 2.2.0")
  s.rubygems_version = "2.4.5"
  s.summary = "Arachni is a feature-full, modular, high-performance Ruby framework aimed towards helping penetration testers and administrators evaluate the security of web applications."

  s.installed_by_version = "2.4.5" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<awesome_print>, ["= 1.6.1"])
      s.add_runtime_dependency(%q<rack>, ["= 1.6.4"])
      s.add_runtime_dependency(%q<bundler>, [">= 0"])
      s.add_runtime_dependency(%q<concurrent-ruby>, ["= 1.0.2"])
      s.add_runtime_dependency(%q<concurrent-ruby-ext>, ["= 1.0.2"])
      s.add_runtime_dependency(%q<rubyzip>, ["= 1.2.1"])
      s.add_runtime_dependency(%q<http_parser.rb>, ["= 0.6.0"])
      s.add_runtime_dependency(%q<coderay>, ["= 1.1.0"])
      s.add_runtime_dependency(%q<childprocess>, ["= 0.5.3"])
      s.add_runtime_dependency(%q<msgpack>, ["= 0.7.0"])
      s.add_runtime_dependency(%q<oj>, ["= 2.15.0"])
      s.add_runtime_dependency(%q<oj_mimic_json>, ["= 1.0.1"])
      s.add_runtime_dependency(%q<puma>, ["= 2.14.0"])
      s.add_runtime_dependency(%q<sinatra>, ["= 1.4.6"])
      s.add_runtime_dependency(%q<sinatra-contrib>, ["= 1.4.6"])
      s.add_runtime_dependency(%q<arachni-rpc>, ["~> 0.2.1.4"])
      s.add_runtime_dependency(%q<typhoeus>, ["= 1.0.2"])
      s.add_runtime_dependency(%q<addressable>, ["= 2.3.6"])
      s.add_runtime_dependency(%q<pony>, ["= 1.11"])
      s.add_runtime_dependency(%q<rb-readline>, ["= 0.5.1"])
      s.add_runtime_dependency(%q<nokogiri>, ["= 1.6.8.1"])
      s.add_runtime_dependency(%q<ox>, ["= 2.4.11"])
      s.add_runtime_dependency(%q<terminal-table>, ["= 1.4.5"])
      s.add_runtime_dependency(%q<selenium-webdriver>, ["= 3.0.1"])
      s.add_runtime_dependency(%q<watir-webdriver>, ["= 0.8.0"])
      s.add_runtime_dependency(%q<kramdown>, ["= 1.4.1"])
      s.add_runtime_dependency(%q<loofah>, ["= 2.0.3"])
    else
      s.add_dependency(%q<awesome_print>, ["= 1.6.1"])
      s.add_dependency(%q<rack>, ["= 1.6.4"])
      s.add_dependency(%q<bundler>, [">= 0"])
      s.add_dependency(%q<concurrent-ruby>, ["= 1.0.2"])
      s.add_dependency(%q<concurrent-ruby-ext>, ["= 1.0.2"])
      s.add_dependency(%q<rubyzip>, ["= 1.2.1"])
      s.add_dependency(%q<http_parser.rb>, ["= 0.6.0"])
      s.add_dependency(%q<coderay>, ["= 1.1.0"])
      s.add_dependency(%q<childprocess>, ["= 0.5.3"])
      s.add_dependency(%q<msgpack>, ["= 0.7.0"])
      s.add_dependency(%q<oj>, ["= 2.15.0"])
      s.add_dependency(%q<oj_mimic_json>, ["= 1.0.1"])
      s.add_dependency(%q<puma>, ["= 2.14.0"])
      s.add_dependency(%q<sinatra>, ["= 1.4.6"])
      s.add_dependency(%q<sinatra-contrib>, ["= 1.4.6"])
      s.add_dependency(%q<arachni-rpc>, ["~> 0.2.1.4"])
      s.add_dependency(%q<typhoeus>, ["= 1.0.2"])
      s.add_dependency(%q<addressable>, ["= 2.3.6"])
      s.add_dependency(%q<pony>, ["= 1.11"])
      s.add_dependency(%q<rb-readline>, ["= 0.5.1"])
      s.add_dependency(%q<nokogiri>, ["= 1.6.8.1"])
      s.add_dependency(%q<ox>, ["= 2.4.11"])
      s.add_dependency(%q<terminal-table>, ["= 1.4.5"])
      s.add_dependency(%q<selenium-webdriver>, ["= 3.0.1"])
      s.add_dependency(%q<watir-webdriver>, ["= 0.8.0"])
      s.add_dependency(%q<kramdown>, ["= 1.4.1"])
      s.add_dependency(%q<loofah>, ["= 2.0.3"])
    end
  else
    s.add_dependency(%q<awesome_print>, ["= 1.6.1"])
    s.add_dependency(%q<rack>, ["= 1.6.4"])
    s.add_dependency(%q<bundler>, [">= 0"])
    s.add_dependency(%q<concurrent-ruby>, ["= 1.0.2"])
    s.add_dependency(%q<concurrent-ruby-ext>, ["= 1.0.2"])
    s.add_dependency(%q<rubyzip>, ["= 1.2.1"])
    s.add_dependency(%q<http_parser.rb>, ["= 0.6.0"])
    s.add_dependency(%q<coderay>, ["= 1.1.0"])
    s.add_dependency(%q<childprocess>, ["= 0.5.3"])
    s.add_dependency(%q<msgpack>, ["= 0.7.0"])
    s.add_dependency(%q<oj>, ["= 2.15.0"])
    s.add_dependency(%q<oj_mimic_json>, ["= 1.0.1"])
    s.add_dependency(%q<puma>, ["= 2.14.0"])
    s.add_dependency(%q<sinatra>, ["= 1.4.6"])
    s.add_dependency(%q<sinatra-contrib>, ["= 1.4.6"])
    s.add_dependency(%q<arachni-rpc>, ["~> 0.2.1.4"])
    s.add_dependency(%q<typhoeus>, ["= 1.0.2"])
    s.add_dependency(%q<addressable>, ["= 2.3.6"])
    s.add_dependency(%q<pony>, ["= 1.11"])
    s.add_dependency(%q<rb-readline>, ["= 0.5.1"])
    s.add_dependency(%q<nokogiri>, ["= 1.6.8.1"])
    s.add_dependency(%q<ox>, ["= 2.4.11"])
    s.add_dependency(%q<terminal-table>, ["= 1.4.5"])
    s.add_dependency(%q<selenium-webdriver>, ["= 3.0.1"])
    s.add_dependency(%q<watir-webdriver>, ["= 0.8.0"])
    s.add_dependency(%q<kramdown>, ["= 1.4.1"])
    s.add_dependency(%q<loofah>, ["= 2.0.3"])
  end
end
