# -*- coding:UTF-8 -*-
import mysql.connector
from mysql.connector import errorcode
from cloud_log import *
import contextlib

class CloudDB(object):

    def __init__(self, **config):
        pass
        self.cnx = self.get_db_connector(**config)

    def get_db_connector(self, *args, **kwargs):
        try:
            cnx = mysql.connector.connect(**kwargs)
            return cnx
        except mysql.connector.Error as err:
            # if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            #     logger.info(err.msg)
            logger.info(err.msg)
            return

    def close(self):
        self.cnx.close()

    @contextlib.contextmanager
    def get_db_cursor(self):
        try:
            if self.cnx:
                cursor = self.cnx.cursor()
            else:
                cursor = None
            yield cursor
        except mysql.connector.Error as err:
            logger.info(err.msg)
        finally:
            if cursor:
                try:
                    cursor.close()
                except mysql.connector.errors.InternalError as err:
                    logger.info(err.msg)

                logger.info('cursor has been closed')

    def qurey(self, cmd, *args):
        with self.get_db_cursor() as cursor:
            if cursor:
                cursor.execute(cmd, *args)
                for i in cursor:
                    yield i

    def insert(self, cmd, *args):
        with self.get_db_cursor() as cursor:
            if cursor:
                cursor.execute(cmd, *args)
                self.cnx.commit()
                return True

    def update(self, cmd):
        pass
if __name__ == '__main__':
    config = {
        'host': '192.168.172.9',
        'port': 3306,
        'user': 'rwy',
        'password': 'rwy123',
        'database': 'PCY'
    }
    db = CloudDB(**config)
    cmd = "select * from point_use"
    import chardet,binascii
    upd_cmd = "update all_branchstore_details set branchstore_name = '中文测试' where branchstore_no = 200101"
    
    print(binascii.hexlify(upd_cmd))
    db.insert(upd_cmd)
    for i in db.qurey(cmd):
        print i
