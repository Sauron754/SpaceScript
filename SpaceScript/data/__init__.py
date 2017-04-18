import os

modulePath = os.path.dirname(exceptions.analysisExceptions.__file__)
modulePathSegments = modulePath.split("/")
subdirectoryCount = len(array)
modulePathReal = []
for iteration in range(subdirectoryCount - 1):
	modulePathReal.append(modulePathSegments[iteration])