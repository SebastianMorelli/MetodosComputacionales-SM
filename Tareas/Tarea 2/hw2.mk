#Este MakeFile corre los archivos de la Segunda Tarea.

FFtIm.pdf ImProceso.pdf ImHybrid.pdf XY_met_dt.pdf VxVy_met_dt.pdf Mome_met_dt.pdf Ener_met_dt.pdf: Fourier.py dataRG.txt Plots_hw2.py
	python3 Fourier.py
	python3 Plots_hw2.py

dataRG.txt: a.out
	./a.out > dataRG.txt

a.out: ODEs.cpp
	 g++ ODEs.cpp
