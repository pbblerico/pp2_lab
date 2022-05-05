from configparser import ConfigParser
import psycopg2

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

def create_table():
    create_tab = '''
        create table snake(
            player varchar,
            score integer,
            level integer
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

def insert_data(nickname, score, lvl): 
    sql = '''
        insert into snake (player, score, level) 
        values(%s, %s, %s);
    '''
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (nickname, score, lvl))
        conn.commit()
        cur.close()
        print('done') #checks whether the action is done
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

#updates the number by its name
def update(nickname, score, lvl):
    sql = """ UPDATE snake
                SET score = %s, level = %s
                WHERE player = %s;"""
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (score, lvl, nickname))
        conn.commit()
        cur.close()
        print('done') #checks whether the action is done
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

#checks whether the player's name already exists
def check_existence(nickname, score, lvl):
    exist = 'select * from snake where player = %s'
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(exist, (nickname,))
        check = cur.fetchone()
        if check == None:
            insert_data(nickname, score, lvl)
        else: 
            if check[1] <= score: 
                update(nickname, score, lvl)
                print(f'good job!\nnew record: {score}')
            else: print(f'Last time you was better...\nrecord: {check[1]}\ncurrent score: {score}')
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def prev_stat(nickname):
    exist = 'select * from snake where player = %s'
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(exist, (nickname,))
        check = cur.fetchone()
        if check != None:
            print('-' * 10, f'Player {nickname}', '-' * 10)
            print(f'Score: {check[1]}')
            print(f'Level: {check[2]}')
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def query():
    all = 'select * from snake;'
    conn, result = None, None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(all)
        result = cur.fetchall()
        for i in result:
            print(list(i))

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()