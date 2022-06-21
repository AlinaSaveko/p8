# This script extract value from a DEM by Feature Class.
import arcpy
from arcpy import env
env.workspace = r"E:\_Sheva\course_3_geoinf\Python_2\GIT\p_8\Lesson4"
inDem = "foxlake"
featureClass = "Temp.shp"
# Enter for loop for each feature
with arcpy.da.SearchCursor(featureClass, ["SHAPE@XY",]) as cursor:
    for row in cursor:        
        x, y = row[0]
        result = arcpy.GetCellValue_management(inDem,str(x) + " " + str(y))
        print "Pixel value: " + result.getOutput(0)
print "All done!"
