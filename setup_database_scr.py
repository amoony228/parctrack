import asyncio
import asyncpg

from config import host, user, password, db_name, port

async def main():
    conn = await asyncpg.connect(host=host, user=user, password=password, database=db_name, port=port)
    await create_tables_in_database(conn)
    await conn.close()

async def create_tables_in_database(connection) -> None:
    await connection.execute('''CREATE TABLE clients
(
	id integer PRIMARY KEY,
	phone_num varchar(20) NOT NULL,
	telegram_id integer NOT NULL,
	name varchar(64) NOT NULL,
	surname varchar(64) NOT NULL
);

CREATE TABLE products
(	
	id integer PRIMARY KEY,
	name varchar(64) NOT NULL, 
	description text NOT NULL,
	adult_content bool NOT NULL,
	price numeric NOT NULL
);

CREATE TABLE orders
(
	id varchar(16) PRIMARY KEY,
	client_id integer NOT NULL,
	product_id integer NOT NULL,
	dateTime timestamp NOT NULL,
	price numeric NOT NULL,
	
	CONSTRAINT client_id_fk FOREIGN KEY (client_id) REFERENCES clients (id)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	CONSTRAINT product_id_fk FOREIGN KEY (product_id) REFERENCES products (id)
		ON DELETE NO ACTION
		ON UPDATE CASCADE
);

CREATE TABLE orders_status
(	
	order_id varchar(16) NOT NULL,
	status text NOT NULL,
	dateTime timestamp NOT NULL,
	
	CONSTRAINT order_id_fk FOREIGN KEY (order_id) REFERENCES orders (id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);

CREATE TABLE admins
(	
	admin_name varchar(25) PRIMARY KEY,
	admin_password varchar(25) NOT NULL
);''')
        

if __name__ == '__main__':
    asyncio.run(main())