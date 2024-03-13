create database March;
Use March;


#QUESTION 1
-- 1.Problem statement
-- Table: Customer

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | customer_id | int     |
-- | product_key | int     |
-- +-------------+---------+
-- product_key is a foreign key to Product table.

-- Table: Product

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | product_key | int     |
-- +-------------+---------+
-- product_key is the primary key column for this table.

-- Write an SQL query for a report that provides the customer ids from the Customer table that bought all the products in the Product
 -- table.

-- Return the result table in any order.

-- The query result format is in the following example:

-- Customer table:
-- +-------------+-------------+
-- | customer_id | product_key |
-- +-------------+-------------+
-- | 1           | 5           |
-- | 2           | 6           |
-- | 3           | 5           |
-- | 3           | 6           |
-- | 1           | 6           |
-- +-------------+-------------+

-- Product table:
-- +-------------+
-- | product_key |
-- +-------------+
-- | 5           |
-- | 6           |
-- +-------------+

-- Result table:
-- +-------------+
-- | customer_id |
-- +-------------+
-- | 1           |
-- | 3           |
-- +-------------+
-- The customers who bought all the products (5 and 6) are customers with id 1 and 3.

#SOLUTION 1
create table Product(product_key int primary key);
insert into Product values (5),(6);
select * from Product;

create table Customer(customer_id int , product_key int, foreign key (product_key) references Product(product_key));
insert into Customer values(1, 5),(2, 6),(3, 5),(3, 6),(1, 6);
select * from Customer;

SELECT customer_id FROM Customer GROUP BY customer_id HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product);


#QUESTION 2
-- 2.Problem statement
-- Table: Products

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | product_id  | int     |
-- | low_fats    | enum    |
-- | recyclable  | enum    |
-- +-------------+---------+
-- product_id is the primary key for this table.
-- low_fats is an ENUM of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
-- recyclable is an ENUM of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.

-- Write an SQL query to find the ids of products that are both low fat and recyclable.

-- Return the result table in any order.

-- The query result format is in the following example:

-- Products table:
-- +-------------+----------+------------+
-- | product_id  | low_fats | recyclable |
-- +-------------+----------+------------+
-- | 0           | Y        | N          |
-- | 1           | Y        | Y          |
-- | 2           | N        | Y          |
-- | 3           | Y        | Y          |
-- | 4           | N        | N          |
-- +-------------+----------+------------+
-- Result table:
-- +-------------+
-- | product_id  |
-- +-------------+
-- | 1           |
-- | 3           |
-- +-------------+
-- Only products 1 and 3 are both low fat and recyclable.

#SOLUTION 2
create table Products(product_id int primary key, low_fats enum('Y', 'N'), recyclable enum('Y', 'N'));
insert into Products values (0,'Y','N'), (1,'Y','Y'), (2,'N','Y'), (3,'Y','Y'), (4,'N','N');
 select product_id from Products where low_fats = "Y" and recyclable = 'Y';
 
 #QUESTION 3
--  3.Problem statement
--  A pupil Tim gets homework to identify whether three line segments could possibly form a triangle.

--  However, this assignment is very heavy because there are hundreds of records to calculate.

-- Could you help Tim by writing a query to judge whether these three  sides can form a triangle, assuming table triangle holds the 
-- length of the three sides x, y and z.

-- | x  | y  | z  |
-- |----|----|----|
-- | 13 | 15 | 30 |
-- | 10 | 20 | 15 |

--  For the sample data above, your query should return the follow result:
--  | x  | y  | z  | triangle |
--  |----|----|----|----------|
--  | 13 | 15 | 30 | No       |
--  | 10 | 20 | 15 | Yes      |

#SOLUTION 3
create table Triangle(x int ,y int, z int);
insert into Triangle values (13,15,30),(10,20,15);
select * from Triangle;
select x,y,z, 
    IF(x + y > z AND x + z > y AND y + z > x, 'Yes', 'No') AS triangle
from Triangle;

select x,y,z, 
	case
		when x+y>z and x+z>y and y+z>x then 'Yes' 
		else 'No' 
 	end as triangle 
from Triangle;

#QUESTION 4
-- 4.Problem statement
-- Table: Friends

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | name          | varchar |
-- | activity      | varchar |
-- +---------------+---------+
-- id is the id of the friend and primary key for this table.
-- name is the name of the friend.
-- activity is the name of the activity which the friend takes part in.
-- Table: Activities

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | name          | varchar |
-- +---------------+---------+
-- id is the primary key for this table.
-- name is the name of the activity.

-- Write an SQL query to find the names of all the activities with neither maximum, nor minimum number of participants.

-- Return the result table in any order. Each activity in table Activities is performed by any person in the table Friends.

-- The query result format is in the following example:

-- Friends table:
-- +------+--------------+---------------+
-- | id   | name         | activity      |
-- +------+--------------+---------------+
-- | 1    | Jonathan D.  | Eating        |
-- | 2    | Jade W.      | Singing       |
-- | 3    | Victor J.    | Singing       |
-- | 4    | Elvis Q.     | Eating        |
-- | 5    | Daniel A.    | Eating        |
-- | 6    | Bob B.       | Horse Riding  |
-- +------+--------------+---------------+

-- Activities table:
-- +------+--------------+
-- | id   | name         |
-- +------+--------------+
-- | 1    | Eating       |
-- | 2    | Singing      |
-- | 3    | Horse Riding |
-- +------+--------------+

-- Result table:
-- +--------------+
-- | activity     |
-- +--------------+
-- | Singing      |
-- +--------------+

