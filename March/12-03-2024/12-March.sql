create database Mar_12;
use mar_12;

-- 1.
-- Write a SQL query to get the second highest salary from the 
-- Employee table.

-- +----+--------+
-- | Id | Salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

-- +---------------------+
-- | SecondHighestSalary |
-- +---------------------+
-- | 200                 |
-- +---------------------+

CREATE TABLE Employee(
Id INT PRIMARY KEY,
Salary INT);

INSERT INTO Employee values
(1,100),(2,200),(3,300);

select * from Employee;

#getting the second highest salary by making all data unique and sorting it in descending order, leaving 1 data from upward
select  distinct Salary AS SecondHighestSalary from Employee order by Salary desc limit 1 offset 1;


-- 2.Table: Calls

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | from_id     | int     |
-- | to_id       | int     |
-- | duration    | int     |
-- +-------------+---------+
-- This table does not have a primary key, it may contain duplicates.
-- This table contains the duration of a phone call between from_id and to_id.
-- from_id != to_id

-- Write an SQL query to report the number of calls and the total call duration between each pair of distinct persons (person1, person2) where person1 < person2.

-- Return the result table in any order.

-- The query result format is in the following example:

-- Calls table:
-- +---------+-------+----------+
-- | from_id | to_id | duration |
-- +---------+-------+----------+
-- | 1       | 2     | 59       |
-- | 2       | 1     | 11       |
-- | 1       | 3     | 20       |
-- | 3       | 4     | 100      |
-- | 3       | 4     | 200      |
-- | 3       | 4     | 200      |
-- | 4       | 3     | 499      |
-- +---------+-------+----------+

-- Result table:
-- +---------+---------+------------+----------------+
-- | person1 | person2 | call_count | total_duration |
-- +---------+---------+------------+----------------+
-- | 1       | 2       | 2          | 70             |
-- | 1       | 3       | 1          | 20             |
-- | 3       | 4       | 4          | 999            |
-- +---------+---------+------------+----------------+
-- Users 1 and 2 had 2 calls and the total duration is 70 (59 + 11).
-- Users 1 and 3 had 1 call and the total duration is 20.
-- Users 3 and 4 had 4 calls and the total duration is 999 (100 + 200 + 200 + 499).

create table Calls(
from_id int, to_id int, duration int);

insert into Calls values (1,2,59),(2,1,11),(1,3,20),(3,4,100),(3,4,200),(3,4,200),(4,3,499);

select * from Calls;

SELECT CASE WHEN from_id < to_id THEN from_id ELSE to_id END AS person1,
	   CASE WHEN from_id < to_id THEN to_id ELSE from_id END AS person2,
	   COUNT(*) AS call_count,
	   SUM(duration) AS total_duration
FROM Calls
GROUP BY person1, person2
ORDER BY person1, person2;


-- 3.A U.S graduate school has students from Asia, Europe and America. 
-- The students' location information are stored in table student as below.


-- | name   | continent |
-- |--------|-----------|
-- | Jack   | America   |
-- | Pascal | Europe    |
-- | Xi     | Asia      |
-- | Jane   | America   |


-- Pivot the continent column in this table so that each name is sorted alphabetically and displayed
-- underneath its corresponding continent. The output headers should be America, Asia and Europe respe
-- ctively.It is guaranteed that the student number from America is no less than either Asia or Europe.


-- For the sample input, the output is:


-- | America | Asia | Europe |
-- |---------|------|--------|
-- | Jack    | Xi   | Pascal |
-- | Jane    |      |        |


create table student (
name varchar(50),
continent varchar(50));

insert into student values ('Jack','America'),('Pascal','Europe'),('Xi','Asia'),('Jane','America');

WITH RankedStudents AS (
    SELECT
        name,
        continent,
        ROW_NUMBER() OVER (PARTITION BY continent ORDER BY name) AS row_num
    FROM student
)

SELECT
    MAX(CASE WHEN continent = 'America' THEN name END) AS America,
    MAX(CASE WHEN continent = 'Asia' THEN name END) AS Asia,
    MAX(CASE WHEN continent = 'Europe' THEN name END) AS Europe
FROM RankedStudents
GROUP BY row_num
ORDER BY row_num;
