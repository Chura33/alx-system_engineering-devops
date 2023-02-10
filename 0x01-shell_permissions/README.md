0.The ```su betty``` script switches the current user to ```betty'```
1. The script ```whoami``` prints the username of the current user
2. The sudo groups script prints all the groups the current user is part of
3.The script sudo chown betty hello changes the owner of file hello to the user betty
4.This script touch hello creates an empty file "hello"
5.This script chmod u+x hello adds execute permissions to the owner of the file hello
6.This script chmod 754 hello adds execute permission to the owner and the group owner, and read permission to other users, to the file hello
7.This script chmod ugo+x hello adds execution permission to the owner, group owner and the other users
8.This script chmod 007 hello sets permission to file hello as follows: owner, no permission. group, no permission. others, all permission
9.This script chmod 754 adds full permission to owner, read and execute to group, and write and execute to others
10.This script chmod --reference=olleh hello copies the permission of olleh to the file hello
11.This script chmod -R ugo+X . Sets directories to be executable without modifying ordinary files in the current directory
12.This script mkdir -m 751 my_dir creates a directory called my_dir and gives it  a permission of 751 which means
owner has full permission, groups are able to read and execute and others would be able to execute only
13.This script chgrp school hello changes the group of hello to school
