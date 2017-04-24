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

class orbiatalObject():
	def __init__(self, eccentricity_float, semiMajorAxis_arr, 
				 inclination_float, argumentOfPeriapsis_float,
				 trueAnomaly_float, position_arr,
				 longitudeOfAscendingNode_float, parent_str,
				 referenceDirection_arr = [1, 0, 0]):
		self.eccentricity_float = eccentricity_float
		self.semiMajorAxis_arr = semiMajorAxis_arr
		self.inclination_float = inclination_float
		self.argumentOfPeriapsis_float = argumentOfPeriapsis_float
		self.trueAnomaly_float = trueAnomaly_float
		self.position_arr = position_arr
		self.longitudeOfAscendingNode_float = longitudeOfAscendingNode_float
		self.parent_str = parent_str
		self.referenceDirection_arr = referenceDirection_arr

class CMO(orbiatalObject):
	def __init__(self, eccentricity_float, semiMajorAxis_arr,inclination_float,
				 argumentOfPeriapsis_float, trueAnomaly_float, position_arr,
				 longitudeOfAscendingNode_float, mass_int, surfaceRadius_int,
				 rotation_arr, parent_str,
				 atmosphereRadius_int = 0, atmospheric_bool = False,
				 referenceDirection_arr = [1, 0, 0]):
		super().__init__(eccentricity_float, semiMajorAxis_arr,
						 inclination_float, argumentOfPeriapsis_float,
						 trueAnomaly_float, position_arr,
						 longitudeOfAscendingNode_float, parent_str,
						 referenceDirection_arr)
		self.mass_int = mass_int
		self.radius_int = radius_int
		self.rotation_arr = rotation_arr

	def getSphereOfInfluence(self, object_obj):
		influence = False
		distance = vectorLength(self.semiMajorAxis_arr) * (self.mass_int / object_obj.mass_int)**(2/5)
		relativePosition_arr = vectorAdd(object_obj.position_arr, vectorInvert(slef.position_arr))
		if (relativePosition_arr[0]**2 + relativePosition_arr[1]**2 + relativePosition_arr[2]**2 < distance**2):
			influence = True
		return influence