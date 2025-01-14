# Web server
  - What is the main role of a web server
  - What is a child process
  - Why web servers usually have a parent process and child processes
  - What are the main HTTP requests
  - What DNS stands for
  - What is DNS main role

## [0-transfer_file](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x0C-web_server/0-transfer_file)
   A bash script that transfers a file from a client to a server
   - Accepts 4 parameters:
     1. The path to the file to be transferred
     2. The `IP` address of the `server` we want to transfer the file to
     3. The username `scp` connects with
     4. The path to the `SSH` private key that `scp` uses
   - Displays `Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if less than 3 parameters are passed
   - `scp` will tranfer the file to the user home directory `~/`
   - Strict host key checking is disabled

## [1-install_nginx_web_server](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x0C-web_server/1-install_nginx_web_server)
   - A bash script that installs an `nginx` web server listening on port 80
   - Sending a GET request to the root directory returns a page containing the string `Hello World`

## [2-setup_a_domain](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x0C-web_server/2-setup_a_domain)
   - Contains my domain name

## [3-redirection](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x0C-web_server/3-redirection)
   - A bash script that configures an `nginx` web server so that `/redirect_me` is redirecting to another page
   - The reidrection will be a `301 Moved Permanently`

## [4-not_found_page_404](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x0C-web_server/4-not_found_page_404)
   - A bash script that	configures an `nginx` web server so that `/redirect_me`	is
   redirecting to another page. The reidrection will be a `301 Moved Permanently`
   - And a custom 404 page that contains the string `Ceci n'est pas une page`

## [7-puppet_install_nginx_web_server.pp](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x0C-web_server/7-puppet_install_nginx_web_server)
   A puppet manifest to cofigure an `nginx` web server
   - Nginx should be listening on port 80
   - When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Hello World!
   - The path `/redirect_me` redirection must be a “301 Moved Permanently”