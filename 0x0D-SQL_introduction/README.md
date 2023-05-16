#0x0D. SQL - Introduction.

ts a database
Whats a relational database
What does SQL stand for
Whats MySQL
How to create a database in MySQL
What does DDL and DML stand for
How to CREATE or ALTER a table
How to SELECT data from a table
How to INSERT, UPDATE or DELETE data
What are subqueries
How to use MySQL functions
#Installation

All the files to be executed on Ubuntu 14.04 LTS using MySQL 5.7 (version 5.7.8-rc)

cat file_name.sql | mysql -hlocalhost -uroot -p
Usage
Educational purposes

Tasks (to run the script values has to be passed as arguments)
0-list_databases.sql: script that lists all databases of your MySQL server

1-create_database_if_missing.sql: script that creates the database hbtn_0c_0 in your MySQL server.

2-remove_database.sql: script that deletes the database hbtn_0c_0 in your MySQL server.

3-list_tables.sql: script that lists all the tables of a database in your MySQL server, the database name will be passed as argument of mysql.

4-first_table.sql: script that creates a table called first_table in the current database in your MySQL server, the database name will be passed as an argument of the mysql command.

5-full_table.sql: script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.

6-list_values.sql: script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.

7-insert_value.sql: script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.

8-count_89.sql: script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.

9-full_creation.sql: Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

10-top_score.sql: script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

11-best_score.sql: script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.

12-no_cheating.sql: script that updates the score of Bob to 10 in the table second_table.

13-change_class.sql: script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.

14-average.sql: Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.

15-groups.sql: Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.

16-no_link.sql: Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

-Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you dont need to handle x and y here.

-Update the class Rectangle by overriding the str method so that it returns [Rectangle] () / - /

-Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y

-Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute. 9- Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes.

-Write the class Square that inherits from Rectangle

-Update the class Square by adding the public getter and setter size

-Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes.

Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle.

Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square.

Update the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries:

-Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs

-Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string

-Update the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set.

-Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances.
