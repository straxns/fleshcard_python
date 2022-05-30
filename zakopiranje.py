from tkinter import *
from random import randint

root=Tk()
root.title("Апликација за учење језика - са картицама")
root.geometry("550x410")

words=[(("Guten Tag"),("Добар дан")),
      (("Hallo"),("Здраво")),
      (("Ich heiße"),("Зовем се")),
      (("Sprechen Sie Serbisch"), ("Говорите ли српски")),
      (("Wie heißt du"),("Како се зовеш")),
      (("Wie geht es dir"),("Како си")),
      (("Gut, danke"),("Добро, хвала")),
      (("Nett, Sie kennen zu lernen"),("Драго ми је да сам Вас упознао")),
      (("Tisch für zwei bitte"),("Сто за двоје молим"))
      ]
count=len(words)
hinter=""
hint_count=0
def next():
    global hinter,hint_count
    answer_label.config(text="")
    my_entry.delete(0,END)
    #Create random selection
    global random_word
    random_word=randint(0, count-1)
    german_word.config(text=words[random_word][0])
    hint_label.config(text="")
    #reset hint variables
    hinter = ""
    hint_count = 0


def answer():
    if my_entry.get().capitalize() == words[random_word][1] :
        answer_label.config(text=f"Тачно! {words[random_word][0]} је {words[random_word][1]}")
    else:
        answer_label.config(text=f"Нетачно! {words[random_word][0]}  није {my_entry.get().capitalize()}")
#Keep track of the hints

def hint():
    global hint_count
    global hinter

    if hint_count < len(words[random_word][1]):
        hinter=hinter+words[random_word][1][hint_count]
        hint_label.config(text=hinter)
        hint_count +=1

german_word=Label(root, text="", font=("Helvetica", 36))
german_word.pack(pady=50)

answer_label = Label(root, text="")
answer_label.pack(pady=20)

my_entry=Entry(root, font=("Helvetica", 18))
my_entry.pack(pady=20)

#Create Buttons
button_frame=Frame(root)
button_frame.pack(pady=20)

answer_button=Button(button_frame, text="Одговор", command=answer)
answer_button.grid(row=0, column=0, padx=20)

next_button=Button(button_frame, text="Следеће", command=next)
next_button.grid(row=0, column=1)

hint_button=Button(button_frame, text="Наговештај",command=hint)
hint_button.grid(row=0, column=2, padx=20)

#Create Hint Label
hint_label=Label(root,text="")
hint_label.pack(pady=20)
next()
root.mainloop()
