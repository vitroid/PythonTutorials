#!/usr/bin/env python -u

from math import *
import random
import sys
import getopt

#General list serializer
def serialize(x):
	dim = len(x)
	s = ""
	for i in range(0,dim):
		s += "%s " % x[i]
	s += "\n"
	return s

#General list unserializer
def unserialize(s):
	s = s.rstrip(" \n")
	x = s.split(" ")
	for i in range(0,len(x)):
		x[i] = float(x[i])
	return x

#graphic context #######################################################
class GC:
	def __init__(self,zoom=1.0):
		self.zoom = zoom


#an LJ particle ########################################################
class Particle:
	def __init__(self,pos=None,vel=None,file=None):
		if file is not None:
			self.load(file)
		else:
			self.pos = pos
			self.vel = vel
			dim = len(self.pos)
			self.force = [0.0]*dim
	
	def forward(self, dt):
		dim = len(self.pos)
		for i in range(0,dim):
			self.pos[i] += self.vel[i] * dt

	def accel(self, dt):
		dim = len(self.pos)
		for i in range(0,dim):
			self.vel[i] += self.force[i] * dt

	def resetforce(self):
		dim = len(self.pos)
		self.force = [0.0]*dim

	def rescale(self,factor):
		dim = len(self.pos)
		for i in range(0,dim):
			self.vel[i] *= factor

	def interact(self, target, cell):
		dim = len(self.pos)
		delta = [0.0] * dim
		force = [0.0] * dim
		ddsum = 0.0
		for i in range(0,dim):
			delta[i] = self.pos[i] - target.pos[i]
			if cell[i] != 0.0:
				delta[i] -= round(delta[i] / cell[i])*cell[i]
			ddsum += delta[i]**2
		pot = 4.0*(ddsum**-6 - ddsum**-3)
		force0 = -48.0*ddsum**-7 + 24.0*ddsum**-4
		virial = force0 * ddsum
		for i in range(0,dim):
			self.force[i] -= force0 * delta[i]
			target.force[i] += force0 * delta[i]
		return (pot,virial)
	
	def kinetic(self):
		dim = len(self.pos)
		kin = 0.0
		for i in range(0,dim):
			kin += self.vel[i]**2
		return kin * 0.5

	def randomize(self,kt):
		v = 4.0*kt
		dim = len(self.pos)
		for i in range(0,dim):
			self.vel[i] = v * (random.random() - 0.5)

	def draw(self, cell, gc, avgvel):
		pos = list(self.pos)
		dim = len(self.pos)
		for i in range(0,dim):
			if cell[i] != 0.0:
				pos[i] -= floor(pos[i] / cell[i])*cell[i]
		if dim < 3:
			oval((pos[0]-0.5)*gc.zoom,(pos[1]-0.5)*gc.zoom, gc.zoom,gc.zoom)
			line(pos[0]*gc.zoom,pos[1]*gc.zoom,(pos[0]+self.vel[0])*gc.zoom,(pos[1]+self.vel[1])*gc.zoom)
		else:
			vel = 0
			for v in self.vel:
				vel += v**2
			vel = sqrt(vel)
			sat = (pos[2] / cell[2])*0.5+0.5
			hue = 0.666 - 0.3 * vel / avgvel
			a = 0.5 / vel
			b = a + 1.0
			fill(hue,1.0,sat, 0.8)
			if self.vel[2] >= 0.0:
				oval((pos[0]-0.5)*gc.zoom,(pos[1]-0.5)*gc.zoom, gc.zoom,gc.zoom)
			line( (pos[0]+self.vel[0]*a)*gc.zoom,(pos[1]+self.vel[1]*a)*gc.zoom,
				  (pos[0]+self.vel[0]*b)*gc.zoom,(pos[1]+self.vel[1]*b)*gc.zoom)
			if self.vel[2] < 0.0:
				oval((pos[0]-0.5)*gc.zoom,(pos[1]-0.5)*gc.zoom, gc.zoom,gc.zoom)

	#serialize
	def __str__(self):
		s = serialize(self.pos) + serialize(self.vel) #+ serialize(self.force)
		return s
	
	def load(self,file):
		s = file.readline()
		self.pos = unserialize(s)
		s = file.readline()
		self.vel = unserialize(s)
		#s = file.readline()
		#self.force = unserialize(s)
		s = file.readline()
		self.force = [0.0] * len(self.pos)

	def save(self,file):
		file.write("%s\n" % self)
	


