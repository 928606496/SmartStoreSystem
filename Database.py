import pymysql

class Database():

    def __init__(self):
        
        self.db = pymysql.connect(host = 'Your host address',user='Your user ID', passwd = 'Your password',db='Your database name',port = "Your port number(integer)",charset='utf8')
        # Check if the database connected
        self.cursor = self.db.cursor()

    def __del__(self):
        # If connected successfully
        if self.db:
            self.db.close()
        # Close the cursor
        if self.cursor:
            self.cursor.close()

    def insert(self,age,name,sex,telephone,consumption):
        try:
            sql = ('INSERT INTO customers(age,name,sex,telephone,consumption) VALUES(%s, %s, %s ,%s, %s)')
            self.cursor.execute(sql,(age,name,sex,telephone,consumption))
            
            # It must be use this statement to commit if made any change, or else it didn't work
            self.db.commit()

        except pymysql.Error as e:
            print(e)
            print('Operate the database failed!')
    
    def delete(self,del_id):
        try:
            sql = ('DELETE FROM customers WHERE id = %s')
            self.cursor.execute(sql,(del_id))
            
            # It must be use this statement to commit if made any change, or else it didn't work
            self.db.commit()

        except pymysql.Error as e:
            print(e)
            print('Operate the database failed!')

    def update(self,update_consumption,update_id):
        try:
            sql = ('UPDATE customers SET consumption = %s WHERE id = %s')
            self.cursor.execute(sql,(update_consumption,update_id))
            
            # It must be use this statement to commit if made any change, or else it didn't work
            self.db.commit()

        except pymysql.Error as e:
            print(e)
            print('Operate the database failed!')

    def get(self,name):
        try:
            sql = ("SELECT * FROM customers where name = %s")
            self.cursor.execute(sql,(name))
            item = self.cursor.fetchall()
            return item
        except pymysql.Error as e:
            print(e)
            print('Operate the database failed!')

    def flowrate_insert(self,number,time):
        try:
            sql = ('INSERT INTO flowrate(number,time) VALUES(%s, %s)')
            self.cursor.execute(sql,(number,time))
            
            # It must be use this statement to commit if made any change, or else it didn't work
            self.db.commit()

        except pymysql.Error as e:
            print(e)
            print('Operate the database failed!')
    
    def flowrate_select(self):
        try:
            sql = ("SELECT * FROM flowrate")
            self.cursor.execute(sql)
            items = self.cursor.fetchall()
            return items
        except pymysql.Error as e:
            print(e)
            print('Operate the database failed!')

    def getAll(self):
        #This is a executed SQL statement
        data = self.cursor.execute('SELECT * FROM customers')

        #Get all data and print
        items = self.cursor.fetchall()
        # for item in items:
            # print(item)
        return items

    def getAllTimeFlowrate(self):
        data = self.cursor.execute('SELECT * FROM flowrate')

        items = self.cursor.fetchall()

        return items