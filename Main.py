from urllib.request import urlopen
from bs4 import BeautifulSoup  
from tkinter import *


def get_variable_value():
    if strfname.get().find("g1") != -1:
      valueresult.set("g1.globo.com/rn") #assign val variable to other
    elif strfname.get().find("tribunadonorte") != -1:
      valueresult.set("www.tribunadonorte.com.br") #assign val variable to other
    else:
      valueresult.set("Site não está em nosso banco de dados") #assign val variable to other
    url = strfname.get() 

    def connect(url):
      try:
        html = urlopen(url)
        
        return html
      except:
        return False

    html = connect(url)

    if( html != False ):
      try:
        bsObj = BeautifulSoup(html, 'html.parser')
        for notice in bsObj.findAll('title'):
          texto1 = notice.get_text()
          labelf = Label(root, text = 'Título').pack()
          T = Text(root, height=2, width=100)
          T.pack()
          T.insert(END, texto1)
        for notice in bsObj.findAll('div', {
          'class': 'text-inner'
        }):
          texto = notice.get_text()
          labelf = Label(root, text = 'Conteúdo').pack()
          S = Scrollbar(root)
          T = Text(root, height=30, width=155)
          S.pack
          T.pack(fill=Y)
          S.config(command=T.yview)
          T.config(yscrollcommand=S.set)
          quote = texto
          T.insert(END, quote)
      except:
        texto = 'Ocorreu um erro na operação!'


root = Tk()
root.geometry('600x500')

strfname = StringVar()
strlname = StringVar()
valueresult = StringVar()

labelf = Label(root, text = 'Link da matéria').pack()
fname = Entry(root, justify='left', textvariable = strfname,width=100).pack() #strlname get input 

button = Button(root, text='Submit', command=get_variable_value).pack()
labelf = Label(root, text = 'Link de referencia').pack()
res = Entry(root, justify='left', textvariable = valueresult,width=100).pack()

root.mainloop()
