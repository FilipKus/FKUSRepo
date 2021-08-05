import math
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm
from mpl_toolkits.mplot3d import Axes3D

plt.style.use('dark_background')

earthRadius = 6378
earthMu = 398600

def coeFromSV(r, v):
	
	mu = earthMu
	rmag = norm(r)

	# Angular Momentum
	h = np.cross(r, v)
	hmag = norm(h)


	# Eccentricity
	e = np.cross(v, h)/mu - r/rmag
	emag = norm(e)


	# Inclination
	irad = math.acos(np.dot(h, [0, 0, 1])/hmag)
	ideg = np.rad2deg(irad)


	# Right ascension of the ascending node
	N = np.cross([0, 0, 1], h)
	Nmag = norm(N)

	if Nmag == 0:
		RAdeg = 0
	else:
		RAtemp = math.acos(np.dot([1, 0, 0], N)/Nmag)
		if np.dot(N, [0, 1, 0]) >= 0:
			RArad = RAtemp
		else:
			RArad = 2*math.pi - RAtemp

	RAdeg = np.rad2deg(RArad)	


	# Argument of Perigee
	if Nmag == 0:
		wdeg = 0
		wrad = 0
	else:
		wtemp = math.acos(np.dot(N, e)/(Nmag*emag))		
		if np.dot(e, [0, 0, 1]) >= 0:
			wrad = wtemp
		else:
			wrad = 2*math.pi - wtemp

	wdeg = np.rad2deg(wrad)		


	# True Anomaly
	if Nmag == 0:
		urad = 0		
	else:
		utemp = math.acos(np.dot(N, r)/(Nmag*rmag))		
		if np.dot(r, [0, 0, 1]) >= 0:
			urad = utemp
		else:
			urad = 2*math.pi - utemp


	TArad = urad - wrad
	if TArad < 0:
		TArad = TArad + 2*math.pi		
	TAdeg = np.rad2deg(TArad)					 	



	return hmag, emag, ideg, RAdeg, wdeg, TAdeg

def plot(rs):
	fig = plt.figure(figsize(18, 6))
	ax = fix.add_subplot(111, projection='3d')

	# Plot trajectory
	ax.plot(rs[:, 0], rs[:, 1], rs[:, 2], 'w', label = 'Trajectory')
	ax.plot([rs[0,0]], [rs[0, 1]], [rs[0, 2]], 'wo', label = 'Initial Position')

	# Plot central body
	_u,_v = np.mgrid[0:2*math.pi:20j, 0:math.pi:10j]
	_x = earthRadius*np.cos(_u)*np.sin(_v)
	_y = earthRadius*np.sin(_u)*np.cos(_v)
	_z = earthRadius*np.cos(_v)
	ax.plot_surface(_x, _y, _z, cmap = 'Blues')

	# Plot the x, y, z vectors
	l = earthRadius*2
	x, y, z = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
	u, v, w = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
	ax.quiver(x, y, z, u, v, w, color = 'k')

	max_val = np.max(np.abs(rs))

	ax.set_xlim([-max_val, max_val])
	ax.set_ylim([-max_val, max_val])
	ax.set_zlim([-max_val, max_val])

	ax.set_xlabel(['X (km)'])
	ax.set_ylabel(['Y (km)'])
	ax.set_zlabel(['Z (km)'])

	#ax.set_aspect('equal')

	ax.set_title('Orbit')

	plt.legend()

	plt.show()


coe = coeFromSV([-3670, -3870, 4400], [4.7, -7.4, 1])
print(coe)
