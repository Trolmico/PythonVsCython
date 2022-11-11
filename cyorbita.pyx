#cython: language_level=3
cimport cython

#It is created squared root function
cdef extern from "math.h":
	double sqrt(double x) nogil

cdef class Planet(object):
	#It is declared class variables of double type
	cdef public double x,y,z,vx,vy,vz,m
	def __init__(self):
	# Alguna posición 
		self.x = 1.0
		self.y = 0.0
		self.z = 0.0
		self.vx = 0.0
		self.vy = 0.5
		self.vz = 0.0
	# Masa
		self.m = 1.0

@cython.cdivision(True)
cdef void single_step(Planet planet, double dt):
	""" Se hace un paso  en el tiempo """

	#Calculo de la fuerza: gravedad sobre el origen
	cdef float x,y,z,Fx,Fy,Fz,distancia
	distancia = sqrt(planet.x**2+planet.y**2+planet.z**2)
	Fx = -planet.x/distancia**3
	Fy = -planet.y/distancia**3
	Fz = -planet.z/distancia**3

	# Paso del tiempo de posicion, de acuero a la v
	planet.x += dt*planet.vx
	planet.y += dt*planet.vy
	planet.z += dt*planet.vz

	# Paso del tiempo de velocidad, de acuero a la f y m
	planet.vx += dt*Fx/planet.m
	planet.vy += d t*Fy/planet.m
	planet.vz += dt*Fz/planet.m
			
cpdef step_time(Planet planet, float time_span,int n_steps):
	cdef double dt
	cdef int j
	dt = time_span/n_steps
	"""Habilitar la posibilidad de paralelismo"""
	with nogil
	for j in range(n_steps):
		single_step(planet, dt)