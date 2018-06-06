<!-- 
.. title: Basic Security
.. slug: basic-security
.. date: 2017-03-23 09:20:37 UTC
.. tags: LAN, Linux, Security, SSH
.. category: Security
.. link: 
.. description: Basic Security for your Raspberry Pi
.. type: text
-->


Here are some security recommendations that relate not only to your [Raspberry Pi][rpi] but to any 
Linux machine on your `LAN`. This is adapted from an email which Tim Chase sent to the list some 
time ago and is reproduced here with Tim's kind permission.

You may think your little Raspberry Pi is a trivial tinker toy, and while it is good fun to mess 
about with it, you should remember it is also a fully network-enabled Linux machine and could be 
hijacked by a bad-guy to provide a jumping-off point from which to make other attacks, not 
necessarily in your own network.

I'm of the opinion that however small and trivial you regard the machines on your LAN, security 
best-practise is a good education and knowing about the basics helps when you scale things up.

Here is where Tim's text begins:

If your router doesn't forward external (WAN) traffic to port 22 of your RPi, the only threat is 
internal.  If something is compromised on your local network (which these days could be your 
toaster, refrigerator, or your phone if you've got smart home), it could jump to your RPi if you 
leave things open.

If your router *does* forward a WAN port to your RPi, you'd want to take greater security measures.

A couple of things I'd recommend either way (but especially if your RPi is accessible from the 
internet bad-lands):

1. change your port number from the default port 22.

Reading the logs of my internet-exposed server, I see a regular barrage of probes on my SSH port 
trying to get in and try various common username/password combinations.  You can either just remap 
some non-22 port externally to the internal port (this would let you use the standard port on your 
local network, but access it via your non-standard port when you're remote), or you can change 
external port *and* the internal port.  I personally use a non-standard port externally but the 
standard port internally.  To do this, change your `/etc/ssh/sshd_config` file and search for a line 
that reads "Port 22" and set it to your desired port number, uncommenting it by removing the hash at 
the beginning if needed.  For example, you can change it to port 2345 with

	sed -i '.bak' '/^ *[Pp][Oo][Rr][Tt]/d;$aPort 2345' /etc/ssh/sshd_config 

which will delete any existing Port line and append a line at the bottom specifying "Port 2345", 
leaving the original backed up as /etc/ssh/sshd_config.bak

2. Don't permit root login.

Again, edit the `/etc/ssh/sshd_config` file and add/edit it to contain the line

	PermitRootLogin no

This way, you have to log in as a user and then "su" or "sudo" to use your root powers.

3. Change the default password for the "pi" user or whichever login you use.

The "passwd" command will prompt you for your old password and then prompt twice for your new 
password. Here is the command:

	passwd

4. Change "sudo" so that it requires a password.

Some systems have this as the default, while others default to allowing you to sudo without a 
password for any command.  To do this, you want to change either

	/etc/sudoers

or possibly a file like "01local" in

	/etc/sudoers.d/

to remove the "NOPASSWD" flag from your account.  I'm of the school that, if I want to do something 
requiring root powers, I should have to type a password to authenticate my authority.  I've got a 
couple small exceptions (and they're NOPASSWD'ed on a per-command basis, such as 'iftop'), but I 
never want wide-open root access without typing in a password.

Finally, if you want to get really locked down, you can forego password authentication and use a 
public/private key-pair for authentication.  You'd put your public SSH key on in your 
~/.ssh/authorized_keys file on the RPi and then disable password login in your /etc/ssh/sshd_config 
file.  I don't usually go this far, but it's one more thing you can lock down if you feel the need.

Here is the end of Tim's text.  I have formatted things a little for this page.  Thanks Tim.


[rpi]: https://www.raspberrypi.org/

