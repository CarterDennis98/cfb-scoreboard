#!/bin/bash
cd /home/carter/Documents/GitHub/cfb-scoreboard
. venv/bin/activate
n=0
until [ $n -ge 10]
do
    sudo -E python3 main.py && break
    n=$[$n+1]
    sleep 10
done
