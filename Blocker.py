from tkinter import *
import shutil
from PIL import ImageTk, Image  
from tkinter import messagebox
import webbrowser

def block():
    try:
        original = r'Host\hosts'
        target = r'C:\Windows\System32\drivers\etc\hosts'
        shutil.copyfile(original, target)
        gallardo = messagebox.showinfo("Done!","Everything done Successfully :)")
    except:
        murcielago = messagebox.showerror("Error","Failed, Maybe you Should Run The Program as an Adminstrator or Check that 'hosts' file is in the same folder as the program")

def about():
    def github():
       webbrowser.open('https://github.com/ahmedbarakat2007')
    m5 = Tk()
    m5.geometry("200x150")
    m5.configure(bg="#1f242b")
    m5.resizable(0, 0)
    m5.iconbitmap("Textures\icon.ico")
    m5.title("About")
    
    Label(m5, text = "",bg="#1f242b", foreground="white").pack()
    Label(m5, text="Porn Blocker", font='san-serif 14 bold' ,bg="#1f242b", foreground="white").pack()
    Label(m5, text="Version : 2.0.1", font='san-serif 10 bold' ,bg="#1f242b", foreground="white").pack()
    Label(m5, text="Made By Ahmed Barakat", font='san-serif 10 bold' ,bg="#1f242b", foreground="white").pack()
    m3 = Button(m5, text='Github', font='san-serif 16 bold', bg='purple',fg='white', padx=2,command= github).pack()

root = Tk()
root.geometry("200x300")
root.resizable(0, 0)
root.iconbitmap("Textures\icon.ico")
root.configure(bg="#1f242b")
root.title("Porn Blocker(Made by Ahmed Barakat)")

menubar = Menu(root, background="#16191f", foreground="white")
root.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)

file_menu.add_command(
    label='About',
    command=about
)

file_menu.add_command(
    label='Exit',
    command=root.destroy
)

# add the File menu to the menubar
menubar.add_cascade(
    label="Menu",
    menu=file_menu
)

Label(root, bg="#1f242b").pack()

lb1 = Label(root, text="Porn Blocker", font='san-serif 14 bold',bg="#1f242b",fg="white").pack()

Label(root, bg="#1f242b").pack()

img = Image.open('Textures/block.png')
img = img.resize((75, 70), Image.ANTIALIAS)    
img = ImageTk.PhotoImage(img)
panel = Label(root, image=img, bg="#1f242b")
panel.image = img
panel.pack(side = "top", expand = "no")

Label(root, bg="#1f242b").pack()
Label(root, bg="#1f242b").pack()
Label(root, bg="#1f242b").pack()

f8 = Button(root, text='Block', font='san-serif 16 bold', bg='red', padx=2,command= block).pack()

root.mainloop()