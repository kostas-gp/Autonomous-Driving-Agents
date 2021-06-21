### DEFINING FUNCTIONS TO TRANSLATE THE DRL OUTPUT INTO NAVIGATION COMMANDS

from digi.xbee.devices import XBeeDevice

# DEFINES PARAMETERS FOR SENDING MESSAGES THROUGH XBee RADIO

PORT = "/dev/ttyUSB0"               # Port which the modem is connected to
BAUD_RATE = 9600                    # Baud rate

speed_base = 250
speed_max = 250

steering_base = 250
steering_max = 250

# TRANSLATE DRL SPEED OUTPUT INTO NAVIGATION COMMAND
def trspeed(in_speed):
    speed = speed_base + in_speed * speed_max
    result = "y1{}!".format(speed)
    return(result) 

# TRANSLATE DRL STEERING OUTPUT INTO NAVIGATION COMMAND
def trsteering(in_steering):
    steering = steering_base + in_steering * steering_max
    result = "y2{}!".format(steering)
    return(result)

# CALLS FOR TRANSLATING THE DRL OUTPUTS INTO NAVIGATION COMMAND
# AND SENDS THE COMMANDS

def sending_data(in_speed,in_steering):

    # INITIALIZING THE XBee MODEM
    device = XBeeDevice(PORT, BAUD_RATE)

    # STARTS
    while(True):
        try:
            device.open()
            
            # REFRESHING THE MODEM CACHED VALUES.
            local_xbee.refresh_device_info()
            
            device.send_data_broadcast(trspeed(in_speed))
            device.send_data_broadcast(trsteering(in_steering))

        finally:
            if device is not None and device.is_open():
                device.close()

def main:
    sending_data(in_speed,in_steering)


if (__name__ == '__main__'): 
    main()