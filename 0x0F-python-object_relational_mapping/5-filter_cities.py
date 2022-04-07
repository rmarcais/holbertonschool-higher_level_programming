#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities \
WHERE state_id IN (SELECT id FROM states WHERE name = %s) ORDER BY id ASC",
                (argv[4], ))
    query_rows = cur.fetchall()
    array = []
    for row in query_rows:
        array.append(row[0])
    arr = ", ".join(array)
    print(arr)
    cur.close()
    conn.close()
