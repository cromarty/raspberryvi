<!-- 
.. title: Raspberry Pi GPIO Bus Pinouts
.. slug: raspberry-pi-gpio-bus-pinouts
.. date: 2015-01-12 11:50:04 UTC
.. tags: Raspberry Pi, GPIO
.. category: Reference
.. link: 
.. description: Blind-friendly Raspberry Pi GPIO Bus Pinouts
.. type: text
-->

The tables on this page show the pin-outs for the GPIO header on the [Raspberry Pi][rpi] connector.  
This is the double row of closely spaced pins on the top-side of the board, in the upper left corner 
if the board is held with the USB connector on the right-hand edge of the board.

With the board held in this orientation, the top row of pins are numbered with even numbers from two 
to twenty-six, left to right.  This is the row of pins closest to the top edge of the board.

The lower row are numbered with odd numbers from 1 to twenty-five.

Don't attempt to connect anything to these pins unless you are sure you know what you are doing.  
There are plenty of projects and notes about interfacing to the GPIO bus on the [Raspberry Pi 
Foundation][rpi] web pages and elsewhere.

I cannot be held responsible for any damage caused to a Raspberry Pi by incorrect or imprudent use 
of the GPIO pins.

Also be aware that the Raspberry Pi hardware is static sensitive.  Do not be tempted to touch the GPIO pins casually, even if the box you have used has a cut-out to allow for external connection of a header cable or adaptor.

Pay close attention to the revision number of your board.

To get the revision number of your board, issue the following command:

	cat /proc/cpuinfo

There will be one line which prints a line starting with 'Revision' and a hexadecimal number.  If 
the number is 4, 5, 6, 14 (e) or 15 (f), you have a revision 2 board.

Another way to tell between revision 1 and 2 boards is to look for the 2 millimetre mounting hole 
just to the left of the USB connector, if you are holding the board in front of you with the short 
side and the USB connector away from you.  You can find this hole with your thumbnail or the point 
of a pencil (without power connected).

To connect a header plug, or any other device into the GPIO header; first shutdown any operating 
system that is running on the Pi.  Disconnect all the cables and make sure your body and your hands 
are at the same potential as the board.  I do this by only handling the board with my forearms 
planted firmly on the table surface.  Offer any plug to the GPIO pins very gently and don't force it 
on.  It is very easy to bend the pins on the header and a few moments taken to do this very 
carefully could avoid permanent damage to your Raspi.

So far I have only connected a full 26 way IDC plug to each of my Raspis and I would recommend you 
invest in something like an Adafruit Cobbler.  Using such a device you could plug into the Raspi 
just once and then make any changes at the other end of the ribbon cable, thus minimising any 
potential for accidents.

It's cheaper and less distressing to destroy the other end of a ribbon cable than it is to break your precious little computer.

If you want to connect something to the GPIO pins other than a full 26-way header, like a 2-wire 
connector for the I2C serial line, confirm you have connected to the correct pins by counting along 
the line of unconnected pins with a fingernail, gently.  Do this several times.  The old carpentry 
maxim of 'measure twice, cut once' is a good one.

Under no circumstances attempt to solder direct to the GPIO pins, even if you get someone who can 
see to do this for you.  The stray currents present on the tip of a soldering iron can be death to 
the delicate insides of the SoC, and nasty solder on those nice gold pins will stop you connecting a 
header plug at a later time.

_Note:_ Added 2014-07-18: The additional fourteen pins on the new Model B+ are now shown in two new 
tables at the bottom of this page.  As before the evenly numbered pins are those closest to the edge 
of the board and the oddly numbered pins are furthest from the edge of the board.

_Note_ Added 2015-11-28: The Pi Zero, released on the 26th of November 2015, has a 40-pin GPIO bus 
which is pin-for-pin compatible with a Model B+ Version 2.

## P1 Header Pinout, top row:

