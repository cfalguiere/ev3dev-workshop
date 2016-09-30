#/bin/bash
for f in /sys/class/lego-sensor/*; do echo -n "$f: "; cat $f/address; done
