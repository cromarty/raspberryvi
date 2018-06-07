<!-- 
.. title: USB Audio
.. slug: usb-audio
.. date: 2016-08-03 10:04:01 UTC
.. tags: USB Audio
.. category: 
.. link: 
.. description: How to configure the Raspberry Pi for USB Audio for all users
.. type: text
-->

Here's how to change the Pi to use USB audio as the default.

This has proven quite hard to pin down online as things recently changed in the kernel, I think to 
use something called `Device Tree Blocks`.

You will find posts online suggesting you change:

* ~/.asoundrc
* /etc/asound.conf
* /usr/share/alsa/alsa.conf

But this method will work for all users, unlike changing ~/.asoundrc.

There is a setting which makes sure that any USB audio dongle you have plugged in is not the 
default. The device with the number of zero is the default.

Look in:

	/lib/modprobe.d/aliases.conf

And you will see a line which reads:

	options snd-usb-audio index=-2

That is the line which keeps the USB audio device from being the zero default.

So, commenting it out like this:

	#options snd-usb-audio index=-2

And then rebooting will make the USB device the new default.

Of course you will need to use `sudo` to do this.

Optionally you can also disable the Broadcom audio driver by commenting out a line in:

	/boot/config.txt

The line is:

	dtparam=audio=on

Comment it out:

	#dtparam=audio=on

Now after rebooting you have USB audio and no Broadcom sound driver.

Note that assuming you don't disable the Broadcom sound driver and still want to hear some 
applications through either HDMI or the the analogue audio jack, you now need to force individual 
applications to use the on-board sound by providing whatever configs or switches each application 
needs.