<!-- TABLE 1 -->
<table cellspacing="0" border="0">
	<colgroup span="6" width="85"></colgroup>
	<tr>
		<td height="17" align="left">Pin Number</td>
		<td align="left">Pin Name Rev1</td>
		<td align="left">Pin Name Rev2</td>
		<td align="left">Hardware Notes</td>
		<td align="left">Alt 0 Function</td>
		<td align="left">Other Alternative Functions</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-02</td>
		<td align="left">5V0</td>
		<td align="left">5V0</td>
		<td align="left">Supply through input poly fuse</td>
		<td align="center">-</td>
		<td align="center">-</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-04</td>
		<td align="left">5V0</td>
		<td align="left">5V0</td>
		<td align="left">Supply through input poly fuse</td>
		<td align="center">-</td>
		<td align="center">-</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-06</td>
		<td align="left">GND</td>
		<td align="left">GND</td>
		<td align="center">-</td>
		<td align="center">-</td>
		<td align="center">-</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-08</td>
		<td align="left">GPIO 14</td>
		<td align="left">GPIO 14</td>
		<td align="left">Boot to Alt 0 -&gt;</td>
		<td align="left">UART0_TXD</td>
		<td align="left">ALT5 = UART1_TXD</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-10</td>
		<td align="left">GPIO 15</td>
		<td align="left">GPIO 15</td>
		<td align="left">Boot to Alt 0 -&gt;</td>
		<td align="left">UART0_RXD</td>
		<td align="left">ALT5 = UART1_RXD</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-12</td>
		<td align="left">GPIO 18</td>
		<td align="left">GPIO 18</td>
		<td align="center">-</td>
		<td align="left">PCM_CLK</td>
		<td align="left">ALT4 = SPI1_CE0_N ALT5 = PWM0</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-14</td>
		<td align="left">GND</td>
		<td align="left">GND</td>
		<td align="center">-</td>
		<td align="center">-</td>
		<td align="center">-</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-16</td>
		<td align="left">GPIO23</td>
		<td align="left">GPIO23</td>
		<td align="center">-</td>
		<td align="center">-</td>
		<td align="left">ALT3 = SD1_CMD ALT4 = ARM_RTCK</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-18</td>
		<td align="left">GPIO24</td>
		<td align="left">GPIO24</td>
		<td align="center">-</td>
		<td align="center">-</td>
		<td align="left">ALT3 = SD1_DAT0 ALT4 = ARM_TDO</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-20</td>
		<td align="left">GND</td>
		<td align="left">GND</td>
		<td align="center">-</td>
		<td align="center">-</td>
		<td align="center">-</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-22</td>
		<td align="left">GPIO25</td>
		<td align="left">GPIO25</td>
		<td align="center">-</td>
		<td align="center">-</td>
		<td align="left">ALT3 = SD1_DAT1 ALT4 = ARM_TCK</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-24</td>
		<td align="left">GPIO08</td>
		<td align="left">GPIO08</td>
		<td align="center">-</td>
		<td align="left">SPI0_CE0_N</td>
		<td align="center">-</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-26</td>
		<td align="left">GPIO07</td>
		<td align="left">GPIO07</td>
		<td align="center">-</td>
		<td align="left">SPI0_CE1_N</td>
		<td align="center">-</td>
	</tr>
</table>
<!-- /TABLE 1 -->

## P1 Header Pinout, bottom row:

<!-- TABLE 2 -->
<table cellspacing="0" border="0">
	<colgroup span="6" width="85"></colgroup>
	<tr>
		<td height="17" align="left">Pin Number</td>
		<td align="left">Pin Name Rev1</td>
		<td align="left">Pin Name Rev2</td>
		<td align="left">Hardware Notes</td>
		<td align="left">Alt 0 Function</td>
		<td align="left">Other Alternative Functions</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-01</td>
		<td align="left">3v3</td>
		<td align="left">3v3</td>
		<td align="left">50 mA max (01 &amp; 17)</td>
		<td align="center">-</td>
		<td align="center">-</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-03</td>
		<td align="left">GPIO 0</td>
		<td align="left">GPIO 2</td>
		<td align="left">1K8 pull up resistor</td>
		<td align="left">I2C0_SDA / I2C1_SDA</td>
		<td align="center">-</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-05</td>
		<td align="left">GPIO 1</td>
		<td align="left">GPIO 3</td>
		<td align="left">1K8 pull up resistor</td>
		<td align="left">I2C0_SCL / I2C1_SCL</td>
		<td align="center">-</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-07</td>
		<td align="left">GPIO 4</td>
		<td align="left">GPIO 4</td>
		<td align="left"><br></td>
		<td align="left">GPCLK0</td>
		<td align="left">ALT5 = ARM_TDI</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-09</td>
		<td align="left">GND</td>
		<td align="left">GND</td>
		<td align="center">-</td>
		<td align="center">-</td>
		<td align="center">-</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-11</td>
		<td align="left">GPIO17</td>
		<td align="left">GPIO17</td>
		<td align="center">-</td>
		<td align="center">-</td>
		<td align="left">ALT3 = UART0_RTS ALT4 = SPI1_CE1_N ALT5 = UART1_RTS</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-13</td>
		<td align="left">GPIO21</td>
		<td align="left">GPIO27</td>
		<td align="center">-</td>
		<td align="left">PCM_DOUT / reserved</td>
		<td align="left">ALT4 = SPI1_SCLK ALT5 = GPCLK1 / ALT3 = SD1_DAT3 ALT4 = ARM_TMS</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-15</td>
		<td align="left">GPIO22</td>
		<td align="left">GPIO22</td>
		<td align="center">-</td>
		<td align="left"><br></td>
		<td align="left">ALT3 = SD1_CLK ALT4 = ARM_TRST</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-17</td>
		<td align="left">3v3</td>
		<td align="left">3v3</td>
		<td align="left">50 mA max (01 &amp; 17)</td>
		<td align="center">-</td>
		<td align="center">-</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-19</td>
		<td align="left">GPIO10</td>
		<td align="left">GPIO10</td>
		<td align="center">-</td>
		<td align="left">SPI0_MOSI</td>
		<td align="center">-</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-21</td>
		<td align="left">GPIO9</td>
		<td align="left">GPIO9</td>
		<td align="center">-</td>
		<td align="left">SPI0_MISO</td>
		<td align="center">-</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-23</td>
		<td align="left">GPIO11</td>
		<td align="left">GPIO11</td>
		<td align="center">-</td>
		<td align="left">SPI0_SCLK</td>
		<td align="center">-</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-25</td>
		<td align="left">GND</td>
		<td align="left">GND</td>
		<td align="center">-</td>
		<td align="center">-</td>
		<td align="center">-</td>
	</tr>
