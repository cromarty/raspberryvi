<!-- 
.. title: SSH Without a Password
.. slug: ssh-without-password
.. date: 2017-03-23 13:35:55 UTC
.. tags: SSH, Security
.. category: Security
.. link: 
.. description: How to SSH to a remote Linux host without giving your password every time
.. type: text
-->

This page will detail how to create a private and public key pair, send the public key to the remote 
server into which you wish to SSH without having to enter a password each time.

First you need to be logged in to the machine from which you
want to access the remote server.  We will call the user name of the account on the remote machine, and the
remote machine itself thusly:

* user
* server

Now do this on your local machine, and do not enter a pass-phrase:

	ssh-keygen -t rsa

You will see these messages, with the exception of the 'created directory /home/user/.ssh' message if it already exists:

	Generating public/private rsa key pair.
	Enter file in which to save the key (/home/a/.ssh/id_rsa):
	Created directory '/home/a/.ssh'.
	Enter passphrase (empty for no passphrase):
	Enter same passphrase again:
	Your identification has been saved in /home/a/.ssh/id_rsa.
	Your public key has been saved in /home/a/.ssh/id_rsa.pub.
	The key fingerprint is:
	<some seemingly random hex numbers>

So simply put, after typing the ssh-keygen command press return three times.

You will now have two files in ~/.ssh:

* id_rsa
* id_rsa.pub

At this point it is very, very important to note the difference between these two files. The file:

* id_rsa.pub

Is your public key and it is that which will be sent to the server and put into the authorized_keys file.

The file:

* id_rsa

Is your private key and must _NOT_ be sent up to the server.

Now use ssh to create a directory ~/.ssh as user on server. (The directory may already exist, which is fine):

	ssh user@server mkdir -p .ssh

You will be asked for your password, that is, the password of the remote machine:

	user@server's password:

Enter the password and press return.

Finally append user's new public key to user@server:.ssh/authorized_keys,
entering the remote user's password one last time:

	cat .ssh/id_rsa.pub | ssh user@server 'cat >> .ssh/authorized_keys'

This is the last time you will be asked for the password:

	user@server's password:

From now on you can log into server as user from your local machine as your user without password:

	ssh user@server

So now you can script anything that uses, for example, rsync to send files to the remote server.

## Alternative Copy

Alternatively, you can use the ssh-copy-id command. Although you can specify a specific key, it will 
take your public key by default. The command is:

	ssh-copy-id user@remote_server

It prompts for the server's password. You can do a dry run by adding the -n switch. ssh-copy-id knows where to put the key.

## How to Use a Config file with ssh

This automates ssh even more. You can create a nickname for any remote and define the user and static ip address in a file.

The filename is .ssh/config. It goes in your .ssh directory in your folder.

The config file consists of lines of text. You may have blank lines and comments beginning with a hash "#". A keyword is followed by an argument. Here's an example explained below.

	Host alarmpi
	CheckHostIp YES
	HostName 192.168.1.15
	User pi

* The Host is the nickname.
* CheckHostIp relates to that message about fingerprint has changed. This config will check. If you don't want to check, say "NO".
* HostName is the address.
* User is the user name.

Now you can ssh into a machine by typing: ssh alarmpi. If you haven't set up keys as above, you will be prompted for your password. 

The great thing about this is that you can have one file that you put on every new machine and you will know which machine is which. Of course, you have to update the config file for each new machine and use static ip addresses.


