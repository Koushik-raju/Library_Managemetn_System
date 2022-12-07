from logging import root
from re import L
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import tkinter
import mysql.connector
import datetime

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1270x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Rahul\Desktop\MyProject\Photos\photo-1554268586-841db307a5cd.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="white")
        frame.place(x=450,y=75,width=420,height=480)

        login_lbl=Label(frame,text="LOGIN HERE",font=("times new roman",18,"bold"),fg="darkblue",bg="white")
        login_lbl.place(x=10,y=10)

        img1=Image.open(r"C:\Users\Rahul\Desktop\MyProject\Photos\images.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(self.root,image=self.photoimage1,bg="white",borderwidth=0)
        lblimg1.place(x=570,y=115,width=150,height=130)


        get_str=Label(frame,text="Get Started",font=("times new roman",25,"bold"),fg="green",bg="white")
        get_str.place(x=110,y=160)

        #label
        username=lbl=Label(frame,text="Username",font=("times new romen",12,"bold"),fg="green",bg="white")
        username.place(x=80,y=220)

        self.txtuser=ttk.Entry(frame,font=("times new romen",15,"bold"))
        self.txtuser.place(x=80,y=240,width=250)

        password=lbl=Label(frame,text="Password",font=("times new romen",12,"bold"),fg="green",bg="white")
        password.place(x=80,y=280)

        self.txtpass=ttk.Entry(frame,font=("times new romen",15,"bold"),show="*")
        self.txtpass.place(x=80,y=300,width=250)

        #LoginButton
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new romen",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=80,y=340,width=75,height=35)
        
        #Registerbutton
        registerbtn=Button(frame,command=self.register_window,text="New User Register",font=("times new roman",12,"bold"),borderwidth=0,fg="blue",bg="white",activeforeground="blue",activebackground="white")
        registerbtn.place(x=80,y=380,width=135)
        #Forget_password
        registerbtn=Button(frame,command=self.forgot_password_window,text="Forgot Password",font=("times new roman",12,"bold"),borderwidth=0,fg="blue",bg="white",activeforeground="blue",activebackground="white")
        registerbtn.place(x=70,y=400,width=135)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="rahul@gmail.com" and self.txtpass.get()=="jaykar123@":
            messagebox.showinfo("Sucess","Welcom to LibraryMS")
        else:
            conn=mysql.connector.connect(host="localhost",port=3307,user="root",password="",database="myproject")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from registern where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get(),
                                                                          ))

            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=LibraryManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
        
#=======================reset password==========================
    

    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select sucurity Quetion",parent=self.root)
        elif self.txt_SecurityA.get()=="":
            messagebox.showerror("Error","Plase enter the answer",parent=self.root)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",port=3307,user="root",password="",database="myproject")
            my_cursor=conn.cursor()
            query=("select * from registern where email=%s and securityQ=%s and securityA=%s") 
            vlaue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_SecurityA.get(),)
            my_cursor.execute(query, vlaue)
            row=my_cursor.fetchone()          
            if row==None:
               messagebox.showerror("Error", "Planse enter correct Answer",parent=self.root)
            else:
                query=("update registern set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Your password has been reset ,plaese login new password",parent=self.root)
                
                
