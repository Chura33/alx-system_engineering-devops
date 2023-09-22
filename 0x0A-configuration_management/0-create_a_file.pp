# This file creates a newfile
# school and gives it permissions
# and also writes content inside it
require 'uri'

$my_text = 'I love Puppet'
$encoded_text = URI.encode_www_form_component($my_text)

file { '/tmp/school':
  ensure  => 'file',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => $encoded_text,
}