</table>
<!-- /TABLE 2 -->

_Notes:_ The maximum current capable of being sourced from P1 pins 1 and 17 is 50mA in total.  That is the current drawn from both pins, not 50mA each.

## Additional Pins on the Model B+

## P1 Header Pinout, top row:

<!-- TABLE 3 -->
<table cellspacing="0" border="0">
	<colgroup span="6" width="85"></colgroup>
	<tr>
		<td height="17" align="left">Pin Number</td>
		<td align="left">Pin Name Rev1</td>
		<td align="left">Pin Name Rev2</td>
		<td align="left">Hardware Notes</td>
		<td align="left">Alt 0 Function</td>
		<td align="left">Other Alternative Functions</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-28</td>
		<td align="left">ID_SC</td>
		<td align="left">ID_SC</td>
		<td align="left">?</td>
		<td align="center">-</td>
		<td align="center">-</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-30</td>
		<td align="left">GND</td>
		<td align="left">GND</td>
		<td align="center">-</td>
		<td align="center">-</td>
		<td align="center">-</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-32</td>
		<td align="left">GPIO12</td>
		<td align="left">GPIO12</td>
		<td align="center">-</td>
		<td align="center">-</td>
		<td align="center">-</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-34</td>
		<td align="left">GND</td>
		<td align="left">GND</td>
		<td align="center">-</td>
		<td align="center">-</td>
		<td align="center">-</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-36</td>
		<td align="left">GPIO16</td>
		<td align="left">GPIO16</td>
		<td align="center">-</td>
		<td align="center">-</td>
		<td align="center">-</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-38</td>
		<td align="left">GPIO20</td>
		<td align="left">GPIO20</td>
		<td align="center">-</td>
		<td align="center">-</td>
		<td align="center">-</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-40</td>
		<td align="left">GPIO21</td>
		<td align="left">GPIO21</td>
		<td align="center">-</td>
		<td align="center">-</td>
		<td align="center">-</td>
	</tr>
</table>
<!-- /TABLE 3 -->

## P1 Header Pinout, bottom row:

<!-- TABLE 4 -->
<table cellspacing="0" border="0">
	<colgroup span="6" width="85"></colgroup>
	<tr>
		<td height="17" align="left">Pin Number</td>
		<td align="left">Pin Name Rev1</td>
		<td align="left">Pin Name Rev2</td>
		<td align="left">Hardware Notes</td>
		<td align="left">Alt 0 Function</td>
		<td align="left">Other Alternative Functions</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-27</td>
		<td align="left">ID_SD</td>
		<td align="left">ID_SD</td>
		<td align="left">?</td>
		<td align="center">-</td>
		<td align="center">-</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-29</td>
		<td align="left">GPIO5</td>
		<td align="left">GPIO5</td>
		<td align="center">-</td>
		<td align="center">-</td>
		<td align="center">-</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-31</td>
		<td align="left">GPIO6</td>
		<td align="left">GPIO6</td>
		<td align="center">-</td>
		<td align="center">-</td>
		<td align="center">-</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-33</td>
		<td align="left">GPIO13</td>
		<td align="left">GPIO13</td>
		<td align="center">-</td>
		<td align="center">-</td>
		<td align="center">-</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-35</td>
		<td align="left">GPIO19</td>
		<td align="left">GPIO19</td>
		<td align="center">-</td>
		<td align="center">-</td>
		<td align="center">-</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-37</td>
		<td align="left">GPIO26</td>
		<td align="left">GPIO26</td>
		<td align="center">-</td>
		<td align="center">-</td>
		<td align="center">-</td>
	</tr>
	<tr>
		<td height="17" align="left">P1-39</td>
		<td align="left">GND</td>
		<td align="left">GND</td>
		<td align="center">-</td>
		<td align="center">-</td>
		<td align="center">-</td>
	</tr>
</table>
<!-- /TABLE 4 -->

_Notes:_ There are currently no split revisions for the Model B+.  I have simply put the same thing in both columns.

At the time of writing I don't know what the alternative functions for the additional GPIO pins are, if any.

It is recommended that you do not attempt to plug a twenty-six way IDC connector onto the forty pin 
GPIO bus of a new Model B+.  This is because the plastic at the ends of an IDC plug is thick enough 
to bend the first two pins which are beyond the plug.  No doubt traders will very quickly 
make forty-way IDC plugs and ribbon cables available.

Thanks to John Washington of the Surrey Linux user group for helping me by looking at the published 
diagram.



[rpi]: http://www.raspberrypi.org/