-- Eating activity is performed by 3 friends, maximum number of participants, (Jonathan D. , Elvis Q. and Daniel A.)
-- Horse Riding activity is performed by 1 friend, minimum number of participants, (Bob B.)
-- Singing is performed by 2 friends (Victor J. and Jade W.)

#SOLUTION 4
create table Friends (id int primary key, name varchar(50), activity varchar(50));
insert into Friends values (1, 'Jonathan D.', 'Eating'),
    (2, 'Jade W.', 'Singing'),
    (3, 'Victor J.', 'Singing'),
    (4, 'Elvis Q.', 'Eating'),
    (5, 'Daniel A.', 'Eating'),
    (6, 'Bob B.', 'Horse Riding');
    
    create table Activities (id int primary key, activity varchar(50));
    INSERT into Activities values (1, 'Eating'),
    (2, 'Singing'),
    (3, 'Horse Riding');
    
SELECT a.activity AS activity
FROM Activities a
JOIN (
    SELECT activity, COUNT(*) AS participant_count
    FROM Friends
    GROUP BY Activity
    HAVING participant_count != (SELECT MIN(participant_count) FROM (SELECT COUNT(*) AS participant_count FROM Friends GROUP BY activity) AS min_count)
    AND participant_count != (SELECT MAX(participant_count) FROM (SELECT COUNT(*) AS participant_count FROM Friends GROUP BY activity) AS max_count)
) AS filtered_activities ON a.activity = filtered_activities.activity;


#QUESTION 5
-- 5.Problem statement
-- There is a table courses with columns: student and class

-- Please list out all classes which have more than or equal to 5 students.

-- For example, the table:

-- +---------+------------+
-- | student | class      |
-- +---------+------------+
-- | A       | Math       |
-- | B       | English    |
-- | C       | Math       |
-- | D       | Biology    |
-- | E       | Math       |
-- | F       | Computer   |
-- | G       | Math       |
-- | H       | Math       |
-- | I       | Math       |
-- +---------+------------+

-- Should output:

-- +---------+
-- | class   |
-- +---------+
-- | Math    |
-- +---------+
    
    
#SOLUTION 5
create table Courses (student varchar(50), class varchar(50));
insert into Courses values ('A','Math'),('B','English'),
                           ('C','Math'),('D','Biology'),
                           ('E','Math'),('F','Computer'),
                           ('G','Math'),('H','Math'),('I','Math');

select class from Courses group by class having count(*) >=5;

#QUESTION 6
-- 6.Problem statement
-- Write a SQL query to find all duplicate emails in a table named Person.

-- +----+---------+
-- | Id | Email   |
-- +----+---------+
-- | 1  | a@b.com |
-- | 2  | c@d.com |
-- | 3  | a@b.com |
-- +----+---------+
-- For example, your query should return the following for the above table:

-- +---------+
-- | Email   |
-- +---------+
-- | a@b.com |
-- +---------+

#ANSWER 6
create table Person (Id int, Email varchar(50));
insert into Person values (1,'a@b.com'),(2,'c@d.com'),(3,'a@b.com');
select * from Person;
select Email from Person group by Email having count(*)>1;


#QUESTION 7
-- 7.Problem statement
-- Table: Submissions

-- +---------------+----------+
-- | Column Name   | Type     |
-- +---------------+----------+
-- | sub_id        | int      |
-- | parent_id     | int      |
-- +---------------+----------+
-- There is no primary key for this table, it may have duplicate rows.
-- Each row can be a post or comment on the post.
-- parent_id is null for posts.
-- parent_id for comments is sub_id for another post in the table.


-- Write an SQL query to find number of comments per each post.

-- Result table should contain post_id and its corresponding number_of_comments, and must be sorted by post_id in ascending order.

-- Submissions may contain duplicate comments. You should count the number of unique comments per post.

-- Submissions may contain duplicate posts. You should treat them as one post.

-- The query result format is in the following example:

-- Submissions table:
-- +---------+------------+
-- | sub_id  | parent_id  |
-- +---------+------------+
-- | 1       | Null       |
-- | 2       | Null       |
-- | 1       | Null       |
-- | 12      | Null       |
-- | 3       | 1          |
-- | 5       | 2          |
-- | 3       | 1          |
-- | 4       | 1          |
-- | 9       | 1          |
-- | 10      | 2          |
-- | 6       | 7          |
-- +---------+------------+

--  Result table:
-- +---------+--------------------+
-- | post_id | number_of_comments |
-- +---------+--------------------+
-- | 1       | 3                  |
-- | 2       | 2                  |
-- | 12      | 0                  |
-- +---------+--------------------+

-- The post with id 1 has three comments in the table with id 3, 4 and 9. The comment with id 3 is repeated in the table, we counted it only once.
-- The post with id 2 has two comments in the table with id 5 and 10.
-- The post with id 12 has no comments in the table.
-- The comment with id 6 is a comment on a deleted post with id 7 so we ignored it.

#ANSWER 7
CREATE TABLE Submissions (sub_id INT,parent_id INT);
INSERT INTO Submissions (sub_id, parent_id)
VALUES(1, NULL),(2, NULL),(1, NULL),(12, NULL),
    (3, 1),(5, 2),(3, 1),(4, 1),(9, 1),(10, 2),(6, 7);
    
-- SELECT parent_id AS post_id, COUNT(DISTINCT sub_id) AS number_of_comments FROM Submissions
-- WHERE parent_id IS NOT NULL GROUP BY parent_id ORDER BY parent_id;

SELECT s.sub_id AS post_id,
COUNT(DISTINCT c.sub_id) AS number_of_comments 
FROM Submissions s LEFT JOIN Submissions c ON s.sub_id=c.parent_id 
WHERE s.parent_id IS NULL 
GROUP BY s.sub_id
ORDER BY s.sub_id;





