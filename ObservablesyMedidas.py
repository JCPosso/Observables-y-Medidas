import math
from SimulacionCuantica import *        
if __name__ == '__main__':
        sz= matriz([ [[1,0],[0,0]],[[0,0,],[-1,0] ] ])
        sy= matriz([ [[0,0],[0,-1]],[[0,1,],[0,0] ] ])
        sx= matriz([ [[0,0],[1,0]],[[1,0,],[0,0] ] ])

        spin_up= matriz([ [[1,0]],[[0,0]] ])
        
        #EXERCISE 4.3.1
        print("Posibles estados del sistema  con un estado en SPIN UP despues de ser observado:\n")
        #caclculamos  vectores propios y valores propios
        sz_valP,sz_vecP= sz.eigen()
        sy_valP,sy_vecP= sy.eigen()
        sx_valP,sx_vecP= sx.eigen()
        print("Para Sz")
        print(sz_vecP[0])
        print(sz_vecP[1])
        print("Para Sy")
        print(sy_vecP[0])
        print(sy_vecP[1])
        print("Para Sx")
        print(sx_vecP[0])
        print(sx_vecP[1])
        print("\n")

        #EXCERCISE 4.3.2
        
        # probabilidad transicion SPIN UP a cada uno de los vectores propios
        print("Los valores propios del sistema son:")
        print("Para Sz: "+str(sz_valP.c[0][0])+" y "+str(sz_valP.c[1][0]))
        print("Para Sy: "+str(sy_valP.c[0][0])+" y "+str(sy_valP.c[1][0]))
        print("Para Sx: "+str(sx_valP.c[0][0])+" y "+str(sx_valP.c[1][0]))
        print("\n")
        
        print("Las respectivos probabilidades de colapso son")
        sz_p1=probbilidad_transitoVec(spin_up,sz_vecP[0])
        sz_p2=probbilidad_transitoVec(spin_up,sz_vecP[1])
        print("Para Sz")
        print(sz_p1,sz_p2)

        sy_p1=probbilidad_transitoVec(spin_up,sy_vecP[0])
        sy_p2=probbilidad_transitoVec(spin_up,sy_vecP[1])
        print("Para Sy")
        print(sy_p1,sy_p2)

        sx_p1=probbilidad_transitoVec(spin_up,sx_vecP[0])
        sx_p2=probbilidad_transitoVec(spin_up,sx_vecP[1])
        print("Para Sx")
        print(sx_p1,sx_p2)
        print('\n')
        print("Las respectivos probabilidades de distribucion son")
        print("Para Sz: "+str(sz_p1*sz_valP.c[0][0].real+sz_p2*sz_valP.c[1][0].real))
        print("Para Sy: "+str(sy_p1*sy_valP.c[0][0].real+sy_p2*sy_valP.c[1][0].real))
        print("Para Sx: "+str(sx_p1*sx_valP.c[0][0].real+sx_p2*sx_valP.c[1][0].real))
        print(" Los valores resultantes confirman el postulado 4.1.1")

        #EXCERCISE 4.4.1
        u1= matriz([[[0,0],[1,0]],[[1,0],[0,0]]])
        u2= matriz([[[math.sqrt(2)/2,0],[math.sqrt(2)/2,0]],[[math.sqrt(2)/2,0],[-math.sqrt(2)/2,0]]])
        print("Probamos que sean unitarias")
        print(u1.isUnitary())
        print(u2.isUnitary())
        res=u2.multiplica(u1)
        print("Probamos que el producto sea unitario")
        print(res.isUnitary())
        
        #EXCERCISE 4.4.2
        billiard_ball= matriz([[ [0,0],[1/math.sqrt(2),0],[1/math.sqrt(2),0],[0,0]],
                               [ [0,1/math.sqrt(2)],[0,0],[0,0],[1/math.sqrt(2),0]],
                               [ [1/math.sqrt(2),0],[0,0],[0,0],[0,1/math.sqrt(2)]],
                               [ [0,0],[1/math.sqrt(2),0],[-1/math.sqrt(2),0],[0,0] ] ])
        stat= matriz([ [[1,0]],[[0,0]],[[0,0]],[[0,0]] ])
        print("estado final para la  billiard_ball :")
        res=  billiard_ball.state(stat,3)
        print(res)
        print(" valor en punto 3 es "+ str(res.c[3][0]))
