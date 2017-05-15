import SpaceScript
from SpaceScript import utility
from SpaceScript.utility import vectorAlgebra
from SpaceScript.utility import constants
from SpaceScript.utility import calcFunctions

gravitationForce = SpaceScript.utility.calcFunctions.gravitationForce()
objectDistance = SpaceScript.utility.calcFunctions.objectDistance()
vectorLength = SpaceScript.utility.vectorAlgebra.length()
vectorInvert = SpaceScript.utility.vectorAlgebra.invert()
vectorAdd = SpaceScript.utility.vectorAlgebra.add()

class orbitalObject():
	"""class that descibes mechanics of orbital objects"""
	def __init__(self, parent_str, position_arr, velocity_arr, 
				 acceleration_arr, ascendingNode_arr = [], 
				 semiMajorAxis_arr = [], semiMinorAxis = [], 
				 inclination_float = False,
				 longitudeOfAscendingNode_float = False, 
				 argumentOfPeriapsis_float = False, trueAnomaly_float = False,
				 eccentricity_float = False, distanceFromParent_float = False):
		self.parent_str = parent_str
		self.position_arr = position_arr
		self.velocity_arr = velocity_arr
		self.acceleration_arr = acceleration_arr
		self.ascendingNode_arr = ascendingNode_arr
		self.semiMajorAxis_arr = semiMajorAxis_arr
		self.semiMinorAxis_arr = semiMinorAxis_arr
		self.inclination_float = inclination_float
		self.longitudeOfAscendingNode_float = longitudeOfAscendingNode_float
		self.argumentOfPeriapsis_float = argumentOfPeriapsis_float
		self.trueAnomaly_float = trueAnomaly_float
		self.eccentricity_float = eccentricity_float
		self.distanceFromParent_float = distanceFromParent_float
		self.kepplerValidity = False

	def kepplerUpdate():
		self.kepplerValidity = True

	def impulseSystemChange():
		self.kepplerValidity = False