import arcpy
##dataElement = r"E:\Cursos\Arcpy\LPA\Data\test.gdb" #path to the element folder
###dataElement = r"E:\Cursos\Arcpy\LPA\Data\test.gdb\NaturalEarth" #path to the element folder
##desc = arcpy.Describe(dataElement) # Criando um objeto descritivo
##print("Describing {0}...".format(dataElement))
##print("Name:     "+ desc.name)
##print("DataType:    " + desc.dataType)
##print("catalogPath:   "+ desc.catalogPath)
##print("Chieldren:")
##for child in desc.children:
##    if child.dataType == "FeatureDataset":
##        pass
##    else:
##        if hasattr(child,"shapeType"):
##            print ("    {0} is a {1} of a shapeType {2}".format(
##            child.name,child.dataType,child.shapeType))
##            print("   with Extent: {0}". format(child.extent))
##        else: print("  {0} is a {1}".format(child.name,child.dataType))
##        print("    and Fields:")
##        for field in child.fields:
##            print("   {0} of a type {1}".format(field.name,field.type))
##    



#Agora com função dicionario arcpy.da.desc()
dataElement = r"E:\Cursos\Arcpy\LPA\Data\test.gdb\Countries"
descDictionary=arcpy.da.Describe(dataElement)

#Enumerando as chaves dos dicionários
for i, key in enumerate(descDictionary):
    print("{0}.{1}:{2}".format(i+1,key,descDictionary[key]))

print("\nScript complete!")
