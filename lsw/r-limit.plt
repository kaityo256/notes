set term post eps enhanced 24
set out "r-limit.eps"
unset key

set ytics 0.1
set xtics 0.5
set label "{/Helvetica=30 (b)}" at 0.04,0.47
set xlabel '{/Palatino-Italic=30 ~R{.8\~}}' offset -2,0
set yla '{/Palatino-Italic=30 ~f{.8\~}}' offset -1,0
p [0:2] [0:0.5] exp(3*x/(x-2))*(2/(2-x))**5*x/4

!ps2pdf r-limit.eps
