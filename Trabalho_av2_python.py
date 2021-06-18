from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import DB


def inserir():
    if vnome.get()=="" or vmateria.get()=="" or vav1.get()=="" or vav2.get()=="" or vavd.get()=="":
        messagebox.showinfo(title="ERRO", message="Digite todos os dados")
        return
    tv.insert("", "end", values=(vnome.get(), vmateria.get(), vav1.get(), vav2.get(), vavd.get()))
    vnome.delete(0,END)
    vmateria.delete(0,END)
    vav1.delete(0,END)
    vav2.delete(0,END)
    vavd.delete(0,END)
    vnome.focus()


def deletar():
    try:
        itemSelecionado=tv.selection()[0]
        tv.delete(itemSelecionado)
    except:
        messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser deletado")

def obter():
    try:
        itemSelecionado=tv.selection()[0]
        valores=tv.item(itemSelecionado, "values")
        print("Nome......: " + valores[0])
        print("Materia...: " + valores[1])
        print("AV1.......: " + valores[2])
        print("AV2.......: " + valores[3])
        print("AVD.......: " + valores[4])
    except:
        messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser obtido")

app=Tk()
app.title("Cadastro de alunos")
app.geometry("620x500")

lbnome=Label(app, text="Nome")
vnome=Entry(app)

lbmateria=Label(app, text="Materia")
vmateria=Entry(app)

lbav1=Label(app, text="AV1")
vav1=Entry(app)

lbav2=Label(app, text="AV2")
vav2=Entry(app)

lbavd=Label(app, text="AVD")
vavd=Entry(app)

tv=ttk.Treeview(app,columns=('nome', 'materia', 'av1', 'av2', 'avd'), show= 'headings')

tv.column('nome', minwidth=0, width= 250)
tv.column('materia', minwidth=0, width=100)
tv.column('av1', minwidth=0, width=50)
tv.column('av2', minwidth=0, width=50)
tv.column('avd', minwidth=0, width=50)
tv.heading('nome', text='Nome')
tv.heading('materia', text='Materia')
tv.heading('av1', text='AV1')
tv.heading('av2', text='AV2')
tv.heading('avd', text='AVD')

btn_inserir=Button(app, text="Inserir", command=inserir)
btn_deletar=Button(app, text="Deletar", command=deletar)
btn_obter=Button(app, text="Obter", command=obter)


lbnome.grid(column=0,row=0,sticky='w')
vnome.grid(column=0,row=1)

lbmateria.grid(column=1,row=0,sticky='w')
vmateria.grid(column=1,row=1,sticky='w')

lbav1.grid(column=2,row=0,sticky='w')
vav1.grid(column=2,row=1,sticky='w')

lbav2.grid(column=3,row=0,sticky='w')
vav2.grid(column=3,row=1,sticky='w')

lbavd.grid(column=4,row=0,sticky='w')
vavd.grid(column=4,row=1,sticky='w')

tv.grid(column=0,row=5,columnspan=5,pady=6)

btn_inserir.grid(column=1,row=7)
btn_deletar.grid(column=2,row=7)
btn_obter.grid(column=3,row=7)


app.mainloop()
