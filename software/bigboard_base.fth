// port constants
&e002c000 constant PINSEL0
&e002c004 constant PINSEL1
&e002c014 constant PINSEL2
&e0028000 constant IO0PIN
&e0028004 constant IO0SET
&e0028008 constant IO0DIR
&e002800c constant IO0CLR
&e0028010 constant IO1PIN
&e0028014 constant IO1SET
&e0028018 constant IO1DIR
&e002801c constant IO1CLR

// move value to mask position, this is used for setting 
// particular bits using a mask, e.g. if the value is 
// 3 and the mask is &fff0ffff, then the value will 
// be &00030000 
// ( val, mask ---- val) 
: (B!) 
        31  for            
                1  rshiftc
                if
                        swap  1  lshift  swap    // value 
                else
                        leave
                then
        next
        drop
;                

// bit store. This is used for clearing and settings 
// bits of a word, needed for most registers 
// example: 
// to set bits 25:25 of pinsel1 to 2 
// 2 &FCFFFFFF PINSEL0, 
// any of the other bits in pinsel0 will not be affected 
// but bits 25:24 will be changed to 2 
// (value, mask, address ----) 
: B! 
        rot  2  pick            // mask, address, value, mask 
        (b!)                         // mask, address, new-value 
        rot                          // address, new-value, mask 
        2  pick  @                // address, new-val, mask, address-contents 
        and                          // address, new-val, new-contents(mask) 
        or                            // update contents 
        swap  !                    // save back 
;

// used as part of pinselect 
// pin is a value from 0 to 15 and function 
// is a value from 0 to 3, 0 is GPIO, 2 to 3 
// are the alternate functions 
// ( pin, function --- ) 
: (sel0) 
        swap                        // function, pin 
        2  *                                  // 2 bits per pin 
        3  swap  lshift  invert    // create mask 
        PINSEL0  b!                    // bit store, function, mask, address 
;        
// used as part of pinselect 
// pin is a value from 0 to 15 and function 
// is a value from 0 to 3, 0 is GPIO, 2 to 3 
// are the alternate functions 
// ( pin, function --- ) 
: (sel1) 
        swap                        // function, pin 
        2  *                                  // 2 bits per pin 
        3  swap  lshift  invert    // create mask 
        PINSEL1  b!                    // bit store, function, mask, address 
;        

// pin is a value from 0 to 31 and function 
// is a value from 0 to 3, 0 is GPIO, 2 to 3 
// are the alternate functions 
// determines which pinsel to use 
// Example: To select function 2 on pin 25 
// 25 2 pinselect 
// ( pin, function --- ) 
: pinselecter 
        swap                // PINSEL0 is 0-15, PINSEL1 is 16-31 
        dup  15  >  if    
                16  -  swap  (sel1)   
                else  
                          swap  (sel0) 
                then
;                        

: >mask 1 swap lshift ;

// clears two bits in the PINSEL1 or PINSEL2 registers
: p0_GPIO_mask
	32 FOR
		dup 1 and IF
			I 0 pinselecter
			." setting" I . CR
		THEN
		1 rshift
	NEXT
	drop
;

: p0set_mask IO0SET ! ;
: p1set_mask IO1SET ! ;
: p0clear_mask IO0CLR ! ;
: p1clear_mask IO1CLR ! ;
: p0set_bit >mask p0set_mask ;
: p1set_bit >mask p1set_mask ;
: p0clear_bit >mask p0clear_mask ;
: p1clear_bit >mask p1clear_mask ;


// ( ports_mask -- )
: p0_out_mask
	dup p0_GPIO_mask
	IO0DIR @
	or
	IO0DIR !
;

// ( ports_mask -- )
: p1_out_mask
	// make sure port 1 is GPIO 
	// The only other functions are debug and trace
	0  PINSEL2  !

	// configure the specific ports
	IO1DIR @
	or
	IO1DIR !
;

// ( port# -- )
: p0_out_bit
	>mask
	p0_out_mask
;

// ( ports_mask -- )
: p0_in_mask
    dup p0_GPIO_mask
	invert
    IO0DIR @
    and
    IO0DIR !
