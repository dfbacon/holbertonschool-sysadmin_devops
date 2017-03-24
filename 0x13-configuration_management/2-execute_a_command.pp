# Kills the 'killmenow' process

exec { 'pkill':
  path    => '/usr/bin/',
  command => 'pkill killmenow'
}
