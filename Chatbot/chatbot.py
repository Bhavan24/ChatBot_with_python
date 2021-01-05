from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from time import strftime
import keyword


def btnSend_command():
    msg = msgText.get().lower()
    send = "you: "+ msgText.get()
    displayText.insert(END,"\n"+send)
    if(msg == 'hi'):
        displayText.insert(END,"\n" + "Bot: hello")
    elif(msg == 'hello'):
        displayText.insert(END,"\n"+ "Bot: hi")
    elif(msg == 'how are you?'):
        displayText.insert(END,"\n"+ "Bot: I am fine :), How are you?")
    elif(msg == 'i am fine'):
        displayText.insert(END,"\n"+ "Bot: Nice to hear that")
    elif(msg == 'i like you'):
        displayText.insert(END,"\n"+ "Bot: I like you too!")
    elif(msg == 'i hate you'):
        displayText.insert(END,"\n"+ "Bot: Why! :(")
    elif(msg == 'i love you'):
        displayText.insert(END,"\n"+ "Bot: i love you too! :)")
    elif(msg in 'bye'):
        displayText.insert(END,"\n"+ "Bot: Bye! Take care:)")
    elif(msg in 'what is the time now?'):
        displayText.insert(END,"\n"+ f"Bot: The time is {strftime('%H:%M')}")
    elif(msg in 'what day is it? or tell me the date'):
        displayText.insert(END,"\n"+ f"Bot: Today is {strftime('%d/%m/%Y')}")
    elif(msg in 'keywords'):
        displayText.insert(END,"\n"+ f"Bot: Python keywords {keyword.kwlist}")
    elif(('+' in msg) or ('-' in msg) or ('*' in msg) or ('/' in msg) or ('**' in msg) or ('%' in msg)):
        displayText.insert(END,"\n"+ f"Bot: Answer is {eval(msg)}")
    else:
        displayText.insert(END,"\n"+ "Bot: Sorry, I didn't get it ")
    msgText.delete(0,END)

root = tk.Tk()
root.title("Chat-Bot")
root.geometry('640x500')
root.resizable(width=False, height=False)
root["bg"] = "#46A2F8"

displayText = tk.Text(root)
displayText["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=18)
displayText["font"] = ft
displayText["fg"] = "#333333"
displayText["relief"] = "flat"
displayText.place(x=20,y=10,width=605,height=426)

msgText = tk.Entry(root)
msgText["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=18)
msgText["font"] = ft
msgText["fg"] = "#333333"
msgText.place(x=20,y=450,width=486,height=40)

btnSend = tk.Button(root)
btnSend["bg"] = "#37fe13"
ft = tkFont.Font(family='Times',size=23)
btnSend["font"] = ft
btnSend["fg"] = "#000000"
btnSend["justify"] = "center"
btnSend["text"] = "SEND"
btnSend.place(x=520,y=450,width=102,height=42)
btnSend["command"] = btnSend_command

root.mainloop()