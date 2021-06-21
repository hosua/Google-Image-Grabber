import google_images_grabber as GIG
from colorama import Fore

fg_prompt = Fore.LIGHTCYAN_EX
fg_num = Fore.GREEN
fg_opts = Fore.YELLOW
fg_reset = Fore.RESET

print( 	 "  __  __           _        _             _   _                               \n"
" |  \\/  | __ _  __| | ___  | |__  _   _  | | | | ___  _____      _____   ___  \n"
" | |\\/| |/ _` |/ _` |/ _ \\ | '_ \\| | | | | |_| |/ _ \\/ __\\ \\ /\\ / / _ \\ / _ \\ \n"
" | |  | | (_| | (_| |  __/ | |_) | |_| | |  _  | (_) \\__ \\\\ V  V / (_) | (_) |\n"
" |_|  |_|\\__,_|\\__,_|\\___| |_.__/ \\__, | |_| |_|\\___/|___/ \\_/\\_/ \\___/ \\___/ \n"
"                                  |___/                                       \n\n")
while True:
    user_opt = int(input(fg_prompt + "What would you like to do?\n" +
                    fg_num + "1. " + fg_opts + "Grab Images\n" +
                    fg_num + "2. "+ fg_opts + "Quit\n" + fg_reset))
    if user_opt == 1:
        GIG.grab_images()
    if user_opt == 2:
        break