#!/usr/bin/env python

import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir='/usr/local/OracleXE/instantclient_19_22')

conn = None
cur = None

try:
    # id/pw@hostname:port_number/sid
    loginfo = 'hr/1234@192.168.1.84:1521/xe'
    conn = cx_Oracle.connect(loginfo)
    print(type(conn))

    cur = conn.cursor()
    print(type(cur))

    sql = 'select power(2, 10) from dual'
    cur.execute(sql)

    for item in cur:
        print(item)

except Exception as err:
    print(err)

finally:
    if cur != None:
        cur.close()

    if conn != None:
        conn.close()

print('finished..')