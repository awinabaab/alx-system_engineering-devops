# SSH
  - What is a server
  - Where servers usually live
  - What is SSH
  - How to create an SSH RSA key pair
  - How to connect to a remote host using an SSH RSA key pair
  - The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash`

## [0-use_a_private_key](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x0B-ssh/0-use_a_private_key)
   - A bash script that uses `ssh` to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`

## [1-create_ssh_key_pair](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x0B-ssh/1-create_ssh_key_pair)
   - A bash script that creates an RSA key pair
   - Name: `school`
   - Number of bits: `4096`
   - Passphrase: `betty`

## [2-ssh_config](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x0B-ssh/2-ssh_config)
   - Configuration to connect to a server without typing a password
   - Identity file: `~/.ssh/school`

## [100-puppet_ssh_config.pp](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x0B-ssh/100-puppet_ssh_config.pp)
   - Setup ssh configuration with puppet to connect to a server without typing a password
   - Identity file: `~/.ssh/school`

