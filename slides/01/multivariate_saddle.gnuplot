set term svg size 800,600 enhanced font 'Times, 18'
set output 'multivariate_saddle.svg'

set multiplot

set xlabel "x"
set ylabel "y"
set zlabel "z"
set xrange [-2.5:2.5]
set yrange [-2.5:2.5]
set zrange [-5.0:5.0]
unset colorbox
set view 50,25
set style fill solid 0.6

set border lw 0.5
unset key
set xlabel font 'Times, 48'
set ylabel font 'Times, 48'
set zlabel font 'Times, 48'

set hidden3d front
set ticslevel 0
set isosamples 20,200

# Draw the grids and intersection curve.
set isosamples 41,41
set palette defined (0 "navy", 10 "cyan")
splot 0.95-1<y && y<1.05-1 ? x*x-0.035 : -6 w lines lt 7 lw 3
splot 0.95-1<x && x<1.05-1 ? -y*y-0.035 : -6 w lines lt 7 lw 3
splot x*x - y*y w pm3d
splot x*x - y*y w lines lt 8 lw 0.1