;

// ( port# --- )
: p0_in_bit
    >mask
;

31 constant led1
: led1_on led1 p0clear_bit ;
: led1_off led1 p0set_bit ;
: led1_setup led1 p0_out_bit ;

: clear_keys BEGIN key? WHILE key drop REPEAT ;
: flash_led led1_setup 3 for led1_on 100 ms led1_off 100 ms next ;


//
// The real program starts here...
//

// P0.2 to P0.6 (5 bits)
31 constant row_mask
2 constant row_bit_start
row_mask row_bit_start lshift constant row_mask_shifted

: row_setup row_mask_shifted p0_out_mask ;

// rows_off clears all bits to set all address lines...
: rows_off row_mask_shifted p0clear_mask ;

// ( row# -- )
: select_row 
	DUP
	0 row_mask BETWEEN
	// ( row# row# -- row# flag )
	// assumes: rows_off clears all bits to set all address lines...
	rows_off
	IF
		row_bit_start LSHIFT
		// we invert - to override transistors already
		invert
		row_mask_shifted AND
		p0set_mask
	ELSE
		." outside allowed row"
		DROP
	THEN 
;

// P0.22 to P0.23, P0.25 to P0.30, P1.16 to P1.31
// representing lowest bit column to highest bit column
// lowest bit of graphic show be wired to right-most LED
//
: write_column ( col_bitmap -- )
	// there are three ranges
	// first P1.16 to P1.31 (16 bits) - highest bits (left-most) of graphic
	&ffff0000 p1clear_mask
	dup &ffff00 and 8 lshift p1set_mask

	// second P0.25 to P0.30 (6 bits)
	&7e000000 p0clear_mask
	dup &fc and 23 lshift p0set_mask

	// third P0.22 to 0.23 (2 bits) - lowest bits (right-most) of graphic
	&00c00000 p0clear_mask
	&3 and 22 lshift p0set_mask
;

: column_setup
	// configure the correct pins as Output
	&ffff0000 p1_out_mask
	&7e000000 p0_out_mask
	&00c00000 p0_out_mask
;

20 constant num_rows
24 constant num_columns
4 constant bytes_per_row

// ( image -- )
: display1
	// originally envisaged to synchronise with the millisecond timer
	// 1 MS
	num_rows FOR
		dup @ write_column
		I select_row
		CELL+
		1 MS
		rows_off
	NEXT
	drop
;

// ( port# -- )
: test_port0
	// program port as an output
	." Testing port 0." dup . ." ->"
	dup p0_out_bit
	BEGIN
		dup p0set_bit ." 1"
		500 ms
		dup p0clear_bit ." 0"
		500 ms
	KEY? UNTIL
	KEY drop
	drop
	CR
;

// ( port# -- )
: test_port1
	// program port as an output
	." Testing port 1." dup . ." ->"
	BEGIN
		dup p1set_bit ." 1"
		500 ms
		dup p1clear_bit ." 0"
		500 ms
	KEY? UNTIL
	KEY drop
	drop
	CR
;

: (testports) { testing_func_xt portnum -- }
		portnum . ." - Test? Y/N" KEY CR
		dup [CHAR] y = 
		IF
			drop
			portnum testing_func_xt EXECUTE
		ELSE
			[CHAR] n <>
			IF
				." Unknown Key - Aborting"
				ABORT
			THEN
		THEN 
;

// type to test all ports
: testports
	clear_keys

	// test P0.0 to P0.31
	32 FOR
		." P0." ['] test_port0 I (testports)
	NEXT
	
	// test P1.16 to P1.31
	&ffff0000 p1_out_mask
	32 16 DO
		." P1." ['] test_port1 I (testports)
	LOOP

	." Finished"
;

: column_only_test
	column_setup
	24 FOR
	." Column = " I . 
	1 I lshift write_column

	clear_keys
	." (Press a key)" CR
	KEY drop
	NEXT
;

// ( image tenths_seconds_to_display -- )
: display
	5 *
	FOR
		dup display1
	NEXT
	drop
;
