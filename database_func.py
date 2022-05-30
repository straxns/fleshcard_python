import sqlite3

def conection():
    global conn
    conn=sqlite3.connect('karte.db')
    global cursor
    cursor=conn.cursor()
def disconection():
    conn.commit()
    conn.close()
def create_table( table):

    conection()
    try:
        x=cursor.execute("SELECT * FROM "+table)
        disconection()
        return "Већ постоји шпил "+table
    except(Exception):
        cursor.execute("CREATE TABLE " + table + " (first_language TEXT,second_language TEXT,image BLOB)")
        disconection()
        return "Креиран шпил "+table
def list_tables():
    conection()
    x = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    odgovor=cursor.fetchall()
    disconection()
    return odgovor
def add_data_in_table(table,lista):
    conection()
    duzina = len(lista)
    values=[]
    for list_element in lista:
        values.append(list_element.add_data())
    cursor.executemany('INSERT INTO '+table+' VALUES(?,?,?);',values)
    disconection()
def fetch_all_data(table):
    conection()
    x = cursor.execute("SELECT * FROM "+table)
    odgovor=cursor.fetchall()
    disconection()
    return odgovor

