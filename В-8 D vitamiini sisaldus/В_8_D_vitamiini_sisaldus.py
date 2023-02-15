from module1 import *
from random import*

nimed=[]
D_vitamiini=[]

#while True:
#    nimed,D_vitamiini=patsiendid(nimed,D_vitamiini)
#    print("nimed")
#    print("D_vitamiini")


nimed,D_vitamiini=patsiendid(nimed,D_vitamiini)
print(nimed)
print(D_vitamiini)


menu=int(input("Valik:\n1- D-vitamiini puudusega patsientide nimekiri \n2- D-vitamiini keskmine näitaja \n3- Näitab K- nimekirja, millel on suurim näitaja \n4- Teosta töötajate otsimine nime järgi ja näita ekraanile selle tulemus \n5- Leiab väikseima arvu\n"))
if menu==1:
    suur_vaike(nimed,D_vitamiini)
elif menu==2:
    keskminepalk(nimed,D_vitamiini)
elif menu==3:
    palk,nimi=bolshe(nimed,D_vitamiini)
    print(f"suurim vitamiini d {palk} {nimi}")
elif menu==4:
    search_patients_by_name(nimed,D_vitamiini)
      
elif menu==5:
    palk,nimi=menshe(nimed,D_vitamiini)
    print(f"suurim vitamiini d {palk} {nimi}")




