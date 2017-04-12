import Tkinter
from Tkinter import *

root = Tk()
root["bg"]="white"
root.resizable(0,0)
master = Frame(root).grid()
f = Frame(root, bg = "orange").grid(padx = 20, pady = 20,sticky='S')
def nasdoc():
    import requests
    import sys
    from requests.exceptions import ConnectionError
    mtext = var.get()
    s="http://download.finance.yahoo.com/d/quotes.csv?s=" +str(mtext)+ "&f=l1"
    
    try:
        res = requests.get(s)
        if res.status_code == 200:
            if res.text!='N/A\n' and res.text!='\n':
                ss= res.text
            else:
                ss= "Invalid Nasdaq symbol"
        else:
            ss= "Didn't got correct response for this url -> %s" 
    except ConnectionError:
        ss= "Failed to establish a connection.\n PLease check your internet connection!!!!"
    return ss

def clear_text():
    s.set(' ')
    ent.delete(0, 'end')
    
var = StringVar()
root.title("Share Value Finder")
root.geometry('350x200')
Label(root,text='Enter nasdaq symbol', font=('helvetica',15),fg='blue', bg='white').grid(row=0, columnspan=4, padx=10,pady=10)
ent = Entry(root,textvariable = var)
ent.font=20
ent.grid(row=1, columnspan=5,sticky=W+E, ipadx=6, ipady=6, padx=10)

s = StringVar()
def show_entry(event):
    r=nasdoc()
    global s
    s.set('%s' %(r.strip())) 

ent.bind('<Return>', show_entry)

s_label = Label(root, textvariable=s,font=(s,12), width=32, bg='white').grid(row=3, columnspan=3,padx=5,pady = 6)


Button(root, text='Exit ', fg='red',font=('Exit ',10), bg='white',  command=root.quit).grid(row=5, columnspan=2,ipadx=5,ipady = 2)

Button(root , text="Clear",fg='red',font=('Clear',10), bg='white', command=clear_text).grid(row=5,column=1,ipadx=4,ipady = 2)

root.mainloop()



