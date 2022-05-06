import psycopg2, csv
from config import *

con = psycopg2.connect(**data) 
cur = con.cursor() 

while True: 
    command = input("""Choose the operation that you need and type its code:
        \t0 - search, \t3 - pagination, 
        \t1 - update, \t4 - delete,
        \t2 - insert, \t5 - exit
    """) 
     
    if command == '0': 
        n = input("Enter the name or the number:\n\t") 
        word = '%' + n + '%' 
        cur.execute(commands['search'], (word,)) 
        if len(cur.fetchall()) != 0: print(*cur.fetchall(), sep = '\n') 
        else: print("Contact doesn't exist\n")
             
    if command == '1': 
        id, name, phone_num = int(input("Enter ID:\t")), input("Enter name:\t"), input("Enter the number:\t")  
        if check(phone_num): cur.execute(commands['update'], (id, name, phone_num)) 
        else: print('Incorrect number format')
 
    if command == '2':
        with open("numbers.csv", "r") as f: 
            no_errors = True
            incorrect_format = []
            reader = csv.reader(f, delimiter=",") 
            for row in reader:  
                if check(row[2]): 
                    cur.execute(commands['update'], row) 
                else:
                    no_errors = False
                    print(*row, 'has incorrect format')
            if no_errors: print('Phonebook was successfully updated')
            print()
            con.commit()

    if command == '3': 
        a, b = map(int, input("LIMIT, OFFSET: ").split()) 
        cur.execute(commands['pagination'], (a, b)) 
        print(*cur.fetchall(), sep = '\n') 

    if command == '4': 
        name = input("Enter the name or the number to delete: ") 
        cur.execute(commands['delete'], (name,)) 
        con.commit() 

    if command == '5': break 
         
cur.close() 
con.commit() 
con.close()