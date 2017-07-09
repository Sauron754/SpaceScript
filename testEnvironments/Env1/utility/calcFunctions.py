import SpaceScript
from SpaceScript import utility
from SpaceScript.utility import constants
from SpaceScript.utility import vectorAlgebra

G = SpaceScript.utility.constants.G

def objectDistance(objectA_obj, objectB_obj):
	vectorAB = objectB_obj.position_arr - objectB_obj.position_arr
	distance = SpaceScript.utility.vectorAlgebra.length(vectorAB)
	return distance

def gravitationForce(mass1_int, mass2_int, distance_int):
	force = G * (mass1_int * mass2_int) / distance_int
	return force