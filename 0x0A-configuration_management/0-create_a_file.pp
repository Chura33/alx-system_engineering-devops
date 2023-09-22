exec { 'create_school_file':
  command => 'echo "I love Puppet" > /tmp/school && chmod 0744 /tmp/school && chown www-data:www-data /tmp/school',
  path    => '/usr/bin:/usr/sbin:/bin',
  creates => '/tmp/school',
}

