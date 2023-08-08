from tkinter import *
from PIL import Image , ImageTk
from tkinter import messagebox # hata messajı vermek için messagebox sınıfını import ettik
import base64
#messagebox bize hata mesajı vermesini sağlayan bir tkinter modülüdür.


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)





def save_and_encrpyt_notes():
     title = title_entry.get()
     message = secret_text.get("1.0",END)  # texte yazılanları birinci satırtan almaya başla sonuna kadar git demekdir hatırla!!!
     master_secret = key_entry.get()   #bu entry ve text leri bu şekilde alabiliriz
     if len(title) == 0 or len(message) == 0 or len(master_secret) == 0 :
         messagebox.showinfo(title="Error",message="Please enter all info") # messagebox sınıfını hata mesajını vermek için kullanırız
# showinfo dediğimizde içine bir hata başlığı ve hata mesajı gireriz)

     else:
         message_encrypt = encode(master_secret, message)# anlamı arayüzde text' e girileni  my_secret.txt' de  şifreleycektir ve bu yüzden try' daki ve except'deki
         # dosyaya ,  message değilde,  message_encrypt ' ı koymamız lazım. Biz bunu key_entrydeki yani master_secret'de şifrelenmiş şifreyi göstermeyi öğrencez

         try:
            with open("my.secret.txt", "a") as data_file:
                     data_file.write(f"\n{title},\n{message_encrypt}, ")
         except FileNotFoundError:
             with open("my.secret.txt" "w") as data_file:
                 data_file.write(f"\n{title},\n{message_encrypt}")
         finally:
             title_entry.delete(0,END)
             secret_text.delete("1.0",END) # text olduğundan 1.0 ile belirttik. (multiline) çünkü.
             key_entry.delete(0,END) # finally her koşulda çalışacaktır ve try ve komutundan sonra hata almaz ise bu girilmiş olan enrty ' i ve text' i
             # arayüzden silecektir . Hata alır ise except'i uygulayıp bu entry ve text' i arayüzden silecektir


# kodun anlamı my_secret.txt oluştur ve data_file ile bunu aç, ve data_file içine kullanıcı title'ı, messege'ı girdiğinde my_secret.txt içine kaydet demektir.
# except tarafında ise data_file ile boş my_secret.txt içine title ve message ' i yazdıracaktır eğer böyle hata alırsa. Hata almaz ise  Try ilede bu dosyayı
# açacaktır
# dosyaları bu şekilde açabiliyoduk "a" modu append modu idi. ekle my_secret.txt içine ekle



def en_encode_encrypt():
    message_encrypt = secret_text.get("1.0",END)
    master_secret  = key_entry.get()

    if len(message_encrypt) == 0 or len(master_secret) == 0 :
        messagebox.showinfo(title="ERROR!",message="Lütfen Tüm Bilgileri Gir")
    else:
        try:
            decrypted_message = decode(master_secret,message_encrypt)
            secret_text.delete("1.0",END)
            secret_text.insert("1.0",decrypted_message)
        except binascii:
            messagebox.showinfo(title="ERRORRR",message="Please Enter encrypt Text")







window = Tk()
window.title("Secret Notes")
window.minsize( 500 ,  750)
image = Image.open('icon3.png')
image = image.resize((100,100))
photo = ImageTk.PhotoImage(image)
resim_label = Label(image=photo)

resim_label.pack()
font = ("Arial",15,"bold")
# label 2
title_label = Label(text="Enter Your Title",fg="black", width=20,font=font)
title_label.place(x = 130, y = 125)



# enry 1

title_entry = Entry(width=30,)
title_entry.place(x=160,y=155)


# label3
secret_label = Label(text="Enter Your Secret",fg="black",font=font)
secret_label.place(x=160,y=190)

# text

secret_text = Text(height=20,width=30,)
secret_text.place(x=135,y=223)

#  label 4
master_key = Label(text="Enter Master Key",fg="black",font=("Arial",13,"bold"))
master_key.place(x=180,y=550)

# entry 2
key_entry= Entry(width=30)
key_entry.place(x=160,y=580)


# button
save_button = Button(text="Save & Encrypt ",font=("Arial",10,"normal"),command=save_and_encrpyt_notes)
save_button.place(x=200,y=610)

#button2
decrypt_button = Button(text="Decrypt",font=("Arial",10,"normal"),command=en_encode_encrypt)
decrypt_button.place(x=222,y=650)





# resultlabel
result_label = Label(font=font,fg="black")
result_label.place(x=135,y=700)



window.mainloop()

