# pylint:disable=C0111,C0103

def order_rank_per_customer(db):
    query = "SELECT o.OrderID, c.CustomerID, o.OrderDate ,\
            RANK() OVER (\
                    PARTITION BY c.CustomerID\
                    ORDER BY o.OrderID\
                ) AS order_rank\
            FROM Orders o \
            LEFT JOIN Customers c ON c.CustomerID = o.CustomerID "
    db.execute(query)
    results = db.fetchall()
    return results


def order_cumulative_amount_per_customer(db):
    query = "SELECT DISTINCT o.OrderID, c.CustomerID, o.OrderDate ,\
            SUM(od.UnitPrice * od.Quantity) OVER (\
                    PARTITION BY o.CustomerID\
                    ORDER BY o.OrderDate\
                ) AS cumulative_amount\
            FROM Orders o \
            JOIN Customers c ON c.CustomerID = o.CustomerID \
            JOIN OrderDetails od ON od.OrderID = o.OrderID "
    db.execute(query)
    results = db.fetchall()
    return results
