<!-- 
.. title: Writing an SD Card on Windows with WinFlashTool
.. slug: writing-an-sd-card-on-windows-with-winflashtool
.. date: 2015-05-26 16:08:15 UTC
.. tags: SD Card, Raspberry Pi, IMG, image
.. category: Configuration
.. link: 
.. description: Writing an SD Card on Windows with WinFlashTool
.. type: text
-->

This page details how to write a **Raspberry Pi** operating system `.img` file to an SD card using a 
tool called `WinFlashTool`.

I have found this tool to be very accessible on Windows using the [NVDA screen-reader][nvda].

First you will need to  [download WinFlashTool][winf] and install it.

You will also need some way of mounting the SD card on your Windows machine.  USB SD card readers 
are good for this if your computer does not have either an SD or micro-SD card slot.

You will need to use a full size SD card for the older type of **Raspberry Pi**, or a micro-SD card 
for the Model B+ or version 2 Model B+.

Dealers who sell micro-SD cards often include a micro-SD to SD adaptor with the purchase of a 
micro-SD card.  These are useful if your card-reader only takes full-size SD cards.

It is important to note that just copying, or using `drag-and-drop` to put a `.img` file onto an SD 
card will not work.  The file needs to be written to the card byte-for-byte.

Also note that if a `.img` file has previously been written to the card, only one of the 2 or more 
disk partitions on the card will be recognised by Windows.  This is because the boot partition is 
`FAT32`, which Windows can read, and the other partitions on the card are Linux partitions which 
Windows is not capable of reading.

Once you have installed `WinFlashTool` on your Windows machine, follow these steps:

1.  Open `WinFlashTool` using the start menu or however you usually launch programs.
2.  You will hear something like `source image grouping` and the text field that has focus is for 
the name of the `.img` file to write to the card.
3.  If you press the `TAB` key at this point you will hear something like `... button`.  This is the 
`browse` button which will open the file-finder dialog for you to locate your file.  Or you can just 
type the full path and file-name into the first text box.
4.  The next control is a list of the devices on your computer.  It will give you a list you can 
navigate up and down with the up and down arrow keys.  But see the next item on this list for a way 
to hide your hard-disk and avoid the nasty accidental over-writing of your system.
5.  The next control to gain focus when you press the `TAB` key is a `checkbox` which allows you to 
hide devices that are not replaceable media.  Checking this box is a good idea as it will prevent 
you 
from accidentally writing the `.img` file to your hard disk.  And you don't want that to happen.
6.  Next control is the `write` button.  Which will begin the write.

# Notes

When you begin the write, Windows will pop-up after a couple of minutes and tell you that you need 
to reformat the drive.  Just cancel out of this as the write will not continue until you do.

When the write is complete you might get another pop-up of the `open folder to view files` variety.  
Again, ignore this nonsense.

At this point you can close `WinFlashTool`, remove the card from it's slot or holder, insert it into 
your **Raspberry Pi** and boot it.

If the file was a valid operating system that is bootable, and if the write has worked correctly, 
the Pi should boot.

# Disclaimer

This guide is correct in my experience of `WinFlashTool`.  However I do not guarantee fitness for 
purpose and I cannot be held responsible for loss or damage to data produced by following this 
guide, either to the letter or erroneously.  It is possible to over-write the boot-sector of your 
primary disk partition using this tool, thus rendering your Windows machine unbootable.

**You have been warned**.


[winf]: http://winflashtool.sysprogs.com/
[nvda]: http://www.nvaccess.org/
