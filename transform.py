import geopandas

## Read-In
path_to_data = r".\data\vg5000_01-01.gk3.shape.ebenen\vg5000_01-01.gk3.shape.ebenen\vg5000_ebenen_0101\VG5000_LAN.shp"
gdf = geopandas.read_file(path_to_data)
## Explore
#gdf.plot()
#gdf.columns
#gdf.loc[0,:]

## Describe
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

## Spit-out
cols = ["ARS", "GEN", "BEZ", "BEM", "geometry"]
gdf[cols].to_file("./data/land_level.geojson", driver="GeoJSON")
