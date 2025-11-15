import psycopg2

def connect_db():
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="future_sales",
            user="mandla",
            password="secret123"
        )
        print("Connected to PostgreSQL successfully!")
        return conn
    except Exception as e:
        print("Connection error:", e)

if __name__ == "__main__":
    connect_db()
# checkin on  the progress 
"""  fot the next task 
TODO:build a traine model to predict future 
     sales based on the stored data in Postgresssql database and more



"""
