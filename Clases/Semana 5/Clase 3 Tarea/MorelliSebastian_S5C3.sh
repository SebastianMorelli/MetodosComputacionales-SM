#Script que corre todo el código y genera la gráfica.

g++ MorelliSebastian_S5C3_ODEs.cpp
./a.out > datos.txt
python3 MorelliSebastian_S5C3_plots.py
