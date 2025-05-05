import asyncpg
from config import host, user, password, db_name, port, DATABASE_URI



def singleton(class_):
    '''Singleton decorator for DbApp'''
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance
 
@singleton
class DbApp:
    '''Singleton class for working with PostgreSQL'''

    async def connect(self):
        try:
            self.connections_pool = await asyncpg.create_pool( min_size=10, max_size=100,
                host=host, 
                user=user, 
                password=password, 
                database=db_name, 
                port=port
                )
            
            '''self.connections_pool = await asyncpg.create_pool(DATABASE_URI)'''

            print("[INFO] conections pool created successfully")

        except Exception as _ex:
            print('[INFO] ERROR while working with PostgreSQL:\n\n', _ex)

    async def disconnect(self):
        try:
            await self.connections_pool.close()
            print('[INFO] connections pool closed')
        except Exception as _ex:
            print('[INFO] ERROR while closing PostgreSQL database connections pool:\n\n', _ex)
            
database = DbApp()
