from abc import ABC

class Locale(ABC):
    """
    Class represents a Language object, which stores all the global text strings in multiple languages.
    It exists only for inheritance purposes.
    """

class English(Locale):

    def __init__(self):
        self._login_screen = (
            "Welcome to PojištěníApp!\n\n"

            "Only authenticated users may use this app.\n"
            "Please enter your username and password below.\n"
        )
        self._continue = "Press any key to continue."
        self._username = "> Username: "
        self._password = "> Password: "
        self._login_success = "Login succesful with regular user privileges."
        self._login_success_admin = "Login successful with administrator privileges."
        self._login_error = "LoginError: Username and/or password don't match, please try again.\n" # replace error
        self._screen_selection = "Please enter one of the actions specified above, e. g. 'A':"
        self._selection_error = "SelectionError: Invalid input, please try again.\n"
        self._insufficient_privileges_error = "InsufficientPrivilegesError: This action may be performed only by administrators.\n"
        self._mainmenu_screen = (
            "MAIN MENU\n"
            "---------\n\n"

            "(1) Actions with insurees\n"
            "(2) Log out\n"
        )
        self._insurees_screen = (
            "ACTIONS WITH INSUREES\n"
            "---------------------\n\n"

            "(L)  Show all insurees\n"
            "(R)  Show insuree's details\n"
            "(C)* Create new insuree\n"
            "(U)* Update insuree's details\n"
            "(D)* Delete insuree\n"
            "<---\n"
            "(B)  Go back to Main Menu\n\n"          

            "NOTE: Actions marked with an asterisk (*) can be only performed by administrators.\n"
        )
        
        # Create insuree strings
        self._create_insuree_form = (
            "CREATE NEW INSUREE\n"
            "------------------\n"
        )
        self._create_insuree_form_surname = "Enter new insuree's surname:\n"
        self._create_insuree_form_names = "Enter new insuree's name/names:\n"
        self._create_insuree_form_birthdate = "Enter new insuree's date of birth (DD-MM-YYYY):\n"
        self._create_insuree_form_phone = "Enter new insuree's phone number:\n"
        self._create_insuree_success = "A new insuree has been created in the database.\n"
        self._create_insuree_failure = "Error while creating a new insuree in the database.\n"

        # Update insuree strings
        self._update_insuree_form = (
            "UPDATE INSUREE\n"
            "--------------\n"
        )
        self._update_insuree_form_id = "Enter insuree ID of the insuree that you want to update:\n"
        self._update_insuree_form_surname = "Enter insuree's new surname:\n"
        self._update_insuree_form_names = "Enter insuree's new name/names:\n"
        self._update_insuree_form_birthdate = "Enter insuree's new date of birth (DD-MM-YYYY):\n"
        self._update_insuree_form_phone = "Enter insuree's new phone number:\n"
        self._update_insuree_success = "An insuree has been successfully updated in the database.\n"
        self._update_insuree_failure = "Error while updating an insuree in the database.\n"

        # Delete insuree strings
        self._delete_insuree_form = (
            "DELETE INSUREE\n"
            "--------------\n"
        )
        self._delete_insuree_form_id = "Enter insuree ID of the insuree that you want to delete:\n"
        self._delete_insuree_success = "Insuree was deleted from the database.\n"
        self._delete_insuree_failure = "Error while deleting an insuree in the database.\n"

        # Read insuree strings
        self._read_insuree_form = (
            "SHOW INSUREE'S DETAILS\n"
            "----------------------\n"
        )
        self._read_insuree_form_surname = "Enter surname of the insuree you wish to find:\n"
        self._read_insuree_form_names = "Enter name of the insuree you wish to find:\n"
        self._read_insuree_found = "The following insurees were found in the database based on your search:\n"
        self._read_insuree_not_found = "No insurees were found in the database based on your search.\n"
        self._read_insuree_category_names = "ID\t\tSurname\t\tName(s)\t\tBirthdate\t\tPhone\n"

        # Read all insurees strings
        self._read_all_insurees = (
            "LIST OF ALL INSUREES\n"
            "--------------------\n\n"

            f"{self._read_insuree_category_names}"           
        )

    def render_ui_screen_headline(self, signed_user):
        self._signed_user = signed_user
        print(
            "+---------------------------------+\n"
            f"|    I n s u r a n c e   A p p    |    Logged in as {signed_user}\n"
            "+---------------------------------+\n"
        )

