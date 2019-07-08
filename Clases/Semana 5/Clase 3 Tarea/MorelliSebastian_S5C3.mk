.PHONY : cabezaimaginaria

cabezaimaginaria : datos.txt MorelliSebastianResorte.pdf

datos.txt : MorelliSebastian_S5C3_ODEs.cpp
	g++ MorelliSebastian_S5C3_ODEs.cpp
	./a.out > datos.txt

MorelliSebastianResorte.pdf : datos.txt MorelliSebastian_S5C3_plots.py
	python3 MorelliSebastian_S5C3_plots.py
