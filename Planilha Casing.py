"""
Created on Wed Nov 18 13:59:05 2020
@author: Lucas Valentim
"""
import math
from matplotlib import pyplot as plt
import materials
from datetime import datetime

print ("---Dimensões do invólucro e Fatores de design---")
Do= float(input('Insira o diâmetro externo em mm: '))
t= float(input('Insira a espessura da parede em mm: '))
Sd= float(input('Insira o Fator de design de segurança: '))

opcao=input("Deseja ver a lista de materiais? (S/N) ")
if opcao=="S" or opcao=="s": 
        for materials.mec_propk, materials.mec_propv in materials.mec_prop.items():
            print(f'{materials.mec_propk}')
else:
    pass
prop = input('Digite o tipo do material do invólucro: ')
p=materials.mec_prop[prop]

print(" ")
print("-------------------------")
b=p['Fty']/p['Ftu']
print("Razão da força do material: ",'{:.5f}'.format(b))
B=(9.5833*b**4)+(-33.528*b**3)+(44.929*b**2)+(-28.479*b)+8.6475
print("Fator de ruptura: ",'{:.5f}'.format(B))


print(" ")
print ("---Pressões de design e ruptura---")
Pd=(2*(t*p['Fty']*1000)/(Do*Sd))#*6.8947
print("Design de pressão: ",'{:.5f}'.format(Pd)," kPa")
Pu=(2*B*t*p['Fty']*1000/Do)#*6.8947
print("Pressão de ruptura: ",'{:.5f}'.format(Pu), " kPa")
Su=Pu/Pd
print("Fator de segurança de ruptura: ",'{:.5f}'.format(Su))

print (" ")
print(" ")
print ("---Deformação elástica sobre pressão---")
dD=(2*Pd*(Do/2)**2/p['E']/10**6/t*(1-p['v']/2))#*0.0254
print("Variação do diâmetro do invólucro: ",'{:.6f}'.format(dD)," m")
dc=((dD*math.pi))#*0.0254
print("Variação da circunferência do invólucro: ",'{:.6f}'.format(dc)," m")

plt.title('Fator de ruptura para cilindros pressurizados')
plt.xlabel('Fty/Ftu')
plt.ylabel('B')
plt.plot([0.5, 0.6, 0.7, 0.8, 0.9, 1], [2.048, 1.735, 1.527, 1.379, 1.254, 1.153], color='g', marker='o')
plt.axis([0.5, 1, 1, 2.2]) # [xmin, xmax, ymin, ymax]
plt.show()

data=datetime.now()
datatxt=data.strftime('%d/%m/%Y %H:%M')

#construção do arquivo em txt com os valores
arquivo = open('casing_results.txt', 'a')
arquivo.write('\n')
arquivo.write(datatxt)
arquivo.write('\n')
arquivo.write('Razão da força do material: b=')
arquivo.write('{}'.format(b))
arquivo.write('\n')
arquivo.write('Fator de ruptura: B=')
arquivo.write('{}'.format(B))
arquivo.write('\n')
arquivo.write('Design de pressão: Pd=')
arquivo.write('{}'.format(Pd))
arquivo.write('\n')
arquivo.write('Pressão de ruptura: Pu=')
arquivo.write('{}'.format(Pu))
arquivo.write('\n')
arquivo.write('Fator de segurança de ruptura: Su=')
arquivo.write('{}'.format(Su))
arquivo.write('\n')
arquivo.write('Variação no diâmetro do invólucro: dD=')
arquivo.write('{}'.format(dD))
arquivo.write('\n')
arquivo.write('Variação na circunferência do invólucro: dc=')
arquivo.write('{}'.format(dc))
arquivo.write('\n')
arquivo.write('--------------------------------')
arquivo.write('\n')
arquivo.write(' ')
arquivo.close()
