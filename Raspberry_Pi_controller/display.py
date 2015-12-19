#
#
# Python 3 required
#


import sys

if sys.version_info.major < 3:
    print("Python 3 required")
    exit(1)

import time
import serial



number_of_lines = 20        # split in show_image()

###########################################################################

all_off_image = [
    0, 0, 0, 0, 
    0, 0, 0, 0,
    0, 0, 0, 0, 
    0, 0, 0, 0,
    0, 0, 0, 0
]

all_on_image = [
    0xffffff, 0xffffff, 0xffffff, 0xffffff,
    0xffffff, 0xffffff, 0xffffff, 0xffffff,
    0xffffff, 0xffffff, 0xffffff, 0xffffff,
    0xffffff, 0xffffff, 0xffffff, 0xffffff,
    0xffffff, 0xffffff, 0xffffff, 0xffffff,
]

###########################################################################
#import xmas
###########################################################################

# converted from Bauble.txt
bauble = [
0 , 6144 , 9216 , 6144 ,
15360 , 49920 , 114816 , 145472 ,
460320 , 311712 , 1048560 , 699056 ,
873808 , 1048560 , 460320 , 319968 ,
138304 , 66432 , 49920 , 15360 ,
]

# converted from xmas tree inv 0.r
xmas_tree_inv_0 = [
0 , 5120 , 8704 , 5120 ,
8704 , 16640 , 32896 , 16640 ,
32896 , 65600 , 131104 , 32896 ,
65600 , 131104 , 262160 , 524296 ,
5120 , 5120 , 32512 , 15872 ,
]

# converted from xmas tree inv 1.r
xmas_tree_inv_1 = [
2048 , 5120 , 8704 , 5120 ,
8704 , 17664 , 32896 , 17664 ,
32896 , 67648 , 147488 , 32896 ,
65600 , 147488 , 263248 , 655368 ,
5120 , 5120 , 32512 , 15872 ,
]

# converted from xmas tree inv 2.r
xmas_tree_inv_2 = [
0 , 5120 , 8704 , 5120 ,
12800 , 16640 , 41088 , 16640 ,
32896 , 65856 , 147488 , 32896 ,
67904 , 131104 , 262160 , 524296 ,
5120 , 5120 , 32512 , 15872 ,
]

# converted from xmas tree inv 4.r
xmas_tree_inv_4 = [
2048 , 5120 , 8704 , 5120 ,
12800 , 17664 , 41088 , 17664 ,
32896 , 67904 , 147488 , 32896 ,
67904 , 147488 , 263248 , 655368 ,
5120 , 5120 , 32512 , 15872 ,
]


# converted from Holly.r
Holly = [
0 , 0 , 0 , 0 ,
1966140 , 1966140 , 2081276 , 2081276 ,
508400 , 522224 , 522224 , 63360 ,
14208 , 49152 , 109568 , 129536 ,
56832 , 3072 , 0 , 0 ,
]

# converted from House and trees.r
House_and_trees = [
2 , 2055 , 5148 , 8762 ,
16640 , 8421552 , 12653681 , 14811185 ,
12850195 , 15204363 , 16252943 , 14859943 ,
15739395 , 16427687 , 14690831 , 15739395 ,
16268807 , 16525839 , 13642271 , 13647365 ,
]

# converted from Santa in his sleigh.r
Santa_in_his_sleigh = [
0 , 0 , 2244608 , 1323008 ,
1865728 , 4093952 , 8335360 , 8353792 ,
4684928 , 4423488 , 4324928 , 4194392 ,
4194372 , 2097282 , 1048706 , 1048322 ,
279042 , 279044 , 2097144 , 0 ,
]

# converted from Star.r
Star = [
0 , 0 , 4096 , 4096 ,
14336 , 14336 , 31744 , 1048544 ,
524224 , 130816 , 65024 , 130816 ,
126720 , 247680 , 196992 , 0 ,
0 , 0 , 0 , 0 ,
]

# converted from ho ho santa.g
ho_ho_santa = [
0 , 5243872 , 7343128 , 5257220 ,
16386 , 2113538 , 5277682 , 5347340 ,
2355748 , 245762 , 5353466 , 7356414 ,
5258270 , 15934 , 2113534 , 5251068 ,
5251068 , 2101240 , 1008 , 0 ,
]
 

