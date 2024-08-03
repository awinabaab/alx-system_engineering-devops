# Shell Basics
   - What is Shell?
   - Navigation
   - Exploring the System
   - Manipulating Files and Directories
   - Working with Commands
   - Symbolic Links
   - Expansion
   - Text Editors (`vi`, `vim` and `emacs`)
   - Magic Files

## [0-whereami](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x00-shell_basics/0-current_working_directory)
   A shell script that prints the absolute path name of the current working directory.

## [1-listit](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x00-shell_basics/1-listit)
   A shell script that displays the contents of your current working directory.

## [2-bring_me_home](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x00-shell_basics/2-bring_me_home)
   A shell script that changes the working directory to the user's home directory without using any shell variables.

## [3-listfiles](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x00-shell_basics/3-listfiles)
   A shell script that display the contents of the current working directory in a long format.

## [4-listmorefiles](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x00-shell_basics/4-listmorefiles)
   A shell script that displays the current directory contents, including hidden files (starting with `.`) usinng the long format.

## [5-listfilesdigitonly](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x00-shell_basics/5-listfilesdigitonly)
   A shell script that displays current directory contents:
   - in long format.
   - with user and group IDs displayed numerically.
   - with hidden files (starting with `.`).

## [6-firstdirectory](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x00-shell_basics/6-firstdirectory)
   A shell script that creates a directory named `my_first_directory` in the `/tmp/` directory.

## [7-movethatfile](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x00-shell_basics/7-movethatfile)
   A shell script that moves the file `betty` from `/tmp/` to `/tmp/my_first_directory`.

## [8-firstdelete](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x00-shell_basics/8-firstdelete)
   A shell script that deletes the file `betty` from the directory `/tmp/my_first_directory`.

## [9-firstdirdeletion](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x00-shell_basics/9-firstdirdeletion)
   A shell script that deletes the directory `my_first_directory` that is in the `/tmp` directory.

## [10-back](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x00-shell_basics/10-back)
   A shell script that changes the current working directory to the previous one.

## [11-lists](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x00-shell_basics/11-lists)
   A shell script that lists all files(even the ones with names beginning with a period character, which are normally hidden) in the current directory and the parent directory of the working directory and the `/boot` directory (in this order), in long format.

## [12-file_type](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x00-shell_basics/12-file_type)
   A shell script that prints the file of file of the file named `iamafile` in the `/tmp/` directory.

## [13-symbolic_link](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x00-shell_basics/13-symbolic_link)
   A shell script that creates a symbolic link to `/bin/ls`, name `__ls__` in the current working directory.

## [14-copy_html](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x00-shell_basics/14-copy_html)
   A shell script that copies all the html files:
   - from the current working directory to the parent.
   - but only copies files that did not exist in the parent directory or were newer than the versions in the parent of the working directory.

## [100-lets_move](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x00-shell_basics/100-lets_move)
   A shell script that moves all files beginning with an uppercase letter to the directory `/tmp/u`.

## [101-clean_emacs](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x00-shell_basics/101-clean_emacs)
   A shell script that deletes all the files in the current working directory that end with the character `~`.

## [102-tree](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x00-shell_basics/102-tree)
   A shell script that creates the directories `welcome/`, `welcome/to/` and `welcome/to/school` in the current directory.
   - only allowed to use two spaces (and lines), not more.

## [103-commas](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x00-shell_basics/103-commas)
   A shell script that lists all the files and directories of the current working directory, separated by commas(`,`):
   - directory names should end with a slash (`/`).
   - files and directories starting with a dot (`.`) should be listed.
   - the listing should be alpha ordered, except for the directories `.` and `..` which should be at the very beginning.
   - only digits and letters are used to sort; Digits should come first.
   - the listing should end with a new line.

## [school.mgc](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x00-shell_basics/school.mgc)
   A magic file to detect School data files. School data files always contain the string `SCHOOL` at offset `0`.