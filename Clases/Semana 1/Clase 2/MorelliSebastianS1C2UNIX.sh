mkdir MorelliSebastianS1C2Dir
cd MorelliSebastianS1C2Dir/
wget http://iopscience.iop.org/1538-3881/122/5/2396/fulltext/datafile3.txt
awk '{if($1=="F571-8")print $0}' datafile3.txt >> Galaxias.dat
awk '{if($4>0 && $5>0 && $6>0)print $0}' datafile3.txt >> RotGalaxias.dat