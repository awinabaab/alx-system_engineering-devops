# Setup SSH configuration file so that it doesn't require a password

file_line { 'Turn off passwd auth' :
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no'
}

file_line { 'Declare identity file' :
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school'
}
