import SpaceScript
from SpaceScript import utility
from SpaceScript.utility import vectorAlgebra as vectorAlgebra
from SpaceScript.utility import constants as constants

def calcGravitationalInfluence(orbital_obj):
	#calculates the gravitational influence of a Parent to a orbiting or passing body
	ParentBody_obj = eval(orbital_obj.parent_str)
	dist_arr = [0,0,0]
	orbitalPos_arr = orbital_obj.position_arr
	ParentPos_arr = ParentBody_obj.position_arr
	if len(orbitalPos_arr) == len(ParentPos_arr):
		iteration_int = 0
		for iteration_int in range(len(orbitalPos_arr)):
			dist_arr[iteration_int] = ParentPos_arr[iteration_int]-orbitalPos_arr[iteration_int]
	gForce_float = constants.G*((orbital_obj.mass_int*ParentBody_obj.mass_int)/vectorAlgebra.length(dist_arr))
	return gForce_float
	
def calcOrbitalPosition(orbital_obj, time_float):
	#calculates the position that the orbital_obj will have in time_float seconds
	momVelocity_arr = orbital_obj.getVelocity()
	momPos_arr = orbital_obj.position_arr
	force_arr = calcGravitationalInfluence(orbital_obj)
	iteration_int = 0
	for iteration_int in range(len(force_arr)):
		velocityAdd_arr[iteration_int] = time_float*(force_arr[iteration_int]/orbital_obj.mass_int)
	newOrbitalVelocity_arr = vectorAlgebra.add(velocityAdd_arr, momVelocity_arr)
	iteration_int = 0
	for iteration_int in range(len(newOrbitalVelocity_arr)):
		deltaPos_arr[iteration_int] = time_float*newOrbitalVelocity_arr[iteration_int]
	momPos_arr = vectorAlgebra.add(deltaPos_arr, momPos_arr)
	orbital_obj.setVelocity(newOrbitalVelocity_arr)
	return momPos_arr
	
def calcKeplerianObjects(orbital_obj):
	r = orbital_obj.position_arr
	v = orbital_obj.getVelocity()
	evec = calcExcentricity(orbital_obj) #calculed eccentricity vector
	e = vectorAlgebra.abs(evec) #calculate eccentricity
	energy = vectorAlgebra.abs(v)**2/2-constants.G/r
	
	
'''def calcExcentricity(orbital_obj):
	orbitalPosition_arr = orbital_obj.position_arr
	orbitalVelocity_arr = orbital_obj.getVelocity()
	h = vectorAlgebra.crossProduct(orbitalPosition_arr, orbitalVelocity_arr)
	nhat = vectorAlgebra.crossProduct([0 0 1], h)
	evec = ((vectorAlgebra.abs(v)**2-mu/vectorAlgebra.abs(r))*r-vectorAlgebra.vectorScalarProduct(r,v)*v)/constants.mu
	e = vectorAlgebra.abs(evec)
	return e 
''' #method as layed out in stackexchange forum. no clue if it works or not.

#now using method as layed out in "orbital mechanics and astrodynamics" by gerald r. hintz
	
def calcInclination(r_arr, v_arr):
	hhat_arr = 
	