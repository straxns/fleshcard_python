from tkinter import *
from tkinter import  filedialog
from  database_func import *
from podaci import Podaci
from functools import partial
import os
import glob
from PIL import ImageTk,Image
import io
from random import randint

root= Tk()
root.title('Флешкард програм')
root.geometry("500x500")
def filedialogs():
    global get_image
    get_image=filedialog.askopenfilename(title="ИЗАБЕРИТЕ СЛИКУ", filetypes=(("png","*.png"),("jpg","*.jpg"),("Allfile","*.*")))
    #print(get_image)
def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
def convert_image_into_binary(filename):
    with open(filename,'rb') as file:
        data_binary= file.read()
    return data_binary

    table_name=""
def new_deck_info(tekst):
    hide_all_frames()
    new_deck_frame.pack(fill="both", expand=1)
    global first_language_entry_widget
    global second_language_entry_widget
    label_status = Label(new_deck_frame, text=tekst, font=('Aerial 15 bold')).grid(row=1, column=1)
    first_language = Label(new_deck_frame, text="Први језик", font=('Aerial 10 bold')).grid(row=2, column=1)
    first_language_entry_widget = Entry(new_deck_frame, width=50)
    first_language_entry_widget.grid(row=3, column=1, padx=100)
    second_language = Label(new_deck_frame, text="Други језик", font=('Aerial 10 bold')).grid(row=4, column=1)
    second_language_entry_widget = Entry(new_deck_frame, width=50)
    second_language_entry_widget.grid(row=5, column=1, padx=100)
    global lista_podataka
    lista_podataka = []
    add_element_in_button_widget = Button(new_deck_frame, text="Изабери слику", font=('Aerial 10 bold'),
                                          command=filedialogs).grid(row=6, column=1)
    add_element_in_button_widget = Button(new_deck_frame, text="Унеси  податак", font=('Aerial 10 bold'),
                                    command=new_deck_info_add_data).grid(row=7, column=1)
    add_element_in_button_widget = Button(new_deck_frame, text="Сачувај податке", font=('Aerial 10 bold'),
                                          command=send_data_to_database).grid(row=8, column=1)

def new_deck_info_add_data():

    first_language_collected = StringVar
    first_language_collected = first_language_entry_widget.get()

    second_language_collected = StringVar
    second_language_collected = second_language_entry_widget.get()
    image_collected=convert_image_into_binary(get_image)
    lista_podataka.append(Podaci(first_language_collected,second_language_collected,image_collected))

    """for f in lista_podataka:
        print(f.first_language)
        print(f.second_language)
        print(f.image)"""

def new_deck():
    hide_all_frames()
    remove_images()
    new_deck_frame.pack(fill="both", expand=1)

    new_deck_label= Label(new_deck_frame, text="Унесите назив шпила",font=('Aerial 20 bold')).grid(row=1,column=1)
    global new_deck_entry_widget
    new_deck_entry_widget = Entry(new_deck_frame, width=50)
    new_deck_entry_widget.grid(row=2, column=1, padx=100)
    #e=new_deck_entry_widget.get()
    #print(e)
    new_deck_button_widget = Button(new_deck_frame,  text="Креирај шпил",font=('Aerial 10 bold'),command=create_or_open).grid(row=3,column=1)
def create_or_open():
    global table_name
    table_name=StringVar
    table_name = new_deck_entry_widget.get()
    tekst=create_table(table_name)
    new_deck_info(tekst)

def show_deck(deck_name):

    podaci = fetch_all_data(deck_name)
    show_deck_pass(podaci)


def show_deck_pass(podaci):
    hide_all_frames()
    duzina = len(podaci)
    random_word = randint(0, duzina - 1)
    slika = podaci[random_word][2]
    img = Image.open(io.BytesIO(slika))
    new_height = 320
    max_width = 320
    new_width = int(new_height / img.height * img.width)
    if new_width>max_width:
        new_width=max_width
        new_height=int(new_width/img.width * img.height)


    img = img.resize((new_width,new_height))
    open_img=ImageTk.PhotoImage(img)
    print(new_width)
    print(new_height)
    open_deck_frame.pack(fill="both", expand=1)
    #open_deck_frame.pack_propagate(False)

    my_frame = Frame(open_deck_frame, height=320, width=320)
    my_frame.grid(row=2, column=1)
    my_frame.pack_propagate(False)
    #my_label = Label(open_deck_frame, text="Шпил "+deck_name, font=('Aerial 19 bold'))
    #my_label.grid(row=1, column=1)
    first_language_label= Label(open_deck_frame, text=podaci[random_word][0], font=('Aerial 20 bold'))
    first_language_label.grid(row=1, column=1)
    picture_label=Label(my_frame, image=open_img)
    picture_label.image=open_img
    #picture_label.grid(row=2, column=1)
    picture_label.pack()

    answer_button = Button(open_deck_frame, text="Одговор")
    answer_button.grid(row=3, column=0, padx=10)

    next_card_with_arg = partial(show_deck_pass,podaci)
    next_button = Button(open_deck_frame, text="Следеће", command=next_card_with_arg)
    next_button.grid(row=3, column=1)

    hint_button = Button(open_deck_frame, text="Наговештај")
    hint_button.grid(row=3, column=2, padx=10)



def open_deck():
    remove_images()
    hide_all_frames()
    open_deck_frame.pack(fill="both", expand=1)
    my_label = Label(open_deck_frame, text="Отворите неке од следећих шпилова", font=('Aerial 19 bold'))
    my_label.grid(row=1, column=1)

    ltables=list_tables()
    duzina=len(ltables)
    i=2
    for element in ltables:
        show_deck_with_arg = partial(show_deck, element[0])
        new_deck_button_widget = Button(open_deck_frame, text=element[0], font=('Aerial 10 bold'),width=60, padx=10,pady=10,command= show_deck_with_arg).grid(row=i, column=1)
        i+=1

def send_data_to_database():
    add_data_in_table(table_name,lista_podataka)
    new_deck()
def remove_images():
    files = glob.glob('slike/*')
    for f in files:
        os.remove(f)

def hide_all_frames():

    table_name=""
    lista_podataka=[]
    for widget in new_deck_frame.winfo_children():
        widget.destroy()
    for widget in open_deck_frame.winfo_children():
        widget.destroy()
    new_deck_frame.pack_forget()
    open_deck_frame.pack_forget()


my_menu=Menu(root)
root.config(menu=my_menu)

option_menu= Menu(my_menu)
my_menu.add_cascade(label="Опције",menu=option_menu)
option_menu.add_command(label="Нови шпил",command=new_deck)
option_menu.add_command(label="Отвори постојеће шпилове",command=open_deck)
option_menu.add_separator()
option_menu.add_command(label="Exit",command=root.quit)


#create frames
new_deck_frame= Frame(root, width=500, height=500)
open_deck_frame= Frame(root, width=500, height=500)

root.mainloop()


