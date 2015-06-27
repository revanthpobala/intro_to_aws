import time
import MySQLdb
import mysql.connector
from mysql.connector import errorcode
import random
import memcache


class connection_executing():
    global connection  
    global query1
    global query2
    global query3

      
    try:
        connection = MySQLdb.connect(host = 'revanth.cpuumacqldvr.eu-central-1.rds.amazonaws.com',
                                 port = 3306,
                                 user = 'revanth1108',
                                 passwd = 'revanth1108',
                                 db='project4',
                                 local_infile = 1)
        print "succesfully connected to database"

        
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    
    
    def execute_query(self): 
        cursor = connection.cursor()
        st = time.time()
        q = """LOAD DATA LOCAL INFILE  'huge_data.csv'
                INTO TABLE huge_data
                FIELDS TERMINATED BY ',' 
                ENCLOSED BY '"'
                LINES TERMINATED BY '\n'
                IGNORE 1 ROWS;"""
        cursor.execute(q)
        et = time.time()
        print "Executed in  time" , (et-st)
        #connection.commit()   
        
             
    def normal_execute(self,num,maxi):
        cursor = connection.cursor()
        rand = random.randint(1,maxi)
        randu = random.randint(0,2)
        st = time.time()
        rand = random.randint(1,maxi)
        if randu == 0:
            for i  in range (0,num):
                query1 = str('select * from huge_data where id = '+str(rand)+' ;')
                cursor.execute(query1)
        elif randu == 1:
            for i  in range (0,num):
                query2 = str('select * from huge_data where id = '+str(rand)+' ;')
                cursor.execute(query2)
        elif randu  == 2:
            for i  in range (0,num):
                query3 = str('select * from huge_data where id = '+str(rand)+' ;') 
                cursor.execute(query3)   
        et = time.time()
        print "Executed in time" , (et-st) 
        
        
                      
    
    def execute_random(self,num,maxi):
        cursor = connection.cursor()
        st = time.time()
        #memc = memcache.Client(['127.0.0.1:11211'], debug=1);
        memc = memcache.Client(["127.0.0.1:11211"], debug=1);
        key = memc.get('testkey')
        rand = random.randint(1,maxi)
        memc.flush_all()
        query1 = str('select * from huge_data where id = '+str(rand)+' ;')
        query2 = str('select * from huge_data where id = '+str(rand)+' ;')
        query3 = str('select * from huge_data where id = '+str(rand)+' ;')

        for i in range(1,maxi):
            randu = random.randint(0,2) 
            if randu == 0:
                query_1 = memc.get('query1')
                if not query1:
                    query1 = str(query1)
                    cursor.execute(query1)
                    row = cursor.fetchall()
                    print row
                    memc.set('query_1',row,maxi)
                    print "done"
                else:
                    print "updated"
            elif randu == 1:
                query2 = str(query2)
                query_2 = memc.get('query2')
                if not query2:
                    cursor.execute(query2)
                    row = cursor.fetchall()
                    print row
                    memc.set('query_2',row,maxi)
                    print "done"
                else:
                    print "updated"
            elif randu ==2 :
                query3 = str(query3)
                query_3 = memc.get('query3')
                if not query3:
                    cursor.execute(query3)
                    row = cursor.fetchall()
                    memc.set('query_3',row,maxi)
                    print "done"
                else:
                    print "updated"
        et = time.time()
        print "Executed in time" , (et-st)       
        
           


con = connection_executing()
#con.execute_query() 
#con.execute_random(1450, 100000)     
#con.normal_execute(100, 100)               
                
                
                
                
                
                
                
                
                
