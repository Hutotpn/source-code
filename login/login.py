#Huto login

#import
import time

print("Welcome!")
loop = 'true'

#Using while for loop find the username and password in the system
while(loop =='true'):
    time.sleep(1)
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    #if username & password correct it will pass
    if (username == "Hutotpn" and password == "1234"):
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        time.sleep(0.03)
        print('Login successfully ' + username)
        loop = 'false'  #When the loop finds the username password in the system, it changes the loop = 'false' interpreter to exit the loop.
        loopcmd = 'true'
        while(loopcmd == 'true'):	#Use while again to use a command
            command = input(username + ">> ")
            
            #commands
            if(command == "drive"):
                time.sleep(1)
                print("Email: contact.hutotpn@gmail.com ")
                print("Password: 1234")

            if(command == "exit"):
                print("Logout successfully")
                time.sleep(3)
                break
            else:
                print("When you type 'drive' it will say 'Not found drive'_")
                print("Not found " +command)
    else:
        print("Username or password is invalid.")
