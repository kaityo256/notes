set term post eps color 28
set xla "Angular Velocity"
set yla "Radius Ratio"
set out "rotate.eps"

set ytic 0.01
set data style linespoints
set pointsize 1.5
unset key
p [][1:]"rotate.dat"  1 7
