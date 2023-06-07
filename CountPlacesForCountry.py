import arcpy
# coding: utf-8
arcpy.env.overwriteOutput = True
arcpy.env.workspace =r"E:\Cursos\Arcpy\Arcpy_Udemy\Arcpy_Udemy.gdb"
countryName = arcpy.GetParameterAsText(0)
arcpy.analysis.Select(r"E:\Cursos\Arcpy\LPA\Data\ne_10m_admin_0_countries.shp",
                      r"E:\Cursos\Arcpy\Arcpy_Udemy\Arcpy_Udemy.gdb\SelCountry",
                      "NAME = '{}'".format(countryName))
arcpy.analysis.Buffer("SelCountry", "SelCountry_Buffer", "200 Kilometers", "FULL", "ROUND", "NONE", None, "PLANAR")
arcpy.analysis.Clip(r"E:\Cursos\Arcpy\LPA\Data\ne_10m_populated_places.shp",
                    "SelCountry_Buffer",
                    "Places_Clip",
                    None)
arcpy.AddMessage("there area {0} populated places in or within 200km of {1}".format(arcpy.management.GetCount("Places_Clip"),countryName))
