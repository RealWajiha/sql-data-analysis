
import sqlite3

DB_NAME = "sales_analysis.db"


def create_database():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("PRAGMA foreign_keys = ON")

        conn.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                city TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        """)

        conn.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY,
                customer_id INTEGER NOT NULL,
                order_date TEXT NOT NULL,
                amount REAL NOT NULL CHECK(amount >= 0),
                status TEXT NOT NULL,
                FOREIGN KEY (customer_id)
                    REFERENCES customers(customer_id)
            )
        """)

        customers = [
            (1, "Ali Khan", "Lahore", "ali@example.com"),
            (2, "Sara Ahmed", "Karachi", "sara@example.com"),
            (3, "Usman Malik", "Lahore", "usman@example.com"),
            (4, "Ayesha Noor", "Islamabad", "ayesha@example.com"),
            (5, "Hamza Tariq", "Karachi", "hamza@example.com"),
            (6, "Zara Iqbal", "Multan", "zara@example.com"),
            (7, "Bilal Shah", "Lahore", "bilal@example.com"),
            (8, "Hina Aslam", "Faisalabad", "hina@example.com"),
        ]

        orders = [
            (101, 1, "2026-01-05", 15000, "Completed"),
            (102, 2, "2026-01-08", 22000, "Completed"),
            (103, 1, "2026-01-15", 8000, "Pending"),
            (104, 3, "2026-02-02", 12000, "Completed"),
            (105, 4, "2026-02-10", 30000, "Completed"),
            (106, 5, "2026-02-14", 5000, "Cancelled"),
            (107, 2, "2026-03-01", 18000, "Completed"),
            (108, 6, "2026-03-05", 9000, "Pending"),
            (109, 7, "2026-03-12", 25000, "Completed"),
            (110, 3, "2026-03-20", 7000, "Completed"),
            (111, 5, "2026-04-01", 11000, "Completed"),
            (112, 4, "2026-04-08", 14000, "Pending"),
        ]

        conn.executemany("""
            INSERT OR IGNORE INTO customers
            (customer_id, name, city, email)
            VALUES (?, ?, ?, ?)
        """, customers)

        conn.executemany("""
            INSERT OR IGNORE INTO orders
            (order_id, customer_id, order_date, amount, status)
            VALUES (?, ?, ?, ?, ?)
        """, orders)

    print("Database and tables created successfully!")
    print("Sample data inserted successfully!")


def run_query(conn, title, query):
    print(f"\n{'=' * 60}")
    print(title)
    print("=" * 60)

    cursor = conn.execute(query)
    columns = [item[0] for item in cursor.description]
    rows = cursor.fetchall()

    print(" | ".join(columns))
    print("-" * 60)

    for row in rows:
        print(" | ".join(str(value) for value in row))

    print(f"Total rows: {len(rows)}")


def main():
    create_database()

    queries = [
        (
            "1. SELECT - Display all customers",
            "SELECT * FROM customers;"
        ),
        (
            "2. WHERE - Find completed orders",
            """
            SELECT order_id, amount, status
            FROM orders
            WHERE status = 'Completed';
            """
        ),
        (
            "3. ORDER BY - Highest-value orders",
            """
            SELECT order_id, amount
            FROM orders
            ORDER BY amount DESC;
            """
        ),
        (
            "4. Aggregate functions - Overall statistics",
            """
            SELECT
                COUNT(*) AS total_orders,
                ROUND(SUM(amount), 2) AS total_order_value,
                ROUND(AVG(amount), 2) AS average_order_value,
                MIN(amount) AS minimum_order,
                MAX(amount) AS maximum_order
            FROM orders;
            """
        ),
        (
            "5. GROUP BY - Revenue by order status",
            """
            SELECT
                status,
                COUNT(*) AS order_count,
                SUM(amount) AS total_amount
            FROM orders
            GROUP BY status
            ORDER BY total_amount DESC;
            """
        ),
        (
            "6. JOIN - Orders with customer details",
            """
            SELECT
                o.order_id,
                c.name AS customer_name,
                c.city,
                o.amount,
                o.status
            FROM orders AS o
            INNER JOIN customers AS c
                ON o.customer_id = c.customer_id
            ORDER BY o.order_id;
            """
        ),
        (
            "7. GROUP BY + JOIN - Spending by customer",
            """
            SELECT
                c.name,
                COUNT(o.order_id) AS total_orders,
                SUM(o.amount) AS total_spent
            FROM customers AS c
            INNER JOIN orders AS o
                ON c.customer_id = o.customer_id
            GROUP BY c.customer_id, c.name
            ORDER BY total_spent DESC;
            """
        ),
        (
            "8. WHERE + GROUP BY - Completed sales by city",
            """
            SELECT
                c.city,
                COUNT(o.order_id) AS completed_orders,
                SUM(o.amount) AS completed_sales
            FROM customers AS c
            INNER JOIN orders AS o
                ON c.customer_id = o.customer_id
            WHERE o.status = 'Completed'
            GROUP BY c.city
            ORDER BY completed_sales DESC;
            """
        ),
    ]

    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("PRAGMA foreign_keys = ON")

        for title, query in queries:
            run_query(conn, title, query)

    print(f"\nProject completed! Database: {DB_NAME}")


if __name__ == "__main__":
    main()
