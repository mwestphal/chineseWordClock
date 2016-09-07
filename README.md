# chineseWordClock
A chinese word clock python script for rpi

Dependencies
============
python (2 or 3)
spidev
apa102pi

Installation
============

Connect a correct layout of led
it should be organized this way :
```
63 - 62 - 61 - 60 - 59 - 58 - 57 - 56 
                                    |
48 - 49 - 50 - 51 - 52 - 53 - 54 - 55
|
47 - 46 - 45 - 44 - 43 - 42 - 41 - 40
                                    |
32 - 33 - 34 - 35 - 36 - 37 - 38 - 39 
|
31 - 30 - 29 - 28 - 27 - 26 - 25 - 24
                                    | 
16 - 17 - 18 - 19 - 20 - 21 - 22 - 23 
|
15 - 14 - 13 - 12 - 11 - 10 - 9 -- 8
                                    |
0 -- 1 -- 2 -- 3 -- 4 -- 5 -- 6 -- 7 
```
with of correct the correct layout of chinese characters on top

Then connect the raspberry pi pin this way : 
 * Black -> GND
 * Blue-> SCLK
 * Green -> MOSI
 * Red -> Power

more info here :
https://github.com/tinue/APA102_Pi

Then run wordclock.sh at startup.

