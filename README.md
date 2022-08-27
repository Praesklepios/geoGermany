geoGermany
==================

## Use the files

You can find the different layers of Germany's administrative districts in the
./geojson folder. Feel free to use them as a basis for Metabase region maps or such.
The files are from 01.01.2021.

## Use the script

The actual script in ./geogermany turns shapefiles, provided by the
"Bundesamt für Kartographie und Geodäsie" (BKG), into geojson while omitting
all columns I deem irrelevant.
The Coordinate Reference System (CRS) of the geojson-files is 4326 (longitude/latitude).
If you want to run the script you need to install the environments.yaml through conda,
download the shapefiles from BKG (see Credits for a link) and drop them in ./geogermany/bkgdata.
Have fun.

## Values in geojson

ARS = Amtlicher Regionalschlüssel (xx-x-xx-xxxx-xxx as Land-RB-Kreis-VWG-Gemeinde)
GEN = Geografischer Name
BEZ = Bezeichnung der Verwaltungseinheit
BEM = Spezifikation für BEZ
geometry = MultiPolygon Coordinates

## Credits

* Data source: [BKG-DATA](https://gdz.bkg.bund.de/index.php/default/open-data/verwaltungsgebiete-1-5-000-000-ebenen-stand-01-01-vg5000-ebenen-01-01.html)
