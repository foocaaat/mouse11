#!/bin/sh
HERE=`xdotool getwindowfocus`
while true
do
sleep 0.05
if [ $HERE != `xdotool getwindowfocus` ]
then
    HERE=`xdotool getwindowfocus`
    if [ $(cat .cache/mose) -eq "1" ]; then
          unset x y w h
          eval $(xwininfo -id $(xdotool getactivewindow) |
            sed -n -e "s/^ \+Absolute upper-left X: \+\([0-9]\+\).*/x=\1/p" \
                   -e "s/^ \+Absolute upper-left Y: \+\([0-9]\+\).*/y=\1/p" \
                   -e "s/^ \+Width: \+\([0-9]\+\).*/w=\1/p" \
                   -e "s/^ \+Height: \+\([0-9]\+\).*/h=\1/p" )
        if [ $x -gt 0 ]; then
        xdotool mousemove $((x+$((w/2)))) $((y+$((h/2))))
        fi
    fi
fi
done
