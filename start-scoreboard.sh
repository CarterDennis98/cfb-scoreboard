#!/bin/bash
cd /home/carter/Documents/GitHub/cfb-scoreboard
. venv/bin/activate
n=0
until [ $n -ge 10]
do
    sudo -E python3 main.py --led-gpio-mapping=adaruit-hat-pwm --led-slowdown-gpio=2 && break
    n=$[$n+1]
    sleep 10
done
