from __future__ import print_function, absolute_import, division
from astropy import constants as const
import numpy as np

# Some limits on our solar system sizes (AU) and velocities (km/s)
MINIMUM_SIZE = 0.3
MAXIMUM_SIZE = 50.0
MINIMUM_VELOCITY = 20.0  # ?
MAXIMUM_VELOCITY = 50.0  # ?


class SolarSystemObject :
	"""
	Base class for all objects in a solar system. This includes planets,
	stars, asteroids, and commets. This is just the base class, and interface
	is intended to be done with the individual object subclasses.
	
	Attributes
	----------
	mass : float
		Mass of object in kilograms
	position : float array-like, optional
		Position (x, y) of object in AU with respect to the focal point.
		Defaults to array of random values within 0.3 and 50 AU
	velocity : float array-like
		Velocity (v_x, v_y) of object in kilometers/second. Defaults to array
		of random values within 20 and 50 km/s
	name : str, optional
		Name of object. Defaults to 'Object'
	"""
	
	def __init__(self, mass, position=None, velocity=None, name="Object") :
		self.mass = mass
		if position is not None :
			self.position = np.asarray(position)
			if self.position.size < 2 :
				raise TypeError(
					  "Expected array-like for position, got {}".format(
							type(position)))
		else :
			self.position = (MAXIMUM_SIZE - MINIMUM_SIZE) * np.random.rand(
				  2) + MINIMUM_SIZE
		if velocity is not None :
			self.velocity = np.asarray(velocity)
			if self.velocity.size < 2 :
				raise TypeError(
					  "Expected array-like for velocity, got {}".format(
							type(velocity)))
		else :
			self.velocity = (
			                MAXIMUM_VELOCITY - MINIMUM_VELOCITY) * \
			                np.random.rand(
				  2) + MINIMUM_VELOCITY
		self.name = name
	
	def __repr__(self) :
		return "{}: Mass = {} kg, position = ({}, {}) AU, velocity = ({}, " \
		       "{}) km/s".format(
			  self.name, self.mass, self.position, self.velocity)


class Star(SolarSystemObject) :
	"""
	Subclass of SolarSystemObject for a star. The star is always located at
	the focal point and thus has position and velocity zero relative to this.
	
	This currently has only mass and name as attributes.
	
	Attributes
	----------
	mass : float
		Mass of planet in kilograms
	name : str, optional
		Name of star. Defaults to 'Star'
	"""
	
	def __init__(self, mass, name="Star") :
		super(Star, self).__init__(mass, np.zeros(2), np.zeros(2), name)
	
	def __repr__(self) :
		return "{}: Mass = {} M_sun".format(self.name,
			  self.mass / const.M_sun.value)


class Planet(SolarSystemObject) :
	"""
	Subclass of SolarSystemObject for a planet.
	
	This currently has no attributes beyond the SolarSystemObject class.
	
	Attributes
	----------
	mass : float
		Mass of planet in kilograms
	position : float array-like
		Position (x, y) of planet in AU with respect to the focal point.
		Defaults to array of random values within 0.3 and 50 AU
	velocity : float array-like
		Velocity (v_x, v_y) of planet in kilometers/second. Defaults to array
		of random values within 20 and 50 km/s
	name : str, optional
		Name of planet. Defaults to 'Planet'
	"""
	
	def __index__(self, mass, position=None, velocity=None, name="Planet") :
		super(Planet, self).__index__(mass, position, velocity, name)
	
	def __repr__(self) :
		return "{}: Mass = {} kg, position = ({}, {}) AU, velocity = ({}, " \
		       "{}) km/s".format(
			  self.name, self.mass, self.position, self.velocity)


class GasPlanet(Planet) :
	"""
	Subclass of Planet for a gas (giant) planet.
	
	This currently has no attributes beyond the SolarSystemObject class.
	
	Attributes
	----------
	mass : float
		Mass of planet in kilograms
	position : float array-like
		Position (x, y) of planet in AU with respect to the focal point.
		Defaults to array of random values within 0.3 and 50 AU
	velocity : float array-like
		Velocity (v_x, v_y) of planet in kilometers/second. Defaults to array
		of random values within 20 and 50 km/s
	name : str, optional
		Name of planet. Defaults to 'Planet'
	"""
	
	def __repr__(self) :
		return "{}: Mass = {} M_jup, position = ({}, {}) AU, velocity = ({}, " \
		       "{}) km/s".format(
			  self.name, self.mass / const.M_jup.value, self.position,
			  self.velocity)


