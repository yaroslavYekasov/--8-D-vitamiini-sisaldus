from random import*
#def patsiendid(n:list,d:list):
#    na=int(input("Mitu inimest: "))
#    for i in range(na):
#        nimi=input("sissesta nimi:")
#        vita=randint(1000,4000)
#        n.append(nimi)
#        d.append(vita)

def patsiendid(n:list,d:list):
    """
    mille käivitamisel toimub kahe massiivi täitmine: nimed[], D_vitamini_sisaldus[]
    """
    na=int(input("Mitu inimest:"))
    for i in range (na):
        nimi=input("sissesta nimi:")
        palk=randint(10,100)
        n.append(nimi)
        d.append(palk)
    return n,d

def suur_vaike(n:list,d:list):
    """
    Programm koostab nimekirja inimestest, kes on vitamonid vähem kui kolmkümmend, kasutades 30i suunanäitajat.
    """
    number=30
    for g in d:
        if g < number:
            ind=d.index(g)
            print(f"{g}, {n[ind]}")

def keskminepalk(n:list,d:list):
    """
    Programm leiab valemi keskmise
    """
    kesk_d=sum(d)/len(d)
    print(f"on keskmine d vitamiini näitleja {kesk_d}")
    return n,d

def bolshe(n:list,d:list):
    """
    Programm leiab valemi keskmise
    """
    palk=max(d)
    ind=d.index(palk)
    nimi=n[ind]
    return palk,nimi

def search_patients_by_name(nimed, D_vitamiini):
    """
    Otsib nimekirjast sarnast elementi
    """
    nimi = input("sissesta nimi ")
    for i in range(len(nimed)):
        if nimed[i].lower() == nimi.lower():
            print("leidud pacient:", nimed[i], D_vitamiini[i])

def menshe(n:list,d:list):
    """
    Funktsiooni abil leiab minimum suurima arvu
    """
    palk=min(d)
    ind=d.index(palk)
    nimi=n[ind]
    return palk,nimi

    


