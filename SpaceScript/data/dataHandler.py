def newWorldSave(saveName_str):
	#Generates a new world save with specified name
	#saveName_str style: name
	saveFolder_str = modulePathReal + saveName_str
	if not os.path.exists(saveFolder_str):
		os.makedirs(saveFolder_str)
		return(true)
		
	else 
		return(false)

		
def setWorldProperties(worldName_str, s)