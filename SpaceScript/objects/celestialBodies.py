class orbiatalObject():
	def __init__(self, eccentricity_float, semiMajorAxis_arr, inclination_float,
				 argumentOfPeriapsis_float, trueAnomaly_float,
				 longitudeOfAscendingNode_float,
				 referenceDirection_arr = [1, 0, 0]):
		self.eccentricity_float = eccentricity_float
		self.semiMajorAxis_arr = semiMajorAxis_arr
		self.inclination_float = inclination_float
		self.argumentOfPeriapsis_float = argumentOfPeriapsis_float
		self.trueAnomaly_float = trueAnomaly_float
		self.longitudeOfAscendingNode_float = longitudeOfAscendingNode_float
		self.referenceDirection_arr = referenceDirection_arr

class CMO():
	def __init__(self, eccentricity_float, semiMajorAxis_arr, inclination_float,
				 argumentOfPeriapsis_float, trueAnomaly_float,
				 longitudeOfAscendingNode_float, mass_int, radius_int,
				 rotationAxis_arr, rotation,
				 atmosphereRadius_int = 0, atmospheric_bool = False,
				 referenceDirection_arr = [1, 0, 0]):
		super().__init__(eccentricity_float, semiMajorAxis_arr, inclination_float,
				 argumentOfPeriapsis_float, trueAnomaly_float,
				 longitudeOfAscendingNode_float,
				 referenceDirection_arr)
		self.mass_int = mass_int
		self.radius_int = radius_int
		self.rotationAxis_arr = rotationAxis_arr
		self.rotation = rotation