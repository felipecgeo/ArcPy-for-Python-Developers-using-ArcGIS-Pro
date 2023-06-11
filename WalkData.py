import arcpy

workspace =r"E:\Cursos\Arcpy\LPA\Data" # Selecionando o espaço de trabalho
#workspace = r"E:\Mestrado\Dados\Dados_Process"
dataList = [] #Criando lista vazia 
for dirpath, dirnames, filenames in arcpy.da.Walk(
    workspace, datatype="FeatureClass", type=["Point","Polygon"]): #loop 1, nesse ex. selecionei apenas os pontos e os polígonos
    for filename in filenames: # loop 2 
        dataList.append(r"{0}\{1}".format(len(dataList),workspace)) # armazenando na lista
print(dataList)
print("\nFound {0} data elements in {1}".format(len(dataList),workspace))
      
print("\nScript completed!")
