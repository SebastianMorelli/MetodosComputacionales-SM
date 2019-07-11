#Este MakeFile corre los archivos de las cuerdas cons sus 3 condiciones.

plotCuerdas.pdf: dataFijos.txt dataLibres.txt dataForzado.txt Plots_cuerdayTambor.py
	python3 Plots_cuerdayTambor.py

dataFijos.txt: MorelliSebastian_cuerdaFijos.cpp
	g++ MorelliSebastian_cuerdaFijos.cpp
	./a.out > dataFijos.txt

dataLibres.txt: MorelliSebastian_cuerdaLibre.cpp 
	g++ MorelliSebastian_cuerdaLibre.cpp
	./a.out > dataLibres.txt

dataForzado.txt: MorelliSebastian_cuerdaForzada.cpp
	g++ MorelliSebastian_cuerdaForzada.cpp
	./a.out > dataForzado.txt
