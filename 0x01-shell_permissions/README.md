# Shell Permissions

## 0-iam_betty
   A shell script that switches the current user to the user `betty`.

## 1-who_am_i
   A shell script that prints the effective username of the current user.

## 2-groups
   A shell script that prints all the groups the current user is part of.

## 3-new_owner
   A shell script that changes the owner of the file `hello` to the user `betty`.

## 4-empty
   A shell script that creates an empty file called `hello`.

## 5-execute
   A shell script that adds execute permissions to the owner of the file `hello` in the working directory.

## 6-multiple_permissions
   A shell script that adds execute permission to the owner and the group owner, and read permission to the other users, to the file `hello` in the working directory.

## 7-everybody
   A shell script that adds execution permission to the owner, the group owner and the other users, to the file `hello` in the working directory.
   - not allowed to use commas(`,`) for this script.

## 8-James_Bond
   A shell script that sets permission to the file `hello` as follows:
   - Owner: no permission at all
   - Group: no permission at all
   - Other users: all the permissions
   in the working directory
   - not allowed to use commas(`,`) for this script.

## 9-John_Doe
   A shell script that sets the mode of the file `hello` to this:
   `-rwxr-x-wx	  1 julien  julien   23	Sep 20	 14:25	 hello`
   in the working directory.
   - not allowed to use commas(`,`) for this script.

## 10-mirror_permissions
   A shell script that sets the mode of the file `hello` the same as `olleh`'s mode in the working directory.

## 11-directories_permissions
   A shell script that adds execute permissions to all subdirectories of the current directory for the owner, the group owner and all the other users.
   - Regular files should not be changed.

## 12-directory_permissions
   A shell script that creates a directory called `my_dir` with permissions `751` in the working directory.

## 13-change_group
   A shell script that changes the group owner to `school` for the file `hello` in the working directory.

## 100-change_owner_and_group
   A shell script that changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.

## 101-symbolic_link_permissions
   A shell script that changes the owner and the group owner of `_hello` to `vincent` and `staff` respectively in the working directory.
   - The file `_hello` is a symbolic link.

## 102-if_only
   A shell script that changes the owner of the file `hello` to `betty` only if it is owned by the user `guillaume` in the current working directory.

## 103-Star_Wars
   A shell script that plays the StarWars IV episode in the terminal.