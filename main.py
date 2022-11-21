
from cryptography.fernet import Fernet

with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
fernet = Fernet(key)

v = 0
while v < 10:
  print ("welcome to Password Manager!")
  usrch = input ("would you like to add a password,change a password, or read a password?")
  if usrch == 'add':
    sitename = input("sitename: ")
    with open(sitename, "a") as f:
        f.write(input())
    with open(sitename, 'rb') as file:
      addoriginal = file.read()
    encrypted = fernet.encrypt(addoriginal)
    with open(sitename, 'wb') as encrypted_file:
      encrypted_file.write(encrypted)
  if usrch == 'read':
    sitename = input("sitename: ")
    with open(sitename, "r") as f:
        with open(sitename, 'rb') as enc_file:
          encrypted = enc_file.read()
          #file_contents = f.read()
          decrypted = fernet.decrypt(encrypted)
          
        print(decrypted)
        
  if usrch == "change":
    sitename = input("sitename: ")
    with open(sitename, "r+") as f:
      file_content = f.read()
      print (file_content)
      f.seek(0)
      f.write(input() + "\n")