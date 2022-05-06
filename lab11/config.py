from configparser import ConfigParser
import psycopg2, re

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

data = config()
commands = {
    'search': """ 
    CREATE OR REPLACE FUNCTION get_table (input VARCHAR) 
        RETURNS TABLE ( 
            id INT, 
            name VARCHAR, 
            number VARCHAR 
    ) 
    AS $$ 
    BEGIN 
        RETURN QUERY SELECT * FROM phonebook WHERE phonebook.name ILIKE input OR phonebook.number ILIKE input; 
    END; $$ 
    
    LANGUAGE PLPGSQL; 
    
    SELECT * FROM get_table (%s); 
    """,
    
    'update': """ 
    CREATE OR REPLACE PROCEDURE insertT(id INT, name_input VARCHAR, phone VARCHAR) 
    AS $$ 
    BEGIN 
        IF EXISTS (SELECT * FROM phonebook WHERE name = name_input) THEN 
            UPDATE phonebook SET number = phone WHERE name = name_input; 
        ELSE 
            INSERT INTO phonebook VALUES(id, name_input, phone); 
        END IF; 
    END; $$ 
    LANGUAGE PLPGSQL; 
    
    CALL insertT(%s, %s, %s); 
    """,
    
    'delete': """ 
    CREATE OR REPLACE PROCEDURE deleteT(input VARCHAR) 
    AS $$ 
    BEGIN 
        DELETE FROM phonebook WHERE phonebook.name = input OR phonebook.number = input; 
    END; $$ 
    LANGUAGE PLPGSQL; 
    
    CALL deleteT(%s); 
    """,
    
    'pagination': """ 
    SELECT * FROM phonebook ORDER BY phonebook.id LIMIT %s OFFSET %s; 
    """ 
}

def check(s): 
    return bool(re.match(r"[\+\d]?(\d{2,3}[-\.\s]??\d{2,3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})", s)) 
 