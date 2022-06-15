import mysql.connector 


class Connect:
    def conn(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="thunder",
                password="0980620014",
                database="hardware"
            )
        except Exception as err:
            print(err)
        finally:
            return mydb
            
class Manager(Connect):
    pass
