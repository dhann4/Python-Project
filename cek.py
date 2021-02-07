
import random
import datetime
import time
import tkinter.messagebox
from tkinter import *
from PIL import ImageTk
from tkinter import ttk

bg_color = 'powder blue'
bg_color1 = 'cadet blue'
bg_color2 = '#1ED760'
bg_color3 = '#84503C'
fg_color = 'black'
font = 'URW Gothic L'

def main():
    root = Tk()
    app = window1(root)

class window1:
    def __init__(self,master):
        self.master = master
        self.master.title('Login System')
        self.master.geometry('1350x900+0+0')

        # Background
        self.bg_icons = ImageTk.PhotoImage(file = 'Screen.jpg') # Ganti dengan foto yang ada di browser kalian, foto dan file ini harus dalam folder yg sama

        # Label
        self.bg_lbl = Label(self.master, image=self.bg_icons)
        self.bg_lbl.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.title = Label(self.master, text='Selamat Datang DI Cafe Murah Meriah', font=(font, 40, 'bold'), bg=bg_color3, fg='white', bd=10,
                      relief=GROOVE)
        self.title.place(x=0, y=0, relwidth=1)

        # Login Frame
        self.login_frame = Frame(self.master, bg= bg_color3, relief = RIDGE, bd = 10)
        self.login_frame.place(x=0, y=120, width = 800, height = 190)

        self.Login_title1 = Label(self.login_frame, text='Silahkan Login Menggunakan ID Member Yang Sudah Terdaftar',
                       font=(font, 18, 'bold'), bg= 'white', fg = fg_color, relief = GROOVE, bd = 5)
        self.Login_title1.place(x=0, y=0, relwidth=1)

        self.Login_title2 = Label(self.login_frame, bg= bg_color, fg = fg_color, relief = GROOVE, bd = 5)
        self.Login_title2.place(x=0, y=48, relwidth=1, height = 123)

        # Label & Entry
        self.label_user = Label(self.Login_title2, text='Username', font=(font, 18,'bold'), bg=bg_color, fg='black')
        self.label_user.place(x = 150, y = 10)

        self.label_pass = Label(self.Login_title2, text='Password', font=(font, 18,'bold'), bg=bg_color, fg='black')
        self.label_pass.place(x = 150, y = 60)

        self.txt_userLog = Entry(self.Login_title2,font=(font, 16,'bold'), bg= 'white', fg='black', relief = RIDGE, bd = 5,
                                 textvariable = self.Username)
        self.txt_userLog.place(x = 350, y = 10)

        self.txt_passLog = Entry(self.Login_title2, font=(font, 16, 'bold'), bg='white', fg='black', relief=RIDGE, bd=5, show = '*',
                                 textvariable = self.Password)
        self.txt_passLog.place(x=350, y=60)

        # Tombol Frame
        self.btn_frame = Frame(self.master, bg=bg_color3, relief=RIDGE, bd=10)
        self.btn_frame.place(x=0, y=320, width=800, height=130)

        self.btn_frame1 = Label(self.btn_frame, bg=bg_color, fg=fg_color, relief=GROOVE, bd=5)
        self.btn_frame1.place(x=0, y=0, relwidth=1, height=110)

        # Tombol Login Frame
        self.btn_Login = Button(self.btn_frame1, bg = bg_color2, fg = fg_color, relief = RIDGE, bd = 10, text = 'Login', font=(font, 20, 'bold'),
                                command = self.login_system)
        self.btn_Login.place(x=15, y= 15, width = 200)

        self.btn_Reset = Button(self.btn_frame1,bg = bg_color2, fg = fg_color, relief = RIDGE, bd = 10, text = 'Reset', font=(font, 20, 'bold'),
                                command = self.reset)
        self.btn_Reset.place(x=285, y= 15, width = 200 )

        self.btn_Exit = Button(self.btn_frame1, bg=bg_color2, fg=fg_color, relief=RIDGE, bd=10, text='Exit', font=(font, 20, 'bold'),
                               command = self.exit)
        self.btn_Exit.place(x=550, y=15, width=200)

        # Frame Register
        self.Reg_frame = Frame(self.master, bg=bg_color3, relief=RIDGE, bd=10)
        self.Reg_frame.place(x=810, y=120, width=540, height=485)

        self.Reg_frame1 = Label(self.Reg_frame, bg=bg_color, fg=fg_color, relief=GROOVE, bd=5)
        self.Reg_frame1.place(x=0, y=0, relwidth=1, height=465)

        # Frame title
        self.Reg_title = Label(self.Reg_frame1, text='Daftar ID Member',
                             font=(font, 18, 'bold'), bg='white', fg=fg_color, relief=GROOVE, bd=5)
        self.Reg_title.place(x=0, y=0, relwidth=1)

        # Register Email & Entry
        self.Reg_email = Label(self.Reg_frame1, text = 'Email', font=(font, 14,'bold'), bg=bg_color, fg='black')
        self.Reg_email.place(x = 20, y = 80)

        self.txt_email = Entry(self.Reg_frame1, font=(font, 10, 'bold'), bg='white', fg='black', relief=RIDGE, bd=5)
        self.txt_email.place(x=195, y=80, width = 280)

        # Register Password & Entry
        self.Reg_gender = Label(self.Reg_frame1, text='Jenis Kelamin', font=(font, 14, 'bold'), bg=bg_color, fg='black')
        self.Reg_gender.place(x=20, y=130)

        self.txt_gender = ttk.Combobox(self.Reg_frame1, font=(font, 12, 'bold'), state = 'readonly')
        self.txt_gender['value'] = ('Laki-Laki', 'Perempuan')
        self.txt_gender.place(x=195, y=130, width=280)

        # Register Username & Entry
        self.Reg_username = Label(self.Reg_frame1, text='Username', font=(font, 14, 'bold'), bg=bg_color, fg='black')
        self.Reg_username.place(x=20, y=180)

        self.txt_userReg = Entry(self.Reg_frame1, font=(font, 10, 'bold'), bg='white', fg='black', relief=RIDGE, bd=5)
        self.txt_userReg.place(x=195, y=180, width=280)

        # Register Password & Entry
        self.Reg_password = Label(self.Reg_frame1, text='Password', font=(font, 14, 'bold'), bg=bg_color, fg='black')
        self.Reg_password.place(x=20, y=230)

        self.txt_passReg = Entry(self.Reg_frame1, font=(font, 16, 'bold'), bg='white', fg='black', relief=RIDGE, bd=5, show ='*')
        self.txt_passReg.place(x=195, y=230, width=280, height = 32)

        # Variable Member status
        self.member_biasa = IntVar()
        self.member_vip = IntVar()
        self.member_vvip = IntVar()

        self.sendirian = IntVar()
        self.berdua = IntVar()
        self.grup = IntVar()
        self.Reg_gender = IntVar()

        self.Reg_username = StringVar()
        self.Reg_password = StringVar()
        self.Reg_email = StringVar()

        # Register Member Reguler
        self.Member_reguler = Checkbutton(self.Reg_frame1,variable = self.member_biasa, onvalue = 1, offvalue = 0, bg = bg_color, fg = fg_color)
        self.Member_reguler.place(x = 30, y = 310, height = 30, width = 45)

        self.txt_reguler = Label(self.Reg_frame1, text='Member Biasa', font=(font, 14, 'bold'), bg=bg_color, fg='black')
        self.txt_reguler.place(x=90, y=310)

        # Register Member VIP
        self.Member_VIP = Checkbutton(self.Reg_frame1, variable=self.member_vip, onvalue=1, offvalue=0, bg=bg_color, fg=fg_color)
        self.Member_VIP.place(x=30, y=360, height=30, width=45)

        self.txt_VIP = Label(self.Reg_frame1, text='Member VIP', font=(font, 14, 'bold'), bg=bg_color, fg='black')
        self.txt_VIP.place(x=90, y=360)

        # Register Member VVIP
        self.Member_VVIP = Checkbutton(self.Reg_frame1, variable=self.member_vvip, onvalue=1, offvalue=0, bg=bg_color, fg=fg_color)
        self.Member_VVIP.place(x=30, y= 410, height=30, width=45)

        self.txt_VVIP = Label(self.Reg_frame1, text='Member VVIP', font=(font, 14, 'bold'), bg=bg_color, fg='black')
        self.txt_VVIP.place(x=90, y=410)

        # Register Member Sendirian
        self.Member_Sendirian = Checkbutton(self.Reg_frame1, variable=self.sendirian, onvalue=1, offvalue=0, bg=bg_color, fg=fg_color)
        self.Member_Sendirian.place(x=300, y=310, height=30, width=45)

        self.txt_Sendirian = Label(self.Reg_frame1, text='Sendirian', font=(font, 14, 'bold'), bg=bg_color, fg='black')
        self.txt_Sendirian.place(x=350, y=310)

        # Register Member Berdua
        self.Member_Bedua = Checkbutton(self.Reg_frame1, variable=self.berdua, onvalue=1, offvalue=0, bg=bg_color, fg=fg_color)
        self.Member_Bedua.place(x=300, y=360, height=30, width=45)

        self.txt_Bedua = Label(self.Reg_frame1, text='Berdua', font=(font, 14, 'bold'), bg=bg_color, fg='black')
        self.txt_Bedua.place(x=350, y=360)

        # Register Member Grup
        self.Member_Grup = Checkbutton(self.Reg_frame1, variable=self.grup, onvalue=1, offvalue=0, bg=bg_color, fg=fg_color)
        self.Member_Grup.place(x=300, y=410, height=30, width=45)

        self.txt_Grup = Label(self.Reg_frame1, text='Grup', font=(font, 14, 'bold'), bg=bg_color, fg='black')
        self.txt_Grup.place(x=350, y=410)

        # Frame tombol register
        self.btn_Reg_frame = Label(self.master,bg=bg_color3, fg=fg_color, relief=RIDGE, bd=10)
        self.btn_Reg_frame.place(x=810, y=610, width=540, height=100)

        self.btn_Reg_frame1 = Label(self.btn_Reg_frame, bg=bg_color, fg=fg_color, relief=RIDGE, bd=5)
        self.btn_Reg_frame1.place(x=0, y=0, relwidth =1, height=80)

        # Tombol Register
        self.btn_Reg = Button(self.btn_Reg_frame1, bg=bg_color2, fg=fg_color, relief=RIDGE, bd=10, text='Register',
                           font=(font, 15, 'bold'), command = self.regis)
        self.btn_Reg.place(x=160, y=6, width=200)

    # Definisi tombol
    def login_system(self):
        username = (self.Username.get())
        password = (self.Password.get())
        reg_username = (self.txt_userReg.get())
        reg_password = (self.txt_passReg.get())
        if (username == str(reg_username) and password == str(reg_password)):
            tkinter.messagebox.showinfo('Login','Login Success !!')
            self.newWindow = Toplevel(self.master)
            self.app = window2(self.newWindow)
        else:
            tkinter.messagebox.askyesno('Error','Member ID Tidak Terdaftar !!')
            self.Username.set("")
            self.Password.set("")

    def regis(self):
        reg_username = (self.txt_userReg.get())
        reg_password = (self.txt_passReg.get())
        reg_email = (self.txt_email.get())
        reg_gender = (self.txt_gender.get())

        if (reg_username == str(self.txt_userReg) and reg_password == str(self.txt_passReg)
                and reg_email == str(self.txt_email) and reg_gender == str(self.txt_gender)
                or self.Member_reguler or self.Member_VIP or self.Member_VVIP or self.Member_Sendirian
                or self. Member_Bedua or self.Member_Grup):
            tkinter.messagebox.showinfo('Register','Berhasil Menjadi Member')

        else:
            tkinter.messagebox.askyesno('Invalid','Kolom Tidak Boleh Kosong !')
            self.txt_userReg.delete(0, END)
            self.txt_passReg.delete(0, END)
            self.txt_email.delete(0, END)
            self.txt_gender.set('')

            self.member_biasa.set(0)
            self.member_vip.set(0)
            self.member_vvip.set(0)
            self.sendirian.set(0)
            self.berdua.set(0)
            self.grup.set(0)

    def exit(self):
        self.exit = tkinter.messagebox.askyesno('Exit', 'Konfirmasi Exit')
        if self.exit > 0:
            self.master.destroy()
        else:
            command = self.new_window()
            return

    def reset(self):
        self.txt_userLog.delete('0', END)
        self.txt_passLog.delete('0', END)
        self.txt_userReg.delete('0', END)
        self.txt_passReg.delete('0', END)
        self.txt_email.delete('0', END)
        self.txt_gender.set('')

        self.member_biasa.set(0)
        self.member_vip.set(0)
        self.member_vvip.set(0)
        self.sendirian.set(0)
        self.berdua.set(0)
        self.grup.set(0)

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = window2(self.newWindow)

