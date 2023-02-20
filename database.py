import sqlite3

class Database:
    # pouze 1 objekt, singleton! zapsat do dokumentace
    """
    Class represents a single Database object, which handles database-related requests received from the user via the
    Interaction object. Constructing more than 1 instance of this class is incorrect.

    ATTRIBUTES:
        _dbfile ... which stores the physical location of the databse file on a hard drive.

    METHODS:
        Connecting and disconnecting to/from the database:
            _connect()
            _disconnect()

        Transactions with the 'insurees' table:
            create_insuree() - admin only
            read_insuree()
            update_insured_person() - admin only
            delete_insured_person() - admin only
            show_all_insurees()
    """

    def __init__(self):
        """
        Constructor of the Database object, which stores the _dbfile ATTRIBUTE.
        """
        import os
        self._dbfile = os.path.abspath(os.path.join(os.path.dirname(__file__), "./app.db"))
        
        # os.path.relpath("C:/Users/CHALON_DT2/Documents/dev/itnetwork/app.db")

    # Methods related to connecting and disconnecting to/from the database:
    def connect(self):
        """
        Try to connect to the SQLite database and create its cursor object.
        Raises error if unsuccesful.
        Returns initiliased db.con ('connection') object and initiliased db.cur ('cursor') object.
        """
        try:
            self._con = sqlite3.connect(self._dbfile)
            self._cur = self._con.cursor()
            # print("Database connection established. Cursor object created.")
        except:
            print("Connection to the database was not established.") # PŘEDĚLAT NA SPRÁVNOU CHYBU!
        return self._con, self._cur

    def disconnect(self):
        """
        Close a connection to the SQLite database and remove its cursor object.
        Returns db.con ('connection') object and initiliased db.cur ('cursor') object as None type.
        """
        self._con.close()
        self._cur.close()
        return self._con, self._cur

    # Methods related to user authentication and user roles
    def check_username_and_password(self, username, password):
        """
        Connects to the database and searches for the 'username' from the table 'users' where the 'username' and
        'password' matches those given in the parameters. Voids the self._username and self._password variables
        at the end.

        Returns False if there is no results found. Returns True if there is a specific user found.

        :param username: Stores username retrieved by the get_credentials() function of the Interaction object.
        :param password: Stores password retrieved by the get_credentials() function of the Interaction object.
        """
        self._username = username
        self._password = password
        try:
            self.connect()
            self._cur.execute(
                f"SELECT username FROM users WHERE username = '{self._username}' AND password = '{self._password}';"
                )
            if not self._cur.fetchone(): # An empty result evaluates to False.
                return False
            else:
                return True
        finally:
            self._username = None 
            self._password = None
    
    def check_user_privileges(self, username):
        """
        Connects to the database and checks whether user given in the parameter
        is an admin or not. Return True if the user is an admin. Returns False if not.
        """
        self._username = username
        try:
            self.connect()
            self._cur.execute(
                f"SELECT is_admin FROM users WHERE username = '{self._username}';"
                )
            self._user_privileges = self._cur.fetchone()
            if self._user_privileges[0] == 1: # For some reason, the fetchone() func saves the value into a tuple.
                return True
            else:
                return False
        finally:
            self._username = None
    
    # Methods related to database transactions with the INSUREES table:
    def read_all_insurees(self):
        """
        Connects to the database and lists all insuress from the insurees table.
        """
        self.connect()
        self._cur.execute(
            """
            SELECT *
            FROM insurees
            """
        )
        for row in self._cur.fetchall():
            print(*row, sep="\t\t") # * means unpacking the collection.
        print()

    def read_insuree(self, surname, names):
        """
        Connects to the database and searches it for insurees who correspond
        to the search criteria given in the method's parameters.
        """
        self._insuree_data = (surname, names)
        try:
            self.connect()
            self._cur.execute(
                """
                SELECT *
                FROM insurees
                WHERE surname LIKE '%'||?||'%' OR names LIKE '%'||?||'%'
                """, (self._insuree_data)
            )
            self._insuree_found = True
            self._search_results = self._cur.fetchall()
            return self._search_results
        except:
            self._insuree_found = False
            return None
        finally:
            self._insuree_data = None

    def create_insuree(self, surname, names, birthdate, phone):
        """
        Connects to the database and creates a new insuree in the insurees table
        based on the method's parameters.
        """
        self._insuree_data = (surname, names, birthdate, phone)
        try:
            self.connect()
            self._cur.execute(
                """
                INSERT INTO insurees (surname, names, birthdate, phone)
                VALUES (?, ?, ?, ?)
                """, (self._insuree_data)
            )
            self._con.commit()
            self._create_insuree_success = True
        except:
            self._create_insuree_success = False
        finally:
            self._insuree_data = None

    def update_insuree(self, insuree_id, surname, names, birthdate, phone):
        """
        Connects to the database and updates an insuree based on the method's
        parameters.
        """
        self._insuree_data = (surname, names, birthdate, phone, insuree_id)
        try:
            self.connect()
            self._cur.execute(
                """
                UPDATE insurees
                SET
                    surname = ?,
                    names = ?,
                    birthdate = ?,
                    phone = ?
                WHERE insuree_id = ?
                """, (self._insuree_data) # Insuree_data is a tuple with multiple values.
            )
            self._con.commit()
            self._update_insuree_success = True
        except:
            self._update_insuree_success = False
        finally:
            self._insuree_data = None        

    def delete_insuree(self, insuree_id):
        """
        Connects to the database and deletes an insuree based on their ID given
        in the method's parameter.
        """
        self._insuree_data = insuree_id
        try:
            self.connect()
            self._cur.execute(
                """
                DELETE
                FROM insurees
                WHERE insuree_id = ?
                """, (self._insuree_data,) # Insuree_data is converted to a tuple containing 1 value.
            )
            self._con.commit()
            self._delete_insuree_success = True
        except:
            self._delete_insuree_success = False
        finally:
            self._insuree_data = None