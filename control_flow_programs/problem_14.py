'''Login System ⭐⭐⭐⭐
Username : admin
Password : python123'''

Username = 'admin'
Password = 'python123'

i=0
while i<3:
    a,b=input("enter username and password with space between them=").split(" ")
    i+=1
    if a==Username and b==Password:
        print("successfully Logged in")
    else:
        print("you entered incorrect creditnals pls try again")    

else:
    print("You have reached the limitation and your system is locked")    