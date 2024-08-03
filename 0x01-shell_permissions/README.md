# Shell Permissions
   - What do the commands `chmod`, `sudo`, `su`, `chown`, `chgrp` do?
   - Linux file permissions
   - How to represent each of the three sets of permissions (owner, group, and other) as a single digit
   - How to change permissions, owner and group of a file
   - Why can’t a normal user `chown` a file
   - How to run a command with root privileges
   - How to change user ID or become superuser
   - How to create a user
   - How to create a group
   - How to print real and effective user and group IDs
   - How to print the groups a user is in
   - How to print the effective `userid`

## [0-iam_betty](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x01-shell_permissions/0-iam_betty)
   A shell script that switches the current user to the user `betty`.

## [1-who_am_i](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x01-shell_permissions/1-who_am_i)
   A shell script that prints the effective username of the current user.

## [2-groups](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x01-shell_permissions/2-groups)
   A shell script that prints all the groups the current user is part of.

## [3-new_owner](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x01-shell_permissions/3-new_owner)
   A shell script that changes the owner of the file `hello` to the user `betty`.

## [4-empty](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x01-shell_permissions/4-empty)
   A shell script that creates an empty file called `hello`.

## [5-execute](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x01-shell_permissions/5-execute)
   A shell script that adds execute permissions to the owner of the file `hello` in the working directory.

## [6-multiple_permissions](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x01-shell_permissions/6-multiple_permissions)
   A shell script that adds execute permission to the owner and the group owner, and read permission to the other users, to the file `hello` in the working directory.

## [7-everybody](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x01-shell_permissions/7-everybody)
   A shell script that adds execution permission to the owner, the group owner and the other users, to the file `hello` in the working directory.
   - not allowed to use commas(`,`) for this script.

## [8-James_Bond](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x01-shell_permissions/8-James_Bond)
   A shell script that sets permission to the file `hello` as follows:
   - Owner: no permission at all
   - Group: no permission at all
   - Other users: all the permissions
   in the working directory
   - not allowed to use commas(`,`) for this script.

## [9-John_Doe](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x01-shell_permissions/9-John_Doe)
   A shell script that sets the mode of the file `hello` to this:
   `-rwxr-x-wx	  1 julien  julien   23	Sep 20	 14:25	 hello`
   in the working directory.
   - not allowed to use commas(`,`) for this script.

## [10-mirror_permissions](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x01-shell_permissions/10-mirror_permissions)
   A shell script that sets the mode of the file `hello` the same as `olleh`'s mode in the working directory.

## [11-directories_permissions](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x01-shell_permissions/11-directories_permissions)
   A shell script that adds execute permissions to all subdirectories of the current directory for the owner, the group owner and all the other users.
   - Regular files should not be changed.

## [12-directory_permissions](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x01-shell_permissions/12-directory_permissions)
   A shell script that creates a directory called `my_dir` with permissions `751` in the working directory.

## [13-change_group](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x01-shell_permissions/13-change_group)
   A shell script that changes the group owner to `school` for the file `hello` in the working directory.

## [100-change_owner_and_group](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x01-shell_permissions/100-change_owner_and_group)
   A shell script that changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.

## [101-symbolic_link_permissions](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x01-shell_permissions/101-symbolic_link_permissions)
   A shell script that changes the owner and the group owner of `_hello` to `vincent` and `staff` respectively in the working directory.
   - The file `_hello` is a symbolic link.

## [102-if_only](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x01-shell_permissions/102-if_only)
   A shell script that changes the owner of the file `hello` to `betty` only if it is owned by the user `guillaume` in the current working directory.

## [103-Star_Wars](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x01-shell_permissions/103-Star_Wars)
   A shell script that plays the StarWars IV episode in the terminal.