import arcpy

arcpy.env.workspace = r"E:\Cursos\Arcpy\LPA" # Choose envirolment
wsList = arcpy.ListWorkspaces()
#Lista dos gdbs dentro de cada workspaces
gdbListAll=[]
for workspace in wsList:
    arcpy.env.workspace=workspace
    gdbList=arcpy.ListWorkspaces("","FileGDB")
    #print("{0} contains {1}".format(workspace,gdbList))
    gdbListAll+=gdbList
print("List of file geodatabases: \n {0}".format(gdbListAll))

#Listar as Classes,datasets e classes dentros dos datasets
for gdb in gdbListAll:
    arcpy.env.workspace=gdb
    print("\nFeature classes in {0}:\n{1}".format(
        gdb, arcpy.ListFeatureClasses()))
    print("\nFeature datasets in {0}:\n{1}".format(
        gdb,arcpy.ListDatasets("","Feature")))
    fdList=arcpy.ListDatasets("","Feature")
    for fd in fdList:
        arcpy.env.workspace =r"{0}\{1}".format(gdb,fd)
        print("\nFeature classes in feature dataset {0}:\n{1}".format(
            arcpy.env.workspace,arcpy.ListFeatureClasses()))
              
print('\nScript completed!')
