// need to include bigboard_base.fth first on target

create all_on_image
&ffffff , &ffffff , &ffffff , &ffffff ,
&ffffff , &ffffff , &ffffff , &ffffff ,
&ffffff , &ffffff , &ffffff , &ffffff ,
&ffffff , &ffffff , &ffffff , &ffffff ,
&ffffff , &ffffff , &ffffff , &ffffff ,
align

create all_off_image
0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,
0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,
0 , 0 , 0 , 0 ,
align

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

\ converted from emily_ghost.g
create emily_ghost
32704 , 65504 , 65504 , 131056 ,
130672 , 237176 , 237560 , 524280 ,
519672 , 519676 , 521212 , 262140 ,
262142 , 262142 , 262143 , 262143 ,
262143 , 524287 , 474317 , 399556 ,
align
\ converted from emily_pumpkin.g
create emily_pumpkin
28672 , 21496 , 130052 , 393218 ,
524289 , 1049089 , 2097665 , 4196097 ,
4456449 , 4456449 , 9314369 , 8417474 ,
8388996 , 8455944 , 4324872 , 2161680 ,
1048608 , 524352 , 262528 , 261632 ,
align
\ converted from emily_spider.g
create emily_spider
0 , 3 , 12 , 16 ,
32 , 32320 , 130951 , 16767992 ,
130944 , 1048448 , 15850495 , 252800 ,
1959808 , 14745471 , 196608 , 786432 ,
15728640 , 0 , 0 , 0 ,
align
\ converted from skull.g
create skull
262112 , 524272 , 1048568 , 1048568 ,
1015672 , 933432 , 793624 , 933432 ,
1015672 , 1043448 , 519152 , 519152 ,
262112 , 131008 , 98112 , 87360 ,
87360 , 120256 , 131008 , 65408 ,
align
\ converted from pumpkin_eyes_1a.g
create pumpkin_eyes_1a
3145731 , 3670023 , 4063263 , 4178175 ,
4088271 , 4088271 , 0 , 0 ,
0 , 0 , 0 , 0 ,
0 , 0 , 0 , 0 ,
0 , 0 , 0 , 0 ,
align
\ converted from pumpkin_eyes_1b.g
create pumpkin_eyes_1b
3145731 , 3670023 , 4063263 , 4178175 ,
3989919 , 3989919 , 0 , 0 ,
0 , 0 , 0 , 0 ,
0 , 0 , 0 , 0 ,
0 , 0 , 0 , 0 ,
align
\ converted from pumpkin_eyes_1c.g
create pumpkin_eyes_1c
3145731 , 3670023 , 4063263 , 4178175 ,
3793215 , 3793215 , 0 , 0 ,
0 , 0 , 0 , 0 ,
0 , 0 , 0 , 0 ,
0 , 0 , 0 , 0 ,
align
\ converted from pumpkin_eyes_1d.g
create pumpkin_eyes_1d
3145731 , 3670023 , 4063263 , 4178175 ,
4137447 , 4137447 , 0 , 0 ,
0 , 0 , 0 , 0 ,
0 , 0 , 0 , 0 ,
0 , 0 , 0 , 0 ,
align
\ converted from face1.txt
create face1
16128 , 32640 , 458712 , 131040 ,
65472 , 65472 , 101472 , 217776 ,
363624 , 325576 , 28544 , 60864 ,
111456 , 183504 , 287112 , 16128 ,
0 , 0 , 0 , 0 ,
align
\ converted from face2.txt
create face2
16128 , 32640 , 65472 , 524280 ,
65472 , 65472 , 101472 , 86688 ,
232560 , 325576 , 290696 , 60864 ,
103008 , 180432 , 156048 , 16128 ,
0 , 0 , 0 , 0 ,
align
\ converted from face3.txt
create face3
16128 , 32640 , 65472 , 458712 ,
131040 , 65472 , 101472 , 86688 ,
99424 , 192464 , 290184 , 316104 ,
37440 , 49344 , 90528 , 409368 ,
0 , 0 , 0 , 0 ,
align
\ converted from face4.txt
create face4
16128 , 294792 , 196560 , 131040 ,
65472 , 35904 , 95136 , 86688 ,
232560 , 194512 , 290696 , 60864 ,
37440 , 246000 , 287112 , 16128 ,
0 , 0 , 0 , 0 ,
align
\ converted from jsw_demon1.txt
create jsw_demon1
0 , 0 , 0 , 0 ,
514 , 8706 , 43348 , 43224 ,
29028 , 8922 , 15150 , 9897 ,
9457 , 8411 , 8344 , 340 ,
0 , 0 , 0 , 0 ,
align
\ converted from jsw_demon2.txt
create jsw_demon2
0 , 0 , 0 , 0 ,
514 , 514 , 372 , 216 ,
20820 , 21226 , 9054 , 58793 ,
7921 , 6361 , 2201 , 2388 ,
1674 , 1024 , 0 , 0 ,
align
\ converted from jsw_demon3.txt
create jsw_demon3
0 , 0 , 0 , 0 ,
514 , 910 , 240 , 340 ,
730 , 950 , 4491 , 19113 ,
11227 , 38520 , 27856 , 1364 ,
650 , 256 , 128 , 64 ,
align


create led_sequence
emily_ghost , 20 ,
emily_pumpkin , 20 ,
emily_spider , 20 ,
skull , 20 ,
all_off_image , 5 ,

pumpkin_eyes_1a , 5 , 
pumpkin_eyes_1b , 5 , 
pumpkin_eyes_1c , 5 , 
pumpkin_eyes_1d , 5 , 
pumpkin_eyes_1a , 5 , 
pumpkin_eyes_1b , 5 , 
pumpkin_eyes_1c , 5 , 
pumpkin_eyes_1d , 5 , 
pumpkin_eyes_1a , 5 , 
pumpkin_eyes_1b , 5 , 
pumpkin_eyes_1c , 5 , 
pumpkin_eyes_1d , 5 , 
all_off_image , 5 ,

face1 , 5 ,
face2 , 5 ,
face3 , 5 ,
face4 , 5 ,
face1 , 5 ,
face2 , 5 ,
face3 , 5 ,
face4 , 5 ,
all_off_image , 5 ,

jsw_demon1 , 5 ,
jsw_demon2 , 5 ,
jsw_demon3 , 5 ,
jsw_demon1 , 5 ,
jsw_demon2 , 5 ,
jsw_demon3 , 5 ,
all_off_image , 5 ,

\ end of sequence
0 ,
align

\ ( sequence_address -- new_sequence_address )
: play_sequence
	dup @ dup 0= IF
		drop drop led_sequence
	ELSE
		( seq_addr image )
		swap CELL+ dup @ 
		( image seq_addr+4 time )
		swap CELL+ >R
			display
		R>
	THEN
;


: slideshow
	flash_led clear_keys ." Started" CR
	led_sequence
	BEGIN 
		play_sequence
	KEY? UNTIL
	drop
	flash_led
	." Finished"
;


FREERAM