##=========================forget password==================================

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error", "Plaese Enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",port=3307,user="root",password="",database="myproject")
            my_cursor=conn.cursor()            
            query=("select * from registern where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()
            #print (row)

            if row==None:
                messagebox.showerror("My Error","Plaese enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x400+500+178")

                l=Label(self.root2, text="Forget Password", font=("times new roman",20, "bold"), fg="red",bg="white") 
                l.place(x=0, y=10, relwidth=1)

                SecurityQ=Label(self.root2,text="Select Security Questions",font=("times new romen",12,"bold"),bg="white")
                SecurityQ.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["value"]=("Select","Your Birth place","Your Favorite actor","Your closely Friend")
                self.combo_security_Q.place(x=50,y=105,width=250)
                self.combo_security_Q.current(0)

                SecurityA=Label(self.root2,text="Security Answer",font=("times new romen",12,"bold"),bg="white")
                SecurityA.place(x=50,y=150)

                self.txt_SecurityA=ttk.Entry(self.root2,font=("times new romen",12,"bold"))
                self.txt_SecurityA.place(x=50,y=175,width=250)

                

                new_password=Label(self.root2, text="New Password", font=("times new roman",15,"bold"),bg="white") 
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold")) 
                self.txt_newpass.place(x=50, y=250,width=250)

                btn=Button(self.root2,command=self.reset_pass,text="Reset", font=("times new roman",15, "bold"),fg="White",bg="green") 
                btn.place(x=100,y=298)

            

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1270x800+0+0")

        #==============Variable===============
        self.var_fname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Rahul\Desktop\MyProject\Photos\SDT_Zoom-Backgrounds_April-8_Windansea-1-logo.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
    

        frame=Frame(self.root,bg="pink")
        frame.place(x=450,y=80,width=480,height=540)


        #Label
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkblue",bg="pink")
        register_lbl.place(x=10,y=10)

        #Label and Entry
        fname=Label(frame,text="Full Name",font=("times new romen",12,"bold"),bg="pink")
        fname.place(x=60,y=50)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new romen",12,"bold"))
        self.fname_entry.place(x=60,y=70,width=250)

        contact=Label(frame,text="Contact No",font=("times new romen",12,"bold"),bg="pink")
        contact.place(x=60,y=100)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new romen",12,"bold"))
        self.txt_contact.place(x=60,y=120,width=250)
    
        email=Label(frame,text="Email",font=("times new romen",12,"bold"),bg="pink")
        email.place(x=60,y=155)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new romen",12,"bold"))
        self.txt_email.place(x=60,y=175,width=250)

        SecurityQ=Label(frame,text="Select Security Questions",font=("times new romen",12,"bold"),bg="pink")
        SecurityQ.place(x=60,y=210)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["value"]=("Select","Your Birth place","Your Favorite actor","Your closely Friend")
        self.combo_security_Q.place(x=60,y=230,width=250)
        self.combo_security_Q.current(0)
        

        SecurityA=Label(frame,text="Security Answer",font=("times new romen",12,"bold"),bg="pink")
        SecurityA.place(x=60,y=260)

        self.txt_SecurityA=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new romen",12,"bold"))
        self.txt_SecurityA.place(x=60,y=280,width=250)

        pswd=Label(frame,text="Password",font=("times new romen",12,"bold"),bg="pink")
        pswd.place(x=60,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new romen",12,"bold"))
        self.txt_pswd.place(x=60,y=330,width=250)

        confirm_pswd=Label(frame,text="Conform Password",font=("times new romen",12,"bold"),bg="pink")
        confirm_pswd.place(x=60,y=360)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new romen",12,"bold"))
        self.txt_confirm_pswd.place(x=60,y=380,width=250)

        
        #===============check button===================
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),bg="pink",onvalue=1,offvalue=0)
        self.checkbtn.place(x=60,y=410)

        #Button
        savebtn=Button(frame,command=self.register_data,text="Save",font=("times new romen",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="darkblue",activeforeground="white",activebackground="darkblue")
        savebtn.place(x=60,y=455,width=75,height=35)

        #=========Function declaration============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & conform password must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","please agree our terms and condition",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",port=3307,user="root",password="",database="myproject")
            my_cursor=conn.cursor()
            query=("select * from registern where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:                
                messagebox.showerror("Error","User already exist,please try another username")
            else:
                my_cursor.execute("insert into registern values(%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_fname.get(),                                                                            
                                                                                    self.var_contact.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_securityQ.get(),
                                                                                    self.var_securityA.get(),                                                                                  
                                                                                    self.var_pass.get()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucess","Register Sucessfully",parent=self.root)


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1270x800+0+0")

        #============================Variables=======================
        self.member_var=StringVar()
        self.regno_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()
        
        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=6,relief=RIDGE,font=("times new romen",22,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=6,relief=RIDGE,padx=10,bg="powder blue")
        frame.place(x=0,y=50,width=1270,height=360)

        # ===========================DataFrameLeft=================================================
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=6,relief=RIDGE,font=("times new romen",12,"bold"))
        DataFrameLeft.place(x=0,y=1,width=850,height=350)

        lblMemeber=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("Times New Romen",12,"bold"),padx=2,pady=6)
        lblMemeber.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.member_var,width=25)
        comMember["value"]=("Admin Staf","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_NO=Label(DataFrameLeft,bg="powder blue",text="Reg No:",font=("Times New Romen",12,"bold"),padx=2,pady=6)
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("Times New Romen",15,"bold"),textvariable=self.regno_var,width=24)
        txtPRN_NO.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="ID No:",font=("Times New Romen",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("Times New Romen",15,"bold"),textvariable=self.id_var,width=24)
        txtTitle.grid(row=2,column=1)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="FirstName:",font=("Times New Romen",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=3,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("Times New Romen",15,"bold"),textvariable=self.firstname_var,width=24)
        txtTitle.grid(row=3,column=1)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="Surname:",font=("Times New Romen",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=4,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("Times New Romen",15,"bold"),textvariable=self.lastname_var,width=24)
        txtTitle.grid(row=4,column=1)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="Address1:",font=("Times New Romen",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=5,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("Times New Romen",15,"bold"),textvariable=self.address1_var,width=24)
        txtTitle.grid(row=5,column=1)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="Address2:",font=("Times New Romen",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=6,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("Times New Romen",15,"bold"),textvariable=self.address2_var,width=24)
        txtTitle.grid(row=6,column=1)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="Post Code:",font=("Times New Romen",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=7,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("Times New Romen",15,"bold"),textvariable=self.postcode_var,width=24)
        txtTitle.grid(row=7,column=1)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="Mobile Number:",font=("Times New Romen",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=8,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("Times New Romen",15,"bold"),textvariable=self.mobile_var,width=24)
        txtTitle.grid(row=8,column=1)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="Book Id:",font=("Times New Romen",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=0,column=2,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("Times New Romen",15,"bold"),textvariable=self.bookid_var,width=24)
        txtTitle.grid(row=0,column=3)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="Book Title:",font=("Times New Romen",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=1,column=2,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("Times New Romen",15,"bold"),textvariable=self.booktitle_var,width=24)
        txtTitle.grid(row=1,column=3)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="Auther Name:",font=("Times New Romen",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=2,column=2,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("Times New Romen",15,"bold"),textvariable=self.auther_var,width=24)
        txtTitle.grid(row=2,column=3)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="Date Borrowed:",font=("Times New Romen",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=3,column=2,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("Times New Romen",15,"bold"),textvariable=self.dateborrowed_var,width=24)
        txtTitle.grid(row=3,column=3)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="Date Due:",font=("Times New Romen",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=4,column=2,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("Times New Romen",15,"bold"),textvariable=self.datedue_var,width=24)
        txtTitle.grid(row=4,column=3)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="Days On Book:",font=("Times New Romen",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=5,column=2,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("Times New Romen",15,"bold"),textvariable=self.daysonbook_var,width=24)
        txtTitle.grid(row=5,column=3)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="Late Return Fine:",font=("Times New Romen",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=6,column=2,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("Times New Romen",15,"bold"),textvariable=self.latereturnfine_var,width=24)
        txtTitle.grid(row=6,column=3)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="Date Over Due:",font=("Times New Romen",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=7,column=2,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("Times New Romen",15,"bold"),textvariable=self.dateoverdue_var,width=24)
        txtTitle.grid(row=7,column=3)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="Actual Price:",font=("Times New Romen",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=8,column=2,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("Times New Romen",15,"bold"),textvariable=self.finalprice_var,width=24)
        txtTitle.grid(row=8,column=3)
        #==============DataFrame Right=============================
        DataFrameRight=LabelFrame(frame,bd=6,padx=20,relief=RIDGE,bg="powder blue",
                                           font=("arial",12,"bold"),text="VIEW DETAILS")
        DataFrameRight.place(x=855,y=1,width=385,height=350)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=40,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)
        
        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.place(x=300,y=5,height=310)


        # =====================================Buttons Frame==========================================
        Framebutton=Frame(self.root,bd=6,relief=RIDGE,padx=10,bg="powder blue")
        Framebutton.place(x=0,y=400,width=1270,height=45)

        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=20,bg="blue",fg="white",activeforeground="white",activebackground="blue")
        btnAddData.grid(row=0,column=0)

        btnShowData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=20,bg="blue",fg="white",activeforeground="white",activebackground="blue")
        btnShowData.grid(row=0,column=1)

        btnUpdateData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=20,bg="blue",fg="white",activeforeground="white",activebackground="blue")
        btnUpdateData.grid(row=0,column=2)

        btnDeleteData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=20,bg="blue",fg="white",activeforeground="white",activebackground="blue")
        btnDeleteData.grid(row=0,column=3)

        btnResetData=Button(Framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=20,bg="blue",fg="white",activeforeground="white",activebackground="blue")
        btnResetData.grid(row=0,column=4)

        btnExit=Button(Framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=18,bg="blue",fg="white",activeforeground="white",activebackground="blue")
        btnExit.grid(row=0,column=5)

         # =====================================Information Frame Search System==========================================
        FrameDetails=LabelFrame(self.root,bd=6,relief=RIDGE,padx=20,bg="white")
        FrameDetails.place(x=0,y=445,width=1270,height=200)

        lblSearchBy=Label(FrameDetails,font=("arial",16,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        com_Search=ttk.Combobox(FrameDetails,textvariable=self.search_var,font=("times new roman",16,"bold"),width=24,state="readonly")
        com_Search["value"]=("regno","mobileno","bookid")
        com_Search.current(0)
        com_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()   
        txtSearch=ttk.Entry(FrameDetails,textvariable=self.txt_search,font=("arial",17,"bold"),width=15)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(FrameDetails,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold",width=8,activeforeground="gold",activebackground="black")
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(FrameDetails,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=8,activeforeground="gold",activebackground="black")
        btnShowAll.grid(row=0,column=4,padx=1)



        Table_frame=Frame(FrameDetails,bd=3,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=35,width=1225,height=150)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.library_table=ttk.Treeview(Table_frame,column=("membertype","regno","idno","firstname","lastname","address1",
                                            "address2","postid","mobile","bookid","booktitles","auther","dateborrowed",
                                            "datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)


        
        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("regno",text="Reg No.")
        self.library_table.heading("idno",text="ID No")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitles",text="Book Title")
        self.library_table.heading("auther",text="Auther")
        self.library_table.heading("dateborrowed",text="Date of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="DaysOnBook")
        self.library_table.heading("latereturnfine",text="LateReturnFine")
        self.library_table.heading("dateoverdue",text="DateOverDue")
        self.library_table.heading("finalprice",text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("regno",width=100)
        self.library_table.column("idno",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitles",width=100)
        self.library_table.column("auther",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
    
    def add_data(self):
        conn=mysql.connector.connect(host="localhost",port=3307,user="root",password="",database="myproject")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into librarym values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                             self.member_var.get(), 
                                                                                                             self.regno_var.get(),                                                                                                            
                                                                                                             self.id_var.get(),
                                                                                                             self.firstname_var.get(),
                                                                                                             self.lastname_var.get(),
                                                                                                             self.address1_var.get(),
                                                                                                             self.address2_var.get(),
                                                                                                             self.postcode_var.get(),
                                                                                                             self.mobile_var.get(),
                                                                                                             self.bookid_var.get(),
                                                                                                             self.booktitle_var.get(),
                                                                                                             self.auther_var.get(),
                                                                                                             self.dateborrowed_var.get(),
                                                                                                             self.datedue_var.get(),
                                                                                                             self.daysonbook_var.get(),
                                                                                                             self.latereturnfine_var.get(),
                                                                                                             self.dateoverdue_var.get(),
                                                                                                             self.finalprice_var.get(),
                                                                                                             
                                                                                                            
                                                                                                             
                                                                                                             ))
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Sucess","Member has been inserted sucessfully",parent=self.root)
    
    def update(self):
        conn=mysql.connector.connect(host="localhost",port=3307,user="root",password="",database="myproject")
        my_cursor=conn.cursor()
        my_cursor.execute("update librarym set 	member=%s,idno=%s,fname=%s,surname=%s,address1=%s,address2=%s,postcode=%s,mobileno=%s,bookid=%s,booktitle=%s,authorname=%s,dateborrowed=%s,datedue=%s,daysonbook=%s,latereturnfine=%s,dateoverdue=%s,actualprice=%s where regno=%s",(
                                                                                                             self.member_var.get(),                                                                                                             
                                                                                                             self.id_var.get(),
                                                                                                             self.firstname_var.get(),
                                                                                                             self.lastname_var.get(),
                                                                                                             self.address1_var.get(),
                                                                                                             self.address2_var.get(),
                                                                                                             self.postcode_var.get(),
                                                                                                             self.mobile_var.get(),
                                                                                                             self.bookid_var.get(),
                                                                                                             self.booktitle_var.get(),
                                                                                                             self.auther_var.get(),
                                                                                                             self.dateborrowed_var.get(),
                                                                                                             self.datedue_var.get(),
                                                                                                             self.daysonbook_var.get(),
                                                                                                             self.latereturnfine_var.get(),
                                                                                                             self.dateoverdue_var.get(),
                                                                                                             self.finalprice_var.get(),
                                                                                                             self.regno_var.get(),

                                                                                                          ))
                            
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close

        messagebox.showinfo("Sucess","Member has been updated",parent=self.root)
                                                                                                                                                                                                    
                                                                                                            
                                                                                                     
        

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",port=3307,user="root",password="",database="myproject")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from librarym")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END, values=i)
                conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.regno_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.auther_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.datedue_var.set(row[16]),        
        self.finalprice_var.set(row[17])

    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END,"Reg No:\t\t"+ self.regno_var.get() + "\n")
        self.txtBox.insert(END,"ID No:\t\t"+ self.id_var.get() + "\n")
        self.txtBox.insert(END,"FirstName:\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"LastName:\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"Address1:\t\t"+ self.address1_var.get() + "\n")
        self.txtBox.insert(END,"Address2:\t\t"+ self.address2_var.get() + "\n")
        self.txtBox.insert(END,"Post Code:\t\t"+ self.postcode_var.get() + "\n")
        self.txtBox.insert(END,"Mobile No:\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"Book ID:\t\t"+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END,"Book Title:\t\t"+ self.booktitle_var.get() + "\n")
        self.txtBox.insert(END,"Auther:\t\t"+ self.auther_var.get() + "\n")
        self.txtBox.insert(END,"DateBorrowed:\t\t"+ self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END,"DateDue:\t\t"+ self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END,"DaysOnBook:\t\t"+ self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END,"LateReturnFine:\t\t"+ self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END,"DataOverDue:\t\t"+ self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END,"FinalPrice:\t\t"+ self.finalprice_var.get() + "\n")

    def reset(self):
        self.member_var.set(""),
        self.regno_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.auther_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set("")
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library managment System","Do you want to exit",parent=self.root)
        if iExit>0:
            self.root.destroy()
            return


    def delete(self):
        if self.regno_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select the Member",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",port=3307,user="root",password="",database="myproject")
            my_cursor=conn.cursor()
            query="delete from librarym where regno=%s"
            value=(self.regno_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Sucess","Member has been Deleted",parent=self.root)

    def search(self):
            conn=mysql.connector.connect(host="localhost",port=3307,user="root",password="",database="myproject")
            my_cursor=conn.cursor()

            my_cursor.execute("select * from librarym where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                    self.library_table.delete(*self.library_table.get_children())
                    for i in rows:
                            self.library_table.insert("",END,values=i)
                    conn.commit()
            conn.close()





       
if __name__=="__main__":
    main()