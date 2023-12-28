import tkinter as tk
from gpiozero import LED, Button
from time import sleep
import requests

#A=8,B=9,C=10,D=11,E=12,F=13,G=17

sega = LED(8)

segb = LED(9)

segc = LED(10)

segd = LED(11)

sege = LED(12)

segf = LED(13)

segg = LED(17)
ledv= LED(7)

## BTN = 27

btn = Button(27)

# Z1 =22 ; Z2 =5 ; Z3 = 6 ; Z4= 19

zone1 = Button(22)

zone2 = Button(5)

zone3 = Button(6)

zone4 = Button(19)

#False= unarmed, True= armed

systemStatus = 0

# DE 0  Ã  9

def show0():

    #0
    
    sega.off()

    segb.off()

    segc.off()

    segd.off()

    sege.off()

    segf.off()

    segg.on()

def show1():

    #1

    sega.on()

    segb.on()

    segc.on()

    segd.on()

    sege.off()

    segf.off()

    segg.on()
    
def show2():

    #2

    sega.off()

    segb.off()

    segc.on()

    segd.off()

    sege.off()

    segf.on()

    segg.off()  

def show3():

    #3

    sega.off()

    segb.off()

    segc.off()

    segd.off()

    sege.on()

    segf.on()

    segg.off()




def show4():

    #4

    sega.on()

    segb.off()

    segc.off()

    segd.on()

    sege.on()

    segf.off()

    segg.off()




def show5():

    #5

    sega.off()

    segb.on()

    segc.off()

    segd.off()

    sege.on()

    segf.off()

    segg.off()  




def show6():

    #6

    sega.off()

    segb.on()

    segc.off()

    segd.off()

    sege.off()

    segf.off()

    segg.off()




def show7():

    #7

    sega.off()

    segb.off()

    segc.off()

    segd.on()

    sege.on()

    segf.on()

    segg.on()    




def show8():

    #8

    sega.off()

    segb.off()

    segc.off()

    segd.off()

    sege.off()

    segf.off()

    segg.off()  




def show9():

    #9

    sega.off()

    segb.off()

    segc.off()

    segd.on()

    sege.on()

    segf.off()

    segg.off()    

# AFF A

def showA():

    #A

    sega.off()

    segb.off()

    segc.off()

    segd.on()

    sege.off()

    segf.off()

    segg.off()




 

# DE 0 Ã  9

def cout_up():

    #0

    show0()

    sleep(1)

    #1

    show1()    

    sleep(1)

    #2

    show2()

    sleep(1)

    #3

    show3()  

    sleep(1)

    #4

    show4()

    sleep(1)

    #5

    show5()

    sleep(1)

    #6

    show6()

    sleep(1)

    #7

    show7()

    sleep(1)
   #8

    show8()  

    sleep(1)

    #9

    show9()

    sleep(1)
    
    showA()


def cout_down():
    showA()

    sleep(1)
    
    show9()

    sleep(1)

    show8()  

    sleep(1)

    #7

    show7()  

    sleep(1)

    #6

    show6()  

    sleep(1)

    #5

    show5()

    sleep(1)

    #4

    show4()  

    sleep(1)

    #3

    show3()    

    sleep(1)

    #2

    show2()  

    sleep(1)


    #1

    show1()    

    sleep(1)

    #0

    show0()

    sleep(1)
    
def showN():
    sega.on()

    segb.on()

    segc.on()

    segd.on()

    sege.on()

    segf.on()

    segg.on()

#show0()

# AFFICHAGE DES ZONES

def aff1():

    z1.configure(bg="green")

    show1()

def aff2():

    z2.configure(bg="green")

    show2()

def aff3():

    z3.configure(bg="green")

    show3()

def aff4():

    z4.configure(bg="green")

    show4()
    
def Activer():
    global systemStatus
    systemStatus = 1
    zA.configure(bg="green")
    response = requests.post('http://10.0.0.18:80/Labo3/api.php/', json={'System_Status': 'on'})
    print(response.text)
    if response.status_code == 200:
        print("System Status Stocked Succesfully")
    else:
        print(f"Error Insert System_Status. Response status code: {response.status_code}")
    cout_up()
    
    
    
def Desactiver():
    global systemStatus
    systemStatus = 0
    zA.configure(bg="green")
    response = requests.post('http://10.0.0.18:80/Labo3/api.php/', json={'System_Status': 'off'})
    print(response.text)
    if response.status_code == 200:
        print("System Status Inserted Succefully")
    else:
        print(f"Error Insert status. Response status code: {response.status_code}")
    cout_down()
    
def Reset():
    zR.configure(bg="green")
    show0()

def on():
    show0()
    
def off():
    showN()
    


show0()
#Connexion avec le fichier api
API_URL = 'http://10.0.0.18:2003/api/'

def query_api(endpoint, params=None):
    try:
        response = requests.get(API_URL + endpoint, params=params)
        response.raise_for_status()  # Check for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error querying the API: {e}")
        return None
    
def save_zone_status_to_api(zone_number, status):
    API_URL = 'http://10.0.0.18:2003/api/update_zone_status'
    data = {"zoneNumber": zone_number, "Status": status}
    try:
        response = requests.post(API_URL, data=data)
        response.raise_for_status()  # Check for HTTP errors
        if response.status_code == 200:
            print(f"Zone {zone_number} status {status} saved successfully")
        else:
            print(f"Error saving zone status. Response status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error adding zone status data to the API: {e}")

# Usage example
save_zone_status_to_api(2, 'on')


#dÃ©finir une fenetre( creer une fenETRE)

root = tk.Tk()

z1 = tk.Button(root, text=" Zone 1", command=aff1, bg="red", fg="white")

z2 = tk.Button(root, text=" Zone 2", command=aff2, bg="red", fg="white")

zA = tk.Button(root, text=" Activate ", command=Activer, bg="red", fg="white")

z3 = tk.Button(root, text=" Zone 3", command=aff3, bg="red", fg="white")

z4 = tk.Button(root, text=" Zone 4", command=aff4, bg="red", fg="white")

zR = tk.Button(root, text=" Reset ", command=Reset, bg="red", fg="white")

zD = tk.Button(root, text=" Desactivate ", command=Desactiver, bg="red", fg="white")

zON= tk.Button(root, text=" ON ", command=on, bg="green", fg="white")

zOFF= tk.Button(root, text=" OF ", command=off, bg="red", fg="white")


titreS = tk.Label(root, text="Status", font=("Arial", 12, "bold"))

if systemStatus == 0:
    titreS=tk.Label(root, text="Active", font=("Arial", 12, "bold"))
    
elif systemStatus == 1:
    titleS=tk.Label(root, text="Desactive", font=("Arial", 12, "bold"))



# placer les element crÃ©er



z1.grid(row=1, column=0, padx=5, pady=10)

z2.grid(row=1, column=1, padx=5, pady=10)
zA.grid(row=1, column=2, padx=5, pady=10)





z3.grid(row=2, column=0, padx=5, pady=10)

z4.grid(row=2, column=1, padx=5, pady=10)
zD.grid(row=2, column=2, padx=5, pady=10)



titreS.grid(row=3, column=0, columnspan=2, padx=5, pady=10)
zR.grid(row=3, column=2,padx=5, pady=10)
zON.grid(row=4, column=0,padx=5, pady=10)
zOFF.grid(row=4, column=1, padx=5 , pady=10)







root.mainloop()