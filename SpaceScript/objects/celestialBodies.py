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

	def setPosition(self, parentPosition_arr, time_int):


class CMO(orbiatalObject):
	def __init__(self, eccentricity_float, semiMajorAxis_arr,inclination_float,
				 argumentOfPeriapsis_float, trueAnomaly_float, position_arr,
				 longitudeOfAscendingNode_float, mass_int, surfaceRadius_int,
				 rotation_arr, parent_str,
				 atmosphereRadius_int = 0, atmospheric_bool = False,
				 referenceDirection_arr = [1, 0, 0]):
		super().__init__(eccentricity_float, semiMajorAxis_arr, inclination_float,
				 argumentOfPeriapsis_float, trueAnomaly_float, position_arr,
				 longitudeOfAscendingNode_float, parent_str,
				 referenceDirection_arr)
		self.mass_int = mass_int
		self.radius_int = radius_int
		self.rotation_arr = rotation_arr

	def getSphereOfInfluence(self, point_arr, pointMass_int):
		