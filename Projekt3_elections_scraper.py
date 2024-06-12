import sys
import csv
import requests
from bs4 import BeautifulSoup

SEPARATOR = "=" * 50
URL = "https://volby.cz/pls/ps2017nss/"


def main(adresa, oznaceni_souboru):
    """
        Kontroluje počet vložených argumentů a spouští hlavní proces stahování a zpracování dat.
    """
    print("Proces stahuje data, prosím vyčkejte.")

    with open(oznaceni_souboru + ".csv", mode="w", newline='') as f:
        f_writer = csv.writer(f, delimiter=";")

        hlavicka = False
        scrap = requests.get(adresa)
        tool = BeautifulSoup(scrap.text, "html.parser")
        regiony = tool.find_all("td", {"class": "cislo"})

        for radek in regiony:
            region_data = []
            region_data = ziskej_id_jmeno(radek, region_data)
            region_soup = ziskej_soup(URL, radek)

            vysledky_regionu = region_soup.find(id="ps311_t1")
            region_data = ziskej_volice(vysledky_regionu, region_data)

            strany = region_soup.find(id="inner").find_all("tr")

            region_data = ziskej_hlasy_stran(strany, region_data)

            if not hlavicka:
                nazvy_sloupcu = ["Kód obce", "Název obce", "Voliči v seznamu", "Vydané obálky", "Platné hlasy"]
                for novy_radek in strany:
                    if not novy_radek.find("th"):
                        nazvy_sloupcu.append(novy_radek.find_all("td")[1].string)
                f_writer.writerow(nazvy_sloupcu)
                hlavicka = True

            f_writer.writerow(region_data)

    print("Proces je nyní hotový!")
    print(f"Váš soubor {oznaceni_souboru}.csv je připraven.")


def ziskej_id_jmeno(radek, seznam):
    """
        Získává kód obce a přidává do seznamu hodnotu z HTML struktury.
    """
    seznam.append(radek.find("a").string)
    seznam.append(radek.parent.find_all()[2].string)
    return seznam


def ziskej_soup(url, radek):
    """
        Vytvoří ze získaného odkazu objekt BeautifulSoup.
    """
    region_url = requests.get(url + radek.find("a").attrs["href"])
    return BeautifulSoup(region_url.text, "html.parser")


def ziskej_volice(vysledky_regionu, seznam):
    """
        Získává specifické údaje z HTML souboru - sa2-seznam voličů, sa3-vydané obálky, sa6-platné hlasy.
    """
    seznam.append(vysledky_regionu.find("td", {"class": "cislo", "headers": "sa2"}).string)
    seznam.append(vysledky_regionu.find("td", {"class": "cislo", "headers": "sa3"}).string)
    seznam.append(vysledky_regionu.find("td", {"class": "cislo", "headers": "sa6"}).string)
    return seznam


def ziskej_hlasy_stran(strany, seznam):
    """
        Získává a přidává do seznamu volební strany a počet hlasů, které získaly.
    """
    for radek in strany:
        if not radek.find("th"):
            hlas = radek.find_all("td", {"class": "cislo"})
            if len(hlas) > 1:
                seznam.append(hlas[1].string.strip())

    return seznam


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Použití: python script.py <odkaz> <nazev_souboru>")
        sys.exit(1)
    odkaz = sys.argv[1]
    nazev_souboru = sys.argv[2]
    if not odkaz.startswith("https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=") or "&xnumnuts=" not in odkaz:
        print("Zadali jste nesprávnou URL. Prosím zkuste to znovu.")
        sys.exit(1)
    if ".csv" in nazev_souboru:
        print("Prosím pojmenujte soubor bez přípony.")
        sys.exit(1)
    if nazev_souboru.startswith("https://volby.cz/"):
        print("Argumenty jsou ve špatném pořadí. Použití: python script.py <odkaz> <nazev_souboru>")
        sys.exit(1)
    sys.exit(main(odkaz, nazev_souboru))
