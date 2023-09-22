# This file creates a newfile
# school and gives it permissions
# and also writes content inside it

file { '/tmp/school':
  ensure  => 'file',
  content => 'I love Puppet',
}
exec { 'set_school_permissions':
  command => 'chmod 0744 /tmp/school && chown www-data:www-data /tmp/school',
  path    => '/bin:/usr/bin',
  creates => '/tmp/school',
  require => File['/tmp/school'],
}
