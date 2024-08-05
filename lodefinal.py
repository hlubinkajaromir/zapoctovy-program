import random
import time
import pygame
pygame.init()


#symbolyka: 0 = voda, 1 = lod, x = vedle, z = zasah, p = potopena
#globalni promenne
pocetradku = 10
pocetsloupcu = 10 
delkylodi = [5,4,3,3,2,2]
pocetlodi = len(delkylodi)
pozicelodi = []#radek,radek,sloupec,sloupec
pocetpolilodihrac = sum(delkylodi)
pocetpolilodipocitac = sum(delkylodi)
hodnocenipoli = {0:[],1:[]}
sirka = 1920
vyska = 1020
pocetradku = 10 
pocetsloupcu = 10
velikostpole = 50
mezeravrsek,mezerabok,mezeramezi = 200,100,200
font = pygame.font.Font('freesansbold.ttf', 32)
barvatext = (200,200,200)
barvapozadi = (100,100,100)


okno = pygame.display.set_mode((sirka,vyska))
pygame.display.set_caption("Námořní bitva")
clock = pygame.time.Clock()

def vytvorpole():#vytvori hraci pole
    hracipole = []
    for i in range (pocetradku):
        radek = []
        for j in range (pocetsloupcu):
            radek.append(0)
        hracipole.append(radek)
    return hracipole

   
def nactilode(hraciplan):#vygeneruje lode pocitace
    pointer = 0
    random.seed(time.time())    
    while pointer < pocetlodi:
        valid = True
        poziceradek1 = random.randrange(0,pocetradku)
        pozicesloupec1 = random.randrange(0,pocetsloupcu)
        if hraciplan[poziceradek1][pozicesloupec1] != 0:
            continue
        smer = random.randint(0,1) #0 vodorovně, 1 svisle
        if smer == 1:
            poziceradek2 = random.choice([poziceradek1-(delkylodi[pointer]),poziceradek1+(delkylodi[pointer])])
            zacatek = min(poziceradek1,poziceradek2)
            konec = max(poziceradek1,poziceradek2)
            if poziceradek2 < 0 or poziceradek2 > pocetradku:
                valid = False
            else:
                for i in range (zacatek,konec):
                    valid = overlod(i,pozicesloupec1,hraciplan)
                    if valid == False:
                        break
            if valid == True:#prepsani pole
                for i in range (zacatek,konec):
                    hraciplan[i][pozicesloupec1] = 1
                pozicelode = [zacatek,konec,pozicesloupec1,pozicesloupec1+1]
                pozicelodi.append(pozicelode)
                pointer += 1
        else:
            pozicesloupec2 = random.choice([pozicesloupec1-(delkylodi[pointer]),pozicesloupec1+(delkylodi[pointer])])
            zacatek =min(pozicesloupec1,pozicesloupec2)
            konec = max(pozicesloupec1,pozicesloupec2)
            if pozicesloupec2 < 0 or pozicesloupec2 > pocetsloupcu:
                valid = False
            else:
                for j in range (zacatek,konec):
                    valid = overlod(poziceradek1,j,hraciplan)
                    if valid == False:
                        break
            if valid == True:
                for j in range (zacatek,konec):
                    hraciplan[poziceradek1][j] = 1
                pozicelode = [poziceradek1,poziceradek1+1,zacatek,konec]
                pozicelodi.append(pozicelode)
                pointer += 1
    return hraciplan


def overlod(radek,sloupec,hraciplan):#overi zda se lod muze umistit na dane misto
    validace = True
    for i in range(radek-1,radek+2):
        for j in range(sloupec-1,sloupec+2):
            if i>-1 and j>-1 and i<pocetradku and j<pocetsloupcu:
                if hraciplan[i][j]!=0:
                    validace = False
                    return validace       
    return validace


