
import time
import serial
import sys

ser = None

def reset_display():
    print("-------- RESET --------")
    ser.setDTR(1)
    ser.setRTS(0)
    time.sleep(0.2)


def release_display():
    print("-------- NORMAL --------")
    ser.setDTR(0)
    ser.setRTS(0)
    time.sleep(0.1)

newline = b"\r\n"
def send_line(data):
    ser.write(data.encode('ascii'))
    #print(len(newline))
    #print(newline)
    ser.write(newline)
    time.sleep(0.1)

def print_read_all():
    data = ser.read(10000)
    #print(data)
    data = data.replace(b'\r\n', b'\r')
    data = data.replace(b'\r', b'\r\n')
    print(data.decode('ascii'))

def miniterm():
    while True:
        try:
            line = input("Enter:")
            send_line(line)
            print_read_all()
        except KeyboardInterrupt:
            break


if len(sys.argv) == 1:
    cmd = "term"
elif len(sys.argv) == 2:
    cmd = sys.argv[1]
else:
    print("Unknown arguments")
    print(sys.argv)
    exit(1)

ser = serial.Serial ("/dev/ttyUSB0", 115200, timeout=0.2)    #Open named port
reset_display()
release_display()
time.sleep(0.5)

print_read_all()

if cmd == "test":
    send_line("")
    print_read_all()
    send_line("12 25 + .")
    print_read_all()
    time.sleep(1)
    print_read_all()

if cmd == "term":
    miniterm()


print("-------- FINISHED --------")
ser.close()      

