from tkinter import messagebox


class Logic:

    def __init__(self,window,rsa):
        self.window = window
        self.rsa  = rsa

        self.private_key = 0
        self.public_key = 0
        self.cipher_text = ''

    def clear_all_fields(self):
        self.window.Cipher_Text_Entry.delete('1.0','end')
        self.window.Original_msg_Entry.delete('1.0','end')
        self.window.Plain_msg_Entry.delete('1.0','end')
        self.window.Public_Key_Entry.delete(0,'end')
        self.window.Private_Key_Entry.delete(0, 'end')
        self.window.Prime_Entry_1.delete(0,'end')
        self.window.Prime_Entry_2.delete(0,'end')

        self.clear_cipher()
        self.clear_keys()

    def button_click_encrypt(self):

        if self.window.Plain_msg_Entry.compare("end-1c", "==", "1.0"):
            messagebox.showerror("Message Section Empty","Please Enter Message to Encrypt")
        else:
            if self.private_key != 0 and self.public_key != 0:
                self.clear_cipher()
                self.cipher_text = self.rsa.encrypt(self.window.Plain_msg_Entry.get("1.0", "end"), self.public_key)
                self.window.Cipher_Text_Entry.insert('end',str(self.cipher_text))
                original_message = self.rsa.decrypt(self.cipher_text, self.private_key)
                self.window.Original_msg_Entry.delete('1.0', 'end')
                self.window.Original_msg_Entry.insert('end', original_message)
                self.public_key = 0
                self.private_key = 0

            else:
                self.button_click_generate_keys()
                if self.private_key != 0 and self.public_key != 0:
                    self.clear_cipher()
                    self.cipher_text = self.rsa.encrypt(self.window.Plain_msg_Entry.get("1.0", "end"), self.public_key)
                    self.window.Cipher_Text_Entry.insert('end', str(self.cipher_text))
                    original_message = self.rsa.decrypt(self.cipher_text,self.private_key)
                    self.window.Original_msg_Entry.delete('1.0', 'end')
                    self.window.Original_msg_Entry.insert('end',original_message)

    def button_click_generate_keys(self):

        prime_1 , prime_2 = self.check_user_inserted_prime()
        if prime_1 !=0 and prime_2!=0:
            self.clear_keys()
            self.public_key, self.private_key = self.rsa.generate_keyPairs(int(prime_1), int(prime_2))
            self.window.Public_Key_Entry.insert(0, self.public_key)
            self.window.Private_Key_Entry.insert(0, self.private_key)


    def clear_keys(self):

        self.private_key = 0
        self.public_key = 0
        self.window.Public_Key_Entry.delete(0, 'end')
        self.window.Private_Key_Entry.delete(0, 'end')

    def clear_cipher(self):

        self.cipher_text = ''
        self.window.Cipher_Text_Entry.delete('1.0', 'end')

    def check_user_inserted_prime(self):

        prime_1 = self.window.Prime_Entry_1.get()
        prime_2 = self.window.Prime_Entry_2.get()

        p1 = False
        p2 = False

        if prime_1:
            try:
                prime_1 = int(prime_1)
                if prime_1 < 0:
                    raise ValueError
                if self.rsa.is_prime(prime_1):
                    if prime_1 < 10:
                        messagebox.showerror("Prime Number Error", "Please Enter Prime Number greater than 10")
                        self.window.Prime_Entry_1.delete(0, 'end')
                        self.clear_keys()
                        self.clear_cipher()
                        self.window.Original_msg_Entry.delete('1.0', 'end')
                    else:
                        p1 = True
                else:
                    messagebox.showerror("Prime Number Error", "Please Enter Prime Number")
                    self.window.Prime_Entry_1.delete(0, 'end')
                    self.clear_keys()
                    self.clear_cipher()
                    self.window.Original_msg_Entry.delete('1.0', 'end')

            except ValueError:
                messagebox.showerror("Invalid Entry","Please Enter Valid Prime Number")
                self.window.Prime_Entry_1.delete(0, 'end')
                self.clear_keys()
                self.clear_cipher()
                self.window.Original_msg_Entry.delete('1.0', 'end')
        else:
            prime_1 = self.rsa.generate_prime_number()
            self.window.Prime_Entry_1.insert(0,str(prime_1))
            p1 = True

        if prime_2:
            try:
                prime_2 = int(prime_2)
                if prime_2 < 0:
                    raise ValueError
                if self.rsa.is_prime(prime_2):
                    if prime_2 < 10:
                        messagebox.showerror("Prime Number Error", "Please Enter Prime Number greater than 10")
                        self.window.Prime_Entry_2.delete(0, 'end')
                        self.clear_keys()
                        self.clear_cipher()
                        self.window.Original_msg_Entry.delete('1.0', 'end')
                    else:
                        p2 = True
                else:
                    messagebox.showerror("Prime Number Error", "Please Enter Prime Number")
                    self.window.Prime_Entry_2.delete(0, 'end')
                    self.clear_keys()
                    self.clear_cipher()
                    self.window.Original_msg_Entry.delete('1.0', 'end')

            except ValueError:
                messagebox.showerror("Invalid Entry","Please Enter Valid Prime Number")
                self.window.Prime_Entry_2.delete(0, 'end')
                self.clear_keys()
                self.clear_cipher()
                self.window.Original_msg_Entry.delete('1.0', 'end')
        else:
            prime_2 = self.rsa.generate_prime_number()
            self.window.Prime_Entry_2.insert(0,str(prime_2))
            p2 = True

        if p1 and p2:
            return prime_1, prime_2
        else:
            return 0,0



