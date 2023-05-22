#import modules 
import sqlite3 as sq



#Connecting to a database and creating a cursor
con = sq.connect("bd.db", check_same_thread=False)
cur = con.cursor()




def CheckUserIdTg(id_tg):
    """Checking users by telegram id"""
    cur.execute("SELECT name, id FROM USERS WHERE id_tg = ?", (id_tg,))
    try:
        return [dict(zip([key[0] for key in cur.description], row)) for row in cur.fetchall()][0]
    except Exception as e:
        return []

# check = CheckUserIdTg("1380181607")
# print(check)



def InsertData(T, V, C=""):
    """Entering data into the database"""
    try:
        cur.execute(f'INSERT INTO {T} {C} VALUES({V})')
        con.commit()
        return[1, 2]
    except Exception as e:
        return [e]





def SelectData(T, C, V, S="*"):
    """Sending data from the database"""
    try:
        cur.execute(f'SELECT {S} FROM {T} WHERE {C} = "{V}"')
        return [dict(zip([key[0] for key in cur.description], row)) for row in cur.fetchall()][0]
    except Exception as e:
        return []


# data = SelectData("trips", "id", "")

def UpdateData(T, U, S, C, V):
    """Edit data from the database"""
    try:
        cur.execute(f'UPDATE {T} SET {U} = "{S}" WHERE {C} = "{V}"')
        con.commit()
        return[1]
    except Exception as e:
        return[]




def SelectAllData(T, C, V, S="*"):
    """Sending an array of data from a database"""
    try:
        cur.execute(f'SELECT {S} FROM {T} WHERE {C} = "{V}"')
        data = cur.fetchall()
        newList = [
            [
                dict(zip([key[0] for key in cur.description], row))
                for row in data
            ][i]
            for i in range(len(data))
        ]
        return newList
    except Exception as e:
        return []


request_bd = '"1", "0/wfaf", "6w594jWECgsLqcG7JyeQ3HSznUkxlI/p1eMlJuVrZbNBvAEwQY2n7WS4iOfdy"'
print(UpdateData("agreedTrips", "(number_of_passengers, id_passenger, ids_trips)", request_bd,  ))