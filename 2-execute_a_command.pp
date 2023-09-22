# Puppet Manifest to Kill a Process

exec { 'kill_killmenow_process':
  command   => 'pkill -f killmenow',
  onlyif    => 'pgrep -f killmenow',
  provider  => shell,
  timeout   => 60,
  logoutput => true,
}

