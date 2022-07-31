from tkinter import *
from tkinter import messagebox
import base64

def ENCRYPT():
    password = code.get()

    if password == "nihangchha":
        ENCscreen = Toplevel(screen)
        ENCscreen.title("ENCRYPTION")
        ENCscreen.geometry("400x200")
        ENCscreen.configure(bg="#ed3833")

        message=text1.get(1.0, END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(ENCscreen, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2=Text(ENCscreen, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypt)

    elif password=="":
        messagebox.showerror("encryption","Input Password")

    elif password !="":
        messagebox.showerror("encryption","Invalid Password")

def DECRYPT():
    password = code.get()

    if password == "nihangchha":
        DECscreen = Toplevel(screen)
        DECscreen.title("DECRYPTION")
        DECscreen.geometry("400x200")
        DECscreen.configure(bg="#00bd56")

        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")

        Label(DECscreen, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(DECscreen, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypt)

    elif password == "":
        messagebox.showerror("encryption", "Input Password")

    elif password != "":
        messagebox.showerror("encryption", "Invalid Password")

def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")
    screen.configure(bg="#797979")

    screen.title("ENC & DEC")
    def RESET():
        code.set("")
        text1.delete(1.0,END)

    Label(text="Enter anything for encryption and decryption",bg="yellow", fg="black", font=("Cambria", 13)).place(x=10, y=10)
    text1 = Text(font="Robote 20", bg="skyblue", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)
    Label(text="Remember your Key?", bg="yellow" , fg="black", font=("Cambria", 13)).place(x=10, y=170)

    code=StringVar()
    Entry(textvariable=code,width=19,bd=0,font=("arial",25),show="*").place(x=10,y=200)

    Button(text="Encrypt", height="2", width=23, bg="#ed3833",fg="white",bd=0,command=ENCRYPT).place(x=10,y=250)
    Button(text="Decrypt", height="2", width=23, bg="#00bd56", fg="white", bd=0,command=DECRYPT).place(x=200, y=250)
    Button(text="Reset",height="2",width="50", bg="#1089ff",fg="white",bd=0,command=RESET).place(x=10,y=300)

    screen.mainloop()
main_screen()