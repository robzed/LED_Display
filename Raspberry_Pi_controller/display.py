
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
    bbytes = data.rstrip().encode('ascii')
    for c in bbytes:
        ser.write(bytes([c]))
        time.sleep(0.03)
    #print(len(newline))
    #print(newline)
    #time.sleep(0.1)
    #print(bbytes)
    ser.write(newline)
    time.sleep(0.05)

def print_read_all():
    data = ser.read(10000)
    #print(data)
    data = data.replace(b'\r\n', b'\r')
    data = data.replace(b'\r', b'\r\n')
    data = data.rstrip()
    print("[[[", data.decode('ascii'))

def check_read_all():
    data = ser.read(10000)
    data = data.replace(b'\r\n', b'\r')
    data = data.replace(b'\r', b'\r\n')
    data = data.rstrip()
    #print(data)
    sdata = data.decode('ascii')
    print("<<<", sdata)
    return sdata.endswith("ok <0>[]") and not "Duplicate word" in sdata, sdata
    # and not sdata.endswith("ok <0>[Underflow]")

blank_image = "20 CELLS VSPACE$ img "

# dimg ( tenths image <20-numbers> )
image_from_stack = ": dimg num_rows FOR I CELLS img + ! NEXT img swap display ;"


#all_on =    \
#"&ffffff &ffffff &ffffff &ffffff " +   \
#"&ffffff &ffffff &ffffff &ffffff " +   \
#"&ffffff &ffffff &ffffff &ffffff " +   \
#"&ffffff &ffffff &ffffff &ffffff " +   \
#"&ffffff &ffffff &ffffff &ffffff " +   \
#"&ffffff &ffffff &ffffff &ffffff " +   \
#"dimg"

def setup_basics():
    
    # make a data space
    send_line(blank_image)
    success, _ = check_read_all()
    if not success:
        print("------- ERROR - ABORTING -------")
        return False

    # make dimg
    send_line(image_from_stack)
    success, _ = check_read_all()
    if not success:
        print("------- ERROR - ABORTING -------")
        return False

    return True


number_of_lines = 20        # split in show_image()

def show_image(t, my_image):
    
    if len(my_image) != number_of_lines:
        print("--------- SHOW IMAGE SUPPLIED WTIH NOT 24 ------")
        return False

    params1 = [ str(int(t * 10)) ]

    for i in range(0,7):
        params1.append("&%x" % my_image[i])
    send_line(" ".join(params1))

    params2 = []
    for i in range(7,14):
        params2.append("&%x" % my_image[i])
    send_line(" ".join(params2))

    params3 = []
    for i in range(14,20):
        params3.append("&%x" % my_image[i])
    send_line(" ".join(params3) + " dimg")

    time.sleep(t)

    success, _ = check_read_all()
    if not success:
        print("------- ERROR - ABORTING -------")
        return False
    return True


def miniterm():
    while True:
        try:
            line = input("Enter:")
            send_line(line)
            print_read_all()
        except KeyboardInterrupt:
            break


def is_base_ok():
    send_line("RPi_BASE")
    success, data = check_read_all()
    if not success:
        print(" ---- ERROR - ABORTING ----- ")
        return False
    if "*YES*" not in data:
        print(" ---- ERROR - ABORTING ----- ")
        return False
    return True


def load_file(filename):
    #send_line("cold")
    send_line("new")
    success, _ = check_read_all()
    if not success:
        print("------- ERROR - ABORTING -------")
        return False
    
    f = open(filename, "r")
    data = f.readlines()
    f.close()

    define_mode = False
    for line in data:
        #print(line.encode('ascii'))
        templine = line.lstrip()
        if(templine.startswith("//")):
            print("Skipping comment line:", line.rstrip())
        elif(templine == ""):    # blank lines
            pass
        else:
            if templine.startswith(":"):
                define_mode = True
            send_line(line)
            success, _ = check_read_all()
            if success:
                define_mode = False
            elif not define_mode:
                print("------- ERROR - ABORTING -------")
                return False

    if not is_base_ok():
        return False
    
    send_line("save")
    success, data = check_read_all()
    if not success:
        print(" ---- ERROR - ABORTING ----- ")
        return False

    return True


def slideshow():
    if not is_base_ok():
        return
    if not setup_basics():
        return

def display_all_on():
    all_on = [ ]
    for i in range(number_of_lines):
        all_on.append(0xffffff)
    
    if not is_base_ok():
        return
    if not setup_basics():
        return
    if not show_image(1, all_on):
        return



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

if cmd == "show" or cmd == "slideshow":
    slideshow()

if cmd == "all":
    display_all_on()
    miniterm()

if cmd == "new":
    success = load_file("rpi_base.fth")
    if not success:
        miniterm()

print("-------- FINISHED --------")
ser.close()



