# -*- coding:utf-8 -*-

import time
import machine
from L76 import l76x
import math
import hashlib
from L76.micropyGPS.micropyGPS import MicropyGPS

get_coord_button = machine.Pin(25, machine.Pin.IN)

# define the UART number and its baudrate , when UARTx is 1 please solder the UART1 0R resistor on Pico-GPS-L76B board
# UARTx = 1
UARTx = 0

# define the rp2040 uart baudrate , the default baudrate is 9600 of L76B 
BAUDRATE = 9600

# make an object of gnss device , the default uart is UART0 and its baudrate is 9600bps
gnss_l76b=l76x.L76X(uartx=UARTx,_baudrate = BAUDRATE)

# exit the backup mode when start
gnss_l76b.l76x_exit_backup_mode()

# enable/disable sync PPS when NMEA output
'''
optional:
SET_SYNC_PPS_NMEA_ON
SET_SYNC_PPS_NMEA_OFF
'''
gnss_l76b.l76x_send_command(gnss_l76b.SET_SYNC_PPS_NMEA_ON)


# make an object of NMEA0183 sentence parser
"""
Setup GPS Object Status Flags, Internal Data Registers, etc
local_offset (int): Timzone Difference to UTC
location_formatting (str): Style For Presenting Longitude/Latitude:
                           Decimal Degree Minute (ddm) - 40° 26.767′ N
                           Degrees Minutes Seconds (dms) - 40° 26′ 46″ N
                           Decimal Degrees (dd) - 40.446° N
"""
parser = MicropyGPS(location_formatting='dd')

sentence = ''

while True:
    if gnss_l76b.uart_any():
        sentence = parser.update(chr(gnss_l76b.uart_receive_byte()[0]))
        if sentence:
            print('WGS84 Coordinate:Latitude(%c),Longitude(%c) %.9f,%.9f'%(parser.latitude[1],parser.longitude[1],parser.latitude[0],parser.longitude[0]))
            lat = parser.latitude[0]
            lon = parser.longitude[0]
            return [lat, lon]

read_gps()