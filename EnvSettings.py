import arcpy


arcpy.env.overwriteOutput = True # Faz sobrepor um já existe te
print("workspace:", arcpy.env.workspace) # vendo o atual workspace
arcpy.env.workspace =r"E:\Cursos\Arcpy\LPA\Data\test.gdb" # selecionando o workspace
print("Workspace:",arcpy.env.workspace) # verificando se foi selecionado

##if arcpy.Exists(r"E:\Cursos\Arcpy\LPA\Data\test.gdb"): # essas duas linhas seriam apra deletar o gdb e escrever por cima, porem ja utilizei a função overwrite
##    arcpy.Delete_management(r"C:\LPA\Data\test.gdb")
           
arcpy.CreateFileGDB_management(r"E:\Cursos\Arcpy\LPA\Data","test") # criando o gdb
#arcpy.management.CreateFileGDB(r"E:\Cursos\Arcpy\LPA\Data","teste") # outra forma de criar o gdb

arcpy.FeatureClassToFeatureClass_conversion(
    r"E:\Cursos\Arcpy\LPA\Data\ne_10m_admin_0_countries",
    r"E:\Cursos\Arcpy\LPA\Data\test.gdb","Countries") # copiando a shape para o gdb
    
print("Copia de Countries", arcpy.Exists(r"E:\Cursos\Arcpy\LPA\Data\test.gdb\Countries")) # verificando se foi copiada

arcpy.Select_analysis("Countries","TrinidadTobago", "NAME = 'Trinidad and Tobago' ") # Selecionando Trinidade e Tobago
print("Trinidade e Tobago =", arcpy.Exists(r"E:\Cursos\Arcpy\LPA\Data\test.gdb\TrinidadTobago")) # Verificando se foi criado

arcpy.Buffer_analysis("TrinidadTobago","TrinidadTobago_EEZ",
                      "200 NauticalMiles",dissolve_option="ALL", method="GEODESIC")
print("Trinidade e Tobago EEZ =", arcpy.Exists(r"E:\Cursos\Arcpy\LPA\Data\test.gdb\TrinidadTobago")) # verificando se foi copiada

arcpy.FeatureClassToFeatureClass_conversion(
    r"E:\Cursos\Arcpy\LPA\Data\ne_10m_admin_1_states_provinces",
    r"E:\Cursos\Arcpy\LPA\Data\test.gdb","States")
print(arcpy.GetCount_management("States"))

arcpy.env.extent= "TrinidadTobago_EEZ" # So quero as dentro desse shape
arcpy.CopyFeatures_management("States","StatesInExtent")
print(arcpy.GetCount_management("StatesInExtent"))

print("\nPrint Script Completed!")
