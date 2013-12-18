// need to include bigboard_base.fth first on target

: make_image create 
, , , , 
, , , , 
, , , , 
, , , , 
, , , ,
DOES> ;

&ffffff &ffffff &ffffff &ffffff
&ffffff &ffffff &ffffff &ffffff
&ffffff &ffffff &ffffff &ffffff
&ffffff &ffffff &ffffff &ffffff
&ffffff &ffffff &ffffff &ffffff
make_image all_on_image

0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0
make_image all_off_image

: display_setup column_setup row_setup rows_off ;

// show all leds on for 2 seconds
: all_on display_setup all_on_image 20 display ;

// show all leds off for 2 seconds
: all_off display_setup all_off_image 20 display ;

// HERE .
num_rows bytes_per_row * VSPACE$ buf
// HERE .
num_rows bytes_per_row * VSPACE$ buf2
// HERE .
// ." buf=" buf .
// ." buf2=" buf2 .

: init_display
	display_setup
	buf 3 and abort" Test image buffer not aligned"
	buf2 3 and abort" Test image buffer 2 not aligned"
;

: clear_buf
	num_rows FOR
		0 buf I CELLS + !
	next
;

// display single pixel moving to each pixel for third of a second
: test_image
	init_display clear_buf
	num_rows FOR
		num_columns FOR
			1 I lshift
			buf J CELLS + !
			buf 1 display
			0 buf j CELLS + !
		NEXT
	NEXT
;

: test_bounce
	init_display clear_buf
	num_rows 2/ FOR
		num_columns FOR
			1 I lshift
			buf J 2* CELLS + !
			buf 1 display
			0 buf j 2* CELLS + !
		NEXT
		num_columns FOR
			1 num_columns 1- I - lshift
			buf J 2* 1+ CELLS + !
			buf 1 display
			0 buf j 2* 1+ CELLS + !
		NEXT
	NEXT
;

( image -- )
: show display_setup 20 display ;

( start_address end_address -- )
: save_data 
	create
	BEGIN
	2dup <>
	WHILE
		over @ ,
		SWAP CELL+
		SWAP
	REPEAT
	2drop
	DOES>
;

\ converted from Bauble.txt
HERE
0 , 6144 , 9216 , 6144 ,
15360 , 49920 , 114816 , 145472 ,
460320 , 311712 , 1048560 , 699056 ,
873808 , 1048560 , 460320 , 319968 ,
138304 , 66432 , 49920 , 15360 ,
HERE
save_data Bauble

\ converted from xmas tree inv 0.r
HERE
0 , 5120 , 8704 , 5120 ,
8704 , 16640 , 32896 , 16640 ,
32896 , 65600 , 131104 , 32896 ,
65600 , 131104 , 262160 , 524296 ,
5120 , 5120 , 32512 , 15872 ,
HERE
save_data xmas_tree_inv_0
\ converted from xmas tree inv 1.r
HERE
2048 , 5120 , 8704 , 5120 ,
8704 , 17664 , 32896 , 17664 ,
32896 , 67648 , 147488 , 32896 ,
65600 , 147488 , 263248 , 655368 ,
5120 , 5120 , 32512 , 15872 ,
HERE
save_data xmas_tree_inv_1
\ converted from xmas tree inv 2.r
HERE
0 , 5120 , 8704 , 5120 ,
12800 , 16640 , 41088 , 16640 ,
32896 , 65856 , 147488 , 32896 ,
67904 , 131104 , 262160 , 524296 ,
5120 , 5120 , 32512 , 15872 ,
HERE
save_data xmas_tree_inv_2
\ converted from xmas tree inv 4.r
HERE
2048 , 5120 , 8704 , 5120 ,
12800 , 17664 , 41088 , 17664 ,
32896 , 67904 , 147488 , 32896 ,
67904 , 147488 , 263248 , 655368 ,
5120 , 5120 , 32512 , 15872 ,
HERE
save_data xmas_tree_inv_4

\ converted from Holly.r
HERE
0 , 0 , 0 , 0 ,
1966140 , 1966140 , 2081276 , 2081276 ,
508400 , 522224 , 522224 , 63360 ,
14208 , 49152 , 109568 , 129536 ,
56832 , 3072 , 0 , 0 ,
HERE
save_data Holly
\ converted from House and trees.r
HERE
2 , 2055 , 5148 , 8762 ,
16640 , 8421552 , 12653681 , 14811185 ,
12850195 , 15204363 , 16252943 , 14859943 ,
15739395 , 16427687 , 14690831 , 15739395 ,
16268807 , 16525839 , 13642271 , 13647365 ,
HERE
save_data House_and_trees
\ converted from Santa in his sleigh.r
HERE
0 , 0 , 2244608 , 1323008 ,
1865728 , 4093952 , 8335360 , 8353792 ,
4684928 , 4423488 , 4324928 , 4194392 ,
4194372 , 2097282 , 1048706 , 1048322 ,
279042 , 279044 , 2097144 , 0 ,
HERE
save_data Santa_in_his_sleigh
\ converted from Star.r
HERE
0 , 0 , 4096 , 4096 ,
14336 , 14336 , 31744 , 1048544 ,
524224 , 130816 , 65024 , 130816 ,
126720 , 247680 , 196992 , 0 ,
0 , 0 , 0 , 0 ,
HERE
save_data Star
\ converted from ho ho santa.g
HERE
0 , 5243872 , 7343128 , 5257220 ,
16386 , 2113538 , 5277682 , 5347340 ,
2355748 , 245762 , 5353466 , 7356414 ,
5258270 , 15934 , 2113534 , 5251068 ,
5251068 , 2101240 , 1008 , 0 ,
HERE
save_data ho_ho_santa 

