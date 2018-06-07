<!-- 
.. title: Raspberry Pi Version 3 Released
.. slug: raspberry-pi-version-3-released
.. date: 2016-02-29 10:02:52 UTC
.. tags: Pi3
.. category: 
.. link: 
.. description: Raspberry Pi 3 Released
.. type: text
-->

Today the [Raspberry Pi][rpi] version 3 has been released.

Here is a list of the specifications:

* SoC: Broadcom BCM2837 (CPU, GPU, DSP, SDRAM)
* CPU: Quad-core 64-bit ARM Cortex A53 clocked at 1.2 GHz
* GPU: 400MHz VideoCore IV multimedia
* Memory: 1GB LPDDR2-900 SDRAM (i.e. 900MHz)
* USB ports: 4
* Video input: 15-pin MIPI camera interface (CSI) connector
* Video outputs: HDMI, composite video (PAL and NTSC) via 3.5 mm jack
* Audio input: I²S
* Audio outputs: Analog via 3.5 mm jack; digital via HDMI and I²S
* Storage: MicroSD
* Network: 10/100Mbps Ethernet and 802.11n Wireless LAN
* Peripherals: 17 GPIO plus specific functions, and HAT ID bus
* Bluetooth: 4.1
* Power rating: 1A (5.0 W)
* Power source: 5 V via MicroUSB or GPIO header
* Size: 85.60mm × 56.5mm
* Weight: 45g (1.6 oz)

So I guess the most significant things to note are:

* 64-bit CPU
* WiFi now included
* Bluetooth included

I will investigate further today to see if there is any impact on the OMX libraries that have been 
previously available for the Pi and Pi2 which made my OMX code possible which solved the stuttery 
TTS with eSpeak.

This version is a different GPU I presume.

[rpi]: http://www.raspberrypi.org/

