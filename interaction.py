from locale import English, Czech
from database import Database
import time

db = Database()

class Interaction:
    """
    Class represents a single Interaction object, which receives requests from users, sends them to the Database object
    for processing and finally returns them back to the users. It controls the UI shown via the console. Constructing
    more than 1 instance of this class is incorrect.
    
    ATTRIBUTES:
        _current_screen = Attribute contains an int number, which defines the screen currently rendered by the App.\n
        _locale = Attribute contains a None value upon App initialisation. After locale selection by the user, this
        attribute contains a reference to either English or Czech language object.\n

    METHODS:
        ui_headline_screen_login()

    """

    # Constructor:
    def __init__(self):
        """
        Constructor of the InteractionController object, which stores ATTRIBUTES _current_screen and _locale.
        """
        self._current_screen = 0
            # 0 = Login Screen
            # 1 = Main Menu Screen
            # 2 = Insurees Screen
            # 5 = Empty Screen
        self._signed_user = None
        self._signed_user_is_admin = None # default value, replaced upon succesful user authentication
        self._locale = None # default value, will be replaced by the Language object upon successful language selection

    def set_locale(self):
        """
        Method allows the Interaction object to change the language in which all the strings will be displayed.
        It requests an input from the user, asking them to select appropriate language. Afterwards, a specific
        Language object is constructed. In case the user provides an invalid input, the method cycles back to
        the beginning.
        """
        while self._locale == None:
            self._locale = input(f"Please select your preferred language:\nen = English\ncs = Česky\nYour input: ")
            self._locale = self._locale.lower()
            if self._locale in ("en", "english"):
                self._locale = English()
                print("English chosen successfully.")
            elif self._locale in ("cs", "česky", "cesky", "čeština", "cestina"):
                self._locale = Czech()
                print("Čeština zvolena úspešně.")
            else:
                self._locale = None
                print("ValueError: Invalid input. Enter either 'en' or 'cs'. Please try again.\n") # Předělat na standardizovanou chybu.

    def clear_screen(self):
        """
        Method allows the Interaction object to clear the console screen.
        """
        import sys as _sys
        import subprocess as _subprocess
        if _sys.platform.startswith("win"):
            _subprocess.call(["cmd.exe", "/C", "cls"])
        else:
            _subprocess.call(["clear"])

    def set_ui_screen(self, _current_screen):
        """
        Method allows the InteractionController object to change the current UI screen.
        It expects 1 argument, i.e. the number of the requested UI screen.
        0 = Login, 1 = Main Menu, 2 = Insured People, 3 = Insurances, 4 = Incidents, 5 = About.
        """
        self._current_screen = _current_screen

    def render_ui_screen(self):
        """
        Method allows the Interaction object to display an appropriate UI screen based on the current value
        of the _current_screen attribute.
        """
        self.clear_screen()
        self._locale.render_ui_screen_headline(self._signed_user)
        if self._current_screen == 0:
            print(self._locale._login_screen)
        elif self._current_screen == 1:
            print(self._locale._mainmenu_screen)
        elif self._current_screen == 2:
            print(self._locale._insurees_screen)
    
    def authenticate_user(self):
        while self._signed_user == None:
            self.get_credentials()
            if db.check_username_and_password(self._username, self._password):
                self._signed_user = self._username
                if db.check_user_privileges(self._signed_user):
                    self._signed_user_is_admin = True
                    print(self._locale._login_success_admin)
                else:
                    self._signed_user_is_admin = False
                    print(self._locale._login_success)
            else:
                print(self._locale._login_error)
                self.authenticate_user()

    def get_credentials(self):
        import pwinput
        print(self._locale._username, end = "")
        self._username = input()
        print(self._locale._password, end = "")
        self._password = pwinput.pwinput("")
        print()
        return self._username, self._password
    
    def main_menu_selection(self):
        """
        Choose one of the actions specified by the Main Menu screen.
        """
        print(self._locale._screen_selection)
        self._selection = input("> ")
        if self._selection == "1":
            self.set_ui_screen(2)
            self.render_ui_screen()
            self.insurees_menu_selection()
        elif self._selection == "2":
            self.log_out()
        else:
            print(self._locale._selection_error)
            self.main_menu_selection()
        
    def insurees_menu_selection(self):
        """
        Choose one of the actions specified by the Insurees screen or go back to the
        Main Menu screen.
        """
        print(self._locale._screen_selection)
        self._selection = input("> ")
        if self._selection == "B":
            self.set_ui_screen(1)
            self.render_ui_screen()
            self.main_menu_selection()
        elif self._selection == "L":
            self.set_ui_screen(5)
            self.render_ui_screen()
            self.read_all_insurees()
        elif self._selection == "R":
            self.set_ui_screen(5)      
            self.render_ui_screen()
            self.read_insuree()
        elif self._selection == "C":
            if self._signed_user_is_admin:
                self.set_ui_screen(5)      
                self.render_ui_screen()
                self.create_insuree()
            else:
                print(self._locale._insufficient_privileges_error)
                self.insurees_menu_selection()
        elif self._selection == "U":
            if self._signed_user_is_admin:
                self.set_ui_screen(5)      
                self.render_ui_screen()
                self.update_insuree()
            else:
                print(self._locale._insufficient_privileges_error)
                self.insurees_menu_selection()
        elif self._selection == "D":
            if self._signed_user_is_admin:
                self.set_ui_screen(5)      
                self.render_ui_screen()
                self.delete_insuree()
            else:
                print(self._locale._insufficient_privileges_error)
                self.insurees_menu_selection()
        else:
            print(self._locale._selection_error)
            self.insurees_menu_selection()

    def log_out(self):
        """
        User logs out and the application will run again from the beginning.
        """
        self._signed_user = None
        self._signed_user_is_admin = None
        self._locale = None
        self.clear_screen()
        self.set_locale()
        self.set_ui_screen(0)
        self.render_ui_screen()
        self.authenticate_user()
        self.set_ui_screen(1)
        self.render_ui_screen()
        self.main_menu_selection()

    # Methods used to manipulate data from the INSUREES database table:
    def read_all_insurees(self):
        """
        Shows a list of all insurees from the database.
        """
        print(self._locale._read_all_insurees)
        db.read_all_insurees()
        input(f"{self._locale._continue}")
        self.set_ui_screen(2)
        self.render_ui_screen()
        self.insurees_menu_selection()

    def read_insuree(self):
        """
        Searches for an insuree in the database based on surname and name
        provided by the user.
        """
        print(self._locale._read_insuree_form)
        self._read_insuree_surname = input(f"{self._locale._read_insuree_form_surname}")
        self._read_insuree_names = input(f"{self._locale._read_insuree_form_names}")
        print()
        db.read_insuree(self._read_insuree_surname, self._read_insuree_names)
        if db._insuree_found:
            print(self._locale._read_insuree_found)
            print(self._locale._read_insuree_category_names)
            for row in db._search_results:
                print(*row, sep="\t\t")
            print()
        else:
            print(self._locale._read_insuree_not_found)
        input(f"{self._locale._continue}")
        self.set_ui_screen(2)
        self.render_ui_screen()
        self.insurees_menu_selection()

    def create_insuree(self):
        """
        Show a form in the console for the user to complete with the details
        of a new insuree to be created: surname, names, date of birth, phone.
        These details are saved into variables and handed over as parameters
        to the corresponding database method. 
        """
        print(self._locale._create_insuree_form)
        self._create_insuree_surname = input(f"{self._locale._create_insuree_form_surname}")
        self._create_insuree_names = input(f"{self._locale._create_insuree_form_names}")
        self._create_insuree_birthdate = input(f"{self._locale._create_insuree_form_birthdate}")
        self._create_insuree_phone = input(f"{self._locale._create_insuree_form_phone}")
        db.create_insuree(self._create_insuree_surname, self._create_insuree_names, 
                          self._create_insuree_birthdate, self._create_insuree_phone)
        if db._create_insuree_success:
            print(self._locale._create_insuree_success)
        else:
            print(self._locale._create_insuree_failure)
        time.sleep(1)
        self.set_ui_screen(2)
        self.render_ui_screen()
        self.insurees_menu_selection()

    def update_insuree(self):
        """
        Show a form in the console for the user to complete with the details
        of the insuree they wish to update: insuree_id, surname, names,
        date of birth, phone. These details are saved into variables and
        handed over as parameters to the corresponding database method.
        """
        print(self._locale._update_insuree_form)
        self._update_insuree_id = input(f"{self._locale._update_insuree_form_id}")
        self._update_insuree_surname = input(f"{self._locale._update_insuree_form_surname}")
        self._update_insuree_names = input(f"{self._locale._update_insuree_form_names}")
        self._update_insuree_birthdate = input(f"{self._locale._update_insuree_form_birthdate}")
        self._update_insuree_phone = input(f"{self._locale._update_insuree_form_phone}")
        db.update_insuree(self._update_insuree_id, self._update_insuree_surname,
                          self._update_insuree_names, self._update_insuree_birthdate,
                          self._update_insuree_phone)
        if db._update_insuree_success:
            print(self._locale._update_insuree_success)
        else:
            print(self._locale._update_insuree_failure)
        time.sleep(1)
        self.set_ui_screen(2)
        self.render_ui_screen()
        self.insurees_menu_selection()

    def delete_insuree(self):
        """
        Ask the user to provide an insuree_id of the insuree to be deleted.
        This is saved into a variable and handed over as parameter to the
        corresponding database method.
        """
        print(self._locale._delete_insuree_form)
        self._delete_insuree_id = input(f"{self._locale._delete_insuree_form_id}")
        db.delete_insuree(self._delete_insuree_id)
        if db._delete_insuree_success:
            print(self._locale._delete_insuree_success)
        else:
            print(self._locale._delete_insuree_failure)
        time.sleep(1)
        self.set_ui_screen(2)
        self.render_ui_screen()
        self.insurees_menu_selection()
    