class Czech(Locale):

    def __init__(self):
        self._login_screen = (
            "Vítejte v PojištěníApp!\n\n"

            "Tuto aplikaci mohou používat pouze přihlášení uživatelé.\n"

            "Zadejte, prosím, své uživatelské jméno a heslo níže.\n"
        )
        self._continue = "Pokračujte stisknutím libovolné klávesy."
        self._username = "> Uživatelské jméno: "
        self._password = "> Heslo: "
        self._login_success = "Uživatel s běžnými právy byl úspěšně přihlášen."
        self._login_success_admin = "Uživatel s administrátorskými právy byl úspěšně přihlášen."
        self._login_error = "LoginError: Uživatelské jméno a/nebo heslo nesouhlasí, prosím opakujte zadání.\n" # replace error
        self._screen_selection = "Zadejte, prosím, jednu z akcí uvedenou výše, např. 'A':"
        self._selection_error = "SelectionError: Neplatné zadání, opakujte, prosím, volbu.\n"        
        self._insufficient_privileges_error = "InsufficientPrivilegesError: Tuto akci mohou provádět pouze administrátoři.\n"
        self._mainmenu_screen = (
            "HLAVNÍ NABÍDKA\n"
            "--------------\n\n"

            "(1) Akce s pojištěnci\n"
            "(2) Odhlásit se\n"
        )
        self._insurees_screen = (
            "AKCE S POJIŠTĚNCI\n"
            "-----------------\n\n"

            "(L)  Zobraz všechny pojištěnce\n"
            "(R)  Zobraz detail pojištěnce\n"
            "(C)* Vytvoř nového pojištěnce\n"
            "(U)* Aktualizuj detaily pojištěnce\n"
            "(D)* Vymaž pojištěnce\n"
            "<---\n"
            "(B)  Návrat do hlavní nabídky\n\n"             

            "POZNÁMKA: Akce označené hvězdičkou (*) mohou provádět pouze administrátoři.\n"
        )

        # Create insuree strings
        self._create_insuree_form = (
            "VYTVOŘ NOVÉHO POJIŠTĚNCE\n"
            "------------------------\n"
        )
        self._create_insuree_form_surname = "Zadejte příjmení nového pojištěnce:\n"
        self._create_insuree_form_names = "Zadejte jméno/jména nového pojištěnce:\n"
        self._create_insuree_form_birthdate = "Zadejte datum narození nového pojištěnce (DD-MM-YYYY):\n"
        self._create_insuree_form_phone = "Zadejte telefonní číslo nového pojištěnce:\n"
        self._create_insuree_success = "V databázi byl vytvořen nový pojištěnec.\n"
        self._create_insuree_failure = "Při vytváření nového pojištěnce nastala chyba.\n"

        # Update insuree strings
        self._update_insuree_form = (
            "AKTUALIZACE POJIŠTĚNCE\n"
            "----------------------\n"
        )
        self._update_insuree_form_id = "Zadejte ID pojištěnce, kterho chcete upravit:\n"
        self._update_insuree_form_surname = "Zadejte nové příjmení pojištěnce:\n"
        self._update_insuree_form_names = "Zadejte nové/á jméno/jména pojištěnce:\n"
        self._update_insuree_form_birthdate = "Zadejte nové datum narození pojištěnce (DD-MM-YYYY):\n"
        self._update_insuree_form_phone = "Zadejte nové telefonní číslo pojištěnce:\n"
        self._update_insuree_success = "V databázi byl upraven pojištěnec.\n"
        self._update_insuree_failure = "Při upravování pojištěnce nastala chyba.\n"

        # Delete insuree strings
        self._delete_insuree_form = (
            "VYMAŽ POJIŠTĚNCE\n"
            "----------------\n"
        )
        self._delete_insuree_form_id = "Zadejte ID pojištěnce, kterého chcete smazat:\n"
        self._delete_insuree_success = "Pojištěnec byl úspešně smazán z databáze.\n"
        self._delete_insuree_failure = "Při mazání pojištěnce nastala chyba.\n"        

        # Read insuree strings
        self._read_insuree_form = (
            "ZOBRAZ DETAIL POJIŠTĚNCE\n"
            "------------------------\n"
        )
        self._read_insuree_form_surname = "Zadejte příjmění pojištěnce, kterého chcete nalézt:\n"
        self._read_insuree_form_names = "Zadejte jméno pojištěnce, kterého nalézt:\n"
        self._read_insuree_found = "V databázi byli na základě Vašeho hledání nalezeni tito pojištěnci:\n"
        self._read_insuree_not_found = "V databázi nebyli na základě Vašeho hledání nalezeni žádní pojištěnci.\n"
        self._read_insuree_category_names = "ID\t\tPříjmení\t\tJméno/a\t\tDatum narození\t\tTelefon\n"

        # Read all insurees strings
        self._read_all_insurees = (
            "SEZNAM VŠECH POJIŠTĚNCŮ\n"
            "-----------------------\n\n"

            f"{self._read_insuree_category_names}"         
        )

    def render_ui_screen_headline(self, signed_user):
        self._signed_user = signed_user
        print(
            "+---------------------------------+\n"
            f"|    P o j i š t ě n í   A p p    |    Přihlášeni jako {signed_user}\n"
            "+---------------------------------+\n"
        )