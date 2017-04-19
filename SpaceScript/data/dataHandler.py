import os

def __init__():
	global modulePath
	modulePath = os.path.dirname(os.path.abspath(__file__))


	
def newWorldSave(saveName_str):
	#Generates a new world save with specified name
	#saveName_str style: name
	saveFolder_str = modulePath + chr(92) +saveName_str
	if not os.path.exists(saveFolder_str):
		os.makedirs(saveFolder_str)
		os.makedirs(saveFolder_str+chr(92)+"crafts")
		os.makedirs(saveFolder_str+chr(92)+"flights")
		universeState_obj= open(saveFolder_str+chr(92)+"current.universe","w")
		universeState_obj.write("0"+chr(10)+chr(13))
		universeState_obj.close()
		return(True)
		
	else:
		return(False)

		
def getWorldProperties(worldName_str, valueCount_int):
	# returns values from the current.universe file
	saveFolder_str = modulePath + chr(92) +worldName_str
	if not os.path.exists(saveFolder_str):
		return(False)
		
	else:
		universeState_obj=open(saveFolder_str+chr(92)+"current.universe","r")
		outPut_str = universeState_obj.readlines()
		universeState_obj.close()
		return(outPut_str[valueCount_int])
		
		
def setWorldProperties(worldName_str, valueCount_int, propertyValue_str):
	#replaces one value of the current.universe with andother one 
	saveFolder_str = modulePath + chr(92) +worldName_str
	if not os.path.exists(saveFolder_str):
		return(False)
		
	else:
		universeState_obj=open(saveFolder_str+chr(92)+"current.universe","r")
		worldProperties_arr = universeState_obj.readlines()
		universeState_obj.close()
		print(worldProperties_arr)
		print(len(worldProperties_arr))
		if len(worldProperties_arr)<(valueCount_int):
			return(False)
			
		elif len(worldProperties_arr) == (valueCount_int):
			universeState_obj=open(saveFolder_str+chr(92)+"current.universe","a")
			universeState_obj.write(propertyValue_str+chr(10)+chr(13))
			universeState_obj.close()
			return(True)
			
		elif len(worldProperties_arr)>(valueCount_int):
			worldProperties_arr[valueCount_int]=propertyValue_str+chr(10)+chr(13)
			universeState_obj=open(saveFolder_str+chr(92)+"current.universe","w")
			universeState_obj.writelines(worldProperties_arr)
			universeState_obj.close()
			return(True)


def newCraftSave(worldName_str, craftName_str)
	saveFolder_str=modulePath+chr(92)+worldName_str+chr(92)+"crafts"
	if not os.path.exists(saveFolder_str+chr(92)+craftName_str+".craft"):
		universeState_obj= open(saveFolder_str+chr(92)+craftName_str+".craft","w")
		universeState_obj.close()
		return(True)
		
	else:
		return(False)
		
def getCraftProperties(worldName_str, craftName_str, valueCount_int):
	# returns values from the current.universe file
	saveFolder_str=modulePath+chr(92)+worldName_str+chr(92)+"crafts"
	if not os.path.exists(saveFolder_str+chr(92)+craftName_str+".craft"):
		return(False)
		
	else:
		universeState_obj=open(saveFolder_str+chr(92)+craftName_str+".craft","r")
		outPut_str = universeState_obj.readlines()
		universeState_obj.close()
		return(outPut_str[valueCount_int])
		
'''	
def setCraftProperties(worldName_str, valueCount_int, propertyValue_str):
	#replaces one value of the current.universe with andother one 
	saveFolder_str = modulePath + chr(92) +worldName_str
	if not os.path.exists(saveFolder_str):
		return(False)
		
	else:
		universeState_obj=open(saveFolder_str+chr(92)+"current.universe","r")
		worldProperties_arr = universeState_obj.readlines()
		universeState_obj.close()
		print(worldProperties_arr)
		print(len(worldProperties_arr))
		if len(worldProperties_arr)<(valueCount_int):
			return(False)
			
		elif len(worldProperties_arr) == (valueCount_int):
			universeState_obj=open(saveFolder_str+chr(92)+"current.universe","a")
			universeState_obj.write(propertyValue_str+chr(10)+chr(13))
			universeState_obj.close()
			return(True)
			
		elif len(worldProperties_arr)>(valueCount_int):
			worldProperties_arr[valueCount_int]=propertyValue_str+chr(10)+chr(13)
			universeState_obj=open(saveFolder_str+chr(92)+"current.universe","w")
			universeState_obj.writelines(worldProperties_arr)
			universeState_obj.close()
			return(True)
'''		