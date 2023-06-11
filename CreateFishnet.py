import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace=r"E:\Cursos\Arcpy\LPA\Projects\GeomProject\GeomProject.gdb"
srWGS84=arcpy.SpatialReference("WGS 1984")
arcpy.management.CreateFishnet("Fishnetlines", # Se eu nao tivesse estabelecido o workspace teria de colocar r"E:\Cursos\Arcpy\LPA\Projects\GeomProject\GeomProject.gdb\Fishnetlines
                               "0 0", "0 1", 1, 1, 10, 15, None,
                               "LABELS", "DEFAULT", "POLYLINE")

if arcpy.Exists("FishnetPoints"):
    arcpy.management.Delete("FishnetPoints")
arcpy.management.Rename("Fishnetlines_label","FishnetPoints")

arcpy.management.CreateFishnet("FishnetPolys", # Se eu nao tivesse estabelecido o workspace teria de colocar r"E:\Cursos\Arcpy\LPA\Projects\GeomProject\GeomProject.gdb\Fishnetlines
                               "0 0", "0 1", 1, 1, 10, 15, None,
                               "NO_LABELS", "DEFAULT", "POLYGON")

for geomType in ["Polys","Lines","Points"]:
    arcpy.management.DefineProjection("Fishnet{0}".format(geomType),srWGS84)

print("\nScript completed!")
