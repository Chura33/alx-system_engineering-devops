# Puppet Manifest to Kill a Process

exec { 'kill_killmenow_process':
  command   => 'pkill -f killmenow || [ $? -eq 1 ]',
  provider  => shell,
  timeout   => 60,
  logoutput => true,
}
