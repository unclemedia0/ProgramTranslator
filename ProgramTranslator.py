#GUItranslator.py
from tkinter import *

from tkinter import ttk #ttk is theme of tk
###---------Google Translate------------
from googletrans import Translator
translator = Translator()

GUI = Tk() 
GUI.geometry('500x300') 
GUI.title('ໂປຣເເກຣມເເປພາສາໂດຍ UncleMedia')
#-----config------
FONT = ('phetsarath ot',15)
#-----Label------
L = ttk.Label(GUI,text='ກະລຸນາໃສ່ຄຳສັບທີ່ຕ້ອງກັນເເປ',font=FONT)
L.pack()

#-----Entry(ຊ່ອງກອກຂໍ້ຄວາມ)-----
v_vocab = StringVar()# ກ່ອງເກັບຂໍ້ມູນ
E1 = ttk.Entry(GUI,textvariable = v_vocab,font=FONT,width=40)
E1.pack(pady=20)


#-----Button(ປຸ່ມເເປ)-----
def Translate():
    vocab = v_vocab.get()#.getຄືໃຫ້ສະເເດງຜົນອອກມາ
    meaning = translator.translate(vocab,dest='lo')
    print(vocab + ':' + meaning.text)
    print(meaning.pronunciation)
    v_result.set(vocab + ':' + meaning.text)
    
B1 = ttk.Button(GUI,text='Translate',command=Translate)
B1.pack(ipadx=20,ipady=10)

#-----Label------
L = ttk.Label(GUI,text='ຄຳເເປ',font=FONT)
L.pack()
#-------Result-----
v_result = StringVar()
FONT2 = ('phetsarath ot',15)
R1 = ttk.Label(GUI,textvariable=v_result,font=FONT2,foreground='blue')
R1.pack()
GUI.mainloop() 