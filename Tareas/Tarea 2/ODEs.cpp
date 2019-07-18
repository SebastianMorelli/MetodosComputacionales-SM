//Este código soluciona la ecuación de segundo orden que describe la trayectoria de la tierra.

#include <iostream>
#include <cmath>
using namespace std;

//Declaración Variables 

float dt0 = 0.1;
float dt1 = 0.01;
float dt2 = 0.001;

int numpunt = 20000;
float Msun = 1.0;
float G = 39.42645673494773;  
//G hallado haciendo las susticiones de unidades y calculado en python: (6.673e-11 * 1.989e30 * (6.68459e-12**3))/(3.171e-8**2)
float Rst = 1.0;

//Declaración funciones

float * rugen_Kutta(float arr1, float arr2, float arr3, float h);

int main()
{
    //Arrays Rugen-Kutta
    float t0_RK[numpunt];
    float t1_RK[numpunt];
    float t2_RK[numpunt];
    
    float x_RK_dt0[numpunt];
    float x_RK_dt1[numpunt];
    float x_RK_dt2[numpunt];
    
    float y_RK_dt0[numpunt];
    float y_RK_dt1[numpunt];
    float y_RK_dt2[numpunt];
    
    float vx_RK_dt0[numpunt];
    float vx_RK_dt1[numpunt];
    float vx_RK_dt2[numpunt];
    
    float vy_RK_dt0[numpunt];
    float vy_RK_dt1[numpunt];
    float vy_RK_dt2[numpunt];
    
    //Condiciones iniciales Rugen-Kutta
    t0_RK[0] = 0;
    t1_RK[0] = 0;
    t2_RK[0] = 0;
    
    x_RK_dt0[0] = 0.1163;
    x_RK_dt1[0] = 0.1163;
    x_RK_dt2[0] = 0.1163;
    
    vx_RK_dt0[0] = -6.35;
    vx_RK_dt1[0] = -6.35;
    vx_RK_dt2[0] = -6.35;
    
    y_RK_dt0[0] = 0.9772;
    y_RK_dt1[0] = 0.9772;
    y_RK_dt2[0] = 0.9772;
    
    vy_RK_dt0[0] = 0.606;
    vy_RK_dt1[0] = 0.606;
    vy_RK_dt2[0] = 0.606;
    
    for(int i = 1; i <= numpunt; i++){
        
        t0_RK[i] = rugen_Kutta(t0_RK[i-1], x_RK_dt0[i-1], vx_RK_dt0[i-1], dt0)[0];
        x_RK_dt0[i] = rugen_Kutta(t0_RK[i-1], x_RK_dt0[i-1], vx_RK_dt0[i-1], dt0)[1];
        vx_RK_dt0[i] = rugen_Kutta(t0_RK[i-1], x_RK_dt0[i-1], vx_RK_dt0[i-1], dt0)[2];
        y_RK_dt0[i] = rugen_Kutta(t0_RK[i-1], y_RK_dt0[i-1], vy_RK_dt0[i-1], dt0)[1];
        vy_RK_dt0[i] = rugen_Kutta(t0_RK[i-1], y_RK_dt0[i-1], vy_RK_dt0[i-1], dt0)[2];
        
        t1_RK[i] = rugen_Kutta(t1_RK[i-1], x_RK_dt1[i-1], vx_RK_dt1[i-1], dt1)[0];
        x_RK_dt1[i] = rugen_Kutta(t1_RK[i-1], x_RK_dt1[i-1], vx_RK_dt1[i-1], dt1)[1];
        vx_RK_dt1[i] = rugen_Kutta(t1_RK[i-1], x_RK_dt1[i-1], vx_RK_dt1[i-1], dt1)[2];
        y_RK_dt1[i] = rugen_Kutta(t1_RK[i-1], y_RK_dt1[i-1], vy_RK_dt1[i-1], dt1)[1];
        vy_RK_dt1[i] = rugen_Kutta(t1_RK[i-1], y_RK_dt1[i-1], vy_RK_dt1[i-1], dt1)[2];
        
        t2_RK[i] = rugen_Kutta(t2_RK[i-1], x_RK_dt2[i-1], vx_RK_dt2[i-1], dt2)[0];
        x_RK_dt2[i] = rugen_Kutta(t2_RK[i-1], x_RK_dt2[i-1], vx_RK_dt2[i-1], dt2)[1];
        vx_RK_dt2[i] = rugen_Kutta(t2_RK[i-1], x_RK_dt2[i-1], vx_RK_dt2[i-1], dt2)[2];
        y_RK_dt2[i] = rugen_Kutta(t2_RK[i-1], y_RK_dt2[i-1], vy_RK_dt2[i-1], dt2)[1];
        vy_RK_dt2[i] = rugen_Kutta(t2_RK[i-1], y_RK_dt2[i-1], vy_RK_dt2[i-1], dt2)[2];    
    }

    cout<<"Tiempo dt = 0.1: "<<"Posición x dt = 0.1: "<<"Velocidad x dt = 0.1: "<<"Posición y dt = 0.1: "<<"Velocidad y dt = 0.1: "<<"Tiempo dt = 0.01: "<<"Posición x dt = 0.01: "<<"Velocidad x dt = 0.01: "<<"Posición y dt = 0.01: "<<"Velocidad y dt = 0.01: "<<"Tiempo dt = 0.001: "<<"Posición x dt = 0.001: "<<"Velocidad x dt = 0.001: "<<"Posición y dt = 0.001: "<<"Velocidad y dt = 0.001:"<<endl;
    for (int i = 1; i <= numpunt; i++){
        cout<<t0_RK[i]<<" "<<x_RK_dt0[i]<<" "<<vx_RK_dt0[i]<<" "<<y_RK_dt0[i]<<" "<<vy_RK_dt0[i]<<" "<<t1_RK[i]<<" "<<x_RK_dt1[i]<<" "<<vx_RK_dt1[i]<<" "<<y_RK_dt1[i]<<" "<<vy_RK_dt1[i]<<" "<<t2_RK[i]<<" "<<x_RK_dt2[i]<<" "<<vx_RK_dt2[i]<<" "<<y_RK_dt2[i]<<" "<<vy_RK_dt2[i]<<endl;
    }
}


