# Shell, init files, variables and expansions
   - What are the `/etc/profile` file and the `/etc/profile.d directory`
   - What is the `~/.bashrc file`
   - What is the difference between a local and a global variable
   - What is a reserved variable
   - How to create, update and delete shell variables
   - What are the roles of the following reserved variables: `HOME`, `PATH`, `PS1`
   - What are special parameters
   - What is the special parameter `$?`?
   - What is expansion and how to use them
   - What is the difference between single and double quotes and how to use them properly
   - How to do command substitution with `$()` and backticks
   - How to perform arithmetic operations with the shell
   - How to create an `alias`
   - How to list aliases
   - How to temporarily disable an alias


## [0-alias](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/0-alias)
   A script that creates an alias
   - Name: `ls`
   -Value: `rm *`

## [1-hello_you](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/1-hello_you)
   A script that prints `hello user`, where user is the current Linux user

## [2-path](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/2-path)
   A script that add `/action` to the `PATH`. `/action` should be the last directory the shell looks into when looking for a program

## [3-paths](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/3-paths)
   A script that counts the number of directories in the `PATH`

## [4-global_variables](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/4-global_variables)
   A script that lists environment variables

## [5-local_variables](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/5-local_variables)
   A script that lists all local variables and environment variables, and functions

## [6-create_local_variable](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/6-create_local_variable)
   A script that creates a new local variable
   - Name: `BEST`
   - Value: `School`

## [7-create_global_variable](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/7-create_global_variable)
   A script that creates a new global variable
   - Name: `BEST`
   - Value: `School`

## [8-true_knowledge](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/8-true_knowledge)
   A script that prints the result of the addition of `128` with the value stored in the environment variable `TRUEKNOWLEDGE`, followed by a new line

## [9-divide_and_rule](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/9-divide_and_rule)
   A script that prints the result of `POWER` divided by `DIVIDE`, followed by a new line
   - `POWER` and `DIVIDE` are environment variables

## [10-love_exponent_breath](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/10-love_exponent_breath)
   A script that displays the result of `BREATH` to the power `LOVE` followed by a new line
   - `BREATH` and `LOVE` are environment variables

## [11-binary_to_decimal](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/11-binary_to_decimal)
   A script that converts a number from `base 2` to `base `10` followed by a new line
   - the `base 2` number is stored in the environment variable `BINARY`

## [12-combinations](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/12-combinations)
   A script that prints all possible combinations of two letters, except `oo`
   - letters are lower cases, from `a` to `z`
   - one combination per line
   - the output should be alpha ordered, starting with `aa`
   - do not print `oo`
   - script file should contain a maximum `64` characters

## [13-print_float](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/13-print_float)
   A script that prints a number with two decimal places, followed by a new line. The number will be stored in the environment variable `NUM`

## [100-decimal_to_hexadecimal](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/100-decimal_to_hexadecimal)
   A script that converts a number from `base 10` to `base 16`
   - the number in `base 10` is stored in the environment variable `DECIMAL`
   - the script displays the number in base 16, followed by a new line

## [101-rot13](https://github.com/awinabaab/alx-system_engineering-devops/blob/master/0x03-shell_variables_expansions/101-rot13)
   A script that encodes and decodes text using the `rot13` encryption. Assume `ASCII`