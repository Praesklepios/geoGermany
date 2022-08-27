import geopandas
from pathlib import Path

PATH_TO_SHAPE = r".\geogermany\bkgdata\vg5000_01-01.gk3.shape.ebenen\vg5000_ebenen_0101"
READFILES = {
            "VG5000_GEM.shp": "Gemeinden",
            "VG5000_KRS.shp": "Kreise",
            "VG5000_LAN.shp": "Länder",
            "VG5000_LI.shp": "Grenzlinien",
            "VG5000_RBZ.shp": "Regierungsbezirke",
            "VG5000_STA.shp": "Staat",
            "VG5000_VWG.shp": "Verwaltungsgemeinschaften"
            }

def etl(readfile, writespec):
    """
    Read in a shape file, transform it to crs4326 and write it as geojson.

    Args:
        readfile (str): filename of a shapefile
        writespec (str): how the exported geojson will be tagged

    Returns:
        str: One of success or fail
    """
    try:
        # extract
        datapath = Path(PATH_TO_SHAPE)
        fileloc = datapath.joinpath(readfile)
        gdf = geopandas.read_file(fileloc)
        ## Values in geojson
        # OBJID = eindeutiger Objektidentifikator
        # BEGINN = Datum, an dem das Objekt in den Datensatz eingefügt oder geändert wurde
        # ADE = Administrative Ebene (z.B. 6 = "Gemeinde")
        # GF = Geofaktor (z.B. 9 = "mit Struktur" falls Ebenen unter dieser existieren)
        # BSG = Besondere Gebiete (1 = "Deutschland" oder 9 = "Bodensee")
        # ARS = Amtlicher Regionalschlüssel (xx-x-xx-xxxx-xxx als Land-RB-Kreis-VWG-Gemeinde)
        # AGS = Amtlicher Gemeindeschlüssel (ARS ohne Verwaltungsgemeinschaft aka. VWG)
        # SDV_ARS = ARS der Gemeinde, der den Sitz der Verwaltung repräsentiert
        # GEN = Geografischer Name
        # BEZ = Bezeichnung der Verwaltungseinheit
        # IBZ = Identifikator für BEZ
        # BEM = Spezifikation für BEZ
        # NBD = Definiert ob BEZ zur vollständigen Namensbildung verwendet wird
        # SN_L, SN_R, SN_V1, SN_V2, SN_G = strukturelle Einzelteile von ARS
        # FK_S3 = Regierungsbezirk oder Kreis
        # NUTS = Europäischer Statistikschlüssel
        # ARS_0, AGS_0 = aufgefüllte Regionalschlüssel
        # WSK = für Änderung juristisch relevantes Datum
        
        # transform
        gdf = gdf.to_crs(4326)

        # load

        cols = ["ARS", "GEN", "BEZ", "BEM", "geometry"]
        gdf[cols].to_file("./geojson/Ebene_{}.geojson".format(writespec), driver="GeoJSON")

        return "success"
    except:
        return "fail"


if __name__ == "__main__":
    for k, v in READFILES.items():
        etl(k, v)
