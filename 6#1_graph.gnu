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
