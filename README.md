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
Spuštění souboru `Projekt3_elections_scraper.py` v rámci příkazového řádku požaduje dva povinné argumenty.

    python Projekt3_elections_scraper <odkaz-uzemniho-celku>, <vysledny-soubor>
Následně se vám stáhnou výsledky jako soubor s příponou `.csv`.

### Ukázka projektu
Výsledky hlasování pro okres Třebíč:
1. argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6104
2. argument: Trebic.csv

### Spuštění programu:
    python Projekt3_elections_scraper.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6104' 'Trebic'

### Průběh stahování:
    Proces stahuje data, prosím vyčkejte.
    Proces je nyní hotový!
    Váš soubor Trebic.csv je připraven.

### Částečný výstup:
    Kód obce;Název obce;Voliči v seznamu;Vydané obálky;Platné hlasy;Občanská demokratická strana;Řád národa - Vlastenecká unie;CESTA ODPOVĚDNÉ SPOLEČNOSTI;Česká str.sociálně demokrat.;STAROSTOVÉ A NEZÁVISLÍ;Komunistická str.Čech a Moravy;Strana zelených;ROZUMNÍ-stop migraci,diktát.EU;Strana svobodných občanů;Blok proti islam.-Obran.domova;Občanská demokratická aliance;Česká pirátská strana;Referendum o Evropské unii;TOP 09;ANO 2011;Dobrá volba 2016;SPR-Republ.str.Čsl. M.Sládka;Křesť.demokr.unie-Čs.str.lid.;Česká strana národně sociální;REALISTÉ;SPORTOVCI;Dělnic.str.sociální spravedl.;Svob.a př.dem.-T.Okamura (SPD);Strana Práv Občanů
    590274;Babice;167;126;126;9;0;0;11;0;8;9;0;0;3;0;0;16;0;1;40;0;19;0;1;0;0;7;2
    590282;Bačice;165;104;104;1;1;0;5;0;6;23;0;1;0;0;0;5;1;2;33;1;7;0;0;0;0;14;4
    ...