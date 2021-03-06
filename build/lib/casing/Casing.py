"""
Created on Wed Nov 18 13:59:05 2020
@author: Lucas Valentim lucasbcamara@gmail.com
Synopsis: Código baseado na planilha casing do Nakka, disponível em:
    <https://www.nakka-rocketry.net/softw.html#casing>
Obetivo de transformar a planilha do excel em uma ferramenta em python.
"""
def main():
    import math
    import matplotlib.pyplot
    from casing import materials
    from datetime import datetime


    print("--Casing--")

    print ("---Dimensões do invólucro e Fatores de design---")
    Do= float(input('Insira o diâmetro externo em mm: '))
    t= float(input('Insira a espessura da parede em mm: '))

    print(" ")
    print("Para inserir, pressione:")
    print("0 para o valor do Fator de design de segurança ")
    print("1 para o valor do Fator de segurança de ruptura")
    op=str(input("") )
    
    if op=="0":
        Sd= float(input('Insira o Fator de design de segurança: '))
    elif op=="1":
        Su= float(input('Insira o Fator de segurança de ruptura: '))

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
    print("Material: ", prop)
    print("Características do material: ", '{}'.format(p))
    b=p['Fty']/p['Ftu']
    print("Razão da força do material: b= ",'{:.5f}'.format(b))
    B=(9.5833*b**4)+(-33.528*b**3)+(44.929*b**2)+(-28.479*b)+8.6475
    print("Fator de ruptura: B= ",'{:.5f}'.format(B))
 
    if op=="0":
        print(" ")
        print ("---Pressões de design e ruptura---")
        Pd=(2*(t*p['Fty']*1000)/(Do*Sd))#*6.8947
        print("Design de pressão: Pd= ",'{:.5f}'.format(Pd)," kPa")
        Pu=(2*B*t*p['Fty']*1000/Do)#*6.8947
        print("Pressão de ruptura: Pu= ",'{:.5f}'.format(Pu), " kPa")
        Su=Pu/Pd
        print("Fator de segurança de ruptura: Su= ",'{:.5f}'.format(Su))
    elif op=="1":
        print(" ")
        print ("---Pressões de design e ruptura---")
        Pu=(2*B*t*p['Fty']*1000/Do)#*6.8947
        print("Pressão de ruptura: Pu= ",'{:.5f}'.format(Pu), " kPa")
        Pd=Pu/Su
        print("Design de pressão: Pd= ",'{:.5f}'.format(Pd)," kPa")
        Sd=(2*(t*p['Fty']*1000)/(Do*Pd))
        print("Fator de design de segurança: Sd= ",'{:.5f}'.format(Sd))
    
    print (" ")
    print(" ")
    print ("---Deformação elástica sobre pressão---")
    dD=(2*Pd*(Do/2)**2/p['E']/10**6/t*(1-p['v']/2))#*0.0254
    print("Variação do diâmetro do invólucro: dD= ",'{:.6f}'.format(dD)," m")
    dc=((dD*math.pi))#*0.0254
    print("Variação da circunferência do invólucro: dc= ",'{:.6f}'.format(dc)," m")

#Construção gráfico
    matplotlib.pyplot.title('Fator de ruptura para cilindros pressurizados')
    matplotlib.pyplot.xlabel('Fty/Ftu')
    matplotlib.pyplot.ylabel('B')
    matplotlib.pyplot.plot([0.5, 0.6, 0.7, 0.8, 0.9, 1], [2.048, 1.735, 1.527, 1.379, 1.254, 1.153], color='g', marker='o')
    matplotlib.pyplot.axis([0.5, 1, 1, 2.2]) # [xmin, xmax, ymin, ymax]
    matplotlib.pyplot.show()

    data=datetime.now()
    datatxt=data.strftime('%d/%m/%Y %H:%M')

#construção do arquivo em txt com os valores
    arquivo = open('casing_results.txt', 'a')
    arquivo.write('\n')
    arquivo.write(datatxt)
    arquivo.write('\n')
    arquivo.write('Material: ')
    arquivo.write(prop)
    arquivo.write('\n')
    arquivo.write('Características do material: ')
    arquivo.write('{}'.format(p))
    arquivo.write('\n')
    arquivo.write('Razão da força do material: b= ')
    arquivo.write('{}'.format(b))
    arquivo.write('\n')
    arquivo.write('Fator de ruptura: B= ')
    arquivo.write('{}'.format(B))
    arquivo.write('\n')
    arquivo.write('Design de pressão: Pd= ')
    arquivo.write('{}'.format(Pd))
    arquivo.write('\n')
    arquivo.write('Pressão de ruptura: Pu= ')
    arquivo.write('{}'.format(Pu))
    arquivo.write('\n')
    if op=="0":
        arquivo.write('Fator de segurança de ruptura: Su= ')
        arquivo.write('{}'.format(Su))
        arquivo.write('\n')
    if op=="1":
        arquivo.write('Fator de design de segurança: Sd= ')
        arquivo.write('{}'.format(Sd))
        arquivo.write('\n')
    arquivo.write('Variação no diâmetro do invólucro: dD= ')
    arquivo.write('{}'.format(dD))
    arquivo.write('\n')
    arquivo.write('Variação na circunferência do invólucro: dc= ')
    arquivo.write('{}'.format(dc))
    arquivo.write('\n')
    arquivo.write('--------------------------------')
    arquivo.write('\n')
    arquivo.write(' ')
    arquivo.close()