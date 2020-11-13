# enable RubyInstaller DevKit usage as a vendorable helper library
unless ENV['PATH'].include?('C:\\builds\\arachni\\build\\extracted\\DevKit-mingw64-64-4.7.2-20130224-1432-sfx\\mingw\\bin') then
  phrase = 'Temporarily enhancing PATH to include DevKit...'
  if defined?(Gem)
    Gem.ui.say(phrase) if Gem.configuration.verbose
  else
    puts phrase
  end
  puts "Prepending ENV['PATH'] to include DevKit..." if $DEBUG
  ENV['PATH'] = 'C:\\builds\\arachni\\build\\extracted\\DevKit-mingw64-64-4.7.2-20130224-1432-sfx\\bin;C:\\builds\\arachni\\build\\extracted\\DevKit-mingw64-64-4.7.2-20130224-1432-sfx\\mingw\\bin;' + ENV['PATH']
end
ENV['RI_DEVKIT'] = 'C:\\builds\\arachni\\build\\extracted\\DevKit-mingw64-64-4.7.2-20130224-1432-sfx'
ENV['CC'] = 'gcc'
ENV['CXX'] = 'g++'
ENV['CPP'] = 'cpp'
