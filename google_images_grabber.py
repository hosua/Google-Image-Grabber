from selenium import webdriver
from colorama import Fore, Back, Style
from datetime import datetime
import time
import urllib.request
import os

fg_prompt = Fore.LIGHTCYAN_EX
fg_page = Fore.LIGHTMAGENTA_EX
fg_error = Fore.RED
fg_reset = Fore.RESET
root = os.getcwd()

def grab_images():
    chrome_opts = webdriver.ChromeOptions()
    chrome_opts.add_argument("-headless")   # You can run the scraper without opening a window
    driver = webdriver.Chrome(options=chrome_opts)

    google_images = "https://google.com/imghp"

    driver.get(google_images)
    max_images = 300
    search_arg = input(fg_prompt + "What do you want to search?\n" + fg_reset)
    num_imgs = int(input(fg_prompt + "How many images do you want to grab? \nNote: " + str(max_images) + " max, Google will block you if you send too many requests!\n" + fg_reset))
    if num_imgs > max_images: 
        print(fg_error + "I will not do more than " + str(max_images) + "! " + "\n")
    search_box = driver.find_element_by_class_name("gLFyf")
    search_box.send_keys(search_arg + "\n")
    images = driver.find_elements_by_class_name("bRMDJf")

    while True:   # Keep scrolling down until we have enough elements
        print(fg_page + "Scrolling..." + fg_reset)
        #currLen = len(images)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")    # Scrolls to bottom
        time.sleep(1)
        images = driver.find_elements_by_class_name("bRMDJf")
        if len(images) >= num_imgs:
            break
    print(fg_page + "Done scrolling" + fg_reset)
    # Saving the images
    os.chdir(root)
    img_dir = os.path.join(root, "Images")
    if not os.path.isdir(img_dir):
        os.makedirs("Images")
    os.chdir("Images")
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    now_name = search_arg + "-" + now
    now_path = os.path.isdir(os.path.join(img_dir, now_name))

    if not os.path.isdir(now_path):   # This should basically be impossible but I'll check anyway
        os.makedirs(now_name)
    os.chdir(now_name)
    j = 0
    for i in range(num_imgs):
        j += 1
        img_src = images[i].find_element_by_tag_name("img").get_attribute("src")
        file_name =  search_arg + "-" + str(j) + ".jpg"
        try:
            urllib.request.urlretrieve(img_src, file_name)
            print(fg_prompt + "Saving " + file_name + fg_reset)
        except TypeError:
            print(fg_error + "Couldn't process a link, skipping..." + fg_reset)   
            j -= 1 # keep track of actual file number
        except:
            print(fg_error + "Google timed you out! Resuming..." + fg_reset)
    print()