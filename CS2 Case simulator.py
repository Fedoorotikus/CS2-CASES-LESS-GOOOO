from random import randint
import os
def opencase(q):
    c=0
    st=''
    skin=''
    patt=''
    wait=15
    rar=0
    skins = [['R8 revolver | Inlay','XM1014 | Blue Spruce', 'P250 | Sand dune','(Consumer grade)','8'],
             ['AK-47 | Olive Garden','Negev | Bulkhead', 'UMP-45 | Gunsmoke','(Industrial grade)','B'],
             ['SG553 | Cyberforce','AK-47 | Uncharted','Desert Eagle | Urban Rubble','(Mil-spec grade)','1'],
             ['AWP | Pit Viper', 'AK-47 | Slate','AUG | Torque', '(Restricted grade)','5'],
             ['AK-47 | Case hardened','Glock-18 | Vogue', 'SCAR-20 | Cardiac', '(Classified grade)','D'],
             ['AWP | Dragon Lore', 'AK-47 | Legion of Anubis','R8 Revolver | Fade', '(Covert grade)','4'],
             ['Karambit | Case Hardened','Gut knife | Safari mesh', 'Butterfly knife | Gamma Doppler', '(Special)','6']]
    rar=randint(1,4)
    if rar == 2:
        st = 'Stattrack '
    rar=randint(0,500)
    if q!='q':
        for i in range(23):
            rar=randint(0,500)
            wait+=wait
            os.system('cls')
            if rar<=299:
                rar=0
            elif rar<=399:
                rar=1
            elif rar<=449:
                rar=2
            elif rar<=479:
                rar=3
            elif rar<=493:
                rar=4
            elif rar<=498:
                rar=5
            else:
                rar=6
            os.system('color '+skins[rar][-1])
            print(skins[rar][randint(0,len(skins[rar])-3)]+' ' + skins[rar][-2])
            for i in range(wait+10_000_000):
                pass
    os.system('cls')
    if rar<=299:
        rar=0
    elif rar<=399:
        rar=1
    elif rar<=449:
        rar=2
    elif rar<=479:
        rar=3
    elif rar<=493:
        rar=4
    elif rar<=498:
        rar=5
    else:
        rar=6
    os.system('color '+skins[rar][-1])
    patt=str(randint(0,1000))
    skin=st+skins[rar][randint(0,len(skins[rar])-3)]+' ' + skins[rar][-2]
    print(skin)
    print('pattern '+ patt)
    f.write(skin+'\n')
    f.write('pattern '+ patt+'\n')
    f.write('--------------------------------------\n')
    f.close()
def Dlore(q):
    c=0
    st=''
    skin=''
    patt=''
    wait=15
    rar=0
    skins = [['AWP | Dragon Lore', '(Covert grade)','4']]
    rar=randint(1,4)
    if rar == 2:
        st = 'Stattrack '
    rar=0
    if q!='q':
        for i in range(23):
            rar=0
            wait+=wait
            os.system('cls')
            os.system('color '+skins[rar][-1])
            print(skins[rar][randint(0,len(skins[rar])-3)]+' ' + skins[rar][-2])
            for i in range(wait+10_000_000):
                pass
    os.system('cls')
    rar=0
    os.system('color '+skins[rar][-1])
    patt=str(randint(0,1000))
    skin=st+skins[rar][randint(0,len(skins[rar])-3)]+' ' + skins[rar][-2]
    print(skin)
    print('pattern '+ patt)
    f.write(skin+'\n')
    f.write('pattern '+ patt+'\n')
    f.write('--------------------------------------\n')
    f.close()
def Revolution(q):
    c=0
    st=''
    skin=''
    patt=''
    wait=15
    rar=0
    skins = [['SG553 | Cyberforce','SCAR-20 | Fragments','P250 | Re.built','Tec-9 | Rebel','MAG-7 | Insomnia', 'MP-5SD | Liquidation', 'MP9 | Featherweight','(Mil-spec grade)','1'],
             ['MAC-10 | Sakkaku','P90 | Neoqueen', 'Glock-18 | Umbral Rabbit', 'Revolver R8 | Banana Cannon', 'M4A1-S | Emphorosaur - S','(Restricted grade)','5'],
             ['UMP-45 | Wild Child','AWP | Duality','P2000 | Wicked Sick','(Classified grade)','D'],
             ['AK-47 | Head Shot','M4A4 | Temukau','(Covert grade)','4'],
             ['Sport Gloves | Vice','Specialist Gloves | Fade','Hand Wraps | Cobalt Skulls','Specialist Gloves | Crimson Web','Sport Gloves | Amphibious','Driver Gloves | Imperial Plaid','Driver Gloves | King Snake','Moto Gloves | POW!','Specialist Gloves | Mogul','Sport Gloves | Omega','Moto Gloves | Polygon','Hand Wraps | Overprint','Moto Gloves | Turtle', 'Sport Gloves | Bronze Morph','Driver Gloves | Overtake','Hydra Gloves | Case Hardened','Hand Wraps | Duct Tape','Hydra Gloves | Emerald','Hand Wraps | Arboreal', 'Moto Gloves | Transport','Specialist Gloves | Buckshot','Driver Gloves | Racing Green','Hydra Gloves | Rattler','Hydra Gloves | Mangrove','(Special)','6']]
    rar=randint(1,4)
    if rar == 2:
        st = 'Stattrack '
    rar=randint(0,500)
    if q!='q':
        for i in range(23):
            rar=randint(0,500)
            wait+=wait
            os.system('cls')
            if rar<=399:
                rar=0
            elif rar<=459:
                rar=1
            elif rar<=489:
                rar=2
            elif rar<=498:
                rar=3
            else:
                rar=4
            os.system('color '+skins[rar][-1])
            print(skins[rar][randint(0,len(skins[rar])-3)]+' ' + skins[rar][-2])
            for i in range(wait+10_000_000):
                pass
    os.system('cls')
    if rar<=399:
        rar=0
    elif rar<=459:
        rar=1
    elif rar<=489:
        rar=2
    elif rar<=498:
        rar=3
    else:
        rar=4
    if rar == 4:
        st = ''
    os.system('color '+skins[rar][-1])
    patt=str(randint(0,1000))
    skin=st+skins[rar][randint(0,len(skins[rar])-3)]+' ' + skins[rar][-2]
    print(skin)
    print('pattern '+ patt)
    f.write(skin+'\n')
    f.write('pattern '+ patt+'\n')
    f.write('--------------------------------------\n')
    f.close()
chosen = 'Simulator case'
while True:
    f = open('Inventory.txt','a')
    print('To open a case, write something. "q" to quickopen.')
    print('"ch" to change the current selected case. Currently '+chosen)
    inp = input()
    os.system('cls')
    if inp == "ch":
        print("Options:")
        print('Simulator case(original case) - "sim"')
        print('Dragon Lore case(original case) - "dlore"')
        print('Revolution case - "rev"')
        inp = input()
        if inp == 'sim':
            chosen = 'Simulator case'
        elif inp == 'dlore':
            chosen = 'Dragon Lore case'
        elif inp == 'rev':
            chosen = 'Revolution case'
        else:
            print('This is not an available option.')
        os.system('cls')
    else:
        if chosen == 'Simulator case':
            opencase(inp)
        elif chosen == 'Dragon Lore case':
            Dlore(inp)
        elif chosen == 'Revolution case':
            Revolution(inp)
