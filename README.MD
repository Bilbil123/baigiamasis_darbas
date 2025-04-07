# Elenta.lt Skelbimų Scraperis

## Aprašymas
Ši programa yra grafinė sąsaja (GUI), skirta rinkti automobilių aparatūros skelbimų duomenis iš elenta.lt tinklapio. Programa leidžia vartotojui įvesti bazinį URL (https://elenta.lt), automatiškai suformuoja pilną URL kategorijai "auto-moto/auto-aparatura", ištraukia skelbimų pavadinimus bei kainas ir išsaugo juos CSV faile. Taip pat pateikia bendrą statistiką apie apdorotus skelbimus ir jų bendrą vertę.

## Funkcijos
- Patikrina, ar įvestas URL yra tinkamas (privalo būti https://elenta.lt domenas).
- Ištraukia skelbimų pavadinimus ir kainas iš nurodytos kategorijos.
- Išsaugo surinktus duomenis CSV faile su unikaliu pavadinimu pagal datą ir laiką.
- Rodo realaus laiko informaciją apie scrapinimo procesą ir rezultatus.
- Apskaičiuoja bendrą skelbimų kainų sumą (jei kainos nurodytos).

## Reikalavimai
- Python 3.x
- PyQt6 biblioteka (`pip install PyQt6`)
- Requests biblioteka (`pip install requests`)
- BeautifulSoup4 biblioteka (`pip install beautifulsoup4`)

## Naudojimas
1. Įdiekite reikalingas bibliotekas, kaip nurodyta aukščiau.
2. Paleiskite programą vykdydami `python main.py`.
3. Atsidariusiame lange įveskite bazinį URL (pvz., https://elenta.lt) į tam skirtą laukelį.
4. Spustelėkite mygtuką, kad pradėtumėte scrapinimo procesą.
5. Programa parodys surinktus duomenis lange ir išsaugos juos CSV faile.

## Pastabos
- Programa tikrina, ar URL atitinka reikalavimus (https:// ir elenta.lt domenas). Jei URL netinkamas, bus rodoma klaida.
- CSV failas sugeneruojamas dabartiniame darbiniame kataloge ir pavadinamas pagal formatą `elenta_scrape_YYYYMMDD_HHMMSS.csv`.
- Jei skelbime kaina nenurodyta arba neatpažįstama, tai bus pažymėta ir programa tęs darbą.

## Atsakomybė
Ši programa skirta tik mokymosi ar asmeninio naudojimo tikslams. Naudotojas yra atsakingas už tai, kad scrapinimas atitiktų elenta.lt svetainės naudojimo taisykles ir galiojančius įstatymus.

## Autorius
Sukurta naudojant PyQt6, requests ir BeautifulSoup4 bibliotekas.