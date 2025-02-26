# Correct typo in php file extension

exec { 'Correct typo in file extension':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell
}
