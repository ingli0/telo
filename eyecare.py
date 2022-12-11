from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class eyecare:
    def __init__(self,root):
        self.root=root
        self.root.title("EYECARE ΔΙΑΧΕΙΡΙΣΗ")
        self.root.geometry("1540x800+0+0")

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="PAXIDI MANAGE EYE",fg="blue",bg="white",font=("time new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #  data frame
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=20,
                                                             font=("times new roman",15,"bold"),text="ΠΛΗΡΟΦΟΡΙΕΣ ΑΣΘΕΝΗ")
        DataframeLeft.place(x=0,y=5,width=490,height=350)

        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=20,
                                                             font=("times new roman",15,"bold"),text="ΑΠΟΤΕΛΕΣΜΑΤΑ")
        DataframeRight.place(x=500,y=5,width=980,height=350)

        # button

        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)
    
        #deitail
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)

        #data frame
        lblNameTable=Label(DataframeLeft,text="ΟΝΟΜΑΤΑ ΠΙΝΑΚΩΝ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTable.grid(row=0,column=0)

        conNametablet=ttk.Combobox(DataframeLeft,font=("times new roman",12,"bold"),
                                                                                   width=33)
        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="amka",padx=0)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtref.grid(row=1,column=1)

        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="ON/PONIMP",padx=2,pady=4)
        lblref.grid(row=2,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtref.grid(row=2,column=1)

        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="ASFALISI",padx=2,pady=6)
        lblref.grid(row=3,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtref.grid(row=3,column=1)

        lblref=Label(DataframeRight,font=("arial",12,"bold"),text="lefta",padx=0)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeRight,font=("arial",13,"bold"),width=35)
        txtref.grid(row=1,column=1)

        lblref=Label(DataframeRight,font=("arial",12,"bold"),text="Ασθένειες",padx=2,pady=4)
        lblref.grid(row=2,column=0,sticky=W)
        txtref=Entry(DataframeRight,font=("arial",13,"bold"),width=35)
        txtref.grid(row=2,column=1)

        lblref=Label(DataframeRight,font=("arial",12,"bold"),text="Τιμές των μετρούμενων τιμών",padx=0,pady=6)
        lblref.grid(row=3,column=0,sticky=W)
        txtref=Entry(DataframeRight,font=("arial",13,"bold"),width=35)
        txtref.grid(row=3,column=1)

        lblref=Label(DataframeRight,font=("arial",12,"bold"),text="Ημερομηνία της επίσκεψης",padx=0,pady=8)
        lblref.grid(row=4,column=0,sticky=W)
        txtref=Entry(DataframeRight,font=("arial",13,"bold"),width=35)
        txtref.grid(row=4,column=1)

        lblref=Label(DataframeRight,font=("arial",12,"bold"),text="Θεραπεία ή λύση ",padx=0,pady=10)
        lblref.grid(row=5,column=0,sticky=W)
        txtref=Entry(DataframeRight,font=("arial",13,"bold"),width=35)
        txtref.grid(row=5,column=1)

        lblref=Label(DataframeRight,font=("arial",12,"bold"),text="Φαρμακευτικ ή αγωγή",padx=0,pady=12)
        lblref.grid(row=6,column=0,sticky=W)
        txtref=Entry(DataframeRight,font=("arial",13,"bold"),width=35)
        txtref.grid(row=6,column=1)

        lblref=Label(DataframeRight,font=("arial",12,"bold"),text="Φαρμακευτικ ή αγωγή",padx=0,pady=14)
        lblref.grid(row=7,column=0,sticky=W)
        txtref=Entry(DataframeRight,font=("arial",13,"bold"),width=35)
        txtref.grid(row=7,column=1)

        lblref=Label(DataframeRight,font=("arial",12,"bold"),text="Αποτέλεσμα της θεραπεία ",padx=0)
        lblref.grid(row=8,column=0,sticky=W)
        txtref=Entry(DataframeRight,font=("arial",13,"bold"),width=35)
        txtref.grid(row=8,column=1)

        lblref=Label(DataframeRight,font=("arial",12,"bold"),text="Μετρ. βαθμό",padx=0)
        lblref.grid(row=1,column=2,sticky=W)
        txtref=Entry(DataframeRight,font=("arial",13,"bold"),width=35)
        txtref.grid(row=1,column=3)

        lblref=Label(DataframeRight,font=("arial",12,"bold"),text="Είδ. φαρμάκων",padx=0,pady=2)
        lblref.grid(row=2,column=2,sticky=W)
        txtref=Entry(DataframeRight,font=("arial",13,"bold"),width=35)
        txtref.grid(row=2,column=3)

        lblref=Label(DataframeRight,font=("arial",12,"bold"),text="Συμπτωμα",padx=0,pady=4)
        lblref.grid(row=3,column=2,sticky=W)
        txtref=Entry(DataframeRight,font=("arial",13,"bold"),width=35)
        txtref.grid(row=3,column=3)

        lblref=Label(DataframeRight,font=("arial",12,"bold"),text="Ονόματα επιχ.",padx=0,pady=6)
        lblref.grid(row=4,column=2,sticky=W)
        txtref=Entry(DataframeRight,font=("arial",13,"bold"),width=35)
        txtref.grid(row=4,column=3)



root=Tk()
ob=eyecare(root)
root.mainloop()
