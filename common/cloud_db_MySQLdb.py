# coding=utf-8

from cloud_log import *
import contextlib
import MySQLdb

class CloudDB(object):

    def __init__(self, **config):
        self.connect_db(**config)

    def connect_db(self, **config):
        try:
            self.cnx = MySQLdb.connect(**config)
        except MySQLdb.Error as err:
            self.cnx = None
            logger.info(err)

    @contextlib.contextmanager
    def get_db_cursor(self):
        try:
            cursor = None
            if self.cnx:
                cursor = self.cnx.cursor()
        except MySQLdb.Error as err:
            logger.info(err)

        try:
            yield cursor
            if cursor:
                self.cnx.commit()
        except MySQLdb.Error as err:
            self.cnx.rollback()
            logger.info(err)
            logger.info('cursor has been rollback')
        finally:
            cursor.close()
            logger.info('cursor has been closed')


    def query(self, cmd, args=None):
        with self.get_db_cursor() as cursor:
            if cursor:
                if isinstance(args, list):
                    cursor.executemany(cmd, args)
                elif isinstance(args, tuple):
                    cursor.execute(cmd, args)

                try:
                    return cursor.fetchall()
                except:
                    return True
                # elif cursor.rowcount == 0:
                #     return True
                # else :
                #     return False

    update = insert = query

if __name__ == '__main__':
    config = {
        'host': '192.168.172.9',
        'port': 3306,
        'user': 'rwy',
        'passwd': 'rwy123',
        'db': 'PCY',
        'charset':"utf8"
    }
    db = CloudDB(**config)
    query_cmd = "SELECT * FROM all_branchstore_details where branchstore_no = %(no)s"
    upd_cmd = "update all_branchstore_details set branchstore_name = %(name)s where branchstore_no = %(no)s"
    # insert_cmd = "INSERT INTO PCY.all_branchstore_details (branchstore_no, chain_no, service_level) VALUES (" \
    #              "%(branchstore_no)s, " \
    #              "%(chain_no)s, " \
    #              "%(service_level)s" \
    #              ")"

    insert_cmd = "INSERT INTO PCY.all_branchstore_details (branchstore_no, chain_no, service_level) VALUES (" \
                 "%s, " \
                 "%s, " \
                 "%s" \
                 ")"
    print db.insert(insert_cmd, [(9987, 2345, 3), (9988, 2345, 3)]

                    )
    # print(db.insert( insert_cmd, [{'branchstore_no': 9988,
    #                                'chain_no': 322,
    #                                'service_level': 2
    #                                },
    #                               {'branchstore_no': 9987,
    #                                'chain_no': 235,
    #                                'service_level': 4
    #                               }]
    #                  ))




