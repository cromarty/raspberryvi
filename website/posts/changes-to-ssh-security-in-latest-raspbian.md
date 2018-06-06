<!-- 
.. title: Changes to SSH Security in Latest Raspbian
.. slug: changes-to-ssh-security-in-latest-raspbian
.. date: 2016-12-09 21:40:50 UTC
.. tags: ssh, security
.. category: 
.. link: 
.. description: Enable SSH Server in Raspbian
.. type: text
-->

In the latest release of Raspbian a new addition to security has been made.

Now there will be no SSH server running unless a file exists in the `/boot` partition. This file can 
be empty and is just called `ssh`.

If you are creating an SD card on a Linux machine you can mount the FAT32 boot partition and create 
the file in there by issueing the command:

	touch ssh

This will create a file of zero length.

I can't help thinking this is a bit ridiculous. Especially as the default `pi` user still has the 
ability to use `sudo` without having to enter a password, making `pi` effectively a `root` user.