# converted from §.r
present = [
0 , 65664 , 181056 , 140352 ,
130944 , 32256 , 524256 , 318240 ,
318240 , 301344 , 268320 , 524256 ,
524256 , 268320 , 268320 , 268320 ,
268320 , 268320 , 524256 , 0 ,
]


# converted from happy new year.g
happy_new_year = [
9018833 , 9065802 , 16506308 , 9064708 ,
9064708 , 0 , 0 , 1145352 ,
1655304 , 1405264 , 1261904 , 1144992 ,
0 , 0 , 2290488 , 1344676 ,
583608 , 558244 , 586916 , 0 ,
]


# converted from angel.r
angel = [
15360 , 16896 , 15360 , 0 ,
6144 , 9216 , 3686940 , 4473378 ,
4334658 , 8460417 , 8447745 , 8430849 ,
8463489 , 8536641 , 8667681 , 8929809 ,
8978193 , 5252106 , 2106372 , 26112 ,
]


# converted from gingerbread man3.r
gingerbread_man3 = [
32256 , 33024 , 65664 , 74880 ,
65664 , 42240 , 39168 , 983280 ,
1048584 , 1054728 , 923760 , 65664 ,
71808 , 71808 , 131136 , 262176 ,
539664 , 1098504 , 1245384 , 786480 ,
]


# converted from rudolph.r
rudolph = [
163840 , 1032192 , 163840 , 163840 ,
2031616 , 2129920 , 13139456 , 12583392 ,
3932190 , 131089 , 131089 , 131088 ,
262176 , 655296 , 656448 , 656448 ,
1180736 , 1312896 , 1312896 , 2361472 ,
]


# converted from rudolph2.r
rudolph2 = [
1081344 , 3211264 , 5472256 , 1966080 ,
786432 , 1277952 , 2637824 , 12595201 ,
12587007 , 3932163 , 131074 , 65538 ,
65538 , 2031618 , 2229234 , 4521554 ,
10027082 , 10813481 , 4489254 , 196636 ,
]


# converted from ho ho santa closed mouth.g
ho_ho_santa_closed_mouth = [
0 , 5243872 , 7343128 , 5257220 ,
16386 , 2113538 , 5277682 , 5347340 ,
2355748 , 245762 , 5353466 , 7356414 ,
5258814 , 16382 , 2113534 , 5251068 ,
5251068 , 2101240 , 1008 , 0 ,
]

# converted from snowman2.r
snowman2 = [
0 , 0 , 15360 , 16896 ,
33024 , 74880 , 65664 , 71808 ,
2133248 , 1131142 , 4078716 , 4456486 ,
268324 , 268320 , 262176 , 268320 ,
137280 , 65664 , 49920 , 15360 ,
]

xmas_list = [
    [ xmas_tree_inv_0, 5],
    [ xmas_tree_inv_1, 5],
    [ xmas_tree_inv_2, 5],
    [ xmas_tree_inv_4, 5],
    [ xmas_tree_inv_1, 5],
    [ xmas_tree_inv_2, 5],
    [ xmas_tree_inv_4, 5],
    [ xmas_tree_inv_1, 5],
    [ xmas_tree_inv_2, 5],
    [ xmas_tree_inv_4, 5],
    [ xmas_tree_inv_0, 5],
    [ all_off_image, 10],
    [ bauble, 20],
    [ Holly, 20],
    [ House_and_trees, 20],
    [ Santa_in_his_sleigh, 20],
    [ Star, 20],
    [ ho_ho_santa, 5],
    [ ho_ho_santa_closed_mouth, 5],
    [ ho_ho_santa, 5],
    [ ho_ho_santa_closed_mouth, 5],
    [ ho_ho_santa, 5],
    [ ho_ho_santa_closed_mouth, 5],
    
    # New pictures
    [ rudolph, 20],
    [ present, 20],
    [ happy_new_year, 20],
    [ angel, 20],
    [ gingerbread_man3, 20],
    [ rudolph2, 20],
    [ snowman2, 20],
    
    [ all_off_image, 10],
]

###########################################################################
#import halloween
###########################################################################
# converted from emily_ghost.g
emily_ghost = [
32704 , 65504 , 65504 , 131056 ,
130672 , 237176 , 237560 , 524280 ,
519672 , 519676 , 521212 , 262140 ,
262142 , 262142 , 262143 , 262143 ,
262143 , 524287 , 474317 , 399556 ,
]