class window2:
    def __init__(self, master):
        self.master1 = master
        self.master1.title('Daftar Menu Cafe Murah Meriah')
        self.master1.geometry('1360x750+0+0')

        # Background
        self.bg_icons1 = ImageTk.PhotoImage(file='Screen.jpg')

        # Label
        self.bg_lbl = Label(self.master1, image=self.bg_icons1)
        self.bg_lbl.pack()

        # Frame Atas
        self.title = Label(self.master1, text='Selamat Datang DI Cafe Murah Meriah', font=(font, 40, 'bold'), bg=bg_color3, fg='white', bd=10,
                           relief=GROOVE)
        self.title.place(x=0, y=0, relwidth=1)

        # Frame 2 bagian kiri
        # Frame Menu
        self.MenuFrame = Frame(self.master1, bg=bg_color1, bd=10, relief=RIDGE)
        self.MenuFrame.place(y=115, x=1, width=905, height=434)

        # Frame untuk minuman
        self.Drinks_F = Frame(self.MenuFrame, bg=bg_color, bd=8, relief=RIDGE)
        self.Drinks_F.place(y=0, x=0, width=380, height=414)

        # Frame untuk makanan
        self.Cake_F = Frame(self.MenuFrame, bg=bg_color, bd=8, relief=RIDGE)
        self.Cake_F.place(y=0, x=385, width=350, height=414)

        # Frame Text Menu
        self.Menu_F = Frame(self.MenuFrame, bg = bg_color, bd = 8, relief = RIDGE)
        self.Menu_F.place(y = 0, x = 740, width = 145, height = 414)

        # Text Menu
        self.l_Menu = Label(self.Menu_F, text = 'M E N U', font = (font, 18, 'bold'), bg = bg_color, fg = fg_color)
        self.l_Menu.place(relwidth = 1, relheight = 1)

        # Variable Minuman
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()
        self.var7 = IntVar()
        self.var8 = IntVar()

        # Variable Makanan
        self.var9 = IntVar()
        self.var10 = IntVar()
        self.var11 = IntVar()
        self.var12 = IntVar()
        self.var13 = IntVar()
        self.var14 = IntVar()
        self.var15 = IntVar()
        self.var16 = IntVar()

        # Variable pembayaran
        self.Tanggal_Order = StringVar()
        self.Nomor_ID = StringVar()
        self.Ongkir = StringVar()
        self.Sub_Total = StringVar()
        self.Total_Pembayaran = StringVar()
        self.Harga_Makanan = StringVar()
        self.Harga_Minuman = StringVar()
        self.Service_Charge = StringVar()

        self.text_Input = StringVar()
        self.operator = ''

        self.E_Kopi_Latte = StringVar()
        self.E_Kopi_Espresso = StringVar()
        self.E_Extra_Joss_Susu = StringVar()
        self.E_Kopi_Susu = StringVar()
        self.E_Cappuccino = StringVar()
        self.E_African_Coffee = StringVar()
        self.E_American_Coffee = StringVar()
        self.E_Es_Cappuccino = StringVar()

        self.E_Ayam_Geprek = StringVar()
        self.E_Ayam_Bakar = StringVar()
        self.E_Lalapan = StringVar()
        self.E_Nasgor_Spesial = StringVar()
        self.E_Pisang_Keju = StringVar()
        self.E_Hamburger = StringVar()
        self.E_Gorengan = StringVar()
        self.E_Mie_Instan = StringVar()

        self.E_Kopi_Latte.set('0')
        self.E_Kopi_Espresso.set('0')
        self.E_Extra_Joss_Susu.set('0')
        self.E_Kopi_Susu.set('0')
        self.E_Cappuccino.set('0')
        self.E_African_Coffee.set('0')
        self.E_American_Coffee.set('0')
        self.E_Es_Cappuccino.set('0')

        self.E_Ayam_Geprek.set('0')
        self.E_Ayam_Bakar.set('0')
        self.E_Lalapan.set('0')
        self.E_Nasgor_Spesial.set('0')
        self.E_Pisang_Keju.set('0')
        self.E_Hamburger.set('0')
        self.E_Gorengan.set('0')
        self.E_Mie_Instan.set('0')

        self.Tanggal_Order.set(time.strftime('%A, %d %B %Y'))

        # Check Tombol untuk minuman
        self.Kopi_Latte = Checkbutton(self.Drinks_F, variable=self.var1, onvalue=1, offvalue=0, bg=bg_color, fg=fg_color,
                                      command = self.Check_Kopi_Latte).place(x=1, y=7, height=30, width=45)

        self.Kopi_Espresso = Checkbutton(self.Drinks_F, variable=self.var2, onvalue=1, offvalue=0, bg=bg_color, fg=fg_color ,
                                         command = self.Check_Kopi_Espresso).place(x=1, y=56, height=30, width=45)

        self.Extra_Joss_Susu = Checkbutton(self.Drinks_F, variable=self.var3, onvalue=1, offvalue=0, bg=bg_color, fg=fg_color,
                                           command = self.Check_Extra_Joss_Susu).place(x=1, y=106, height=30, width=45)

        self.Kopi_Susu = Checkbutton(self.Drinks_F, variable=self.var4, onvalue=1, offvalue=0, bg=bg_color, fg=fg_color,
                                     command = self.Check_Kopi_Susu).place(x=1, y=156, height=30, width=45)

        self.Cappuccino = Checkbutton(self.Drinks_F, variable=self.var5, onvalue=1, offvalue=0, bg=bg_color, fg=fg_color,
                                      command = self.Check_Cappuccino).place(x=1, y=206, height=30, width=45)

        self.African_Coffee = Checkbutton(self.Drinks_F, variable=self.var6, onvalue=1, offvalue=0, bg=bg_color, fg=fg_color,
                                          command = self.Check_African_Coffee).place(x=1, y=256, height=30, width=45)

        self.American_Coffee = Checkbutton(self.Drinks_F, variable=self.var7, onvalue=1, offvalue=0, bg=bg_color, fg=fg_color,
                                           command = self.Check_American_Coffee).place(x=1, y=306, height=30, width=45)

        self.Es_Cappuccino = Checkbutton(self.Drinks_F, variable=self.var8, onvalue=1, offvalue=0, bg=bg_color, fg=fg_color,
                                         command = self.Check_Es_Cappuccino).place(x=1, y=356, height=30, width=45)

        # Text Minuman
        self.l_Kopi_Latte = Label(self.Drinks_F, text='Kopi Latte', font=(font, 18,), bg=bg_color, fg=fg_color)\
            .place(x=50, y=5)
        self.l_Kopi_Espresso = Label(self.Drinks_F, text='Kopi Espresso', font=(font, 18,), bg=bg_color, fg=fg_color)\
            .place(x=50, y=55)
        self.l_Extra_Joss_Susu = Label(self.Drinks_F, text='Extra Joss Susu', font=(font, 18,), bg=bg_color, fg=fg_color)\
            .place(x=50,y=105)
        self.l_Kopi_Susu = Label(self.Drinks_F, text='Kopi Susu', font=(font, 18,), bg=bg_color, fg=fg_color)\
            .place(x=50, y=155)
        self.l_Cappuccino = Label(self.Drinks_F, text='Cappuccino', font=(font, 18,), bg=bg_color, fg=fg_color)\
            .place(x=50, y=205)
        self.l_African_Coffee = Label(self.Drinks_F, text='African Coffee', font=(font, 18,), bg=bg_color, fg=fg_color)\
            .place(x=50,y=255)
        self.l_American_Coffee = Label(self.Drinks_F, text='American Coffee', font=(font, 18,), bg=bg_color, fg=fg_color)\
            .place(x=50, y=305)
        self.l_Es_Cappuccino = Label(self.Drinks_F, text='Es Cappuccino', font=(font, 18,), bg=bg_color, fg=fg_color)\
            .place(x=50,y=355)

        # Entry untuk minuman
        self.txt_Kopi_Latte = Entry(self.Drinks_F, font=(font, 12), bd=2, width=7, state=DISABLED,
                                    textvariable=self.E_Kopi_Latte, bg='white',fg=fg_color)
        self.txt_Kopi_Latte.place(x=280, y=8)

        self.txt_Kopi_Espresso = Entry(self.Drinks_F, font=(font, 12), bd=2, width=7, state=DISABLED,
                                       textvariable=self.E_Kopi_Espresso,bg='white', fg=fg_color)
        self.txt_Kopi_Espresso.place(x=280, y=57)

        self.txt_Extra_Joss_Susu = Entry(self.Drinks_F, font=(font, 12), bd=2, width=7, state=DISABLED,
                                         textvariable=self.E_Extra_Joss_Susu,bg='white', fg=fg_color)
        self.txt_Extra_Joss_Susu.place(x=280, y=107)

        self.txt_Kopi_Susu = Entry(self.Drinks_F, font=(font, 12), bd=2, width=7, state=DISABLED,
                                   textvariable=self.E_Kopi_Susu,bg='white', fg=fg_color)
        self.txt_Kopi_Susu.place(x=280, y=157)

        self.txt_Cappuccino = Entry(self.Drinks_F, font=(font, 12), bd=2, width=7, state=DISABLED,
                                    textvariable=self.E_Cappuccino,bg='white', fg=fg_color)
        self.txt_Cappuccino.place(x=280, y=207)

        self.txt_African_Coffee = Entry(self.Drinks_F, font=(font, 12), bd=2, width=7, state=DISABLED,
                                   textvariable=self.E_African_Coffee, bg='white', fg=fg_color)
        self.txt_African_Coffee.place(x=280, y=257)

        self.txt_American_Coffee = Entry(self.Drinks_F, font=(font, 12), bd=2, width=7, state=DISABLED,
                                    textvariable=self.E_American_Coffee, bg='white', fg=fg_color)
        self.txt_American_Coffee.place(x=280, y=307)

        self.txt_Es_Cappuccino = Entry(self.Drinks_F, font=(font, 12), bd=2, width=7, state=DISABLED,
                                    textvariable=self.E_Es_Cappuccino, bg='white', fg=fg_color)
        self.txt_Es_Cappuccino.place(x=280, y=357)

        # Check Tombol untuk makanan
        self.Ayam_Geprek = Checkbutton(self.Cake_F, variable=self.var9, onvalue=1, offvalue=0, bg=bg_color, fg=fg_color,
                                       command = self.Check_Ayam_Geprek).place(x=1, y=7, height=30, width=45)
        self.Ayam_Bakar = Checkbutton(self.Cake_F, variable=self.var10, onvalue=1, offvalue=0, bg=bg_color, fg=fg_color,
                                      command = self.Check_Ayam_Bakar).place(x=1, y=56, height=30, width=45)
        self.Lalapan = Checkbutton(self.Cake_F, variable=self.var11, onvalue=1, offvalue=0, bg=bg_color, fg=fg_color,
                                   command = self.Check_Lalapan).place(x=1, y=106, height=30, width=45)
        self.Nasgor_Spesial = Checkbutton(self.Cake_F, variable=self.var12, onvalue=1, offvalue=0, bg=bg_color, fg=fg_color,
                                          command = self.Check_Nasgor_Spesial).place(x=1, y=156, height=30, width=45)
        self.Pisang_Keju = Checkbutton(self.Cake_F, variable=self.var13, onvalue=1, offvalue=0, bg=bg_color, fg=fg_color,
                                       command = self.Check_Pisang_Keju).place(x=1, y=206, height=30, width=45)
        self.Hamburger = Checkbutton(self.Cake_F, variable=self.var14, onvalue=1, offvalue=0, bg=bg_color, fg=fg_color,
                                     command = self.Check_Hamburger).place(x=1, y=256, height=30,width=45)
        self.Gorengan = Checkbutton(self.Cake_F, variable=self.var15, onvalue=1, offvalue=0, bg=bg_color, fg=fg_color,
                                    command = self.Check_Gorengan).place(x=1, y=306,height=30, width=45)
        self.Mie_Instan = Checkbutton(self.Cake_F, variable=self.var16, onvalue=1, offvalue=0, bg=bg_color, fg=fg_color,
                                      command = self.Check_Mie_Instan).place(x=1, y=356, height=30,width=45)

        # Text Makanan
        self.l_Ayam_Geprek = Label(self.Cake_F, text='Ayam Geprek', font=(font, 18,), bg=bg_color, fg=fg_color)\
            .place(x=50, y=5)
        self.l_Ayam_Bakar = Label(self.Cake_F, text='Ayam Bakar', font=(font, 18,), bg=bg_color, fg=fg_color)\
            .place(x=50, y=55)
        self.l_Lalapan = Label(self.Cake_F, text='Lalapan', font=(font, 18,), bg=bg_color, fg=fg_color)\
            .place(x=50, y=105)
        self.l_Nasgor_Spesial = Label(self.Cake_F, text='NasGor Spesial', font=(font, 18,), bg=bg_color, fg=fg_color)\
            .place(x=50,y=155)
        self.l_Pisang_Keju = Label(self.Cake_F, text='Pisang Keju', font=(font, 18,), bg=bg_color, fg=fg_color)\
            .place(x=50,y=205)
        self.l_Hamburger = Label(self.Cake_F, text='Hamburger', font=(font, 18,), bg=bg_color, fg=fg_color)\
            .place(x=50,y=255)
        self.l_Gorengan = Label(self.Cake_F, text='Gorengan', font=(font, 18,), bg=bg_color, fg=fg_color)\
            .place(x=50, y=305)
        self.l_Mie_Instan = Label(self.Cake_F, text='Mie Instan', font=(font, 18,), bg=bg_color, fg=fg_color)\
            .place(x=50, y=355)

        # Entry untuk makanan
        self.txt_Ayam_Geprek = Entry(self.Cake_F, font=(font, 12), bd=2, width=7, state=DISABLED,
                                     textvariable=self.E_Ayam_Geprek,bg='white', fg=fg_color)
        self.txt_Ayam_Geprek.place(x=250, y=8)

        self.txt_Ayam_Bakar = Entry(self.Cake_F, font=(font, 12), bd=2, width=7, state=DISABLED,
                                    textvariable=self.E_Ayam_Bakar,bg='white', fg=fg_color)
        self.txt_Ayam_Bakar.place(x=250, y=57)

        self.txt_Lalapan = Entry(self.Cake_F, font=(font, 12), bd=2, width=7, state=DISABLED,
                                 textvariable=self.E_Lalapan, bg='white', fg=fg_color)
        self.txt_Lalapan.place(x=250, y=107)

        self.txt_Nasgor_Spesial = Entry(self.Cake_F, font=(font, 12), bd=2, width=7, state=DISABLED,
                                        textvariable=self.E_Nasgor_Spesial, bg='white', fg=fg_color)
        self.txt_Nasgor_Spesial.place(x=250, y=157)

        self.txt_Pisang_Keju = Entry(self.Cake_F, font=(font, 12), bd=2, width=7, state=DISABLED,
                                     textvariable=self.E_Pisang_Keju, bg='white', fg=fg_color)
        self.txt_Pisang_Keju.place(x=250, y=207)

        self.txt_Hamburger = Entry(self.Cake_F, font=(font, 12), bd=2, width=7, state=DISABLED,
                                   textvariable=self.E_Hamburger, bg='white', fg=fg_color)
        self.txt_Hamburger.place(x=250, y=257)

        self.txt_Gorengan = Entry(self.Cake_F, font=(font, 12), bd=2, width=7, state=DISABLED,
                                  textvariable=self.E_Gorengan, bg='white', fg=fg_color)
        self.txt_Gorengan.place(x=250, y=307)

        self.txt_Mie_Instan = Entry(self.Cake_F, font=(font, 12), bd=2, width=7, state=DISABLED,
                                    textvariable=self.E_Mie_Instan, bg='white', fg=fg_color)
        self.txt_Mie_Instan.place(x=250, y=357)

        # Frame untuk pembayaran
        self.Cost_F = Frame(self.master1, bg=bg_color, bd=10, relief=RIDGE)
        self.Cost_F.place(y=553, x=1, width=905, height=163)

        # Frame ke 2 untuk pembayaran
        self.Cost_F1 = Frame(self.Cost_F, bg=bg_color, bd=8, relief=RIDGE)
        self.Cost_F1.place(y=0, x=0, width=885, height=143)

        # Frame pembayaran untuk minuman
        self.lbl_Harga_Minuman = Label(self.Cost_F1, font=(font, 14,), text='Harga Minuman', bg=bg_color, fg=fg_color)
        self.lbl_Harga_Minuman.place(x=7, y=7)

        self.lbl_Harga_Makanan = Label(self.Cost_F1, font=(font, 14,), text='Harga Makanan', bg=bg_color, fg=fg_color)
        self.lbl_Harga_Makanan.place(x=7, y=53)

        self.lbl_service_charge = Label(self.Cost_F1, font=(font, 14,), text='Service Charge', bg=bg_color, fg=fg_color)
        self.lbl_service_charge.place(x=7, y=95)

        self.lbl_Ongkir = Label(self.Cost_F1, font=(font, 14,), text='Ongkos Kirim', bg=bg_color, fg=fg_color)
        self.lbl_Ongkir.place(x=460, y=7)

        self.lbl_Sub_Total = Label(self.Cost_F1, font=(font, 14,), text='Biaya Admin', bg=bg_color, fg=fg_color)
        self.lbl_Sub_Total.place(x=460, y=53)

        self.lbl_Total_Pembayaran = Label(self.Cost_F1, font=(font, 14,), text='Total Bayar', bg=bg_color, fg=fg_color)
        self.lbl_Total_Pembayaran.place(x=460, y=95)

        # Entry untuk Pembayaran
        self.txt_Harga_Minuman = Entry(self.Cost_F1, font=('DS-Digital', 16, 'bold'), bd=5, bg='white', fg=fg_color,
                                   justify=RIGHT, textvariable = self.Harga_Minuman)
        self.txt_Harga_Minuman.place(y=8, x=200, width=215, height=33)
        self.txt_Harga_Minuman.insert(0, '0')

        self.txt_Harga_Makanan = Entry(self.Cost_F1, font=('DS-Digital', 16, 'bold'), bd=5, bg='white', fg=fg_color, justify=RIGHT,
                                 textvariable=self.Harga_Makanan)
        self.txt_Harga_Makanan.place(y=50, x=200, width=215, height=33)
        self.txt_Harga_Makanan.insert(0, '0')

        self.txt_Service_Charge = Entry(self.Cost_F1, font=('DS-Digital', 16, 'bold'), bd=5, bg='white', fg=fg_color,
                                   justify=RIGHT, textvariable=self.Service_Charge)
        self.txt_Service_Charge.place(y=90, x=200, width=215, height=33)
        self.txt_Service_Charge.insert(0, '0')

        self.txt_Ongkir = Entry(self.Cost_F1, font=('DS-Digital', 16, 'bold'), bd=5, bg='white', fg=fg_color, justify=RIGHT,
                             textvariable=self.Ongkir)
        self.txt_Ongkir.place(y=8, x=652, width=215, height=33)
        self.txt_Ongkir.insert(0, '0')

        self.txt_Sub_Total = Entry(self.Cost_F1, font=('DS-Digital', 16, 'bold'), bd=5, bg='white', fg=fg_color, justify=RIGHT,
                              textvariable=self.Sub_Total)
        self.txt_Sub_Total.place(y=50, x=652, width=215, height=33)
        self.txt_Sub_Total.insert(0, '0')

        self.txt_Total_Pembayaran = Entry(self.Cost_F1, font=('DS-Digital', 16, 'bold'), bd=5, bg='white', fg=fg_color, justify=RIGHT,
                               textvariable=self.Total_Pembayaran)
        self.txt_Total_Pembayaran.place(y=90, x=652, width=215, height=33)
        self.txt_Total_Pembayaran.insert(0, '0')

        # Frame Kanan
        self.ReceiptCal_F = Frame(self.master1, bg=bg_color, bd=10, relief=RIDGE)
        self.ReceiptCal_F.place(y=115, x=913, width=454, height=600)

        # Frame Resep di Frame Kanan
        self.Print_F = Frame(self.ReceiptCal_F, bg='#BC9A0E', bd=8, relief=RIDGE)
        self.Print_F.place(y=265, x=0, width=433, height=210)

        # Tampilan Text di Frame Resep
        self.txt_Print = Text(self.Print_F, bg='white', fg=fg_color, bd=5, font=(font, 12, 'bold'))  # , state = 'readonly')
        self.txt_Print.place(y=0, x=0, width=417, height=194)

        # Frame Tombol Menu di Frame Kanan
        self.Buttons_F = Frame(self.ReceiptCal_F, bg='#BC9A0E', bd=5, relief=RIDGE)
        self.Buttons_F.place(y=475, x=0, width=433, height=105)

        # Tombol di Frame Tombol
        self.btn_Total = Button(self.Buttons_F, padx=75, pady=8, bd=5, fg=fg_color, font=('DejaVu Math TeX Gyre', 12, 'bold'),
                           text='TOTAL', bg='#8AE234', width=4, command = self.Total_Item)
        self.btn_Total.place(y=0, x=0)

        self.btn_Resep = Button(self.Buttons_F, padx=75, pady=8, bd=5, fg=fg_color, font=('DejaVu Math TeX Gyre', 12, 'bold'),
                           text='PRINT', bg='#8AE234', width=4, command = self.Print)
        self.btn_Resep.place(y=48, x=0)

        self.btn_Reset = Button(self.Buttons_F, padx=75, pady=8, bd=5, fg=fg_color, font=('DejaVu Math TeX Gyre', 12, 'bold'),
                           text='RESET', bg='#8AE234', width=4, command =self.reset)
        self.btn_Reset.place(y=0, x=215)

        self.btn_Exit = Button(self.Buttons_F, padx=75, pady=8, bd=5, fg=fg_color, font=('DejaVu Math TeX Gyre', 12, 'bold'),
                          text='EXIT', bg='#8AE234', width=4, command =self.iExit)
        self.btn_Exit.place(y=48, x=215)

        # Frame Kalkulator di Frame Kanan
        self.Cal_F = Frame(self.ReceiptCal_F, bg='#204A87', bd=8, relief=RIDGE)
        self.Cal_F.place(y=0, x=0, width=433, height=260)

        # Kalkulator Display
        self.txt_Display = Entry(self.Cal_F, bg='white', fg=fg_color, bd=5, font=('DS-Digital', 30, 'bold'), justify=RIGHT,
                            textvariable=self.text_Input, state = 'readonly')  # , state = 'readonly')
        self.txt_Display.place(y=0, x=0, width=417, height=45)
        self.txt_Display.insert(0, '0')

        # Kalkulator Tombol 1 - =
        self.btn1 = Button(self.Cal_F, padx=10, pady=1, fg=fg_color, width=3, text='1',
                      bg='#888A85', font=('URW Gothic L, Demi', 20, 'bold',), bd=5, command = lambda :self.btn_Click('1'))
        self.btn1.place(y=46, x=0)

        self.btn4 = Button(self.Cal_F, padx=10, pady=1, fg=fg_color, width=3, text='4',
                      bg='#888A85', font=('URW Gothic L, Demi', 20, 'bold'), bd=5, command = lambda :self.btn_Click('4'))
        self.btn4.place(y=96, x=0)

        self.btn7 = Button(self.Cal_F, padx=10, pady=1, fg=fg_color, width=3, text='7',
                      bg='#888A85', font=('URW Gothic L, Demi', 20, 'bold'), bd=5, command = lambda :self.btn_Click('7'))
        self.btn7.place(y=146, x=0)

        self.btnEq = Button(self.Cal_F, padx=10, pady=1, fg=fg_color, width=3, text='=',
                       bg='#888A85', font=('URW Gothic L, Demi', 20, 'bold'), bd=5, command = lambda :self.btn_Equals())
        self.btnEq.place(y=196, x=0)

        # Kalkulator Tombol 2 - 0
        self.btn2 = Button(self.Cal_F, padx=10, pady=1, fg=fg_color, width=3, text='2',
                      bg='#888A85', font=('URW Gothic L, Demi', 20, 'bold'), bd=5, command = lambda :self.btn_Click('2'))
        self.btn2.place(y=46, x=108)

        self.btn5 = Button(self.Cal_F, padx=10, pady=1, fg=fg_color, width=3, text='5',
                      bg='#888A85', font=('URW Gothic L, Demi', 20, 'bold'), bd=5, command = lambda :self.btn_Click('5'))
        self.btn5.place(y=96, x=108)

        self.btn8 = Button(self.Cal_F, padx=10, pady=1, fg=fg_color, width=3, text='8',
                      bg='#888A85', font=('URW Gothic L, Demi', 20, 'bold'), bd=5, command = lambda :self.btn_Click('8'))
        self.btn8.place(y=146, x=108)

        self.btn0 = Button(self.Cal_F, padx=10, pady=1, fg=fg_color, width=3, text='0',
                      bg='#888A85', font=('URW Gothic L, Demi', 20, 'bold'), bd=5, command = lambda :self.btn_Click('0'))
        self.btn0.place(y=196, x=108)

        # Kalkulator Tombol 3 - C
        self.btn3 = Button(self.Cal_F, padx=10, pady=1, fg=fg_color, width=3, text='3',
                      bg='#888A85', font=('URW Gothic L, Demi', 20, 'bold'), bd=5, command = lambda :self.btn_Click('3'))
        self.btn3.place(y=46, x=217)

        self.btn6 = Button(self.Cal_F, padx=10, pady=1, fg=fg_color, width=3, text='6',
                      bg='#888A85', font=('URW Gothic L, Demi', 20, 'bold'), bd=5, command = lambda :self.btn_Click('6'))
        self.btn6.place(y=96, x=217)

        self.btn9 = Button(self.Cal_F, padx=10, pady=1, fg=fg_color, width=3, text='9',
                      bg='#888A85', font=('URW Gothic L, Demi', 20, 'bold'), bd=5, command = lambda :self.btn_Click('9'))
        self.btn9.place(y=146, x=217)

        self.btnC = Button(self.Cal_F, padx=10, pady=1, fg=fg_color, width=3, text='C',
                      bg='#888A85', font=('URW Gothic L, Demi', 20, 'bold'), bd=5, command = lambda :self.btn_Clear())
        self.btnC.place(y=196, x=217)

        # Kalkulator Tombol + - /
        self.btnTambah = Button(self.Cal_F, padx=10, pady=1, fg=fg_color, width=3, text='+',
                           bg='#888A85', font=('URW Gothic L, Demi', 20, 'bold'), bd=5, command = lambda :self.btn_Click('+'))
        self.btnTambah.place(y=46, x=325)

        self.btnKurang = Button(self.Cal_F, padx=10, pady=1, fg=fg_color, width=3, text='-',
                           bg='#888A85', font=('URW Gothic L, Demi', 20, 'bold'), bd=5, command = lambda :self.btn_Click('-'))
        self.btnKurang.place(y=96, x=325)

        self.btnKali = Button(self.Cal_F, padx=10, pady=1, fg=fg_color, width=3, text='*',
                         bg='#888A85', font=('URW Gothic L, Demi', 20, 'bold'), bd=5, command = lambda :self.btn_Click('*'))
        self.btnKali.place(y=146, x=325)

        self.btnBagi = Button(self.Cal_F, padx=10, pady=1, fg=fg_color, width=3, text='/',
                         bg='#888A85', font=('URW Gothic L, Demi', 20, 'bold'), bd=5, command = lambda :self.btn_Click('/'))
        self.btnBagi.place(y=196, x=325)

    def btn_Click(self,numbers):
        global operator
        self.operator = self.operator + str(numbers)
        self.text_Input.set(self.operator)

    def btn_Clear(self):
        global operator
        self.operator = ''
        self.text_Input.set('')

    def btn_Equals(self):
        global operator
        self.sumup = str(eval(self.operator))
        self.text_Input.set(self.sumup)
        self.operator = ''

    # Definisi untuk tombol menu
    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno('Exit Cafe Murah Meriah', 'Konfirmasi Exit')
        if self.iExit > 0:
            self.master1.destroy()
            return

    def reset(self):
        self.Ongkir.set('0')
        self.Sub_Total.set('0')
        self.Total_Pembayaran.set('0')
        self.Harga_Makanan.set('0')
        self.Harga_Minuman.set('0')
        self.Service_Charge.set('0')
        self.txt_Print.delete('1.0', END)
        self.text_Input.set('0')

        self.E_Kopi_Latte.set('0')
        self.E_Kopi_Espresso.set('0')
        self.E_Extra_Joss_Susu.set('0')
        self.E_Kopi_Susu.set('0')
        self.E_Cappuccino.set('0')
        self.E_African_Coffee.set('0')
        self.E_American_Coffee.set('0')
        self.E_Es_Cappuccino.set('0')

        self.E_Ayam_Geprek.set('0')
        self.E_Ayam_Bakar.set('0')
        self.E_Lalapan.set('0')
        self.E_Nasgor_Spesial.set('0')
        self.E_Pisang_Keju.set('0')
        self.E_Hamburger.set('0')
        self.E_Gorengan.set('0')
        self.E_Mie_Instan.set('0')

        self.var1.set(0)
        self.var2.set(0)
        self.var3.set(0)
        self.var4.set(0)
        self.var5.set(0)
        self.var6.set(0)
        self.var7.set(0)
        self.var8.set(0)
        self.var9.set(0)
        self.var10.set(0)
        self.var11.set(0)
        self.var12.set(0)
        self.var13.set(0)
        self.var14.set(0)
        self.var15.set(0)
        self.var16.set(0)

        self.txt_Kopi_Latte.configure(state=DISABLED)
        self.txt_Kopi_Espresso.configure(state=DISABLED)
        self.txt_Extra_Joss_Susu.configure(state=DISABLED)
        self.txt_Kopi_Susu.configure(state=DISABLED)
        self.txt_Cappuccino.configure(state=DISABLED)
        self.txt_African_Coffee.configure(state=DISABLED)
        self.txt_American_Coffee.configure(state=DISABLED)
        self.txt_Es_Cappuccino.configure(state=DISABLED)

        self.txt_Ayam_Geprek.configure(state=DISABLED)
        self.txt_Ayam_Bakar.configure(state=DISABLED)
        self.txt_Lalapan.configure(state=DISABLED)
        self.txt_Nasgor_Spesial.configure(state=DISABLED)
        self.txt_Pisang_Keju.configure(state=DISABLED)
        self.txt_Hamburger.configure(state=DISABLED)
        self.txt_Gorengan.configure(state=DISABLED)
        self.txt_Mie_Instan.configure(state=DISABLED)

    def Total_Item(self):
        self.Item1 = int(self.E_Kopi_Latte.get())
        self.Item2 = int(self.E_Kopi_Espresso.get())
        self.Item3 = int(self.E_Extra_Joss_Susu.get())
        self.Item4 = int(self.E_Kopi_Susu.get())
        self.Item5 = int(self.E_Cappuccino.get())
        self.Item6 = int(self.E_African_Coffee.get())
        self.Item7 = int(self.E_American_Coffee.get())
        self.Item8 = int(self.E_Es_Cappuccino.get())

        self.Item9 = int(self.E_Ayam_Geprek.get())
        self.Item10 = int(self.E_Ayam_Bakar.get())
        self.Item11 = int(self.E_Lalapan.get())
        self.Item12 = int(self.E_Nasgor_Spesial.get())
        self.Item13 = int(self.E_Pisang_Keju.get())
        self.Item14 = int(self.E_Hamburger.get())
        self.Item15 = int(self.E_Gorengan.get())
        self.Item16 = int(self.E_Mie_Instan.get())

        self.Minuman = (self.Item1 * 5) + (self.Item2 * 6) + (self.Item3 * 5) + (self.Item4 * 6) + (self.Item5 * 5) + (self.Item6 * 8) + (self.Item7 * 8) + (self.Item8 * 5)
        self.Makanan = (self.Item9 * 10) + (self.Item10 * 12) + (self.Item11 * 10) + (self.Item12 * 15) + (self.Item13 * 7) + (self.Item14 * 7) + (self.Item15 * 12) + (self.Item16 * 5)

        self.total_minuman = 'IDR', ('%.3f'%(self.Minuman))
        self.total_makanan = 'IDR', ('%.3f'%(self.Makanan))

        self.Harga_Minuman.set(self.total_minuman)
        self.Harga_Makanan.set(self.total_makanan)

        self.SC = 'IDR', ('%.3f' % (1))
        self.Service_Charge.set(self.SC)

        self.total_semuanya = 'IDR', ('%.3f' % (self.Minuman + self.Makanan + 1))
        self.Sub_Total.set(self.total_semuanya)

        self.Ongkos_Kirim = 'IDR', ('%.3f' % ((self.Minuman + self.Makanan + 1) + 1))
        self.Ongkir.set(self.Ongkos_Kirim)

        self.TT = ((self.Minuman + self.Makanan + 2) + 1)
        self.TC = 'IDR', ('%.3f' % ((self.Minuman + self.Makanan + 1) + self.TT))
        self.Total_Pembayaran.set(self.TC)

    # Minuman ==========================================================================================================
    def Check_Kopi_Latte(self):
        if (self.var1.get() == 1):
            self.txt_Kopi_Latte.configure(state=NORMAL)
            self.txt_Kopi_Latte.focus()
            self.txt_Kopi_Latte.delete(0, END)
            self.E_Kopi_Latte.set('')
        elif self.var1.get() == 0:
            self.txt_Kopi_Latte.configure(state=DISABLED)
            self.E_Kopi_Latte.set('0')

    def Check_Kopi_Espresso(self):
        if (self.var2.get() == 1):
            self.txt_Kopi_Espresso.configure(state=NORMAL)
            self.txt_Kopi_Espresso.focus()
            self.txt_Kopi_Espresso.delete(0, END)
            self.E_Kopi_Espresso.set('')
        elif var2.get() == 0:
            self.txt_Kopi_Espresso.configure(state=DISABLED)
            self.E_Kopi_Espresso.set('0')

    def Check_Kopi_Espresso(self):
        if (self.var2.get() == 1):
            self.txt_Kopi_Espresso.configure(state=NORMAL)
            self.txt_Kopi_Espresso.focus()
            self.txt_Kopi_Espresso.delete(0, END)
            self.E_Kopi_Espresso.set('')
        elif self.var2.get() == 0:
            self.txt_Kopi_Espresso.configure(state=DISABLED)
            self.E_Kopi_Espresso.set('0')

    def Check_Extra_Joss_Susu(self):
        if (self.var3.get() == 1):
            self.txt_Extra_Joss_Susu.configure(state=NORMAL)
            self.txt_Extra_Joss_Susu.focus()
            self.txt_Extra_Joss_Susu.delete(0, END)
            self.E_Extra_Joss_Susu.set('')
        elif self.var3.get() == 0:
            self.txt_Extra_Joss_Susu.configure(state=DISABLED)
            self.E_Extra_Joss_Susu.set('0')

    def Check_Kopi_Susu(self):
        if (self.var4.get() == 1):
            self.txt_Kopi_Susu.configure(state=NORMAL)
            self.txt_Kopi_Susu.focus()
            self.txt_Kopi_Susu.delete(0, END)
            self.E_Kopi_Susu.set('')
        elif self.var4.get() == 0:
            self.txt_Kopi_Susu.configure(state=DISABLED)
            self.E_Kopi_Susu.set('0')

    def Check_Cappuccino(self):
        if (self.var5.get() == 1):
            self.txt_Cappuccino.configure(state=NORMAL)
            self.txt_Cappuccino.focus()
            self.txt_Cappuccino.delete(0, END)
            self.E_Cappuccino.set('')
        elif self.var5.get() == 0:
            self.txt_Cappuccino.configure(state=DISABLED)
            self.E_Cappuccino.set('0')

    def Check_African_Coffee(self):
        if (self.var6.get() == 1):
            self.txt_African_Coffee.configure(state=NORMAL)
            self.txt_African_Coffee.focus()
            self.txt_African_Coffee.delete(0, END)
            self.E_African_Coffee.set('')
        elif self.var6.get() == 0:
            self.txt_African_Coffee.configure(state=DISABLED)
            self.E_African_Coffee.set('0')

    def Check_American_Coffee(self):
        if (self.var7.get() == 1):
            self.txt_American_Coffee.configure(state=NORMAL)
            self.txt_American_Coffee.focus()
            self.txt_American_Coffee.delete(0, END)
            self.E_American_Coffee.set('')
        elif self.var7.get() == 0:
            self.txt_American_Coffee.configure(state=DISABLED)
            self.E_American_Coffee.set('0')

    def Check_Es_Cappuccino(self):
        if (self.var8.get() == 1):
            self.txt_Es_Cappuccino.configure(state=NORMAL)
            self.txt_Es_Cappuccino.focus()
            self.txt_Es_Cappuccino.delete(0, END)
            self.E_Es_Cappuccino.set('')
        elif self.var8.get() == 0:
            self.txt_Es_Cappuccino.configure(state=DISABLED)
            self.E_Es_Cappuccino.set('0')

    # Makanan ==========================================================================================================
    def Check_Ayam_Geprek(self):
        if (self.var9.get() == 1):
            self.txt_Ayam_Geprek.configure(state=NORMAL)
            self.txt_Ayam_Geprek.focus()
            self.txt_Ayam_Geprek.delete(0, END)
            self.E_Ayam_Geprek.set('')
        elif self.var9.get() == 0:
            self.txt_Ayam_Geprek.configure(state=DISABLED)
            self.E_Ayam_Geprek.set('0')

    def Check_Ayam_Bakar(self):
        if (self.var10.get() == 1):
            self.txt_Ayam_Bakar.configure(state=NORMAL)
            self.txt_Ayam_Bakar.focus()
            self.txt_Ayam_Bakar.delete(0, END)
            self.E_Ayam_Bakar.set('')
        elif self.var10.get() == 0:
            self.txt_Ayam_Bakar.configure(state=DISABLED)
            self.E_Ayam_Bakar.set('0')

    def Check_Lalapan(self):
        if (self.var11.get() == 1):
            self.txt_Lalapan.configure(state=NORMAL)
            self.txt_Lalapan.focus()
            self.txt_Lalapan.delete(0, END)
            self.E_Lalapan.set('')
        elif self.var11.get() == 0:
            self.txt_Lalapan.configure(state=DISABLED)
            self.E_Lalapan.set('0')

    def Check_Nasgor_Spesial(self):
        if (self.var12.get() == 1):
            self.txt_Nasgor_Spesial.configure(state=NORMAL)
            self.txt_Nasgor_Spesial.focus()
            self.txt_Nasgor_Spesial.delete(0, END)
            self.E_Nasgor_Spesial.set('')
        elif self.var12.get() == 0:
            self.txt_Nasgor_Spesial.configure(state=DISABLED)
            self.E_Nasgor_Spesial.set('0')

    def Check_Pisang_Keju(self):
        if (self.var13.get() == 1):
            self.txt_Pisang_Keju.configure(state=NORMAL)
            self.txt_Pisang_Keju.focus()
            self.txt_Pisang_Keju.delete(0, END)
            self.E_Pisang_Keju.set('')
        elif self.var13.get() == 0:
            self.txt_Pisang_Keju.configure(state=DISABLED)
            self.E_Pisang_Keju.set('0')

    def Check_Hamburger(self):
        if (self.var14.get() == 1):
            self.txt_Hamburger.configure(state=NORMAL)
            self.txt_Hamburger.focus()
            self.txt_Hamburger.delete(0, END)
            self.E_Hamburger.set('')
        elif self.var14.get() == 0:
            self.txt_Hamburger.configure(state=DISABLED)
            self.E_Hamburger.set('0')

    def Check_Gorengan(self):
        if (self.var15.get() == 1):
            self.txt_Gorengan.configure(state=NORMAL)
            self.txt_Gorengan.focus()
            self.txt_Gorengan.delete(0, END)
            self.E_Gorengan.set('')
        elif self.var15.get() == 0:
            self.txt_Gorengan.configure(state=DISABLED)
            self.E_Gorengan.set('0')

    def Check_Mie_Instan(self):
        if (self.var16.get() == 1):
            self.txt_Mie_Instan.configure(state=NORMAL)
            self.txt_Mie_Instan.focus()
            self.txt_Mie_Instan.delete(0, END)
            self.E_Mie_Instan.set('')
        elif self.var16.get() == 0:
            self.txt_Mie_Instan.configure(state=DISABLED)
            Eself.E_Mie_Instan.set('0')

    # Resep ============================================================================================================
    def Print(self):
        self.txt_Print.delete('1.0', END)
        self.x = random.randint(10908, 500876)
        self.random_Ref = str(self.x)
        self.Nomor_ID.set(self.random_Ref)

        self.txt_Print.insert(END, 'Date:\t\t         ' + self.Tanggal_Order.get() + '\n')
        self.txt_Print.insert(END, 'Nomor ID:\t\t         ' + self.Nomor_ID.get() + '\n')
        self.txt_Print.insert(END, '=' * 40 + '\n')
        self.txt_Print.insert(END, 'Items\t\t\t' + '       Cost Of Items\n')
        self.txt_Print.insert(END, '=' * 40 + '\n')
        self.txt_Print.insert(END, '+ Minuman\n')
        self.txt_Print.insert(END, '\nKopi Latte \t\t\t\t' + self.E_Kopi_Latte.get() + '\n')
        self.txt_Print.insert(END, 'Kopi Espresso \t\t\t\t' + self.E_Kopi_Espresso.get() + '\n')
        self.txt_Print.insert(END, 'Extra Joss Susu \t\t\t\t' + self.E_Extra_Joss_Susu.get() + '\n')
        self.txt_Print.insert(END, 'Kopi Susu \t\t\t\t' + self.E_Kopi_Susu.get() + '\n')
        self.txt_Print.insert(END, 'Cappuccino \t\t\t\t' + self.E_Cappuccino.get() + '\n')
        self.txt_Print.insert(END, 'African Coffee \t\t\t\t' + self.E_African_Coffee.get() + '\n')
        self.txt_Print.insert(END, 'American Coffee \t\t\t\t' + self.E_American_Coffee.get() + '\n')
        self.txt_Print.insert(END, 'Es Cappuccino \t\t\t\t' + self.E_Es_Cappuccino.get() + '\n')
        self.txt_Print.insert(END, '=' * 40 + '\n')
        self.txt_Print.insert(END, '+ Makanan\n')
        self.txt_Print.insert(END, '\nAyam Geprek \t\t\t\t' + self.E_Ayam_Geprek.get() + '\n')
        self.txt_Print.insert(END, 'Ayam Bakar \t\t\t\t' + self.E_Ayam_Bakar.get() + '\n')
        self.txt_Print.insert(END, 'Lalapan \t\t\t\t' + self.E_Lalapan.get() + '\n')
        self.txt_Print.insert(END, 'Nasgor Spesial \t\t\t\t' + self.E_Nasgor_Spesial.get() + '\n')
        self.txt_Print.insert(END, 'Pisang Keju \t\t\t\t' + self.E_Pisang_Keju.get() + '\n')
        self.txt_Print.insert(END, 'Hamburger \t\t\t\t' + self.E_Hamburger.get() + '\n')
        self.txt_Print.insert(END, 'Gorengan \t\t\t\t' + self.E_Gorengan.get() + '\n')
        self.txt_Print.insert(END, 'Mie Instan \t\t\t\t' + self.E_Mie_Instan.get() + '\n')
        self.txt_Print.insert(END, '=' * 40 + '\n')
        self.txt_Print.insert(END, '+ Pembayaran\n')
        self.txt_Print.insert(END, '\nHarga Minuman \t\t' + self.Harga_Minuman.get() + '\nOngkos Kirim\t\t' + self.Ongkir.get() + '\n')
        self.txt_Print.insert(END, 'Harga Makanan \t\t' + self.Harga_Makanan.get() + '\nBiaya Admin\t\t' + str(self.Sub_Total.get()) + '\n')
        self.txt_Print.insert(END, 'Service Charge \t\t' + self.Service_Charge.get() + '\nTotal Bayar\t\t' + str(self.Total_Pembayaran.get()))


main()
mainloop()
