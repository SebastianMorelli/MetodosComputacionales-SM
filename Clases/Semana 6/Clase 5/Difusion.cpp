//Este código soluciona una ecuación de difusión térmica de segundo orden en una placa de dos dimensiones.

#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;

//Declaración Variables 

float lado = 1.0;
float cofdif = 1e-4;
float dx = 0.01;
float dt = 0.25*pow(dx,2)/cofdif;
float ladopeq = 0.20;
int numpunt = lado/dx;
float itera = 2500.0;
float T0 = 50.0;
float Tpeq = 100.0;

//Declaración funciones

float * yoAdivinoFuturos (float arrPres[], float arrFut[]);
float * yoReemplazoPasados (float arrPresnt[], float arrFutu[]);

int main()
{
    ofstream outfile;
    outfile.open("data.txt");
    
    //Declaración Arrays
    float x[numpunt][numpunt];
    float presentTxTy[numpunt][numpunt];
    float futureTxTy[numpunt][numpunt];
    
    //Condiciones de Frontera 
   
    
    //Condición inicial

    for (int i = 0; i < numpunt; i++){
        float xlam = dx*i;
        for(int j = 0; j < numpunt; j++){
            
            float ylam = dx*j;
            
            if(xlam >= 0.20 && xlam <=0.40 && ylam >= 0.40 && ylam <= 0.60){
              presentTxTy[i][j] = Tpeq;
            }
            else{
              presentTxTy[i][j] = T0;
            }    
            
            outfile<<presentTxTy[i][j]<<" ";
        }
        outfile<<endl;
    }
    
    outfile.close();
    
    outfile.open("data100.txt");

   //Output de las oscilaciones futuras halladas
   int contador = 0;
   for (int i = 0; i < itera; i++){
       
       yoAdivinoFuturos (presentTxTy, futureTxTy);
       yoReemplazoPasados(presentTxTy, futureTxTy);
       
       for(int k=0; k <= numpunt; k++){
           if(contador == 100){
               for(int j = 0; j <= numpunt; j++){
                   outfile<<presentTxTy[k][j]<<" ";
               }
           }
       }
       outfile<<endl;
       contador ++;
   }
    
   outfile.close();
    
   outfile.open("data2500.txt");
    
   int contador1 = 0;
   for (int i = 0; i < itera; i++){
       
       yoAdivinoFuturos (presentTxTy, futureTxTy);
       yoReemplazoPasados (presentTxTy, futureTxTy);
       
       for(int k=0; k <= numpunt; k++){
           if(contador1 == 2500){
               for(int j = 0; j <= numpunt; j++){
                   outfile<<presentTxTy[k][j]<<" ";
               }
           }
       }
       outfile<<endl;
       contador1 ++;
   }
   outfile.close();
}

float * yoAdivinoFuturos (float arrPres[], float arrFut[]){
    
    float * p0 = arrFut;
    
    for( int i = 1; i < numpunt; i++){
        for( int j = 1; j < numpunt; j++){
            arrFut[i][j] = ((pow(cofdif,2)*dt,2/pow(dx,2)) * (2*arrPres[i+1]+2*arrPres[i-1]-4*arrPres[i])) + (arrPres[i]);
        }
    }
    return p0;
}


float * yoReemplazoPasados (float arrPresnt[],float arrFutu[]){

    float * p1 = arrPresnt;
    
    for( int i = 1; i < numpunt; i++){
        for( int j = 1; j < numpunt; j++){
            arrPresnt[i][j] = arrFutu[i][j];
        }
    }
    return p1;   
}