\ converted from Present.r
HERE
0 , 65664 , 181056 , 140352 ,
130944 , 32256 , 524256 , 318240 ,
318240 , 301344 , 268320 , 524256 ,
524256 , 268320 , 268320 , 268320 ,
268320 , 268320 , 524256 , 0 ,
HERE
save_data Present

\ converted from happy new year.g
HERE
9018833 , 9065802 , 16506308 , 9064708 ,
9064708 , 0 , 0 , 1145352 ,
1655304 , 1405264 , 1261904 , 1144992 ,
0 , 0 , 2290488 , 1344676 ,
583608 , 558244 , 586916 , 0 ,
HERE
save_data happy_new_year

\ converted from angel.r
HERE
15360 , 16896 , 15360 , 0 ,
6144 , 9216 , 3686940 , 4473378 ,
4334658 , 8460417 , 8447745 , 8430849 ,
8463489 , 8536641 , 8667681 , 8929809 ,
8978193 , 5252106 , 2106372 , 26112 ,
HERE
save_data angel

\ converted from gingerbread man3.r
HERE
32256 , 33024 , 65664 , 74880 ,
65664 , 42240 , 39168 , 983280 ,
1048584 , 1054728 , 923760 , 65664 ,
71808 , 71808 , 131136 , 262176 ,
539664 , 1098504 , 1245384 , 786480 ,
HERE
save_data gingerbread_man3

\ converted from rudolph.r
HERE
163840 , 1032192 , 163840 , 163840 ,
2031616 , 2129920 , 13139456 , 12583392 ,
3932190 , 131089 , 131089 , 131088 ,
262176 , 655296 , 656448 , 656448 ,
1180736 , 1312896 , 1312896 , 2361472 ,
HERE
save_data rudolph

\ converted from rudolph2.r
HERE
1081344 , 3211264 , 5472256 , 1966080 ,
786432 , 1277952 , 2637824 , 12595201 ,
12587007 , 3932163 , 131074 , 65538 ,
65538 , 2031618 , 2229234 , 4521554 ,
10027082 , 10813481 , 4489254 , 196636 ,
HERE
save_data rudolph2

\ converted from ho ho santa closed mouth.g
HERE
0 , 5243872 , 7343128 , 5257220 ,
16386 , 2113538 , 5277682 , 5347340 ,
2355748 , 245762 , 5353466 , 7356414 ,
5258814 , 16382 , 2113534 , 5251068 ,
5251068 , 2101240 , 1008 , 0 ,
HERE
save_data ho_ho_santa_closed_mouth

\ converted from snowman2.r
HERE
0 , 0 , 15360 , 16896 ,
33024 , 74880 , 65664 , 71808 ,
2133248 , 1131142 , 4078716 , 4456486 ,
268324 , 268320 , 262176 , 268320 ,
137280 , 65664 , 49920 , 15360 ,
HERE
save_data snowman2



: disp_quit display KEY? IF QUIT THEN ;

: show_all
xmas_tree_inv_0 5 disp_quit
xmas_tree_inv_1 5 disp_quit
xmas_tree_inv_2 5 disp_quit
xmas_tree_inv_4 5 disp_quit
xmas_tree_inv_1 5 disp_quit
xmas_tree_inv_2 5 disp_quit
xmas_tree_inv_4 5 disp_quit
xmas_tree_inv_1 5 disp_quit
xmas_tree_inv_2 5 disp_quit
xmas_tree_inv_4 5 disp_quit
xmas_tree_inv_0 5 disp_quit
all_off_image 10 disp_quit
bauble 20 disp_quit
Holly 20 disp_quit
House_and_trees 20 disp_quit
Santa_in_his_sleigh 20 disp_quit
Star 20 disp_quit
ho_ho_santa 5 disp_quit
ho_ho_santa_closed_mouth 5 disp_quit
ho_ho_santa 5 disp_quit
ho_ho_santa_closed_mouth 5 disp_quit
ho_ho_santa 5 disp_quit
ho_ho_santa_closed_mouth 5 disp_quit

\ New pictures
rudolph 20 disp_quit
present 20 disp_quit
happy_new_year 20 disp_quit
angel 20 disp_quit
gingerbread_man3 20 disp_quit
rudolph2 20 disp_quit
snowman2 20 disp_quit

all_off_image 10 disp_quit
;

: show_all_loop
	all_on
	flash_led clear_keys ." Started" CR

	BEGIN 	
	show_all
	KEY? UNTIL

	flash_led
	." Finished"
	QUIT
;

FREERAM
