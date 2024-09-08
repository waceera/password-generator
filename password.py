import random 

kecil = "abcdefghijklmnopqrstuvwxyz"
besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
simbol = "!@#$%^&*():;'<>,/?`~[]\|}{"

string = kecil + besar + simbol
length = 16
password = "".join (random.sample(string, length))

print("\n\n\n\n\n\n")
print("Welcome To Password Generator!\n -- Your New Password: " + password)
print("\nJagalah password ini dengan baik\nKetik python password.py untuk membuat password lagi.")
print("\nMade By: Hazel")
print("\n\n\n\n\n\n")