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
		universeState_obj= open(saveFolder_str+chr(92)+"current.universe","w")
		universeState_obj.write("0")
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
		if len(worldProperties_arr)<valueCount_int-1:
			return(False)
			
		elif len(worldProperties_arr) == (valueCount_int-1):
			worldProperties_arr.insert(len(worldProperties_arr), propertyValue_str)
			
		elif len(worldProperties_arr)>valueCount_int-1:
			worldProperties_arr[valueCount_int]=propertyValue_str+chr(10)
			universeState_obj=open(saveFolder_str+chr(92)+"current.universe","w")
			universeState_obj.writelines(worldProperties_arr)
			return(True)