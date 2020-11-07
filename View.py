import tkinter as tk
from Model import Logic
from Crypto import Rsa

class Interface:

    def __init__(self,window):
        self.rsa = Rsa()
        self.logic = Logic(self,self.rsa)

        self.window = window
        self.window.geometry("605x692+802+110")
        self.window.minsize(120, 1)
        self.window.maxsize(3844, 1061)
        self.window.resizable(1, 1)
        self.window.title("Eranga Perera")
        self.window.configure(borderwidth="5")
        self.window.configure(background="#aaaaaa")

        self.Header_Label = tk.Label(self.window)
        self.Header_Label.place(relx=0.268, rely=0.043, height=33, width=326)
        self.Header_Label.configure(background="#aaaaaa", disabledforeground="#a3a3a3",
                                    font="-family {Segoe UI} -size 16 -weight bold -underline 1",
                                    foreground="#000000", text='''RSA Implementation In Python''')

        self.Footer_Label = tk.Label(self.window)
        self.Footer_Label.place(relx=0.281, rely=0.957, height=29, width=306)
        self.Footer_Label.configure(background="#aaaaaa", disabledforeground="#a3a3a3",
                                    font="-family {Segoe UI} -size 9 -weight bold",
                                    foreground="#000000", text='''Ⓒ 2020 Eranga Perera. All Rights Reserved''')

        self.Prime_Num_1_Label = tk.Label(self.window)
        self.Prime_Num_1_Label.place(relx=0.15, rely=0.152, height=28, width=135)
        self.Prime_Num_1_Label.configure(background="#aaaaaa", disabledforeground="#a3a3a3",
                                         font="-family {@Arial Unicode MS} -size 11 -weight bold",
                                         foreground="#000000", text='''Prime Number 1''')

        self.Prime_Entry_1 = tk.Entry(self.window)
        self.Prime_Entry_1.place(relx=0.413, rely=0.158, height=20, relwidth=0.42)
        self.Prime_Entry_1.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                     foreground="#000000", insertbackground="black")

        self.Prime_Num_2_Label = tk.Label(self.window)
        self.Prime_Num_2_Label.place(relx=0.149, rely=0.210, height=28, width=135)
        self.Prime_Num_2_Label.configure(background="#aaaaaa", disabledforeground="#a3a3a3",
                                         font="-family {@Arial Unicode MS} -size 11 -weight bold",
                                         foreground="#000000", text='''Prime Number 2''')

        self.Prime_Entry_2 = tk.Entry(self.window)
        self.Prime_Entry_2.place(relx=0.413, rely=0.215, height=20, relwidth=0.42)
        self.Prime_Entry_2.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                     foreground="#000000", insertbackground="black")

        self.Public_Key_Label = tk.Label(self.window)
        self.Public_Key_Label.place(relx=0.215, rely=0.270, height=21, width=94)
        self.Public_Key_Label.configure(background="#aaaaaa", disabledforeground="#a3a3a3",
                                        font="-family {@Arial Unicode MS} -size 11 -weight bold",
                                        foreground="#000000", text='''Public Key''')

        self.Public_Key_Entry = tk.Entry(self.window)
        self.Public_Key_Entry.place(relx=0.413, rely=0.270, height=20, relwidth=0.42)
        self.Public_Key_Entry.configure(background="white", disabledforeground="#a3a3a3",
                                        font="TkFixedFont",
                                        foreground="#000000",
                                        insertbackground="black")

        self.Private_Key_Label = tk.Label(self.window)
        self.Private_Key_Label.place(relx=0.215, rely=0.330, height=21, width=94)
        self.Private_Key_Label.configure(background="#aaaaaa", disabledforeground="#a3a3a3",
                                         font="-family {@Arial Unicode MS} -size 11 -weight bold",
                                         foreground="#000000", text='''Private Key''')

        self.Private_Key_Entry = tk.Entry(self.window)
        self.Private_Key_Entry.place(relx=0.413, rely=0.330, height=20, relwidth=0.42)
        self.Private_Key_Entry.configure(background="white", disabledforeground="#a3a3a3",
                                         font="TkFixedFont",
                                         foreground="#000000",
                                         insertbackground="black")

        self.Plain_msg_Entry = tk.Text(self.window)
        self.Plain_msg_Entry.place(relx=0.417, rely=0.390, height=60, relwidth=0.42)

        self.Plain_msg_Label = tk.Label(self.window)
        self.Plain_msg_Label.place(relx=0.05, rely=0.390, height=27, width=214)
        self.Plain_msg_Label.configure(background="#aaaaaa", disabledforeground="#a3a3a3",
                                       font="-family {@Arial Unicode MS} -size 11 -weight bold",
                                       foreground="#000000", text='''Message To Encrypt''')

        self.Cipher_Text_Entry = tk.Text(self.window)
        self.Cipher_Text_Entry.place(relx=0.417, rely=0.498, height=120, relwidth=0.42)

        self.Cipher_Text_Label = tk.Label(self.window)
        self.Cipher_Text_Label.place(relx=0.215, rely=0.491, height=27, width=93)
        self.Cipher_Text_Label.configure(background="#aaaaaa", disabledforeground="#a3a3a3",
                                         font="-family {@Arial Unicode MS} -size 11 -weight bold",
                                         foreground="#000000", text='''Cipher Text''')

        self.Original_msg_Entry = tk.Text(self.window)
        self.Original_msg_Entry.place(relx=0.413, rely=0.699, height=90, relwidth=0.42)

        self.Original_msg_Label = tk.Label(self.window)
        self.Original_msg_Label.place(relx=0.132, rely=0.708, height=21, width=144)
        self.Original_msg_Label.configure(background="#aaaaaa", disabledforeground="#a3a3a3",
                                          font="-family {@Arial Unicode MS} -size 11 -weight bold",
                                          foreground="#000000", text='''Original Message''')

        self.Button_Generate_Key = tk.Button(self.window, command=self.logic.button_click_generate_keys)
        self.Button_Generate_Key.place(relx=0.370, rely=0.853, height=44, width=90)
        self.Button_Generate_Key.configure(activebackground="#ececec", activeforeground="#000000", background="#7268ea",
                                           disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 -weight bold",
                                           foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                           pady="0", text='''Generate Key''')

        self.Button_Encrypt = tk.Button(self.window, command=self.logic.button_click_encrypt)
        self.Button_Encrypt.place(relx=0.540, rely=0.853, height=44, width=90)
        self.Button_Encrypt.configure(activebackground="#ececec", activeforeground="#000000", background="#7268ea",
                                      disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 -weight bold",
                                      foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                      pady="0", text='''Encrypt''')

        self.Button_Clear_Fields = tk.Button(self.window, command=self.logic.clear_all_fields)
        self.Button_Clear_Fields.place(relx=0.710, rely=0.853, height=44, width=90)
        self.Button_Clear_Fields.configure(activebackground="#ececec", activeforeground="#000000", background="#7268ea",
                                           disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 -weight bold",
                                           foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                           pady="0", text='''Clear''')
