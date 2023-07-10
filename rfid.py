from mfrc522 import MFRC522 
import utime
from machine import Pin

lock =Pin(28,Pin.OUT)
buzzer = Pin(27, Pin.OUT)

def uidToString(uid):
    mystring = ""
    for i in uid:
        mystring = "%02X" % i + mystring
    return mystring
                  
rc522 = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=3)

print("")
print("Place the card")
print("")


while True:

    (stat, tag_type) = rc522.request(rc522.REQALL)

    if stat == rc522.OK:
        (status, raw_uid) = rc522.SelectTagSN()
        if stat == rc522.OK:
            rfid_data = "{:02x}{:02x}{:02x}{:02x}".format(raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            print("Card detected! UID: {}".format(rfid_data))
            if rfid_data == "c645224b":
                
                lock.value(1)
                utime.sleep(5)
                lock.value(0)
                
            elif rfid_data == "4247b01e":
                
                lock.value(1)
                utime.sleep(5)
                lock.value(0)

            else:
                
                buzzer.value(1)
                utime.sleep(1)
                buzzer.value(0)