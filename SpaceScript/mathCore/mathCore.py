import SpaceScript
from SpaceScript import utility
from SpaceScript.utility import vectorAlgebra
from SpaceScript.utility import constants

def calcGravitationalInfluence(orbital_obj):
	#calculates the gravitational influence of a Parent to a orbiting or passing body
	ParentBody_obj = eval(orbital_obj.parent_str)
	dist_arr=[0,0,0]
	orbitalPos_arr=orbital_obj.position_arr
	ParentPos_arr=ParentBody_obj.position_arr
	if len(orbitalPos_arr)==len(ParentPos_arr):
		iteration_int=0
		for iteration_int in range(len(orbitalPos_arr)):
			dist_arr[iteration_int]=ParentPos_arr[iteration_int]-orbitalPos_arr[iteration_int]
	gForce_float = G*((orbital_obj.mass_int*ParentBody_obj.mass_int)/SpaceScript.utility.vectorAlgebra.length(dist_arr))
	return gForce_float
	
def calcOrbitalPosition(orbital_obj, time_float):
	#calculates the position that the orbital_obj will have in time_float
	momVelocity_arr = orbital_obj.getVelocity()
	momPos_arr = orbital_obj.position_arr
	force_arr = calcGravitationalInfluence(orbital_obj)
	iteration_int=0
	for iteration_int in range(len(force_arr)):
		velocityAdd_arr[iteration_int]=time_float*(force_arr[iteration_int]/orbital_obj.mass_int)
	newOrbitalVelocity_arr=SpaceScript.utility.vectorAlgebra.add(velocityAdd_arr, momVelocity_arr)
	iteration_int=0
	for iteration_int in range(len(newOrbitalVelocity_arr)):
		deltaPos_arr[iteration_int]=time_float*newOrbitalVelocity_arr[iteration_int]
	momPos_arr= SpaceScript.utility.vectorAlgebra.add(deltaPos_arr, momPos_arr)
	orbital_obj.setVelocity(newOrbitalVelocity_arr)
	return momPos_arr