from bs4 import BeautifulSoup
from PIL import Image
import sqlite3
import string
import os

def generate_db():
    """
    A function that generates training_data/data.db file and initializes the table values.
    :return: None
    """
    conn = sqlite3.connect("./training_data/data.db")
    cur = conn.cursor()
    conn.execute("CREATE TABLE data(data_name TEXT, data_count INTEGER)")
    
    default_data = [(x, 0) for x in string.ascii_lowercase]
    default_data = default_data + [(str(x), 0) for x in range(0, 10, 1)]
    default_data.append(("null", 0))
    
    cur.executemany("INSERT INTO data VALUES(?, ?)", default_data)
    
    conn.commit()
    conn.close()
    
def get_data_count(data_name):
    """
    A function that gets data count from data.db for specific data_name
    :param data_name: the data_name to look for data counts
    :return: returns count of data_count value for provided data_name, returns -1 if data_name does not exist.
    """
    conn = sqlite3.connect("./training_data/data.db")
    cur = conn.cursor()
    cur.execute("SELECT data_count FROM data WHERE data_name=\"" + data_name + "\"")
    rows = cur.fetchall()
    try:
        return rows[0][0]
    except IndexError:
        return -1
    
    conn.close()
    
def update_data_count(data_name):
    """
    A function that adds 1 to the current data_count for specified data_name
    :param data_name: the data_name to update values into
    :return: None
    """
    before_count = get_data_count(data_name)    
    new_count = before_count + 1
    
    conn = sqlite3.connect("./training_data/data.db")
    cur = conn.cursor()
    cur.execute("UPDATE data SET data_count=" + str(new_count) + " WHERE data_name=\"" + data_name + "\"")
    conn.commit()
    conn.close()

def cut_image_and_save(x_min:int, y_min:int, x_max:int, y_max:int, original_image:Image, category:str):
    """
    A function that cuts image with dimension from original image and then saves it to category directory
    :param x_min: int type that represents x_min
    :param y_min: int type that represents y_min
    :param x_max: int type that represents x_max
    :param y_max: int type that represents y_max
    :param original_image: PIL.Image object that represents original image.
    :param category: a string object that represents category of the selected image.
    :return: None
    """
    area = (x_min, y_min, x_max, y_max)
    cropped_img = original_image.crop(area)
    save_path = os.path.join(os.getcwd(), "training_data", category, str(get_data_count(category)) + ".png")
    cropped_img.save(save_path)
    update_data_count(category)

def process_single_object(bs_object:BeautifulSoup, original_image:Image):
    """
    A function that processes single object from xml.
    :param bs_object: the BeautifulSoup object that represents current object
    :param original_image: the Image object that represents original image
    :return: None
    """
    # Get data info.
    name = bs_object.find("name").string
    bndbox = bs_object.find("bndbox")
    x_min = bndbox.find("xmin").string
    y_min = bndbox.find("ymin").string
    x_max = bndbox.find("xmax").string
    y_max = bndbox.find("ymax").string

    x_min = int(x_min)
    y_min = int(y_min)
    x_max = int(x_max)
    y_max = int(y_max)

    # Cut image and then save it
    cut_image_and_save(x_min, y_min, x_max, y_max, original_image, name)

def generate_all_directories():
    """
    A function that generates training_data directories.
    This will generate trainig_data/a~z and 0~9 directories.
    :return: None
    """
    dir_names = [x for x in string.ascii_lowercase]
    dir_names = dir_names + [str(x) for x in range(0, 10, 1)]

    training_data_path = os.path.join(os.getcwd(), "training_data")

    if not os.path.exists(training_data_path):  # generate training_data directory
        os.mkdir(training_data_path)
    
    for i in dir_names:  # generate subdirectories such as a ~ z, 0 ~ 9
        new_dir= os.path.join(training_data_path, i)
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)

def process_file(xml_name):
    """
    A function that processes the whole file
    :param xml_name: the name of xml to load and process
    :return: None
    """
    print("[+] Processing File : " + xml_name)
    with open(xml_name, 'r') as f:
        data = f.read()
        bs_data = BeautifulSoup(data, "xml")
        
    print("[+] Opened File : " + xml_name)
    objects = bs_data.find_all('object')
    image_name = bs_data.find("path").string
    print("[+] Original Image : " + image_name)
    image_data = Image.open(image_name)
    print("[+] Opened Image")
    
    count = 0
    for i in objects:
        process_single_object(i, image_data)
        count += 1
        print("Processed " + str(count) + " / " + str(len(objects)) + " objects")
    print("[+] Finished Job")
    
if __name__ == "__main__":
    try:
        generate_db()
        print("[+] DB not found, generating a new one")
    except sqlite3.OperationalError:  # when db already exists
        pass
    generate_all_directories()
    
    process_file('combined_1.xml')
