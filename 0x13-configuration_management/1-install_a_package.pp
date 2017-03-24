# Install the 'puppet-lint' package

exec { 'apt-update':
  command => '/usr/bin/apt-get update'
}

package { 'puppet-lint':
  ensure   => latest,
  require  => Exec['apt-update'],
  provider => 'gem'
}
