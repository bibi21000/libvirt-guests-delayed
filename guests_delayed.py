#!/usr/bin/python3
import os
import re
import threading
import subprocess
import syslog

started = []
errors = []
conf_file = '/etc/libvirt/guests_delayed.conf'
virsh = '/usr/bin/virsh'

def start_guest_delay(guest, delay=10):
    syslog.syslog(syslog.LOG_INFO, 'Schedule start of %s in %s seconds' % (guest, delay))
    t = threading.Timer(delay, start_guest, args=[guest])
    t.start()
    started.append(t)

def start_guest(guest):
    syslog.syslog(syslog.LOG_INFO, 'Start guest %s' % (guest))
    lxc_list = list_guests()
    if guest in lxc_list:
        p = subprocess.run([virsh, 'start', guest], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if p.returncode != 0:
            errors.append(guest)
            for err in p.stderr.split('\n'):
                if err != '':
                    syslog.syslog(syslog.LOG_ERR, '%s' % (err))

def load_conf():
    if os.path.isfile(conf_file):
        with open(conf_file) as _file:
            data = _file.read().splitlines(True)
        res = [ r.strip() for r in data ]
        res = [ r for r in res if r != '' and r[0] != "#" ]
        res = [ re.split(' |\t', r) for r in res ]
        return [ [r[0].strip(), r[1].strip()] for r in res]
    return []

def list_guests():
    result = subprocess.run([virsh, 'list', '--inactive', '--no-autostart', '--name'], text=True, stdout=subprocess.PIPE)
    res = [ r.strip() for r in result.stdout.split() ]
    return [ r for r in res if r != '' ]

def main():
    syslog.openlog('guests_delayed', logoption=syslog.LOG_PID, facility=syslog.LOG_DAEMON)
    conf = load_conf()
    syslog.syslog(syslog.LOG_INFO, 'Found configuration : %s' % conf)
    lxc_list = list_guests()
    syslog.syslog(syslog.LOG_INFO, 'Found inactive guests : %s' % lxc_list)
    for lxc in conf:
        if lxc[0] in lxc_list:
            start_guest_delay(lxc[0], delay=int(lxc[1]))
    for t in started:
        t.join()
    if len(errors) > 0:
        syslog.syslog(syslog.LOG_ERR, 'Errors starting guests : %s' % errors)
        import sys
        sys.exit(1)
    syslog.syslog(syslog.LOG_INFO, 'All delayed guests started')

if __name__ == '__main__':

    main()
