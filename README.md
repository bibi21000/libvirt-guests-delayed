# libvirt-guests-delayed
Autostart libvirt guests with a delay.

- Copy guests_delayed.py to /usr/lib/libvirt

- Make it executable

- Copy libvirt-guests-delayed.service to /etc/systemd/system

- Enable it to start it at boot

- Create the configuration file in /etc/libvirt/guests_delayed.conf

> guest1 800<br>
> guest2 500<br>
> guest3 120

- Remove autostart in the configuration of guests you want to delay

- And reboot to try it

> service libvirt-guests-delayed status

> ● libvirt-guests-delayed.service - Running libvirt delayed Guests<br>
>   Loaded: loaded (/etc/systemd/system/libvirt-guests-delayed.service; enabled; vendor preset: enabled)<br>
>   Active: active (exited) since Thu 2024-08-01 23:27:59 CEST; 16min ago<br>
>   Process: 70440 ExecStart=/usr/lib/libvirt/guests_delayed.py (code=exited, status=0/SUCCESS)<br>
>   Main PID: 70440 (code=exited, status=0/SUCCESS)<br>
> <br>
> août 01 23:27:59 xxxxxxxx systemd[1]: Started Running libvirt delayed Guests.
> août 01 23:27:59 xxxxxxxx guests_delayed[70440]: Found configuration : [['guest1', '800'], ['guest2', '500'], ['guest3', '120']]<br>
> août 01 23:27:59 xxxxxxxx guests_delayed[70440]: Found inactive guests : ['guest1', 'guest2', 'guest3']<br>
> août 01 23:27:59 xxxxxxxx guests_delayed[70440]: Schedule start of guest1 in 800 seconds<br>
> août 01 23:27:59 xxxxxxxx guests_delayed[70440]: Schedule start of guest2 in 500 seconds<br>
> août 01 23:27:59 xxxxxxxx guests_delayed[70440]: Schedule start of guest3 in 120 seconds<br>
> août 01 23:29:59 xxxxxxxx guests_delayed[70440]: Start guest guest3<br>
> août 01 23:32:59 xxxxxxxx guests_delayed[70440]: Start guest guest2<br>
> août 01 23:41:19 xxxxxxxx guests_delayed[70440]: Start guest guest1<br>
> août 01 23:41:21 xxxxxxxx guests_delayed[70440]: All delayed guests started

