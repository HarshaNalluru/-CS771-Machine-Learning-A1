Rough

# set terminal pngcairo  transparent enhanced font "arial,10" fontscale 1.0 size 500, 350 
# set output 'fillbetween.1.png'
set style data lines
set title "Fill area between two curves" 
set xrange [ 10.0000 : * ] noreverse nowriteback
set yrange [ 0.00000 : 175.000 ] noreverse nowriteback
plot 'silver.dat' u 1:2:3 w filledcu,       '' u 1:2 lt -1 notitle, '' u 1:3 lt -1 notitle






------------------------
# We need to set lw in order for error bars to actually appear.
set style histogram errorbars linewidth 1
# Make the bars semi-transparent so that the errorbars are easier to see.
set style fill solid 0.3
set bars front
plot 'date_mins.tsv' using 2:3:4:xticlabels(1) title columnheader


# We need to set lw in order for error bars to actually appear.
set style histogram rowstacked linewidth 1
set style fill solid 0.3
set bars front
set yrange [0 to 1]
plot 'accuracies.dat' using 2:xticlabels(1) title columnheader


set boxwidth 0.2 relative
set style data histograms
set style fill solid 1.0 border -1
set yrange [0 to 1]
plot 'accuracies.dat' using 2:xticlabels(1) title columnheader lt rgb "#174a9b" 


set title 'Accuracies vs K'
set style data lines
set style data linespoints
set xlabel 'K'
set ylabel 'Accuracies'
set yrange [0 to 100]
set xrange [ 1 : *] noreverse nowriteback
plot 'accuracies#2.dat' u 1:2 title 'Accuracies' pt 7 ps 0.5 lw 1 lc rgb "blue"


plot 'accuracies#2.dat' using 2:xticlabels(1) w filledcu title columnheader lt rgb "#174a9b" 



