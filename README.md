# Zápočtový program
## Zadání:
<p align="justify">
 Hra lodě/námořní bitva 
</p>

## Návod jak hrát:
<p align="justify">
	Pro spuštění programu si po naistalování pythonu nejprve musíte nainstalovat také rozšíření pygame následujícím způsobem. 
	    </p>
    <p align="justify">
	Pokud jste uživatelem windows, otevřete příkazový řádek (klikněte pravým tlačítkem myši na ikonu start, vyberte možnost spustit a do ní zadejte cmd) a napište do něj příkaz: pip install pygame. Pokud se vám rozšíření nestáhlo, zkuste se podívat na  </p> [GitHub Pages](https://www.youtube.com/watch?v=AdUZArA-kZw&t=0s/). 
	        
    <p align="justify">
	Pokud jste uživatelem linux, otevřete svůj terminál do kterého napíšete: sudo apt-get install python-pygame nebo sudo apt-get install python3-pygame. 
	        </p>
    <p align="justify">
	Pokud jste uživatelem Mac OS, otevřete svůj terminál do kterého napíšete: curl https://bootstrap.pypa.io/get-pip.py > get-pip.py Poté zmáčkněte enter a napište: sudo pip install pygame zde budete muset zadat své heslo.
	        </p>
    <p align="justify">
	Pokud již máte naistalované rozšíření pygame, stačí stáhnout program, otevřít ho v nějakém editoru a spustit.
	Po spuštění programu nejprve rozmístíte své lodě na plánek tím, že zadáte počáteční pole
lodě (ve tvaru písmeno řádku a číslo sloupce dohromady bez mezery, např: a1/A1 ), které potvrdíte
klávesou enter. Následně stejným způsobem zadáte koncové pole lodě. Loď nesmí sousedit
s jinou lodí žádným políčkem (ani rohovým). 
    </p>
    <p align="justify">
	Poté začíná fáze střílení jejíž výsledek se po každém tahu vypíše pod mapami (Váš výsledek pod mapou počítače a obráceně) a zároveň zobrazí na mapě. Vyhrává ten, komu se jako prvnímu podaří zničit všechny nepřátelské lodě.
    </p>
    
## Technický popis:
### Funkce:
- Vytvorpole – vytvoří prázdné hrací pole 
- Nactilode – vygeneruje pozice lodí počítače
- Overlod – ověřuje zda lze na danou pozici položit loď
- Vystrel – ověřuje zda je výstřel na dané pole zásah nebo ne
- Potopena – při zásahu lodi ověřuje zda je loď potopena či nikoliv
- Nactilodehrace – umisťuje lodě na hráčem zadané pozice
- Vyhodnotsituaci – zadává pole výstřelu počítače
- Souradnicepoli – generuje souradnice jednotlivých políček v okně pygame
- Vykreslovanipole – vykresluje hrací plán na okno pygame
### Main:
Vytváření polí a okna pygame  
Cyklus pro správný chod pygame tvořený dvěma podcykly  
První cyklus – načtení a vykreslení lodí hráče  
Druhý cyklus výstřely a vykreslení jejich výsledků  
