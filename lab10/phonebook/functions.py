from configparser import ConfigParser
import psycopg2, csv

def config(file='database.ini', section='postrgresql'):
    parser = ConfigParser()
    parser.read(file)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('not found')

    return db


#creates new table
def create_table():
    create_tab = '''
        create table phonebook(
            id integer,
            name varchar,
            number varchar
        )
        ;
        '''
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(create_tab)
        cur.close()
        conn.commit()
        print('done') #checks whether the action is done
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

#inserts new data in the table
def insert_data(): 
    method = int(input('print 0 if you want to use csv method, 1 otherwise:\n'))
    sql = '''
        insert into phonebook (id, name, number) 
        values(%s, %s, %s);
    '''
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        if method == 0:
            with open("numbers.csv", "r") as f:
                reader = csv.reader(f, delimiter=",")
                for row in reader:
                    cur.execute(sql, row)
                    
        elif method == 1:
            id, name, ph_number = input('print id\t'), input('print name\t'), input('print number\t')
            cur.execute(sql, (id, name, ph_number))

        conn.commit()
        cur.close()
        print('done') #checks whether the action is done
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

#updates the number by its name
def update(name, ph_number):
    sql = """ UPDATE phonebook
                SET number = %s
                WHERE name = %s;"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (ph_number, name))
        conn.commit()
        cur.close()
        print('done') #checks whether the action is done
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def query():
    action = int(input('0 for complete table, 1 for id and number, 2 for name and number'))
    all = 'select * from phonebook;'
    conn, result = None, None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(all)
        if action == 0:
            result = cur.fetchall()
            for i in result:
                print(list(i))
        elif action == 1:
            result = cur.fetchall()
            for i in result:
                print(result[i][0], result[i][1])
        elif action == 2:
            result = cur.fetchall()
            for i in result:
                print(result[i][1], result[i][2])
            
        conn.commit()
        cur.close()
        print('done') #checks whether the action is done
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

#delete some rows in the table
def delete_data():
    method = int(input('print 0 if you want delete all rows, and 1 if only some of them\t'))
    delete_all = '''delete from phonebook;'''
    delete_by_name = '''delete from phonebook where name = %s;'''
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        if method == 0: cur.execute(delete_all)
        elif method == 1: 
            name = input()
            cur.execute(delete_by_name, (name,))
        conn.commit()
        cur.close()
        print('done') #checks whether the action is done
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

