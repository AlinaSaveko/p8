'''import arcpy
from arcpy import env
env.workspace = r"E:\_Sheva\course_3_geoinf\Python_2\GIT\p_8\Lesson4"
rasterlist = arcpy.ListRasters( )
for raster in rasterlist:
    print raster

'''
import arcpy
from arcpy import env
env.workspace = r"E:\_Sheva\course_3_geoinf\Python_2\GIT\p_8\Lesson4"
rasterlist = arcpy.ListRasters( )
for raster in rasterlist:
    desc = arcpy.Describe(raster)
    print raster + " is <<<" + desc.dataType + ">>> raster type"
