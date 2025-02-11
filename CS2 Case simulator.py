from random import randint
import os
def opencase(q):
    c=0
    fl=randint(0,100_000_000)/100_000_000
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
    print('float ', str(fl))
    f.write(skin+'\n')
    f.write('pattern '+ patt+'\n')
    f.write('float '+ str(fl)+'\n')
    f.write('--------------------------------------\n')
    f.close()
def Dlore(q):
    c=0
    fl=randint(0,100_000_000)/100_000_000
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
    print('float ', str(fl))
    f.write(skin+'\n')
    f.write('pattern '+ patt+'\n')
    f.write('float '+ str(fl)+'\n')
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
        inp = input()
        if inp == 'sim':
            chosen = 'Simulator case'
        elif inp == 'dlore':
            chosen = 'Dragon Lore case'
        else:
            print('This is not an available option.')
        os.system('cls')
    else:
        if chosen == 'Simulator case':
            opencase(inp)
        elif chosen == 'Dragon Lore case':
            Dlore(inp)
