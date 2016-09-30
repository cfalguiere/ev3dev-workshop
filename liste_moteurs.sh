#/bin/bash
for f in /sys/class/tacho-motor/*; do echo -n "$f: "; cat $f/address; done
