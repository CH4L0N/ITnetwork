from interaction import Interaction
import time

# App initialisation, i.e. construction of the main object.
interaction = Interaction()

# Step 1: Ask the user which language the App shall use.
interaction.clear_screen()
interaction.set_locale()

# Step 2: Clears the screen and sets the UI screen to Login.
interaction.render_ui_screen()

# Step 3: User authentication on repeat until successful.
interaction.authenticate_user()
time.sleep(1)

# Step 4: Clears the screen and sets the UI screen to Main Menu.
interaction.set_ui_screen(1)
interaction.render_ui_screen()
interaction.main_menu_selection()