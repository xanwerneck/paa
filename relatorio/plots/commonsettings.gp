set encoding utf8
set terminal postscript eps enhanced color font 'Helvetica,22'
set grid

set style data histogram
set style histogram cluster gap 1
set style fill solid border -1
set xtic font "Helvetica,14"
#set boxwidth 0.9
set logscale y 10

set xlabel "Número de itens"
set ylabel "Tempo de execução (segundos)"
set key left
