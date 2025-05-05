Thank you for your interest in viewing this code! 

First, use "pip install -r requirements.txt" command to download the environment

You need to specify the parameters for connecting to your local database in the "config.py" file. 
If you need to connect to database by URI, read *1.

After, you need to run "setup_database_scr.py" it will create the necessary empty tables.
If you want to enter demo data into these tables run "setup_fake_data_scr".

For the API ".../add new order status" you need to use the admin name and password. To do this, insert the information of admin in the "admins" table.

Done. Now you can run "main.py" file.


*1
Specify the URI in the "config.py" file.
Inside db_connection/DbApp.connect change the creation of self.connections_pool to '''self.connections_pool = await asyncpg.create_pool(DATABASE_URI)'''.
Done.
