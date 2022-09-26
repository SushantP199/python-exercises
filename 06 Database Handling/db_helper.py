import sqlite3

db = 'my_todo.db'
table_name = 'tasks'
con = sqlite3.connect(db)
c = con.cursor()

def create_table():
    sql = 'CREATE TABLE IF NOT EXISTS ' + table_name\
          + '(ID INTEGER PRIMARY KEY, \
          TaskName text)'
    c.execute(sql)

def data_entry(t_id,task):
    c.execute("INSERT INTO "+ table_name + " VALUES ( ? ,?)",\
              (t_id,task))
    print("Task is added")
    con.commit()

def print_data():
    sql = 'SELECT * FROM '+ table_name
    data = c.execute(sql)
    # for row in c.fetchall():
    print(" ID       TaskName ")
    print("_ _ _   _ _ _ _ _ _")
    for row in data:
        print(row[0] ,"\t"+row[1])

def delete_task(index):
    c.execute('DELETE FROM '+table_name+' WHERE ID = ?',\
              (index, ))
    print("Task is deleted from databse")
    con.commit()

def close():
    c.close()
    con.close()