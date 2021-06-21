### MANUAL NAVIGATION CODE FOR TESTING THE XBee MODEM, COMMUNICATION WITH
### WITH ROBOT AND SPEED AND STEERING 

from digi.xbee.devices import XBeeDevice

# DEFINES PARAMETERS FOR SENDING MESSAGES THROUGH XBee RADIO

PORT = "/dev/ttyUSB0"               # Port which the modem is connected to
BAUD_RATE = 9600                    # Baud rate
DATA_TO_SEND = "XBee Command"      # Assigning a variable and intial value 
                                    # to be send to modem
Base_steering = 250
Base_speed = 250

speed_max = 490
steering_max = 490

speed_min = 10
steering_min = 10

speed_interval = 10
steering_interval = 10

def main() :

    Speed = Base_speed
    Steering = Base_steering
    
    # USER INSTRUCTION 
    print("Navigation Keys\nMove Forward \\ Speed Increase : 'w' \n ")
    print("Move Backward \\ Speed Decrease : 's' \n ")
    print("Move Left : 'a' \n ")
    print("Move Right : 's' \n ")
    print("Exit : 'x' \n")
    
    # INITIALIZING THE XBee MODEM
    device = XBeeDevice(PORT, BAUD_RATE)

    # SETTING THE SPEED AND STREEING VALUES AND GENERATING NAVIGATION 
    # COMMANDS BASED ON INPUT

    while(True):

        kb_input = input()
        if kb_input == "w":
            if speed_min <= Speed <= speed_max:
                Speed = Speed + speed_interval
            else:
                Speed = Speed + 0
            DATA_TO_SEND = "y1{}!".format(Speed)
            print(DATA_TO_SEND)

        elif kb_input == "s":
            if speed_min <= Speed <= speed_max:
                Speed = Speed - speed_interval
            else:
                Speed = Speed + 0
            DATA_TO_SEND = "y1{}!".format(Speed)
            print(DATA_TO_SEND)

        elif kb_input == "a":
            if steering_min <= Steering <= steering_max:
                Steering = Steering - steering_interval
            else:
                Steering = Steering + 0
            DATA_TO_SEND = "y2{}!".format(Steering)
            print(DATA_TO_SEND)

        elif kb_input == "d":
            if steering_min <= Steering <= steering_max:
                Steering = Steering + steering_interval
            else:
                Steering = Steering + 0
            DATA_TO_SEND = "y2{}!".format(Steering)
            print(DATA_TO_SEND)
        
        elif kb_input == "z":
            Speed = Base_speed + 0
            DATA_TO_SEND = "y2{}!".format(Speed)

        elif kb_input == "x":
            break

# SENDING THE COMMANDS THROUGH THE XBee MODEM

        try:
        device.open()

        # REFRESHING THE MODEM CACHED VALUES.
        # local_xbee.refresh_device_info()

        device.send_data_broadcast(DATA_TO_SEND)

        finally:
        if device is not None and device.is_open():
            device.close()

if (__name__ == '__main__'): 
    main()