#System of particles ###################################################
class System:
	def __init__(self,cell=None,nballs=10,step=0,gc=None,
				 input=None,logfile=sys.stdout,velfile=None,velint=0,
				 kT=None ):
		if input is not None:
			self.load(input)
		else:
			self.lattice(cell,nballs)
			if kT is not None:
				random.seed(1)
				self.thermalize(kT)
		#initialize force
		self.interact()
		self.step = step
		self.gc = gc
		self.logfile = logfile
		self.velfile = velfile
		self.velinterval = velint
		self.kT = kT
		
	def lattice(self,cell,nballs):
		self.balls = []
		self.cell = cell
		dim = len(cell)
		if dim == 1:
			self.lattice1d(nballs)
		elif dim == 2:
			self.lattice2d(nballs)
		elif dim == 3:
			self.lattice3d(nballs)

	def thermalize(self,kT):
		for b in self.balls:
			b.randomize(kT)
		#Remove total translation
		dim = len(self.cell)
		N = len(self.balls)
		for i in range(0,dim):
			velsum = 0.0
			for b in self.balls:
				velsum += b.vel[i]
			velsum /= N
			for b in self.balls:
				b.vel[i] -= velsum

	def rescale(self,factor):
		for b in self.balls:
			b.rescale(factor)

	def lattice1d(self,nballs):
		n = nballs
		x = 0.0
		while 0 < n:
			self.balls += [Particle([x],[0.0])]
			n -= 1
			x += 1.12

	def lattice2d(self,nballs):
		n = nballs
		nx = int(self.cell[0] /1.12)
		ny = int(self.cell[1] / (1.12 * sqrt(3.0)/2))
		for iy in range(0,ny):
			for ix in range(0,nx):
				x = ix * 1.12
				y = iy * 1.12 * sqrt(3.0)/2 + 0.1
				if iy % 2 != 0:
					x += 1.12 / 2.0
				self.balls += [Particle([x,y],[0.0,0.0])]
				n -= 1
				if n == 0:
					break
			if n==0:
				break

	def lattice3d(self,nballs):
		n = nballs
		nx = int(self.cell[0] /1.12)
		ny = int(self.cell[1] / (1.12 * sqrt(3.0)/2))
		nz = int(self.cell[2] / (1.12 * sqrt(6.0)/3.0))
		for iz in range(0,nz):
			for iy in range(0,ny):
				for ix in range(0,nx):
					x = ix * 1.12
					y = iy * 1.12 * sqrt(3.0)/2 + 0.1
					z = iz * 1.12 * sqrt(6.0)/3 + 0.1
					if iy % 2 != 0:
						x += 1.12 / 2.0
					if iz % 2 != 0:
						x += 1.12 / 2.0
						y += 1.12 * sqrt(3.0)/2 * 2.0/3.0
					self.balls += [Particle([x,y,z],[0.0,0.0,0.0])]
					n -= 1
					if n==0:
						break
				if n == 0:
					break
			if n==0:
				break


	def interact(self):
		N = len(self.balls)
		potsum = 0.0
		virsum = 0.0
		for i in range(0,N):
			for j in range(i+1,N):
				(pot,vir) = self.balls[i].interact( self.balls[j], self.cell )
				potsum += pot
				virsum += vir
		self.pot = potsum
		return (potsum,virsum)

	def OneStep(self,dt):
		#Progress Momenta (half)
		for b in self.balls:
			b.accel(dt/2.0)
		#Progress Position
		for b in self.balls:
			b.forward(dt)
			b.resetforce()
		#Force
		(pot,virsum) = self.interact()
		#Progress Momenta (half)
		for b in self.balls:
			b.accel(dt/2.0)
		#temperature scaling
		if self.kT is not None:
			kin = 0.0
			for b in self.balls:
				kin += b.kinetic()
			dof = len(self.balls) * len(self.cell)
			factor =   (self.kT * dof / 2.0)  / kin
			factor = 1.0 - (1.0 - factor)* 0.001
			self.rescale(factor)
		#Data output
		if self.logfile is not None:
			dim = len(self.cell)
			N = len(self.balls)
			kin = 0.0
			for b in self.balls:
				kin += b.kinetic()
			kT = 2.0 * kin / ( dim * N )
			z = 1.0 - virsum / (dim * N * kT )
			self.logfile.write("%s %s %s %s %s %s\n" %
							   (self.step, kT, z, kin+pot, kin, pot))
		if self.velfile is not None and self.step%self.velinterval == 0:
			for i in range(0,N):
				self.velfile.write("%s\n" % sqrt(2.0*self.balls[i].kinetic()))
		self.step += 1
	
	def draw(self):
		if self.gc is not None:
			dim = len(self.cell)
			if 2 < dim:
				avgvel = 0.0
				if self.kT > 0.0:
					avgvel = sqrt(dim * self.kT)
				tmp = list(self.balls)
				tmp.sort(cmp=lambda x, y:cmp(y.pos[2],x.pos[2]))
				for b in tmp:
					b.draw(self.cell,self.gc,avgvel)
			else:
				for b in self.balls:
					b.draw(self.cell,self.gc,0.0)

	def load(self,file):
		self.balls = []
		s = file.readline()
		self.cell = unserialize(s)
		s = file.readline()
		x = unserialize(s)
		x = int(x[0])
		for i in range(0,x):
			self.balls.append(Particle(file=file))
		s = file.readline()

	#serialize
	def __str__(self):
		s = serialize(self.cell)
		s += "%s\n" % len(self.balls)
		for i in range(0,len(self.balls)):
			s+= "%s\n" % self.balls[i]
		return s

	def save(self,file):
		file.write("%s\n" % self)


