import psycopg2

class DatabaseConnection:


    #connection
    conn = psycopg2.connect(
        "dbname =levelup user =postgres password=root123 host =127.0.0.1")

    #connection cursor activation
    cur = conn.cursor()


    def create_user_table(self):
            self.user_table = (
                "CREATE TABLE IF NOT EXISTS users (userId serial primary key, username varchar(50) not null, password varchar not null )")
            self.cur.execute(self.user_table)






# self.connection = psycopg2.connect(user="postgres",
#                                    password="root123",
#                                    host="127.0.0.1",
#                                    port="5432",
#                                    database="challengethree")
