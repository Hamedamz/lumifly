import serial
import struct
import time

ser = serial.Serial('/dev/serial0', 115200, timeout=1)

def create_msp_packet(command, data=b''):
    header = b'$M<'
    size = len(data)
    checksum = (size ^ command ^ sum(data)) & 0xFF
    packet = header + struct.pack('<BB', size, command) + data + struct.pack('<B', checksum)
    return packet

# Command to request attitude (MSP_ATTITUDE = 108)
MSP_ATTITUDE = 108
packet = create_msp_packet(MSP_ATTITUDE)

ser.write(packet)

time.sleep(0.1)
if ser.in_waiting:
    response = ser.read(ser.in_waiting)
    print("Response:", response)

ser.close()