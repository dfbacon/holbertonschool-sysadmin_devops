# Install the 'puppet-lint' package

exec { 'apt-update':
  command => '/usr/bin/apt-get update'
}

package { 'puppet-lint':
  require => Exec['apt-update'],
  ensure  => installed
}

service { 'puppet-lint':
  ensure => running
}