# converted from emily_pumpkin.g
emily_pumpkin = [
28672 , 21496 , 130052 , 393218 ,
524289 , 1049089 , 2097665 , 4196097 ,
4456449 , 4456449 , 9314369 , 8417474 ,
8388996 , 8455944 , 4324872 , 2161680 ,
1048608 , 524352 , 262528 , 261632 ,
]

# converted from emily_spider.g
emily_spider = [
0 , 3 , 12 , 16 ,
32 , 32320 , 130951 , 16767992 ,
130944 , 1048448 , 15850495 , 252800 ,
1959808 , 14745471 , 196608 , 786432 ,
15728640 , 0 , 0 , 0 ,
]

# converted from skull.g
skull = [
262112 , 524272 , 1048568 , 1048568 ,
1015672 , 933432 , 793624 , 933432 ,
1015672 , 1043448 , 519152 , 519152 ,
262112 , 131008 , 98112 , 87360 ,
87360 , 120256 , 131008 , 65408 ,
]

# converted from pumpkin_eyes_1a.g
pumpkin_eyes_1a = [
3145731 , 3670023 , 4063263 , 4178175 ,
4088271 , 4088271 , 0 , 0 ,
0 , 0 , 0 , 0 ,
0 , 0 , 0 , 0 ,
0 , 0 , 0 , 0 ,
]

# converted from pumpkin_eyes_1b.g
pumpkin_eyes_1b = [
3145731 , 3670023 , 4063263 , 4178175 ,
3989919 , 3989919 , 0 , 0 ,
0 , 0 , 0 , 0 ,
0 , 0 , 0 , 0 ,
0 , 0 , 0 , 0 ,
]

# converted from pumpkin_eyes_1c.g
pumpkin_eyes_1c = [
3145731 , 3670023 , 4063263 , 4178175 ,
3793215 , 3793215 , 0 , 0 ,
0 , 0 , 0 , 0 ,
0 , 0 , 0 , 0 ,
0 , 0 , 0 , 0 ,
]

# converted from pumpkin_eyes_1d.g
pumpkin_eyes_1d = [
3145731 , 3670023 , 4063263 , 4178175 ,
4137447 , 4137447 , 0 , 0 ,
0 , 0 , 0 , 0 ,
0 , 0 , 0 , 0 ,
0 , 0 , 0 , 0 ,
]

# converted from face1.txt
face1 = [
16128 , 32640 , 458712 , 131040 ,
65472 , 65472 , 101472 , 217776 ,
363624 , 325576 , 28544 , 60864 ,
111456 , 183504 , 287112 , 16128 ,
0 , 0 , 0 , 0 ,
]

# converted from face2.txt
face2 = [
16128 , 32640 , 65472 , 524280 ,
65472 , 65472 , 101472 , 86688 ,
232560 , 325576 , 290696 , 60864 ,
103008 , 180432 , 156048 , 16128 ,
0 , 0 , 0 , 0 ,
]

# converted from face3.txt
face3 = [
16128 , 32640 , 65472 , 458712 ,
131040 , 65472 , 101472 , 86688 ,
99424 , 192464 , 290184 , 316104 ,
37440 , 49344 , 90528 , 409368 ,
0 , 0 , 0 , 0 ,
]

# converted from face4.txt
face4 = [
16128 , 294792 , 196560 , 131040 ,
65472 , 35904 , 95136 , 86688 ,
232560 , 194512 , 290696 , 60864 ,
37440 , 246000 , 287112 , 16128 ,
0 , 0 , 0 , 0 ,
]

# converted from jsw_demon1.txt
jsw_demon1 = [
0 , 0 , 0 , 0 ,
514 , 8706 , 43348 , 43224 ,
29028 , 8922 , 15150 , 9897 ,
9457 , 8411 , 8344 , 340 ,
0 , 0 , 0 , 0 ,
]

# converted from jsw_demon2.txt
jsw_demon2 = [
0 , 0 , 0 , 0 ,
514 , 514 , 372 , 216 ,
20820 , 21226 , 9054 , 58793 ,
7921 , 6361 , 2201 , 2388 ,
1674 , 1024 , 0 , 0 ,
]

# converted from jsw_demon3.txt
jsw_demon3 = [
0 , 0 , 0 , 0 ,
514 , 910 , 240 , 340 ,
730 , 950 , 4491 , 19113 ,
11227 , 38520 , 27856 , 1364 ,
650 , 256 , 128 , 64 ,
]



