set term post eps enhanced 24
set out "d-limit.eps"
unset key

set label "{/Helvetica=30 (a)}" at 0.04,0.75
set ytics 0.2
set xtics (0,0.5,1.0,1.5)
set xlabel '{/Palatino-Italic=30 ~R{.8\~}}'
set yla '{/Palatino-Italic=30 ~f{.8\~}}' offset -1,0
p [0:1.5] exp(-x/(1.5-x))*(3.0/(3.0+x))**(7.0/3)*x**2*(1.5/(1.5-x))**(11.0/3)*4/27

!ps2pdf d-limit.eps