class TerrestrialPlanet(Planet) :
	"""
	Subclass of Planet for a terrestrial planet.

	This currently has no attributes beyond the SolarSystemObject class.

	Attributes
	----------
	mass : float
		Mass of planet in kilograms
	position : float array-like
		Position (x, y) of planet in AU with respect to the focal point.
		Defaults to array of random values within 0.3 and 50 AU
	velocity : float array-like
		Velocity (v_x, v_y) of planet in kilometers/second. Defaults to array
		of random values within 20 and 50 km/s
	name : str, optional
		Name of planet. Defaults to 'Planet'
	"""
	
	def __repr__(self) :
		return "{}: Mass = {} M_earth, position = ({}, {}) AU, velocity = ({}, " \
		       "{}) km/s".format(
			  self.name, self.mass / const.M_earth.value, self.position,
			  self.velocity)


class DwarfPlanet(Planet) :
	"""
	Subclass of Planet for a dwarf planet.

	This currently has no attributes beyond the SolarSystemObject class.

	Attributes
	----------
	mass : float
		Mass of planet in kilograms
	position : float array-like
		Position (x, y) of planet in AU with respect to the focal point.
		Defaults to array of random values within 0.3 and 50 AU
	velocity : float array-like
		Velocity (v_x, v_y) of planet in kilometers/second. Defaults to array
		of random values within 20 and 50 km/s
	name : str, optional
		Name of planet. Defaults to 'Planet'
	"""
	
	def __repr__(self) :
		M_pluto = 1.309e22
		return "{}: Mass = {} M_pluto, position = ({}, {}) AU, velocity = ({}, " \
		       "{}) km/s".format(
			  self.name, self.mass / M_pluto, self.position, self.velocity)


class Asteroid(SolarSystemObject) :
	"""
	Subclass of SolarSystemObject for an asteroid.

	This currently has no attributes beyond the SolarSystemObject class.

	Attributes
	----------
	mass : float
		Mass of asteroid in kilograms
	position : float array-like
		Position (x, y) of asteroid in AU with respect to the focal point.
		Defaults to array of random values within 0.3 and 50 AU
	velocity : float array-like
		Velocity (v_x, v_y) of asteroid in kilometers/second. Defaults to
		array of random values within 20 and 50 km/s
	name : str, optional
		Name of asteroid. Defaults to 'Asteroid'
	"""
	
	def __init__(self, mass, position=None, velocity=None, name="Asteroid") :
		super(Asteroid, self).__init__(mass, position, velocity, name)
	
	def __repr__(self) :
		return "{}: Mass = {} kg, position = ({}, {}) AU, velocity = ({}, " \
		       "{}) km/s".format(
			  self.name, self.mass, self.position, self.velocity)


class Comet(SolarSystemObject) :
	"""
	Subclass of SolarSystemObject for a comet.

	This currently has no attributes beyond the SolarSystemObject class.

	Attributes
	----------
	mass : float
		Mass of comet in kilograms
	position : float array-like
		Position (x, y) of comet in AU with respect to the focal point.
		Defaults to array of random values within 0.3 and 50 AU
	velocity : float array-like
		Velocity (v_x, v_y) of comet in kilometers/second. Defaults to array
		of random values within 20 and 50 km/s
	name : str, optional
		Name of comet. Defaults to 'Comet'
	"""
	
	def __init__(self, mass, position=None, velocity=None, name="Comet") :
		super(Comet, self).__init__(mass, position, velocity, name)
	
	def __repr__(self) :
		return "{}: Mass = {} kg, position = ({}, {}) AU, velocity = ({}, {}) km/s".format(
			  self.name, self.mass, self.position, self.velocity)