halloween_list = [
    [ emily_ghost , 20],
    [ emily_pumpkin , 20],
    [ emily_spider , 20],
    [ skull , 20],
    [ all_off_image , 5],
    
    [ pumpkin_eyes_1a , 5],
    [ pumpkin_eyes_1b , 5],
    [ pumpkin_eyes_1c , 5],
    [ pumpkin_eyes_1d , 5],
    [ pumpkin_eyes_1a , 5],
    [ pumpkin_eyes_1b , 5],
    [ pumpkin_eyes_1c , 5],
    [ pumpkin_eyes_1d , 5],
    [ pumpkin_eyes_1a , 5],
    [ pumpkin_eyes_1b , 5],
    [ pumpkin_eyes_1c , 5],
    [ pumpkin_eyes_1d , 5],
    [ all_off_image , 5],
    
    [ face1 , 5],
    [ face2 , 5],
    [ face3 , 5],
    [ face4 , 5],
    [ face1 , 5],
    [ face2 , 5],
    [ face3 , 5],
    [ face4 , 5],
    [ all_off_image , 5],
    
    [ jsw_demon1 , 5],
    [ jsw_demon2 , 5],
    [ jsw_demon3 , 5],
    [ jsw_demon1 , 5],
    [ jsw_demon2 , 5],
    [ jsw_demon3 , 5],
    [ all_off_image , 5],
]

###########################################################################

def locally_print_image(image):
    for line in image:
        pic = "{0:24b}".format(line)
        pic = pic.replace("0", " ")
        pic = pic.replace("1", "o")
        print(pic)

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



# There is a 16 byte hardware buffer for both UARTS, but
# no overrun protection.
#   #TIB    -> length of input buffer
#   TIB     -> start of text input buffer
#   SOURCE  -> start of source for processing, and length to process. address = TIB usually
#   PAD     ->  c-addr is the address of a transient region that can be used to hold data for intermediate processing. 
"""
  80 CELLS VSPACE$ in
variable ptr

: display_cmd
    5 *
    FOR
        dup display1
        KEY? IF
            KEY ptr !
        END
    NEXT
    drop
;
"""



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

my_ser = None

def establish_comms():
    global ser
    ser = serial.Serial ("/dev/ttyUSB0", 115200, timeout=0.2)    #Open named port
    
    reset_display()
    release_display()
    time.sleep(0.5)
    
    print_read_all()

def test_command():
    establish_comms()
    
    send_line("")
    print_read_all()
    send_line("12 25 + .")
    print_read_all()
    time.sleep(1)
    print_read_all()

def all_on_command():
    establish_comms()
    
    display_all_on()
    miniterm()

def halloween_slideshow():
    establish_comms()
    
    pass

def xmas_slideshow():
    establish_comms()
    
    pass

def new_command():
    establish_comms()
    
    success = load_file("rpi_base.fth")
    if not success:
        miniterm()

def demo_xmas_command():
    for display in xmas_list:
        locally_print_image(display[0])
        time.sleep(display[1]/10)

def demo_halloween_command():
    for display in halloween_list:
        locally_print_image(display[0])
        time.sleep(display[1]/10)

command_list = []

def help_command():
    print(" ")
    print("List of accepted commands")
    print("=========================")
    for c in command_list:
        print("%14s - %s" % (c[0], c[2]))

command_list = [
    [ "test", test_command, "Send a simple sequence to the Forth board to test communication", ],
    [ "term", miniterm, "Start a crude terminal with access to the Forth board", ],
    [ "all", all_on_command, "Turn all the LEDS on for 1 second, then go into terminal mode"],
    [ "xmas", xmas_slideshow, "Do the Xmas slideshow"],
    [ "halloween", halloween_slideshow, "Do the Halloween slideshow"],
    [ "new", new_command, "initialise forth board with base word set"],
    [ "help", help_command, "show this list"],
    [ "demo_xmas", demo_xmas_command, "Show xmas locally only"],
    [ "demo_halloween", demo_halloween_command, "Show Halloween locally only"],
]

#if len(sys.argv) == 1:
#    cmd = "term"
if len(sys.argv) == 2:
    cmd = sys.argv[1]
else:
    print("Unknown arguments")
    print(sys.argv)
    print("Type help for help")
    exit(1)

cmd = cmd.strip().lower()
for c in command_list:
    if c[0] == cmd:
        c[1]()
        break

# close off any serial connection
if ser:
    ser.close()
print("-------- FINISHED --------")