float * rugen_Kutta(float arr1, float arr2, float arr3, float h){
    
    float arrayresult[3];
    float *p = arrayresult;
    
    float k1x1 = arr3;
    float k1x2 = -((G*Msun)/pow(Rst,2))*arr2;
    
    float x1 = arr1 + (h/2.0);
    float y1x1 = arr2 + (h/2.0) * k1x1;
    float y2x1 = arr3 + (h/2.0) * k1x2;
    float k2x1 = y2x1;
    float k2x2 = -((G*Msun)/pow(Rst,2))*y1x1;
    
    float x2 = arr1 + (h/2.0);
    float y1x2 = arr2 + (h/2.0) * k2x1;
    float y2x2 = arr3 + (h/2.0) * k2x2;
    float k3x1 = y2x2;
    float k3x2 = -((G*Msun)/pow(Rst,2))*y1x2;
    
    float x3 = arr1 + (h/2.0);
    float y1x3 = arr2 + (h) * k3x1;
    float y2x3 = arr3 + (h) * k3x2;
    float k4x1 = y2x3;
    float k4x2 = -((G*Msun)/pow(Rst,2))*y1x3;
    
    float prom_kx1 = (1.0/6.0)*(k1x1 + 2.0*k2x1 + 2.0*k3x1 + k4x1);
    float prom_kx2 = (1.0/6.0)*(k1x2 + 2.0*k2x2 + 2.0*k3x2 + k4x2);
    
    float x_new = arr1 + h;
    float y1_new = arr2 + h * prom_kx1;
    float y2_new = arr3 + h * prom_kx2;
    
    arrayresult[0] = x_new;
    arrayresult[1] = y1_new;
    arrayresult[2] = y2_new;
    
    return p;
}
