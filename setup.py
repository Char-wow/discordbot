#discord plugins
import discord
import os
from dotenv import load_dotenv
import tkinter as tk

import mysql.connector
from mysql.connector import Error
import pandas as pd
from discordconnect import connect
#


load_dotenv()
pw = os.getenv('SQLROOTPASS')

def threadmain():
    t = tk.Tk()
    b = tk.Button(t,text='test', command=connect)
    b.grid(row=1)
    t.mainloop()

    
#tkinter GUI initialisation
root = tk.Tk()
root.geometry("300x200")
root.title("Discord Bot")


button1 = tk.Button(text="   Discord Control Window   ",bg="brown",command=threadmain)
button1.grid(column=0,row=1)




    
#


#

root.mainloop()