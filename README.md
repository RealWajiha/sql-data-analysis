# SQL Data Analysis — Customer & Sales Insights

## Project Overview

This project demonstrates practical SQL data analysis using SQLite. It uses a relational database containing customer information and sales orders to extract meaningful business insights.

## Objectives

- Create relational database tables.
- Insert and query sample datasets.
- Retrieve records using `SELECT`.
- Filter data using `WHERE`.
- Sort results using `ORDER BY`.
- Group records using `GROUP BY`.
- Combine tables using `INNER JOIN` and `LEFT JOIN`.
- Apply aggregate functions such as `COUNT`, `SUM`, `AVG`, `MIN`, and `MAX`.
- Filter grouped results using `HAVING`.
- Analyze customer spending and completed sales by city.

## Technologies Used

- SQLite
- SQL
- GitHub

## Database Schema

### Customers

| Column | Description |
|---|---|
| customer_id | Primary key |
| name | Customer name |
| city | Customer city |
| email | Customer email |

### Orders

| Column | Description |
|---|---|
| order_id | Primary key |
| customer_id | Foreign key referencing customers |
| order_date | Order date |
| amount | Order amount |
| status | Order status |

## Dataset

The project contains:
- 8 sample customers
- 5 sample orders
- Completed and pending order statuses

All records are fictional and intended for learning purposes. Amounts are expressed in generic currency units.

## How to Run

1. Open [SQLite Online](https://sqliteonline.com/).
2. Select SQLite as the database engine.
3. Open the `analysis_queries.sql` file from this repository and copy its contents into the SQL editor.
4. Execute the script.
5. Review the query outputs and analytical results.

**Note:** The script drops and recreates the project tables. Use it as a fresh setup script.

## SQL Concepts Demonstrated

| SQL Concept | Purpose |
|---|---|
| SELECT | Retrieve records |
| WHERE | Filter records |
| ORDER BY | Sort results |
| GROUP BY | Summarize groups |
| INNER JOIN | Match related records |
| LEFT JOIN | Preserve all records from the left table |
| Aggregate functions | Calculate totals, averages, minimums, maximums, and counts |
| HAVING | Filter grouped results |

## Expected Results

- Total customers: 8
- Total orders: 5
- Completed orders: 4
- Total order value: 87,000
- Completed sales value: 79,000

## Conclusion

This project demonstrates how SQL can be used to organize relational data, analyze sales performance, compare customer spending, and produce useful business summaries.

## Author

Wajiha Fareed

## License

This project is available for educational and portfolio purposes.
