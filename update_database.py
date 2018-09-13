import pymysql

class MySqlCommand(object):
    # initialization
    def __init__(self):
        self.host = 'localhost'
        self.port = 3306
        self.user = 'root'
        self.password = 'geniusroot'
        self.db = 'blackEyePeans'
    # connect to database
    def connectMySql(self):
        try:
            self.conn = pymysql.connect(host=self.host,port=self.port,user=self.user,
                                        passwd=self.password,db=self.db,charset='utf8')
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(e)

    def insertData(self,mydict, table='devs'):
        #fix insertdata into format values
        for key, value in mydict.items():
            mydict[key] = str(value)
        if (mydict[key] == '[]' or mydict[key] == '{}'):
                mydict[key] = 'null'
        '''
        # check if the data exist
        sqlSelect = 'select dev_ip from {} where dev_ip = "{}"'.format(table,mydict['dev_ip'])
        response = self.cursor.execute(sqlSelect)
        if response:
            print(' the dev {} is already exist, insert a new one '.format(mydict['dev_ip']))
            return 0
        '''
        # insert data to database
        try:
            cols = ', '.join(mydict.keys())
            values = '\",\"'.join(mydict.values())
            sqlInsert = 'insert into {} ({}) values (\"{}\")'.format(table, cols, values)
            try:
                result = self.cursor.execute(sqlInsert)
                insert_id = self.conn.insert_id()
                self.conn.commit()
                if result:
                    print('insert success, the id is {}.'.format(insert_id))
                    return insert_id+1
            except pymysql.Error as e:
                # rollback if something goes wrong
                self.conn.rollback()
                # check primary key
                if "key 'PRIMARY'" in e.args[1]:
                    print(' the data is already exist.')
                else:
                    print('insert failed, {} : {}'.format(e.args[0],e.args[1]))
        except pymysql.Error as e:
            print('insert failed, {} : {}'.format(e.args[0],e.args[1]))