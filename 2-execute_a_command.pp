# Puppet Manifest to Kill a Process

exec { 'kill_killmenow_process':
  command   => 'pkill -f killmenow',
  provider  => 'shell',
  onlyif    => 'pgrep -f killmenow',
  subscribe => Exec['start_killmenow_process'], # Ensure this runs after the process starts
  refreshonly => true,
}
