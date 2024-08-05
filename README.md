# Zápočtový program

## Zadání:
<p align="justify">
 Hra lodě/námořní bitva 
</p>

## Návod jak hrát:
<p align="justify">
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
