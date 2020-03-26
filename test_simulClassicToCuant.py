import unittest
import math
from SimulacionCuantica import *
class TestMathMethods(unittest.TestCase):
        def test01_Canicas_Booleanos(self):
                ways=matriz([ [ [0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                              [ [0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                              [ [0,0],[1,0],[0,0],[0,0],[0,0],[1,0] ],
                              [ [0,0],[0,0],[0,0],[1,0],[0,0],[0,0]],
                              [ [0,0],[0,0],[1,0],[0,0],[0,0],[0,0]],
                              [ [1,0],[0,0],[0,0],[0,0],[1,0],[0,0 ] ] ])
                
                x=matriz([ [[6,0]],[[2,0]],[[1,0]],[[5,0]],[[3,0]],[[10,0]] ])
                
                ans=ways.state(x,1)
                self.assertTrue(ans == matriz([ [[ 0,0 ]],[[ 0,0 ]],[[ 12,0 ]],[[5,0]],[[ 1,0]],[[ 9,0]] ]))

        def test01_Multirendija_Probabilistico_DosRendijas(self):
                v= matriz([ [[1/3,0]],[[1/3,0]],[[1/3,0]] ])
                matrizCaminos, estado     =    experimento_multirendija_probabilistico(2,5,v)

                self.assertTrue(matrizCaminos == matriz([ [ [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [1/2,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [1/2,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [0,0],[1/3,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [0,0],[1/3,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0] ],
                                                          [ [0,0],[1/3,0],[1/3,0],[0,0],[0,0],[1,0],[0,0],[0,0] ],
                                                          [ [0,0],[0,0],[1/3,0],[0,0],[0,0],[0,0],[1,0],[0,0] ],
                                                          [ [0,0],[0,0],[1/3,0],[0,0],[0,0],[0,0],[0,0],[1,0] ]] ))
                
                self.assertTrue(estado == matriz([ [[ 0,0 ]],[[ 0,0 ]],[[ 0,0 ]],[[1/6,0]],[[ 1/6,0]],[[ 1/3,0]],[[1/6,0]],[[ 1/6,0]] ]))

        def test02_Multirendija_Probabilistico_TresRendijas(self):
                matrizCaminos, estado     =    experimento_multirendija_probabilistico(3,11,1/5)

                self.assertTrue(matrizCaminos == matriz([ [ [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [1/3,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [1/3,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [1/3,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [0,0],[1/5,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [0,0],[1/5,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [0,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [0,0],[1/5,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [0,0],[1/5,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [0,0],[0,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [0,0],[0,0],[1/5,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [0,0],[0,0],[1/5,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0] ],
                                                          [ [0,0],[0,0],[0,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0] ],
                                                          [ [0,0],[0,0],[0,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0] ],
                                                          [ [0,0],[0,0],[0,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0] ], ] ))
                
                self.assertTrue(estado == matriz([ [[ 0,0 ]],[[ 0,0 ]],[[ 0,0 ]],[[ 0,0 ]],[[1/15,0]],[[ 1/15,0]],
                                                   [[ 1/15,0]],[[2/15,0]],[[ 2/15,0]],[[ 1/15,0]],[[ 2/15,0]],[[ 2/15,0]],
                                                   [[ 1/15,0]],[[ 1/15,0]],[[ 1/15,0]]]))
                """
                Funcion para graficar ==>  graficar(estado,title)
                """
        def test01_Multirendija_Cuantico_DosRendijas(self):
                v= matriz([ [[-math.sqrt(6)/6,math.sqrt(6)/6]],[[-math.sqrt(6)/6,-math.sqrt(6)/6]],[[math.sqrt(6)/6,-math.sqrt(6)/6]] ])
                matrizCaminos, estado     =    experimento_multirendija_cuantico(2,5,v)

                self.assertTrue(matrizCaminos ==matriz([[ [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                        [ [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                        [ [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                        [ [1/6,0],[1/3,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0] ],
                                                        [ [1/6,0],[1/3,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0] ],
                                                        [ [0,0],[1/3,0],[1/3,0],[0,0],[0,0],[1,0],[0,0],[0,0] ],
                                                        [ [1/6,0],[0,0],[1/3,0],[0,0],[0,0],[0,0],[1,0],[0,0] ],
                                                        [ [1/6,0],[0,0],[1/3,0],[0,0],[0,0],[0,0],[0,0],[1,0] ] ]) )
                
                self.assertTrue(estado == matriz([ [[ 0,0 ]],[[ 0,0 ]],[[ 0,0 ]],[[1/6,0]],[[ 1/6,0]],[[ 0,0]],[[1/6,0]],[[ 1/6,0]] ]))
                graficar(estado,"Fenómeno interferencia 2 rendijas cuantico")
        def test02_Multirendija_Cuantico_TresRendijas(self):
                v= matriz([ [[-math.sqrt(10)/10,math.sqrt(10)/10]],[[-math.sqrt(10)/10,math.sqrt(10)/10]],[[-math.sqrt(10)/10,-math.sqrt(10)/10]],[[math.sqrt(10)/10,-math.sqrt(10)/10]],[[math.sqrt(10)/10,-math.sqrt(10)/10]] ])
                matrizCaminos, estado     =    experimento_multirendija_cuantico(3,11,v)
                
                self.assertTrue(matrizCaminos ==matriz([ [  [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [1/15,0],[1/5,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [1/15,0],[1/5,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [1/15,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [0,0],[1/5,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [0,0],[1/5,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [1/15,0],[0,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [0,0],[0,0],[1/5,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [0,0],[0,0],[1/5,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0] ],
                                                          [ [1/15,0],[0,0],[0,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0] ],
                                                          [ [1/15,0],[0,0],[0,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0] ],
                                                          [ [1/15,0],[0,0],[0,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0] ], ] ))
               
                self.assertTrue(estado == matriz([ [[ 0,0 ]],[[ 0,0 ]],[[ 0,0 ]],[[ 0,0 ]]
                                                ,[[1/15,0]],[[ 1/15,0]],[[ 1/15,0]],
                                                [[ 0,0 ]],[[ 0,0 ]],[[1/15,0]],[[ 0,0 ]],[[ 0,0 ]],
                                                [[ 1/15,0]],[[ 1/15,0]],[[ 1/15,0]] ]))
                graficar(estado,"Fenómeno interferencia 3 rendijas Cuantico")
        def test01_probabilidadEncontrarParticula_PosicionDada(self):
                stateV=matriz ([ [[-3,-1]],[[0,-2]],[[0,1]],[[2,0]] ])
                pos=2
                n_probabilidades,probabilidadPedida=probabilidad(stateV,pos)
                self.assertTrue(probabilidadPedida==5.263157894736841)
        def test02_probabilidadEncontrarParticula_CualquierPosicion(self):
                stateV=matriz ([ [[-3,-1]],[[0,-2]],[[0,1]],[[2,0]] ])
                pos=2
                n_probabilidades,probabilidadPedida=probabilidad(stateV,None)
                self.assertTrue(n_probabilidades==matriz([ [[52.63157894736841,0]],[[21.052631578947363,0]],[[5.263157894736841,0]],[[21.052631578947363,0]] ]) )
                graficar(n_probabilidades,"test02_probabilidadEncontrarParticula_CualquierPosicion")
        def test01_probabilidad_Transitar_otra_Posicion(self):
                c= complejo(math.sqrt(2)/2,0)
                v1= matriz([ [[1,0]],[[0,1]] ])
                v2= matriz([ [[0,1]],[[-1,0]] ] )
                v1=v1.multiplicaEscalar(c)
                v2=v2.multiplicaEscalar(c)
                res= transicionAmplitud(v1,v2)
                self.assertTrue(res== complejo(0,-1) )
        def test02_probabilidad_Transitar_otra_Posicion(self):
                c= complejo(math.sqrt(2)/2,0)
                v1= matriz([ [[0,1]],[[-1,0]] ])
                v2= matriz([ [[1,0]],[[-1,0]] ] )
                v1=v1.multiplicaEscalar(c)
                v2=v2.multiplicaEscalar(c)
                res= transicionAmplitud(v1,v2)
                self.assertTrue(res== complejo(1/2,1/2) )
        def test01_calcular_media_varianza(self):
                c= complejo(1/math.sqrt(2),0)
                ob= matriz([ [ [2,0],[1,1] ],[ [1,-1],[3,0] ] ])
                v2= matriz([ [[1,0]],[[0,1]] ] )
                v2=v2.multiplicaEscalar(c)
                media,varianza= sistema_estadistico(ob,v2)
                self.assertTrue(round(media,2)==1.5)
                self.assertTrue(round(varianza,2)==1.25 )
        def test01_probbilidad_transito_vectores_propios(self):
                fi= matriz([ [[1/math.sqrt(2),0]],[[1/math.sqrt(2),0]] ])
                a= matriz([ [ [-1,0],[0,-1] ],[ [0,1],[1,0] ] ])
                valores_propios,vectores_propios=a.eigen()
                res1=probbilidad_transitoVec(fi,vectores_propios[0])
                res2=probbilidad_transitoVec(fi,vectores_propios[1])
                self.assertTrue(res1==0.5)
                self.assertTrue(res2==0.5)
        def test01_dinamica(self):
                array=[]
                u1= matriz([ [ [0,0], [1,0]],[[1,0],[0,0]]])
                u2= matriz([ [ [math.sqrt(2)/2,0],[math.sqrt(2)/2,0]],[[math.sqrt(2)/2,0],[math.sqrt(2)/2,0]] ])
                array.append(u1)
                array.append(u2)
                fi=matriz([ [[1,0]],[[0,0]] ])
                res=dinamica(1,array,fi)
                #go back!
                u1= matriz([ [ [0,0], [1,0]],[[1,0],[0,0]]])
                u2= matriz([ [ [math.sqrt(2)/2,0],[math.sqrt(2)/2,0]],[[math.sqrt(2)/2,0],[math.sqrt(2)/2,0]] ])
                array=[]
                array.append(u2)
                array.append(u1)
                res2=dinamica(1,array,fi)
                self.assertTrue(res==res2)
        def  test01_excercise_4_3_1(self):
                sz= matriz([ [[1,0],[0,0]],[[0,0,],[-1,0] ] ])
                sy= matriz([ [[0,0],[0,-1]],[[0,1,],[0,0] ] ])
                sz= matriz([ [[0,0],[1,0]],[[1,0,],[0,0] ] ])
                #caclculamos  vectores propios y valores propios
                sz_valP,sz_vecP= sz.eigen()
                sx_valP,sy_vecP= sz.eigen()
                sx_valP,sx_vecP= sz.eigen()

                spin_up= matriz([ [[1,0]],[[0,0]] ])
                spin_down=matriz([ [[0,0]],[[1,0]] ])
                
                # probabilidad transicion SPIN UP a cada uno de los vectores propios
                sz_res1=probbilidad_transitoVec(spin_up,sz_vecP[0])
                sz_res2=probbilidad_transitoVec(spin_up,sz_vecP[1])
                print(sz_res1,sz_res2)

                sy_res1=probbilidad_transitoVec(spin_up,sy_vecP[0])
                sy_res2=probbilidad_transitoVec(spin_up,sy_vecP[1])
                print(sz_res1,sz_res2)

                sx_res1=probbilidad_transitoVec(spin_up,sx_vecP[0])
                sx_res2=probbilidad_transitoVec(spin_up,sx_vecP[1])
                print(sz_res1,sz_res2)
                print('\n')

                # probabilidad transicion SPIN DOWN a cada uno de los vectores propios
                sz_valP,sz_vecP= sz.eigen()
                sx_valP,sy_vecP= sz.eigen()
                sx_valP,sx_vecP= sz.eigen()
                
                sz_res1=probbilidad_transitoVec(spin_down,sz_vecP[0])
                sz_res2=probbilidad_transitoVec(spin_down,sz_vecP[1])
                print(sz_res1,sz_res2)

                sy_res1=probbilidad_transitoVec(spin_down,sy_vecP[0])
                sy_res2=probbilidad_transitoVec(spin_down,sy_vecP[1])
                print(sz_res1,sz_res2)

                sx_res1=probbilidad_transitoVec(spin_down,sx_vecP[0])
                sx_res2=probbilidad_transitoVec(spin_down,sx_vecP[1])
                print(sz_res1,sz_res2)
                
if __name__ == '__main__':
	unittest.main()
