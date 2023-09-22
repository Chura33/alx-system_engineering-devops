# Puppet Manifest to Kill a Process

exec { 'killmenow':
  command   => 'pkill -f killmenow',
  provider  => 'shell',
  refreshonly => true,
}
