import SpaceScript
from SpaceScript import utility
from SpaceScript.utility import constants
from SpaceScript.utility import vectorAlgebra

G = SpaceScript.utility.constants.G

def objectDistance(objectA_obj, objectB_obj):
	vectorAB = objectB_obj.position_arr - objectB_obj.position_arr
	distance = SpaceScript.utility.vectorAlgebra.length(vectorAB)
	return distance
def gravitationForce(objectA_obj, objectB_obj):
	force_float = G * (objectA_obj.mass_int * objectB_obj.mass_int) / (SpaceScript.utility.vectorAlgebra.length(objectA_obj,objectB_obj))
	return force_float