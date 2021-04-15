# KEYWORDS

### Select

### Where

[Comparisons](https://www.notion.so/d3b74f4272bf47b4b15acf0287199879)

### Like

- using wildcards: _____(exact amount of characters), %TEXT%(with that substring)

### And & Or

- all or either one respectively

### In & Not In

- Check for all that are in parentheses and check for all that are not in parentheses

### Distinct

`SELECT DISTINCT nationality FROM characters;`

### Order By

`SELECT *[COLUMNS] FROM characters ORDER BY height DESC;`

### Case statements

- create a new variable and set the values based on a series of conditions being met

`SELECT name, CASE WHEN species = 'Human' THEN 'HUMAN' ELSE 'ALIEN' END FROM characters;`

### Limit

`SELECT * FROM characters ORDER BY height ASC LIMIT 1;`

### COUNT, SUM, MIN, MAX and AVG

- SUM: use it to add up all of the values in a particular column

    `SELECT SUM(budget) FROM movies;`

- COUNT:

    `SELECT COUNT(*) FROM characters;`

    `SELECT COUNT(*) FROM characters WHERE nationality='Asgardian';`

- AVG:

    `SELECT AVG(budget) FROM movies;`

- MAX: find out what the highest value within a specified column is
- MIN: find out what the lowest value within a specified column is

    `SELECT MIN(budget), MAX(budget) FROM movies;`

### GROUP BY

- split our data up into smaller segments to allow greater comparison

    `SELECT nationality, COUNT(*) FROM characters GROUP BY nationality;`

- HAVING Clause: apply filters and constraints to the grouped data and aggregate functions

    `SELECT nationality, COUNT(*) FROM characters GROUP BY nationality HAVING COUNT(id) > 1;`

### "IS NULL" or "IS NOT NULL

`SELECT * FROM characters WHERE alter_ego IS NOT NULL;`

- COALESCE: lets us take several columns within one row of our data and return the first column that has a non-NULL value. If all columns specified are NULL then we can set a default value in the COALESCE function.
    - eg if you want to do an AVG aggregate

        ```sql
        SELECT AVG(COALESCE(HolidaysTaken, 0))
        FROM AnnualLeave;

        ```

    - We could also use COALESCE to consolidate several columns into a "best fit" value amongst them. Imagine our Customers table had three separate fields for Home Phone Number, Mobile Phone Number and Business Phone Number. All allow NULL values as not every customer would have all of those means of contact.

        ```sql
        SELECT
            CustomerName,
            COALESCE(HomePhone, MobilePhone, BusinessPhone) as PhoneNumber
        FROM Customers;
        ```

        `SELECT COALESCE(alter_ego, name) FROM characters;`
