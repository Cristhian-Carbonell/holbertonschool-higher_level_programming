# Project 0x0E. SQL - More queries

![imagen](https://cambiodigital-ol.com/wp-content/uploads/2020/02/sql_portada_opt.png)

## Resources
#### Read or watch:

- [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
- [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://intranet.hbtn.io/rltoken/ztrEKQexfEDtZ-8EUsG70Q)
- [MySQL constraints](http://zetcode.com/mysql/constraints/)
- [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
- [Basic query operation: the join](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/join.php)
- [SQL technique: multiple joins and the distinct keyword](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/multijoin.php)
- [SQL technique: join types](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/jointypes.php)
- [SQL technique: union and minus](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/setops.php)
- [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf)
- [The Seven Types of SQL Joins](https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html)
- [MySQL Tutorial](https://www.youtube.com/watch?v=yPu6qV5byu4)
- [SQL Style Guide](https://www.sqlstyle.guide/)
- [MySQL 5.7 SQL Statement Syntax](https://dev.mysql.com/doc/refman/5.7/en/sql-statements.html)

Extra resources around relational database model design:

- [Design](https://www.guru99.com/database-design.html)
- [Normalization](https://www.guru99.com/database-normalization.html)
- [ER Modeling](https://www.guru99.com/er-modeling.html)

## Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/2012/04/feynman-technique/), **without the help of Google:**

### General
- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a ```PRIMARY KEY```
- What’s a ```FOREIGN KEY```
- How to use ```NOT NULL``` and ```UNIQUE``` constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
What are ```JOIN``` and ```UNION```

## Requirements
### General
- Allowed editors: ```vi```, ```vim```, ```emacs```
- All your files will be executed on Ubuntu 14.04 LTS using ```MySQL 5.7``` (version 5.7.8-rc)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (```SELECT```, ```WHERE```…)
- A ```README.md``` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using ```wc```

## More Info
## Comments for your SQL file:
```SQL
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```
## Install MySQL 5.7 on Ubuntu 14.04 LTS
```SQL
$ echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
$ sudo apt-get update
$ sudo apt-get install mysql-server-5.7
...
$ mysql --version
mysql  Ver 14.14 Distrib 5.7.8-rc, for Linux (x86_64) using  EditLine wrapper
$
```

**Don’t forget your ```root``` password**

If you had before MySQL 5.5 installed, please run these 2 commands after the installation of the version 5.7:
```SQL
$ mysql_upgrade -u root -p
Password: 
$ sudo service mysql restart
```
If you have some issues to upgrade to 5.7, don’t hesitate to cleanup your server of any MySQL packages: ```sudo apt-get remove --purge mysql-server mysql-client mysql-common```

## Use “container-on-demand” to run MySQL
- Ask for container ```Ubuntu 14.04 - Python 3.4```
- Connect via SSH
- Or via the WebTerminal
- In the container, you should start MySQL before playing with it:
```SQL
$ service mysql start
 * MySQL Community Server 5.7.8-rc is started
$
$ cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password: 
Database
information_schema
mysql
performance_schema
sys
$
```
**In the container, credentials are ```root/root```**

How to import a SQL dump

```sql
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```
![imagen](https://m.yht7.com/upload/image/20200606/1892531-20200606125217781-1655014001.png)
