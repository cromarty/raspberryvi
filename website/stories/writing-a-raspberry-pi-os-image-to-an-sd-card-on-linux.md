<!-- 
.. title: Writing a Raspberry Pi OS Image to an SD Card on Linux
.. slug: writing-a-raspberry-pi-os-image-to-an-sd-card-on-linux
.. date: 2015-05-26 12:50:31 UTC
.. tags: Raspberry Pi, SD Card, IMG, image
.. category: Configuration
.. link: 
.. description: Writing a Raspberry Pi OS Image to an SD Card on Linux
.. type: text
-->


Writing an OS image to an SD card on a Linux desktop or laptop machine
is simple.  It can even be done on a running Raspberry Pi.

You will need the image file, an SD or micro-SD card depending on
which type of Raspberry Pi you are writing it for, and some way of
mounting the card into the Linux machine on which you are going to do
this process.

This may be a dedicated SD or micro-SD card reader slot built into the
machine, or a USB card reader which plugs into one of the USB ports on
the working machine.

Many SD card sellers include a micro-SD to SD converter with any
micro-SD card purchase.  These can be useful for mounting a micro-SD
card for writing.

First, you need to know what device name has been assigned to the card
once it has been plugged into the machine.

With some flavours of Linux, it may be necessary to do this once the
card has been plugged in and before you can start:

$ sudo partprobe

This is certainly true on my Debian machine.

Next you can find out what the device name is by doing something like
this:

$ sudo fdisk -l | grep -i "disk /"

You can redirect the output to a file if that helps.

You need to pay very close attention to the device names and the sizes
of the volume to which each relates.

I cannot stress strongly enough that it is very important to correctly
identify the correct device.  It is not without good reason that the
`dd` command is sometimes said to stand for 'data destroyer'.  You
will not get a second chance if you accidentally give the wrong device
name and wipe out your hard-disk.

Now, suppose the name of the `.img` file is `filename.img` and the
device which has been assigned to the SD card is `/dev/sdx`.  This
command will write the file, byte-for-byte, to the SD card:

$ sudo dd bs=1M if=filename.img of=/dev/sdx

The `dd` command is not very helpful, if you have entered it correctly
it will go totally silent until it completes and reports the number of
blocks written to the card.

Check the output at the completion to see if the messages printed to
the screen include `no space left on device`.  If it does, you have
not used an SD card that is big enough.

Now it is a good idea to give the `sync` command, for which `sudo` is
not needed, to make sure that no data is buffered by the OS.

# **Important Notes**

Just using a `copy` command on either Linux or Windows will not work.
The `.img` files which contain Raspberry Pi operating system images
are byte files which must be written to an SD card byte-for-byte.

I will stress here again the need to **be sure you are specifying the
right device name** and not your hard-disk.  Otherwise there will be
tears before bedtime.


