pwd
ls
wget https://data.giss.nasa.gov/gistemp/tabledata_v3/GLB.Ts.txt
awk ' NR>8 {if($13>0 &&  $1 != "Year") print $1}' GLB.Ts.txt >> TempDic.txt
awk ' NR>8 {if($1 != "Year") print $20,$14}' GLB.Ts.txt >> TempPomedios.txt
python3 plotTemp.py
rm GLB.Ts.txt