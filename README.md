magic_color
===========

Python classes to talk to a WF300 WiFi LED Strip Controller

The wf-300 is a low cost, poorly made Chinese LED controller with
little to no documentation in english. It's capable of driving SPI or
Non-SPI LED strips. It emulates an access point, which really sucks,
because then you can only talk to the one device with your Wifi card.

You can use this code to interface these hunks of junk to your home
automation system. That's what I do, at least.

http://www.ledyilighting.com/portfolio/led-controller-ly-wf-300

Warning! This is incredibly messy alpha code as it's full of my notes
while I was reverse engineering the client software, which was
previously only available on Android and iPhone.

I'm not done with this, don't judge me.

