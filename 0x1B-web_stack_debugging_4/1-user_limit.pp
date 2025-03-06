# Increases hard and soft nofile limit for holberton user

exec { 'increase hard nofile for holberton user':
  command  => 'sudo sed -i "s/holberton hard nofile 5/holberton hard nofile 10000/" /etc/security/limits.conf',
  provider => shell
}

exec { 'increase soft nofile for holberton user':
  command  => 'sudo sed -i "s/holberton soft nofile 4/holberton soft nofile 100000/" /etc/security/limits.conf',
  provider => shell
}
