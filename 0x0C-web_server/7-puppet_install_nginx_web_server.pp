# Puppet manifest to configure nginx

exec { 'update' :
  command  => '/usr/bin/apt-get update',
  provider => 'shell'
}

package { 'nginx' :
  ensure  => 'installed',
  require => Exec['update']
}

file { '/var/www/html/index.html' :
  content => "Hello World!\n",
}

file { '/etc/nginx/sites-available/default' :
  content => '
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;

	index index.html index.htm index.nginx-debian.html;

	server_name _;

	location /redirect_me {
		return 301 https://gitub.com/awinabaab?tab=repositories;
	}

	location / {
		try_files $uri $uri/ =404;
	}
}'
}

service { 'nginx' :
  ensure  => 'running',
  require => Package['nginx']
}
