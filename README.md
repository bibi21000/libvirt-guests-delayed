# libvirt-guests-delayed
Autostart libvirt guests at boot with a delay.

Installation via PPA for Ubuntu
-------------------------------

- Add ppa to your system and install package

> sudo add-apt-repository ppa:sgallet/libvirt-guests-delayed
> sudo apt update
> sudo apt install libvirt-guests-delayed

And use it

Installation for Debian/Ubuntu
------------------------------

- Copy guests_delayed.py to /usr/lib/libvirt

- Make it executable

- Copy libvirt-guests-delayed.service to /etc/systemd/system

- Enable it to start it at boot

> systemctl enable libvirt-guests-delayed.service

And use it

Use it
------

- Create or update the configuration file in /etc/libvirt/guests_delayed.conf

> guest1 800<br>
> guest2 500<br>
> guest3 120

- Remove autostart in the configuration of guests you want to delay

> virsh autostart guest1 --disable<br>
> virsh autostart guest2 --disable<br>
> virsh autostart guest3 --disable

- Reboot your host to try it

- Check status after restarting

> systemctl status libvirt-guests-delayed

> ● libvirt-guests-delayed.service - Running libvirt delayed Guests<br>
>> Loaded: loaded (/etc/systemd/system/libvirt-guests-delayed.service; enabled; vendor preset: enabled)<br>
>> Active: active (exited) since Thu 2024-08-01 23:27:59 CEST; 16min ago<br>
>> Process: 70440 ExecStart=/usr/lib/libvirt/guests_delayed.py (code=exited, status=0/SUCCESS)<br>
>> Main PID: 70440 (code=exited, status=0/SUCCESS)<br>
> <br>
> août 01 23:27:59 xxxxxxxx systemd[1]: Started Running libvirt delayed Guests.<br>
> août 01 23:27:59 xxxxxxxx guests_delayed[70440]: Found configuration : [['guest1', '800'], ['guest2', '500'], ['guest3', '120']]<br>
> août 01 23:27:59 xxxxxxxx guests_delayed[70440]: Found inactive guests : ['guest1', 'guest2', 'guest3', 'guest4']<br>
> août 01 23:27:59 xxxxxxxx guests_delayed[70440]: Schedule start of guest1 in 800 seconds<br>
> août 01 23:27:59 xxxxxxxx guests_delayed[70440]: Schedule start of guest2 in 500 seconds<br>
> août 01 23:27:59 xxxxxxxx guests_delayed[70440]: Schedule start of guest3 in 120 seconds<br>
> août 01 23:29:59 xxxxxxxx guests_delayed[70440]: Start guest guest3<br>
> août 01 23:32:59 xxxxxxxx guests_delayed[70440]: Start guest guest2<br>
> août 01 23:41:19 xxxxxxxx guests_delayed[70440]: Start guest guest1<br>
> août 01 23:41:21 xxxxxxxx guests_delayed[70440]: All delayed guests started

- If something went wrong when starting guests, unit will enter in fail mode

- If you want to stop startup process of guests, stop the service

> systemctl stop libvirt-guests-delayed

Others linux
------------

You need to update the paths in script and systemd service according to your distribution

