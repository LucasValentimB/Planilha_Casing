"""
Created on Wed Nov 18 13:59:05 2020
@author: Lucas Valentim
"""
import math
print ("---Dimensões do invólucro e Fatores de design---")
print (" ")
Do= float(input('Insira o diâmetro externo em mm: '))
t= float(input('Insira a espessura da parede em mm: '))
Sd= float(input('Insira o Fator de design de segurança: '))
print(" ")
print ("---Propriedades de materiais---")
print (" ")
Fty= float(input('Insira a Força de rendimento em MPa: '))
Ftu= float(input('Insira a Força máxima em MPa: '))
E= float(input('Insira o modulo de elasticidade em MPa: '))
v= float(input('Insira o coeficinte de poisson: '))

print(" ")
b=(Fty/Ftu)
print("Razão da força do material: ",'{:.3f}'.format(b))
B=(9.5833*b**4)+(-33.528*b**3)+(44.929*b**2)+(-28.479*b)+8.6475
print("Fator de ruptura: ",'{:.3f}'.format(B))

print(" ")
print ("---Pressões de design e ruptura---")
print (" ")
Pd=2*(t*Fty*1000)/(Do*Sd)
print("Pressão de Design: ",'{:.3f}'.format(Pd)," kPa")
Pu=2*B*t*Fty*1000/Do
print("Pressão de ruptura: ",'{:.3f}'.format(Pu), " kPa")
Su=Pu/Pd
print("Fator de segurança de ruptura: ",'{:.3f}'.format(Su))

print(" ")
print ("---Deformação elástica sobre pressão---")
print (" ")
dD=2*Pd*(Do/2)**2/E/10**6/t*(1-v/2)
print("Variação do diâmetro do invólucro: ",'{:.5f}'.format(dD)," m")
dc=(dD*math.pi)
print("Variação da circunferência do invólucro: ",'{:.5f}'.format(dc)," m")

