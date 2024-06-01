## ENGETO-Python-3-projekt
Třetí projekt na Python Akademii od Engeta.

## Popis projektu
Tento projekt slouží k extrahování výsledků z parlamentních voleb v roce 2017. Odkaz k prohlédnutí najdete [zde](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).

## Instalace knihoven
Knihovny, které jsou použity v kódu jsou uložené v souboru requirements.txt.
Pro instalaci doporučuji použít nové virtuálníprostředí s nainstalovaným manažerem spustit následovně:

    $ pip3 --version			# ověřím verzi manažeru
    $ pip install -r requirements.txt	# nainstaluje knihovny

## Spuštění projektu
Spuštění souboru `Election_scraper_Vašková.py` v rámci příkazového řádku požaduje dva povinné argumenty.

    python Election_scraper_Vašková <odkaz-uzemniho-celku>, <vysledny-soubor>
Následně se vám stáhnou výsledky jako soubor s příponou `.csv`.

### Ukázka projektu
Výsledky hlasování pro okres Ústí nad Labem:
1. argument: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=6&xnumnuts=4207
2. argument: Vysledky_UnL.csv

### Spuštění programu:
    python Election_scraper_Vašková.py 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=6&xnumnuts=4207' 'vysledky_UnL'

### Průběh stahování:
    Proces stahuje data, prosím vyčkejte.
    Proces je nyní hotový!
    Váš soubor Vysledky_UnL.csv je připraven.

### Částečný výstup:
    Kód obce;Název obce;Voliči v seznamu;Vydané obálky;Platné hlasy;Občanská demokratická strana;Řád národa - Vlastenecká unie;CESTA ODPOVĚDNÉ SPOLEČNOSTI;Česká str.sociálně demokrat.;STAROSTOVÉ A NEZÁVISLÍ;Komunistická str.Čech a Moravy;Strana zelených;ROZUMNÍ-stop migraci,diktát.EU;Strana svobodných občanů;Blok proti islam.-Obran.domova;Občanská demokratická aliance;Česká pirátská strana;Referendum o Evropské unii;TOP 09;ANO 2011;Dobrá volba 2016;SPR-Republ.str.Čsl. M.Sládka;Křesť.demokr.unie-Čs.str.lid.;Česká strana národně sociální;REALISTÉ;SPORTOVCI;Dělnic.str.sociální spravedl.;Svob.a př.dem.-T.Okamura (SPD);Strana Práv Občanů
    567931;Dolní Zálezly;462;316;314;39;0;0;14;21;35;4;1;2;0;3;28;0;14;102;0;0;6;0;2;1;1;36;5
    567957;Habrovany;182;101;100;5;0;0;4;2;19;0;0;3;2;0;1;0;2;42;0;1;2;0;1;1;1;14;0
    ...