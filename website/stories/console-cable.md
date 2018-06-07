<!-- 
.. title: Using a Serial Console Cable
.. slug: console-cable
.. date: 2015-11-30 15:56:51 UTC
.. tags: serial, console
.. category: Configuration
.. link: 
.. description: Using a serial console cable with a Raspberry Pi
.. type: text
-->

Here's how to use a serial console cable with a [Raspberry Pi][rpi].

Every model of the Pi so far released, has a serial UART (universal asynchronous 
receiver/transmitter) available on the GPIO bus.

And in the `Raspbian` image, and probably other images available for download from the Web, there is 
a file:

	/boot/config.txt

This file contains all kinds of configuration options, including `tty` options.  By default a 
`serial console` is configured to run on:

	/dev/ttyAMA0

Which is the serial console (UART).

## Why should I want to use this?

Most of us are often using our RPIs over `SSH`, but there are times when you may not want to do 
that, and some good reasons why you may want to see what's happening over the serial console.

Here are some compelling reasons:

* You may not have either hard-wired or wireless ethernet options available at all times.
* The Raspberry Pi Zero does not have an ethernet port.
* The default kernel configuration is often set up to write kernel debugging information to the 
serial console, so you can see what happened to cause a `kernel oops`.

## The cable

These cables are commonly available, from [Adafruit][ada] in the USA for example, and from 
[modmypi][mmp] here in the UK.

This is a full-sized USB lead with a USB plug on one end and four flying leads with female IDC 
sockets on the other end.

Inside the USB plug there is either a `PL2303` or an `FTDI` (and maybe other flavours) USB to serial 
adaptor chip.

To use the lead, plug one end into the USB port on a computer with a serial `tty` client program 
installed.

For Windows this could be `PuTTY`.  On Linux I use `picocom`.  I don't know about Mac, although I 
expect `picocom` can either be installed or compiled from source.

## How to connect the lead to the Pi

Attach the wires to the GPIO header on a powered-down RPi as follows:

* Red (USB VBUS) -- not connected, but see later.
* Black (GND for USB and PL2303) -- Pin 6 (Ground for RPi).
	* White (PL2303 RXD) -- Pin 8 (RPi BCM2835 UART0_TXD/GPIO14).
* Green (PL2303 TXD) -- Pin 10 (RPi BCM2835 UART0_RXD/GPIO15).

If you do connect the red lead, perhaps to pin 2, in the extreme corner of the board, then the Pi 
can be powered from the supply over the USB connection.  Note it would __not__ be a good idea to use 
another Pi for providing this power unless the USB end of the lead is plugged into a powered hub.

## Lead Identification

Of course if, like me, you can't see the colours of the flying leads at the business end of the 
cable you will need to get someone to identify them.  But I have found a way that means I only had 
to do this once:

Three of the pins the leads connect to are next to each other on the GPIO bus.  These are pins 6, 8 
and 10 (see above).

My lead has square female IDC sockets on the business end and I was able to hold the black, green 
and white leads together and then wrap some Sellotape (Scotch tape if you're a leftpondian), around 
the three leads and then stick a small tactile bump on the side which will be nearest the edge of 
the Pi board.  The red power lead is left flying loose and can either be taped back against the 
cable out of the way or plugged in to a 5v pin on the Pi.

Refer to the connection details given above to work out which pin should be in the centre of this 
group of three and which side the bump-on should be applied to.

__DO NOT__ be tempted to use PVC electrical tape for this.  I have found over the years that the goo 
on the sticky side of such tape has a tendency to creep out of where it is supposed to be and leave 
everything gummy and unpleasant.  On the other hand Sellotape/Scotch stays put and stays nice and 
clean.

_Note:_ There are more than one pin for each of ground and 5v on the Raspberry Pi, but pin 6 is the 
most convenient ground pin to use if you tape three of the flying leads together, and pin 2, being 
in the very corner of the board, is the easiest to find for a 5v connection if you can't see.

Refer to the [GPIO Pinouts guide][gpio] page on this site for tables of the GPIO pins and their 
designations.

## Terminal Emulator

Configure a terminal emulator with 115000N81, no handshaking, ignore DTR/DCD, no modem AT setup or 
hangup strings. Boot the RPi and kernel messages should appear within 1 second. At end of boot a 
login prompt will appear.

## `picocom`

Here's how to use `picocom`.  Because I always want to know one thing before I ever use a piece of 
software I haven't used before, which is _how do I get out?_, here is the way to exit `picocom`:

Press Control+a followed by control+x.

To launch `picocom` you will first need to know which device name has been allocated to the console 
cable you have plugged in.  If it is the only USB to serial adaptor plugged in to your Linux machine 
it is probably `/dev/ttyUSB0`.

So, to launch `picocom` and connect to the serial console on the connected Pi:

	picocom --baud=115200 /dev/ttyUSB0

When connected, pressing return a couple of times will probably present you with the log-in prompt.

Read the `man page` for `picocom` for more about how to use it.  I have never found `minicom`, an 
alternative terminal emulator for Linux, to be very accessible.

[rpi]: http://www.raspberrypi.org/
[ada]: http://www.adafruit.com/product/954
[mmp]: http://www.modmypi.com/raspberry-pi/gpio-and-breadboarding/gpio-debugging-console-cables/usb-to-ttl-serial-cable-debug--console-cable-for-raspberry-pi
[gpio]: /stories/raspberry-pi-gpio-bus-pinouts.html





