--Create psql database-- (from terminal)
psql
CREATE DATABASE readychef

--Import database-- (from dir containg data)
cd data
psql readychef < readychef.sql
--Should see some sql commands flow


--open psql database
psql readychef


-->example
SELECT owner, COUNT(*) as count
FROM pets
WHERE species = 'cat'
GROUP BY owner
HAVING COUNT(*)>=2;
ORDER BY count
LIMIT 2

-->QUERY ORDER
SELECT (DISTINCT, AGG*) <table1.col1, ..., table1.colm, table2.col1 >
FROM <table1>
JOIN <table2>
ON <table1.col1 = table2.col1>
WHERE <
GROUP BY
HAVING
ORDER BY

-->Order of evaluations
FROM + JOIN
WHERE
GROUP BY
HAVING
SELECT
DISTINCT
ORDER BY
LIMIT


--> Aggregate Functions
COUNT(*) --> counts rows
MAX(colname) --> returns max from group
MIN(colname)
AVG(colname)
