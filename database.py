import psycopg2 as sql


def create_table():
    conn=sql.connect("dbname='vanniew' user='vanniew' password='' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = sql.connect("dbname='vanniew' user='vanniew' password='' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = sql.connect("dbname='vanniew' user='vanniew' password='' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute('SELECT * FROM store')
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = sql.connect("dbname='vanniew' user='vanniew' password='' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute('DELETE FROM store WHERE item=%s', (item,))
    conn.commit()
    conn.close()


def update_quantity(item, quantity):
    conn = sql.connect("dbname='vanniew' user='vanniew' password='' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute('UPDATE store SET quantity=%s WHERE item=%s', (quantity, item))
    conn.commit()
    conn.close()


create_table()
#insert('China Plate', 1, 9.75)
#insert('Tea Cup', 5, 5)
delete('Tea Cup')
# delete('Wine Glass')
update_quantity('Wine Glass', 1000)
print(view())



