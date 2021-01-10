# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 18:21:16 2020

@author: Riya
"""
from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage

class qr_code:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Generator")
        self.root.resizable(False,False)
        
        title=Label(self.root,text="QR Code Generator",font=("times new roman",40),bg='#053246',fg='white',anchor='w').place(x=0,y=0,relwidth=1)
        
        ##---------Employee details window-----------##
        ##variable-----##
        self.var_Emp=StringVar()
        self.var_Name=StringVar()
        self.var_Department=StringVar()
        self.var_Designation=StringVar()
        
        
        Emp_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='White')
        Emp_Frame.place(x=50,y=100,width=500,height=380)
       
        Emp_title=Label(Emp_Frame,text="Employee Details",font=("guody old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)
        
        label_Emp=Label(Emp_Frame,text="Employee ID",font=("times new roman",15,'bold'),bg='white').place(x=20,y=60)
        label_Name=Label(Emp_Frame,text="Name",font=("times new roman",15,'bold'),bg='white').place(x=20,y=100)
        label_Department=Label(Emp_Frame,text="Department",font=("times new roman",15,'bold'),bg='white').place(x=20,y=140)
        label_Designation=Label(Emp_Frame,text="Designation",font=("times new roman",15,'bold'),bg='white').place(x=20,y=180)
        
        
        txt_Emp=Entry(Emp_Frame,font=("times new roman",15),textvariable=self.var_Emp,bg='lightyellow').place(x=200,y=60)
        txt_Name=Entry(Emp_Frame,font=("times new roman",15),textvariable=self.var_Name,bg='lightyellow').place(x=200,y=100)
        txt_Department=Entry(Emp_Frame,font=("times new roman",15),textvariable=self.var_Department,bg='lightyellow').place(x=200,y=140)
        txt_Designation=Entry(Emp_Frame,font=("times new roman",15),textvariable=self.var_Designation,bg='lightyellow').place(x=200,y=180)
        
        
        btn_button=Button(Emp_Frame,text="Qr Generate",command=self.generate,font=("times nwe roman",18,'bold'),bg='#2196f3',fg='white').place(x=90,y=250,width=180,height=30)
        btn_clear=Button(Emp_Frame,text="Clear",command=self.Clear,font=("times nwe roman",18,'bold'),bg='#607d8b',fg='white').place(x=280,y=250,width=120,height=30)
        
        self.msg=''
        self.lbl_msg=Label(Emp_Frame,text=self.msg,font=("times new roman",20),bg='white',fg='green')
        self.lbl_msg.place(x=0,y=310,relwidth=1)
        
        ##---------Employee QR Code window-----------##
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='White')
        qr_Frame.place(x=600,y=100,width=250,height=380)
       
        qr_title=Label(qr_Frame,text="Employee QR Code",font=("guody old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)
        
        self.qr_code=Label(qr_Frame,text="No QR \nAvailable",font=("times new roman",15),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=200)
        
    def Clear(self):
        self.var_Emp.set('')
        self.var_Name.set('')
        self.var_Department.set('')
        self.var_Designation.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')
        
        
    def generate(self):
        if self.var_Designation.get()=='' or self.var_Emp.get()=='' or self.var_Department.get()=='' or self.var_Name.get()=='':
            self.msg="All fields are required for this!!!"
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"Employee ID: {self.var_Emp.get()}\nEmployee name: {self.var_Name.get()}\nDepartment : {self.var_Department.get()}\nDesignation: {self.var_Designation.get()}")
            qr_code=qrcode.make(qr_data)
            #print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,200])
            qr_code.save("D:\QR-Project/Emp_"+str(self.var_Emp.get())+'.png')
            ## image update--##
            self.im=ImageTk.PhotoImage(file="D:\QR-Project/Emp_"+str(self.var_Emp.get())+'.png')
            self.qr_code.config(image=self.im)
            ##----------Updating notification ----##
            self.msg="QR Generated succeessfully!!"
            self.lbl_msg.config(text=self.msg,fg='green')
           
      
root=Tk()
obj = qr_code(root)
root.mainloop()
