# Puppet Manifest to Install Flask

# Ensure the package 'python3-pip' is installed
package { 'python3-pip':
  ensure => 'installed',
}

# Install Flask using pip3 with the specified version
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => '/usr/bin',
  require => Package['python3-pip'],
}
