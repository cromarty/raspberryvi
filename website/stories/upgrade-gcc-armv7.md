<!--
.. title: Upgrading the gcc and g++ Compilers for ARM V7 (Pi2) Compilations
.. slug: upgrade-gcc-armv7
.. date: 2015-10-21 17:18:21 UTC
.. tags: GCC, ARMV7, compilation
.. category:Configuration
.. link:
.. description: How to upgrade the GCC compilers in Raspbian to compile specifically for ARM V7 (Pi2)
.. type: text
-->

This page is composed from a post to the Raspberry VI email list by Travis Siegel. It details
something we should all know about the difference between the older [Raspberry Pi][rpi],
both models A and B, and the newer Raspberry Pi2.

From here are Travis' posts, with slight editing to glue together two separate emails seemlessly (I hope), and to add some Markdown formatting to command-line stuff etc.:

## Replacing the GCC Compilers

Today, I was doing some digging around just for the heck of it, and
discovered that the gcc (version 4.6) that ships with raspbian does not
produce arm7 executables by default.  In fact, I've not found any way to
get version 4.6 to produce arm7 executables at all.  Admittedly, I only
searched for an answer until I found one that worked, so it's possible
there is a solution with the default gcc install, but I didn't find it.

Note added by Mike...the older versions of the Pi are ARM V6, and the newer Pi2 is ARM V7.

So, for those of you who are compiling your own programs, and wish for
them to actually produce arm7 code, and not arm6 executables, there's a
few things you'll need to do.

Keep in mind, that compiling for arm7 processors will make your code not
run on anything before the pi 2, but if you're ok with that, then here's
what needs to be done.

Note added by Mike...as Travis suggests ARMV7 code will not run on ARMV6, but ARMV6 code _will_ run on ARMV7.

Install gcc 4.8 (or later, I believe 4.9 is out as well, though I didn't
try it):

	sudo apt-get install gcc-4.8 g++-4.8

Then, you can remove gcc version 4.6, as it is no longer needed.

	sudo apt-get remove gcc-4.6 g++-4.6

You can of course remove the 4.6 versions first, as this will
produce the proper sim-links for gcc and g++ in the /usr/bin directory,
but since we'll be putting in our own gcc and g++ scripts, it won't really
matter.

Now, remove the gcc and g++ sim-links, so we can replace them with custom
scripts instead:

	sudo rm /usr/bin/gcc /usr/bin/g++

Then create the scripts to replace gcc and g++:

	sudo pico /usr/bin/gcc

(you'll need to do the same for g++.  Also, you need not use pico, you can
use the editor of your choice)

In the files, we'll  put the following text.

	#!/bin/bash
	gcc-4.8 $* -mcpu=cortex-a7 -mfpu=neon-vfpv4 -mfloat-abi=hard

The $* is to ensure that any parameters passed on the command-line are
passed on to the actual compilers.

Parameters are the same for the g++ command, only gcc gets replaced with
g++.

Make the scripts executable by doing:

	sudo chmod 0755 /usr/bin/gcc /usr/bin/g++

Now, by default, your compiles will produce arm7 executables, unless the
parameters are overridden in the make files or build scripts, but under
normal circumstances, this isn't likely, and generally if they do have
such parameters in the make files, it's because they have some reason for
choosing a different build type, in which case you'd not want to override
it anyhow.

If you need to use the default versions of the compilers, simply call
gcc-4.8 or g++-4.8 instead of the gcc or g++ commands.

I was very puzzled to learn that most of the applications (well, all of
the ones I've checked) were compiled for arm6 cpus, but I guess it makes
sense when you're producing an os image that needs to run on as many
systems as possible.

Now my next project is to build me a version of
raspbian that has as many v7 executables as I can manage.

## Checking Executables

To check the parameters of your programs, use the readelf program like this:

	readelf -a /usr/bin/gcc

This will produce all kinds of output, but the two lines you're concerned
with  are the ones that say:

	Tag_CPU_name: ...

Which will say "6" for an arm6 compile, but after the
changes made in the previous email, it will say: "Cortex-A7"
and the line:

	Tag_CPU_arch: ...

Which will say v6 for those compiled for an arm6
processor, and: v7 for those compiled for arm7 cpus.

Again, this change will only produce programs that run on the pi2, and
they will not work on earlier versions of the pi, so if you need backward
compatibility, then you won't want this hack, or you'll need to use the
whole name of the compilers as mentioned above if you want
to make them compatible with earlier pi versions.

## Additional Findings

I've done a little bit of additional digging, and it appears one of the
parameters isn't actually necessary, but without additional steps, it
won't actually affect the output of the compiler any, but if so desired,
you can remove the neon reference, since it appears to cause problems with
floating-point calculations if it's truly activated, (which requires
additional steps), but left inactive doesn't change output of the compiler
at all.

It has to do with the implementation of the floating-point software
library, and it not being strictly compliant with the standard.  That's
about all I could find on it, everyone says the same thing, only they say
it in more complex terms that all boils down to the same thing, if neon
isn't needed, it's best to leave it off.  There seems to be some
disagreement as to what exactly activates the neon portion of the
compiler, some claim you need to include a header file in your programs,
others say that's not necessary, but all agree that without additional
compiler directives, the parameter in my script has no affect.  Might be
better to take it out anyhow, just to avoid confusion.

Note added by Mike...I would certainly recommend it is removed, as Travis says, to avoid confusion, ([Occam's Razor][occam]).

Thanks Travis for this valuable hack.

[rpi]: http://www.raspberrypi.org/
[occam]: https://en.wikipedia.org/wiki/Occam's_razor