def vystrel(radek, sloupec, herniplan, pohledhrace, hrac):   
    if radek<0 or radek>=pocetradku or sloupec<0 or sloupec>=pocetsloupcu:
        text12 = font.render("Špatně zadané pole, jelikož neleží ne plánku.", True, barvatext)
        okno.blit(text12,(mezerabok-50,sourpolihrac[pocetradku-1][0][0]+200))
        pygame.display.update((0,sourpolipocitac[0][pocetradku-1][1]+velikostpole+10,2000,mezeravrsek+velikostpole*pocetradku))
        return pohledhrace,0
    if pohledhrace[radek][sloupec] != 0:
        text12 = font.render("Špatně zadané pole, sem už jsi střílel", True, barvatext)
        okno.blit(text12,(mezerabok-50,sourpolihrac[pocetradku-1][0][0]+200))
        pygame.display.update((0,sourpolipocitac[0][pocetradku-1][1]+velikostpole+10,2000,mezeravrsek+velikostpole*pocetradku))
        return pohledhrace,0
    else:
        if herniplan[radek][sloupec] == 0:
            if hrac == 1:
                text14 = font.render("Vedle!", True, barvatext)
                vysechr = text14.get_rect()
                vysechr.center = ((sourpolipocitac[pocetsloupcu-1][0][0]+sourpolipocitac[0][0][0])//2,sourpolipocitac[0][pocetradku-1][1]+150)
                okno.blit(text14,vysechr) 
            else:
                text15 = font.render("Nepřítel minul!", True, barvatext)
                vysecpoc = text15.get_rect()
                vysecpoc.center = ((sourpolihrac[pocetsloupcu-1][0][0]+mezerabok)//2,sourpolihrac[0][pocetradku-1][1]+150)
                okno.blit(text15,vysecpoc) 
            pohledhrace[radek][sloupec] = 'x'           
        else:
            if hrac == 1:
                text14 = font.render("Zásah!", True, barvatext)
                vysechr = text14.get_rect()
                vysechr.center = ((sourpolipocitac[pocetsloupcu-1][0][0]+sourpolipocitac[0][0][0])//2,sourpolipocitac[0][pocetradku-1][1]+150)
                okno.blit(text14,vysechr)
            else:
                text15 = font.render("Nepřítel zasáhl vaši loď!", True, barvatext)
                vysecpoc = text15.get_rect()
                vysecpoc.center = ((sourpolihrac[pocetsloupcu-1][0][0]+mezerabok)//2,sourpolihrac[0][pocetradku-1][1]+150)
                okno.blit(text15,vysecpoc)                 
            pohledhrace[radek][sloupec] = 'z' 
            pohledhrace = potopena(pohledhrace,hrac)
            if hrac == 0:
                global pocetpolilodihrac
                pocetpolilodihrac -=  1
            else:
                global pocetpolilodipocitac
                pocetpolilodipocitac -= 1      
        pygame.display.update((0,sourpolipocitac[0][pocetradku-1][1]+velikostpole+10,2000,mezeravrsek+velikostpole*pocetradku))
        return pohledhrace,1


def potopena(pohledhrace,hrac):#overuje zda nejaka lod neni potopena
    global pocetlodi 
    for lod in pozicelodi:
        r1,r2,s1,s2 = lod[0],lod[1],lod[2],lod[3]
        jepotopena = True
        for radek in range(r1,r2):
            for sloupec in range(s1,s2):
                if pohledhrace[radek][sloupec] != 'z':
                    jepotopena = False
        if jepotopena == True:
            for radek in range(r1,r2):
                for sloupec in range(s1,s2):
                    pohledhrace[radek][sloupec] = 'p'
            if hrac == 0:
                text16 = font.render("Nepřítel potopil vaši loď!", True, barvatext)
                vysech = text16.get_rect()
                vysech.center = ((sourpolihrac[pocetsloupcu-1][0][0]+mezerabok)//2,sourpolihrac[0][pocetradku-1][1]+185)
                vys = sourpolihrac[r2-1][s2-1][0]+50-sourpolihrac[r1][s1][0]
                sir = sourpolihrac[r2-1][s2-1][1]+50-sourpolihrac[r1][s1][1]
                pygame.draw.rect(okno,(0,185,255),(sourpolihrac[s1][r1][0],sourpolihrac[s1][r1][1],sir,vys))            
                pygame.draw.ellipse(okno,(255,35,35),(sourpolihrac[s1][r1][0]+5,sourpolihrac[s1][r1][1]+5,sir-10,vys-10))
                okno.blit(text16,vysech)
            if hrac == 1:
                text17 = font.render("Potopili jste nepřátelskou loď", True, barvatext)
                vysecp = text17.get_rect()
                vysecp.center = ((sourpolipocitac[pocetsloupcu-1][0][0]+sourpolipocitac[0][0][0])//2,sourpolipocitac[0][pocetradku-1][1]+185)
                vys = sourpolipocitac[r2-1][s2-1][0]+50-sourpolipocitac[r1][s1][0]
                sir = sourpolipocitac[r2-1][s2-1][1]+50-sourpolipocitac[r1][s1][1]
                pygame.draw.rect(okno,(0,185,255),(sourpolipocitac[s1][r1][0],sourpolipocitac[s1][r1][1],sir,vys))            
                pygame.draw.ellipse(okno,(255,35,35),(sourpolipocitac[s1][r1][0]+5,sourpolipocitac[s1][r1][1]+5,sir-10,vys-10))
                okno.blit(text17,vysecp)               
            pozicelodi.remove(lod)
    return pohledhrace


def nactilodehrace(hrachraciplan,poz1,poz2):
    global pozicelodi
    for i in range(poz1[0],poz2[0]):
        for j in range(poz1[1],poz2[1]):
            hrachraciplan[i][j] = 1
    pozicelodi.append([poz1[0],poz2[0],poz1[1],poz2[1]])
    return hrachraciplan


def vyhodnotsituaci(pohlpoc, poslednivystrel):#vysledek bude souradnice[radek,slouopec]
    global hodnocenipoli
    rvystrelu = poslednivystrel[0]
    svystrelu = poslednivystrel[1]
    okolnipole = []
    #zjistit jestli okolnich 9 poli ve slovniku
    for i in range(rvystrelu-1,rvystrelu+2):
        for j in range(svystrelu-1,svystrelu+2):
            if [i,j] in hodnocenipoli[0]:
                okolnipole.append(0)
            elif [i,j] in hodnocenipoli[1]:
                okolnipole.append(1)
            else:
                okolnipole.append(None)

    if pohlpoc[rvystrelu][svystrelu] == 'x':
        hodnocenipoli[okolnipole[4]].remove([rvystrelu,svystrelu])
        if hodnocenipoli[1] == []:
            return random.choice(hodnocenipoli[0])

    elif pohlpoc[rvystrelu][svystrelu] == 'z' or pohlpoc[rvystrelu][svystrelu] == 'p':
        if okolnipole[0] != None:
            hodnocenipoli[okolnipole[0]].remove([rvystrelu-1,svystrelu-1])   
        if okolnipole[2] != None:
            hodnocenipoli[okolnipole[2]].remove([rvystrelu-1,svystrelu+1])
        if okolnipole[6] != None:
            hodnocenipoli[okolnipole[6]].remove([rvystrelu+1,svystrelu-1])
        if okolnipole[8] != None:
            hodnocenipoli[okolnipole[8]].remove([rvystrelu+1,svystrelu+1])
        #v polickach šikmo od zasazeneho lod byt nemuze

        if pohlpoc[rvystrelu][svystrelu] == 'p':
            hodnocenipoli[1] = []
            return random.choice(hodnocenipoli[0])
        
        if pohlpoc[rvystrelu][svystrelu] == 'z':
            if okolnipole[1] != None and rvystrelu-1 in range(0,pocetradku) and svystrelu in range(0,pocetsloupcu):
                hodnocenipoli[okolnipole[1]].remove([rvystrelu-1,svystrelu])   
                hodnocenipoli[1].append([rvystrelu-1,svystrelu])
            if okolnipole[3] != None and rvystrelu in range(0,pocetradku) and svystrelu-1 in range(0,pocetsloupcu):
                hodnocenipoli[okolnipole[3]].remove([rvystrelu,svystrelu-1])   
                hodnocenipoli[1].append([rvystrelu,svystrelu-1])
            if okolnipole[5] != None and rvystrelu in range(0,pocetradku) and svystrelu+1 in range(0,pocetsloupcu):
                hodnocenipoli[okolnipole[5]].remove([rvystrelu,svystrelu+1])
                hodnocenipoli[1].append([rvystrelu,svystrelu+1])
            if okolnipole[7] != None and rvystrelu+1 in range(0,pocetradku) and svystrelu in range(0,pocetsloupcu):
                hodnocenipoli[okolnipole[7]].remove([rvystrelu+1,svystrelu])
                hodnocenipoli[1].append([rvystrelu+1,svystrelu])
        hodnocenipoli[okolnipole[4]].remove([rvystrelu,svystrelu])        
    return random.choice(hodnocenipoli[1])


def souradnicepoli(pocatecnipozice):
    xsouradnice = pocatecnipozice[0]
    ysouradnice = pocatecnipozice[1]
    souradnicepole = []
    for i in range(pocetradku):
        radek = []
        for j in range(pocetsloupcu):
            radek.append((xsouradnice,ysouradnice))
            ysouradnice += velikostpole
        souradnicepole.append(radek)
        ysouradnice = pocatecnipozice[1]
        xsouradnice += velikostpole
    return souradnicepole


def vykreslovanipole(window,polehr, polepoc):
    plan = [polehr,polepoc]
    for hracipole in plan:
        for i in hracipole:
            for j in i:
                pygame.draw.rect(window,(0,0,0),(j[0],j[1],velikostpole,velikostpole),1)
    for c in range (1,11):
        cislo = 0+c
        slp = font.render(str(cislo), True, barvatext)
        okno.blit(slp,(mezerabok+15+(c-1)*50,mezeravrsek-40))
        okno.blit(slp,(velikostpole*pocetsloupcu+mezeramezi+15+(c-1)*50,mezeravrsek-40))        
    for poz in range(pocetradku):
        pis = font.render(chr(65+poz),True,barvatext)
        okno.blit(pis,(mezerabok-40,mezeravrsek+15+poz*50))
        okno.blit(pis,(velikostpole*pocetsloupcu+mezeramezi-40,mezeravrsek+15+poz*50))
    hrac0 = font.render('Pole nepřítele', True, barvatext)
    hrac1 = font.render('Vaše pole', True, barvatext)
    vys0 = hrac0.get_rect()
    vys0.center = (velikostpole*pocetsloupcu+mezeramezi+(velikostpole*pocetsloupcu)//2,mezeravrsek-80)
    vys1 = hrac1.get_rect()
    vys1.center = (mezerabok+(velikostpole*pocetsloupcu)//2,mezeravrsek-80)
    okno.blit(hrac0,vys0)   
    okno.blit(hrac1,vys1)



#main
polepocitac = vytvorpole()
polepocitac = nactilode(polepocitac)
pohledpocitace = vytvorpole()
sourpolipocitac = souradnicepoli((velikostpole*pocetsloupcu + mezeramezi, mezeravrsek))
polehrac = vytvorpole()
pohledhrace = vytvorpole()
sourpolihrac = souradnicepoli((mezerabok,mezeravrsek))

for i in range(pocetradku):
    for j in range(pocetsloupcu):
        hodnocenipoli[0].append([i,j])
nejlepsitah = [random.randrange(0,pocetradku),random.randrange(0,pocetsloupcu)]

okno.fill(barvapozadi)
text14 = font.render('Vítejte ve hře bitevní lodě.',True, barvatext)
text15 = font.render('Po zobrazení bitevního plánu nejprve položte své lodě zadáním písmena řádku a čísla sloupce.',True, barvatext)
text16 = font.render('V momentě, kdy budete mít všechny lodě umístěny na herním plánu, můžete začít střílet na nepřítele.',True, barvatext)
vysec2 = text14.get_rect()
vysec2.center = (sirka//2,300)
okno.blit(text14,vysec2)
okno.blit(text15,(100,460))
okno.blit(text16,(100,500))
pygame.display.flip()
pygame.time.wait(8000)

okno.fill(barvapozadi)
pygame.draw.rect(okno,(0,185,255),(mezerabok,mezeravrsek,velikostpole*pocetsloupcu,velikostpole*pocetradku))
pygame.draw.rect(okno,(0,185,255),(sourpolipocitac[0][0][0],sourpolipocitac[0][0][1],velikostpole*pocetsloupcu,velikostpole*pocetradku))
vykreslovanipole(okno,sourpolihrac,sourpolipocitac)
text1 = font.render('Bitevní lodě', True, barvatext)
vysec1 = text1.get_rect()
vysec1.center = (sirka//2,20)
okno.blit(text1,vysec1)

prubehhry = True
lodipolozeno = 0
klavesa = ''
nactilod = []
pygame.display.flip()
while prubehhry:
    clock.tick(60)
    while lodipolozeno != pocetlodi:
        if len(nactilod)==0:
            pygame.draw.rect(okno,barvapozadi,(sourpolipocitac[pocetsloupcu-1][0][0]+velikostpole+10,mezeravrsek,1000,velikostpole*pocetradku))           
            text2 = font.render("Zadejte dvě pole vzdálená od sebe", True, barvatext)
            veta1 = font.render(str(delkylodi[lodipolozeno]), True, barvatext)
            if delkylodi[lodipolozeno] > 4:
                veta2 = font.render("políček ve tvaru pismenocislo, enter.", True, barvatext)
            elif delkylodi[lodipolozeno] > 1:
                veta2 = font.render("políčka ve tvaru pismenocislo, enter.", True, barvatext) 
            else:
                veta2 = font.render("políčko ve tvaru pismenocislo, enter.", True, barvatext)               
            okno.blit(text2,(sourpolipocitac[pocetsloupcu-1][0][0]+velikostpole+40,mezeravrsek+20))
            okno.blit(veta1,(sourpolipocitac[pocetsloupcu-1][0][0]+velikostpole+40,mezeravrsek+55))
            okno.blit(veta2,(sourpolipocitac[pocetsloupcu-1][0][0]+velikostpole+76,mezeravrsek+55))
            text4 = font.render("Počáteční pole:",True,barvatext)
            text5 = font.render(klavesa,True,barvatext)
            okno.blit(text4,(sourpolipocitac[pocetsloupcu-1][0][0]+velikostpole+40,mezeravrsek+140))
            okno.blit(text5,(sourpolipocitac[pocetsloupcu-1][0][0]+velikostpole+300,mezeravrsek+140))            
            pygame.display.update((sourpolipocitac[pocetsloupcu-1][0][0]+velikostpole+10,mezeravrsek,1000,velikostpole*pocetradku))
        if len(nactilod)==1:
            pygame.draw.rect(okno,barvapozadi,(sourpolipocitac[pocetsloupcu-1][0][0]+velikostpole+40,mezeravrsek+220,1000,50))
            text6 = font.render("Koncové pole:",True,barvatext)
            text7 = font.render(klavesa,True,barvatext)
            okno.blit(text6,(sourpolipocitac[pocetsloupcu-1][0][0]+velikostpole+40,mezeravrsek+220))
            okno.blit(text7,(sourpolipocitac[pocetsloupcu-1][0][0]+velikostpole+300,mezeravrsek+220))
            pygame.display.update((sourpolipocitac[pocetsloupcu-1][0][0]+velikostpole+40,mezeravrsek+220,1000,50))            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                prubehhry = False
                break            
            if event.type == pygame.KEYDOWN:
                pygame.draw.rect(okno,barvapozadi,(0,sourpolipocitac[0][pocetradku-1][1]+velikostpole+10,2000,mezeravrsek+velikostpole*pocetradku)) 
                if event.unicode.isalpha() == True or event.unicode.isnumeric() == True:
                    klavesa += event.unicode
                    pygame.display.update((0,sourpolipocitac[0][pocetradku-1][1]+velikostpole+10,2000,mezeravrsek+velikostpole*pocetradku))
                elif event.key == pygame.K_BACKSPACE:
                    klavesa = klavesa[:-1]
                elif event.key == pygame.K_RETURN:
                    nactilod.append(klavesa)
                    klavesa = ''
        if len(nactilod)==2:
            try:
                nactilod1 = nactilod[0]
                radeklodi1 = nactilod1[0].lower()
                radeklodi1 = ord(radeklodi1)-97
                sloupeclodi1 = int(nactilod1[1:])-1
                nactilod2 = nactilod[1]
                radeklodi2 = nactilod2[0].lower()
                radeklodi2 = ord(radeklodi2)-97
                sloupeclodi2 = int(nactilod2[1:])-1
                souradnice1 = [min(radeklodi1,radeklodi2),min(sloupeclodi1,sloupeclodi2)]
                souradnice2 = [max(radeklodi1,radeklodi2)+1,max(sloupeclodi1,sloupeclodi2)+1]  
                if radeklodi1 != radeklodi2 and sloupeclodi1 != sloupeclodi2:
                    text3 = font.render("Špatně zadané pole, lod musí být vodorovně nebo svisle.", True, barvatext)
                    okno.blit(text3,(mezerabok-50,sourpolihrac[pocetradku-1][0][0]+200))
                    pygame.display.update((0,sourpolipocitac[0][pocetradku-1][1]+velikostpole+10,2000,mezeravrsek+velikostpole*pocetradku))
                    nactilod = []
                    continue
                if souradnice1[0] != souradnice2[0]-delkylodi[lodipolozeno] and souradnice1[1]!=souradnice2[1]-delkylodi[lodipolozeno]:
                    text3 = font.render("Špatně zadané pole, zadejte lod s odpovidajici delkou.", True, barvatext)
                    okno.blit(text3,(mezerabok-50,sourpolihrac[pocetradku-1][0][0]+200))
                    pygame.display.update((0,sourpolipocitac[0][pocetradku-1][1]+velikostpole+10,2000,mezeravrsek+velikostpole*pocetradku))
                    nactilod = []
                    continue
                if souradnice1[0] not in range(0,pocetradku+1) or souradnice2[0] not in range(0,pocetradku+1) or souradnice1[1] not in range(0,pocetsloupcu+1) or souradnice2[1] not in range(0,pocetsloupcu+1):
                    text3 = font.render("Špatně zadané pole, loď musí ležet na hracím plánu.", True, barvatext)               
                    okno.blit(text3,(mezerabok-50,sourpolihrac[pocetradku-1][0][0]+200))
                    pygame.display.update((0,sourpolipocitac[0][pocetradku-1][1]+velikostpole+10,2000,mezeravrsek+velikostpole*pocetradku))
                    nactilod = []                
                    continue
                for i in range(souradnice1[0],souradnice2[0]):
                    for j in range(souradnice1[1],souradnice2[1]):
                        valid = overlod(i,j,polehrac)
                        if valid == False:
                            break
                    if valid == False:
                        break
                if valid == False:
                    text3 = font.render("Špatně zadané pole, existující loď v přímé blízkosti.", True, barvatext)
                    okno.blit(text3,(mezerabok-50,sourpolihrac[pocetradku-1][0][0]+200))
                    pygame.display.update((0,sourpolipocitac[0][pocetradku-1][1]+velikostpole+10,2000,mezeravrsek+velikostpole*pocetradku))
                    nactilod = []
                    continue
            except:
                text3 = font.render("Špatně zadané pole, zadejte vstup ve tvaru pismenocislo pismenocislo.", True, barvatext)
                okno.blit(text3,(mezerabok-50,sourpolihrac[pocetradku-1][0][0]+200))
                nactilod = []
                pygame.display.update((0,sourpolipocitac[0][pocetradku-1][1]+velikostpole+10,2000,mezeravrsek+velikostpole*pocetradku))
            else: 
                polehrac = nactilodehrace(polehrac,souradnice1,souradnice2)
                vyskalode = sourpolihrac[souradnice2[0]-1][souradnice2[1]-1][0]+50-sourpolihrac[souradnice1[0]][souradnice1[1]][0]
                sirkalode = sourpolihrac[souradnice2[0]-1][souradnice2[1]-1][1]+50-sourpolihrac[souradnice1[0]][souradnice1[1]][1]
                pygame.draw.ellipse(okno,(35,35,35),(sourpolihrac[souradnice1[1]][souradnice1[0]][0]+5,sourpolihrac[souradnice1[1]][souradnice1[0]][1]+5,sirkalode-10,vyskalode-10))
                lodipolozeno +=1
            nactilod = []
            pygame.display.update()
        if prubehhry == False:
            break

    zkus = False
    if prubehhry == False:
        break
    klavesa = ''
    while True:
        poztext = pygame.Rect(sourpolipocitac[pocetsloupcu-1][0][0]+velikostpole+10,mezeravrsek,sirka-sourpolipocitac[pocetsloupcu-1][0][0]+55,velikostpole*pocetradku)
        pygame.draw.rect(okno,barvapozadi,poztext)
        text8 = font.render("Střílej zadáním požadovaného pole ve tva-", True, barvatext)
        text12 = font.render("ru písmenočíslo.", True, barvatext)
        text13 = font.render("Úspěšnost střelby se zobrazí na mapě.", True, barvatext)
        okno.blit(text8,(poztext.x+30,poztext.y+20))
        okno.blit(text12,(poztext.x+30,poztext.y+55))
        okno.blit(text13,(poztext.x+30,poztext.y+90))
        text10 = font.render("Výstřel na pole:",True,barvatext)
        text11 = font.render(klavesa,True,barvatext)
        okno.blit(text10,(sourpolipocitac[pocetsloupcu-1][0][0]+velikostpole+40,mezeravrsek+200))
        okno.blit(text11,(sourpolipocitac[pocetsloupcu-1][0][0]+velikostpole+300,mezeravrsek+200))
        pygame.display.update(poztext)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                prubehhry = False
                break 
            if event.type == pygame.KEYDOWN: 
                pygame.draw.rect(okno,barvapozadi,(0,sourpolipocitac[0][pocetradku-1][1]+velikostpole+10,2000,mezeravrsek+velikostpole*pocetradku))
                if event.unicode.isalpha() == True or event.unicode.isnumeric() == True:
                    klavesa += event.unicode
                    pygame.display.update((0,sourpolipocitac[0][pocetradku-1][1]+velikostpole+10,2000,mezeravrsek+velikostpole*pocetradku))
                elif event.key == pygame.K_BACKSPACE:
                    klavesa = klavesa[:-1]
                elif event.key == pygame.K_RETURN:
                    nactivstup = klavesa
                    klavesa = ''
                    zkus = True  
        if event.type == pygame.QUIT:
            prubehhry = False
            break 
        if zkus == True: 
            zkus = False  
            try:
                nactiradek = nactivstup[0].lower()
                nactiradek = ord(nactiradek)-97
                nactisloupec = int(nactivstup[1:])-1
            except:
                text9 = font.render("Špatně zadané pole, zadejte vstup ve tvaru pismenocislo.", True, barvatext)
                okno.blit(text9,(mezerabok-50,sourpolihrac[pocetradku-1][0][0]+200))
                pygame.display.update((0,sourpolipocitac[0][pocetradku-1][1]+velikostpole+10,2000,mezeravrsek+velikostpole*pocetradku))
            else:

                #tah hrace
                strelba = vystrel(nactiradek,nactisloupec,polepocitac,pohledhrace,1)
                if strelba[1] == 0:
                    continue
                pohledhrace = strelba[0]
                if pohledhrace[nactiradek][nactisloupec] == 'z':
                    pygame.draw.ellipse(okno,(255,35,35),(sourpolipocitac[nactisloupec][nactiradek][0]+5,sourpolipocitac[nactisloupec][nactiradek][1]+5,velikostpole-10,velikostpole-10))
                if pohledhrace[nactiradek][nactisloupec] == 'x':
                    pygame.draw.ellipse(okno,(0,0,50),(sourpolipocitac[nactisloupec][nactiradek][0]+5,sourpolipocitac[nactisloupec][nactiradek][1]+5,velikostpole-10,velikostpole-10))                
                if pocetpolilodipocitac == 0:
                    okno.fill((50,255,100))
                    textvyh = font.render("Gratuluji, vyhrál jste!!!", True, barvatext)
                    vyseckon = textvyh.get_rect()
                    vyseckon.center = (sirka//2,vyska//2)
                    okno.blit(textvyh,vyseckon)
                    break


                #tah pocitace
                pohledpocitace = vystrel(nejlepsitah[0],nejlepsitah[1],polehrac,pohledpocitace,0)[0]
                if pohledpocitace[nejlepsitah[0]][nejlepsitah[1]] == 'z':
                    pygame.draw.ellipse(okno,(255,35,35),(sourpolihrac[nejlepsitah[1]][nejlepsitah[0]][0]+5,sourpolihrac[nejlepsitah[1]][nejlepsitah[0]][1]+5,velikostpole-10,velikostpole-10))
                if pohledpocitace[nejlepsitah[0]][nejlepsitah[1]] == 'x':
                    pygame.draw.ellipse(okno,(0,0,50),(sourpolihrac[nejlepsitah[1]][nejlepsitah[0]][0]+5,sourpolihrac[nejlepsitah[1]][nejlepsitah[0]][1]+5,velikostpole-10,velikostpole-10))
                nejlepsitah = vyhodnotsituaci(pohledpocitace,nejlepsitah) 
                if pocetpolilodihrac == 0:
                    okno.fill((150,10,10))
                    textproh = font.render("Smůla, váš nepřítel vás porazil. Možná příště.", True, barvatext)
                    vyseckon = textproh.get_rect()
                    vyseckon.center = (sirka//2,vyska//2)
                    okno.blit(textproh,vyseckon)
                    break
                pygame.display.update()
    if pocetpolilodipocitac == 0 or pocetpolilodihrac == 0:
        pygame.display.update()
        pygame.time.wait(5000)
        break
pygame.quit() 