#For nodebox animation #################################################


def setup():
	global system
	width = 4.5
	height = 4.5
	zoom = 10.0
	size(width*zoom, height*zoom)
	system=System(step=0, nballs=64 , cell=[width, height,height],
				   gc=GC(zoom=zoom),logfile=None, kT=1.0)

def draw():
	global system
	colormode(HSB)
	stroke(0,0,0)
	fill(0,0,1)
	#時間0.01だけアニメーションを進める。
	system.OneStep(0.001)
	system.draw()
	
#for slient run #######################################################
#コマンドライン引数は1番目がステップ数(省略不可)、2番目が出力ベース名、
#継続データは標準入力。ただし、dimenが指定された場合は初期化。

def usage():
	print("usage: %s [-a n|--atoms=n][-d t|--dt=t][-t x|--temp=x][-c x,y|--cell=x,y,z][-v i|--vel=i] steps outputbase" % sys.argv[0])
	print("	-a n|--atoms=n		Specify number of atoms.")
	print("	-v i|--vel=i 		Output velocity list every i steps.")
	print("	-d t|--dt=t  		Step interval(default=0.01).")
	print("	-t x|--temp=x		Specify initial temperature in kT.")
	print("	-c x,y|--cell=x,y	Specify initial cell size.")
	print("-c and -a must be specified at a time.")
	print(" If they are not specified, last data *.lj2 will be read from stdin.")
	sys.exit(2)

def main():
	#コマンドラインオプションの解析 ####################################
	args = sys.argv[1:len(sys.argv)]
	optlist, args = getopt.getopt(args, 'v:d:t:c:a:', ['vel=','dt=','temp=','cell=','atoms='])
	if len(args) < 2:
		usage()
	steps = int(args[0])
	basename = args[1]
	temp = 0.0
	cell = None
	natom = 0
	velinterval = 0
	deltatime = 0.01
	for o,a in optlist:
		if o in ("-t","--temp"):
			temp = float(a)
		if o in ("-a","--atoms"):
			natom = int(a)
		if o in ("-v","--vel"):
			velinterval = int(a)
		if o in ("-d","--dt"):
			deltatime = float(a)
		if o in ("-c","--cell"):
			c = a.split(",")
			for i in range(0,len(c)):
				c[i] = float(c[i])
			cell = c
	#Initialize ########################################################
	velfile = None
	if velinterval > 0:
		velfilename = "%s.vel" % basename
		velfile = open(velfilename, "w")
	logfilename = "%s.log" % basename
	logfile = open(logfilename,"w")
	system = None
	if cell is None:
		#cell is not defined; Continue from the last data.
		if temp > 0.0:
			system = System(input=sys.stdin,logfile=logfile,
						velfile=velfile,velint=velinterval,kT=temp)
		else:	
			system = System(input=sys.stdin,logfile=logfile,
						velfile=velfile,velint=velinterval)
	else:
		if natom==0:
			usage()
		#Cell is defined. Start new run.
		system = System(nballs=natom,cell=cell,gc=None,logfile=logfile,
						velfile=velfile,velint=velinterval,kT=temp)

	#Main Loop #########################################################
	for step in range(0,steps):
		system.OneStep(deltatime)

	#Finish ############################################################
	outfilename = "%s.lj2" % basename
	outfile = open(outfilename,"w")
	system.save(outfile)
	outfile.close()


#Uncomment one of them	
speed(10)  #for NodeBox
# main()     #for Commandline execution
