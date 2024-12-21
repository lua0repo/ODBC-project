import pyodbc

class DatabaseConnectionManager:
    def __init__(self):
        self.connection = None

    def connect(self, driver, server, database, username, password):
        """Establish a connection to the database using ODBC."""
        try:
            connection_string = f'DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={username};PWD={password};'
            self.connection = pyodbc.connect(connection_string)
            print("Connection successful!")
        except Exception as e:
            print(f"Error connecting to database: {e}")

    def execute_query(self, query):
        """Execute a SQL query and return the results."""
        if self.connection is None:
            print("No connection established.")
            return None
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            if query.strip().upper().startswith("SELECT"):
                return cursor.fetchall()
            else:
                self.connection.commit()
                return cursor.rowcount
        except Exception as e:
            print(f"Error executing query: {e}")
            return None

    def close_connection(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            print("Connection closed.")

# Example usage
if __name__ == "__main__":
    db_manager = DatabaseConnectionManager()
    
    # Replace with your database credentials
    driver = "ODBC Driver 17 for SQL Server"  # Example for SQL Server
    server = "your_server"
    database = "your_database"
    username = "your_username"
    password = "your_password"

    db_manager.connect(driver, server, database, username, password)

    # Example query
    select_query = "SELECT * FROM your_table"
    results = db_manager.execute_query(select_query)
    if results:
        for row in results:
            print(row)

    # Close the connection
    db_manager.close_connection()
