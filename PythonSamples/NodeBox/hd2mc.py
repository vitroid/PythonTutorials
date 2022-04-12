#!/usr/bin/env python

#ToDo
#record last1 and last2 in the trajectory file.

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


class RDF:
	def __init__(self,cell=None,gc=None):
		self.cell = cell
		self.gc = gc
		s = 0.0
		for c in cell:
			s += c**2
		self.bin = [0.0] * int(s*10)
		self.count = 0.0
	def accum(self,balls):
		nballs = len(balls)
		for i in range(nballs):
			for j in range(i+1,nballs):
				d = balls[i].sqdistance(balls[j].pos,self.cell)
				if d < 1.0:
					print i,j,d
				self.bin[int(d*10.0)] += 1
		self.count += 1
	def draw(self):
		zoom = self.gc.zoom
		yorigin = (self.cell[1]+5)*zoom
		print yorigin
		stroke(0,0,0)
		nofill()
		m = min(len(self.bin),int(self.cell[0]*zoom))
		print m
		beginpath(0,yorigin)
		for i in range(m):
			lineto(i*0.1*zoom,yorigin - zoom*self.bin[i]/10.0/self.count)
		moveto(0,yorigin)
		endpath()
	        
		


class Wall:
	def __init__(self,coeff=None,file=None):
		if file is not None:
			self.load(file)
		else:
			self.coeff = coeff

	#serialize
	def __str__(self):
		s = serialize(self.coeff)
		return s
	
	def load(self,file):
		s = file.readline()
		self.coeff = unserialize(s)
		s = file.readline()

	def save(self,file):
		file.write("%s\n" % self)

#graphic context #######################################################
class GC:
	def __init__(self,zoom=1.0):
		self.zoom = zoom


#a HardDisk #######################
class HardDisk:
	def __init__(self,pos=None,vel=None,file=None):
		if file is not None:
			self.load(file)
		else:
			self.pos = pos
			self.vel = vel
			self.flighttime = 0.0

	def randomize(self,kt):
		v = kt
		vec = []
		ss = 0.0
		dim = len(self.pos)
		for i in range(0,dim):
				x = random.random() - 0.5
				vec.append(x)
				ss += x**2
		s = sqrt(ss)
		for i in range(0,dim):
				vec[i] *= v / s
		self.vel = vec
		
	def forward(self,dt):
		for i in range(0,len(self.pos)):
			self.pos[i] += self.vel[i] * dt
		self.flighttime += dt
	
	# ball-to-ball collision time
	def sqdistance(self,newpos,cell):
		dim = len(self.pos)
		c = 0.0
		for i in range(dim):
			pos = newpos[i] - self.pos[i]
			pos -= floor(pos / cell[i] + 0.5)*cell[i]
			c += pos**2
		#if c < 1.0 and c != 0.0:
		#	print self.pos,newpos,c
		return c
		

	# ball-to-ball collision time
	def collide(self,target):
		dim = len(self.pos)
		vel = [0] * dim
		pos = [0] * dim
		a = 0.0
		b = 0.0
		c = -1.0
		for i in range(0,dim):
			vel[i] = target.vel[i] - self.vel[i]
			pos[i] = target.pos[i] - self.pos[i]
			a += vel[i]*vel[i]
			b += vel[i]*pos[i]
			c += pos[i]*pos[i]
		d = b*b - a*c
		if d < 0.0 or a == 0.0:
			dt = -1.0
		else:
			dt = (-b-sqrt(d))/a
		return dt
	
    # ball-to-ball reflection
	def reflect(self, target):
		dim = len(self.pos)
		pos = [0] * dim
		vels = 0.0
		velt = 0.0
		for i in range(0,dim):
			pos[i] = target.pos[i] - self.pos[i]
			vels += self.vel[i] * pos[i]
			velt += target.vel[i] * pos[i]
		for i in range(0,dim):
			self.vel[i] += pos[i] * (velt - vels)
			target.vel[i] +=pos[i] * (vels - velt)
		vels = 0.0
		velt = 0.0
		for i in range(0,dim):
				vels += self.vel[i]**2
				velt += target.vel[i]**2
		times = self.flighttime
		timet = target.flighttime
		#reset the time accumulator
		self.flighttime = 0.0
		target.flighttime = 0.0
		return (sqrt(vels),times,sqrt(velt),timet)
		
			
	#wallはax+by=cのabcからなるリスト
	def collideWall(self,wall):
		dim = len(self.pos)
		bunsi = wall.coeff[dim]
		bunbo = 0
		for i in range(0,dim):
			bunsi -= self.pos[i] * wall.coeff[i]
			bunbo += self.vel[i] * wall.coeff[i]
		if bunbo == 0.0:
			dt = -1.0
		else:
			dt = bunsi/bunbo
		return dt

	#wallはax+by=cのabcからなるリスト
	def reflectWall(self,wall):
		dim = len(self.pos)
		vels = 0.0
		#壁に垂直な方向の運動量をとりだす。
		for i in range(0,dim):
			vels += self.vel[i] * wall.coeff[i]
		for i in range(0,dim):
			self.vel[i] -= 2.0 * wall.coeff[i] * vels
		return abs(2.0*vels)

	def kinetic(self):
		dim = len(self.pos)
		kin = 0.0
		for i in range(0,dim):
			kin += self.vel[i]**2
		return kin * 0.5
	
	def draw(self, cell, gc, avgvel,label=None):
		pos = list(self.pos)
		dim = len(self.pos)
		if dim ==1:
			oval((pos[0]-0.5)*gc.zoom,0.0, gc.zoom,gc.zoom)
			line(pos[0]*gc.zoom,0.5*gc.zoom,(pos[0]+self.vel[0])*gc.zoom,0.5*gc.zoom)
		elif dim==2:
			oval((pos[0]-0.5)*gc.zoom,(pos[1]-0.5)*gc.zoom, gc.zoom,gc.zoom)
			line(pos[0]*gc.zoom,pos[1]*gc.zoom,(pos[0]+self.vel[0])*gc.zoom,(pos[1]+self.vel[1])*gc.zoom)
			if label:
				text(label,pos[0]*gc.zoom,pos[1]*gc.zoom)

		else:
			vel = 0
			for v in self.vel:
				vel += v**2
			vel = sqrt(vel)
			sat = (pos[2] / cell[2])*0.5+0.5
			hue = 0.666 - 0.3 * vel / avgvel
			fill(hue,1.0,sat, 0.8)
			if self.vel[2] >= 0.0:
				oval((pos[0]-0.5)*gc.zoom,(pos[1]-0.5)*gc.zoom, gc.zoom,gc.zoom)
			if vel > 0.0:
				a = 0.5 / vel
				b = a + 1.0
				line( (pos[0]+self.vel[0]*a)*gc.zoom,(pos[1]+self.vel[1]*a)*gc.zoom,
				  (pos[0]+self.vel[0]*b)*gc.zoom,(pos[1]+self.vel[1]*b)*gc.zoom)
			if self.vel[2] < 0.0:
				oval((pos[0]-0.5)*gc.zoom,(pos[1]-0.5)*gc.zoom, gc.zoom,gc.zoom)

	#serialize
	def __str__(self):
		s = serialize(self.pos) + serialize(self.vel)
		return s
	
	def load(self,file):
		s = file.readline()
		self.pos = unserialize(s)
		s = file.readline()
		self.vel = unserialize(s)
		s = file.readline()

	def save(self,file):
		file.write("%s\n" % self)


#System of HardDisks ###################################################
class System:
	def __init__(self,cell=None,nballs=10,step=0,gc=None,
				 input=None,logfile=sys.stdout,velfile=None,
				 kT=None, MC=None ):
		if input is not None:
			self.load(input)
		else:
			self.lattice(cell,nballs)
			if kT is not None:
				random.seed(1)
				self.thermalize(kT)
			self.last1 = self.last2 = None
		#initialize force
		self.step = step
		self.gc = gc
		self.logfile = logfile
		self.velfile = velfile
		self.kT = kT
		self.MC = MC
		if MC:
			self.grid = dict()
			for ball in self.balls:
				p = tuple(map(int,ball.pos))
				if self.grid.has_key(p):
					self.grid[p].append(ball)
				else:
					self.grid[p] = [ball]
				ball.vel = [0.0] * len(cell)
			self.delta=0.1

		
	def lattice(self,cell,nballs):
		self.balls = []
		self.cell = cell
		dim = len(cell)
		if dim == 1:
			self.lattice1d(nballs)
			self.walls= [ Wall(coeff=[1.0, 0.0]), 
						  Wall(coeff=[1.0, cell[0]])]
			self.area = 2.0*1.0
			self.volume = cell[0]

		elif dim == 2:
			self.lattice2d(nballs)
			#d次元の壁はd+1個の係数で指示する。
			#最後の要素以外は単位ベクトルでなければいけない。
			self.walls= [ Wall(coeff=[1.0, 0.0, 0.0]), 
						  Wall(coeff=[1.0, 0.0, cell[0]]),
						  Wall(coeff=[0.0, 1.0, 0.0]),
						  Wall(coeff=[0.0, 1.0, cell[1]]) ]
			self.area = 2.0*(cell[0]+cell[1])
			self.volume = cell[0]*cell[1]
		elif dim == 3:
			self.lattice3d(nballs)
			self.walls= [ Wall(coeff=[1.0, 0.0, 0.0, 0.0]), 
						  Wall(coeff=[1.0, 0.0, 0.0, cell[0]]),
						  Wall(coeff=[0.0, 1.0, 0.0, 0.0]),
						  Wall(coeff=[0.0, 1.0, 0.0, cell[1]]),
						  Wall(coeff=[0.0, 0.0, 1.0, 0.0]),
						  Wall(coeff=[0.0, 0.0, 1.0, cell[1]]) ]
			self.area = 2.0*(cell[0]*cell[1]+cell[1]*cell[2]+cell[0]*cell[2])
			self.volume = cell[0]*cell[1]*cell[2]

	def thermalize(self,kT):
		dim = len(self.cell)
		N = len(self.balls)
		#1粒子だけにエネルギーを与える。
		self.balls[0].randomize(sqrt(dim*kT*float(N)))
	
	def rescale(self,factor):
		for b in self.balls:
			b.rescale(factor)

	def lattice1d(self,nballs):
		n = nballs
		x = 0.1
		while 0 < n:
			self.balls += [HardDisk([x],[0.0])]
			n -= 1
			x += 1.12

	def lattice2d(self,nballs):
		n = nballs
		x = 0.01
		y = 0.01
		dan = 0
		while 0 < n:
			self.balls += [HardDisk([x,y],[0.0,0.0])]
			n -= 1
			x += 1.01
			if self.cell[0] < x+1.01:
				dan += 1
				if dan % 2 == 0:
					x = 0.01
				else:
					x = 0.51
				print dan,x
				y += 1.01 * sqrt(3.0) / 2.0

	def lattice3d(self,nballs):
		n = nballs
		x = 0.1
		y = 0.1
		z = 0.1
		while 0 < n:
			self.balls += [HardDisk([x,y,z],[0.0,0.0,0.0])]
			n -= 1
			x += 1.12
			if self.cell[0] < x:
				x -= self.cell[0] - (1.12 /2.0)
				y += 1.12 * sqrt(3.0) / 2.0
				if self.cell[0] < y:
					y = 0.1
					z += 1.12 * sqrt(3.0) / 2.0

	def OneCollision(self,deltat):
		dtmin = deltat
		object1 = 0
		object2 = 0
		#粒子のいずれかが壁にぶつかるまでの最短時間を調べる。
		for b in self.balls:
			for w in self.walls:
				if b != self.last1 or w != self.last2:
					dt = b.collideWall(w)
					if 0 < dt < dtmin:
						dtmin = dt
						object1 = b
						object2 = w
		#粒子同士が衝突するまでの最短時間を調べる。
		N = len(self.balls)
		for i in range(0,N):
			for j in range(i+1,N):
				if self.balls[i] != self.last1 or self.balls[j] != self.last2:
					dt = self.balls[i].collide(self.balls[j])
					if 0 < dt < dtmin:
						dtmin = dt
						object1 = self.balls[i]
						object2 = self.balls[j]
		#粒子をdtminだけ進める。
		for b in self.balls:
			b.forward(dtmin)
		impulse = 0.0
		#衝突相手が粒子なら
		if isinstance(object2,HardDisk):
		   	(v1,t1,v2,t2) = object1.reflect(object2)
			if self.velfile is not None:
					self.velfile.write("%s %s\n" % (v1,t1))
					self.velfile.write("%s %s\n" % (v2,t2))
			self.last1 = object1
			self.last2 = object2
		#壁に衝突する場合は、壁への力積から圧力が出せる。
		elif isinstance(object1,HardDisk):
			impulse = object1.reflectWall(object2)
			self.last1 = object1
			self.last2 = object2
		#最後に衝突した物体と、消費した時間を返す。
		return (dtmin,impulse)



	def OneStep(self,dt):
		bunbo = dt * self.area
	   	sumpulse = 0.0
		ncollision = 0
		while 0.0 < dt:
			#次の衝突またはdtまで粒子を進める。
		   	(progress,impulse) = self.OneCollision( dt )
			dt -= progress
			sumpulse += impulse
			if impulse == 0.0:
					ncollision += 1
		#Data output
		if self.logfile is not None:
			dim = len(self.cell)
			N = len(self.balls)
			kin = 0.0
			for b in self.balls:
				kin += b.kinetic()
			kT = 2.0 * kin / ( dim * N )
			#z = 1.0 + virsum / (dim * N * kT )
			pressure = sumpulse / bunbo
			self.logfile.write("%s %s %s %s %s\n" %
							   (self.step, kT, pressure*self.volume/(N * kT), kin, ncollision))
		self.step += 1
	
	def neighbors(self,ipos,dim):
		if dim < 0:
			if self.grid.has_key(ipos):
				return self.grid[ipos]
			else:
				return []
		nei = []
		for j in range(-1,2):
			newipos = list(ipos)
			newipos[dim] += j
			if int(self.cell[dim]) <= newipos[dim]:
				newipos[dim] -= int(self.cell[dim])
			elif newipos[dim] < 0:
				newipos[dim] += int(self.cell[dim])
			nei += self.neighbors(tuple(newipos),dim-1)
		return nei
		
	def OneStepMC(self):
		i = int(random.random() * len(self.balls))
		ball = self.balls[i]
		dim = len(self.cell)
		v = [0.0] * dim
		s = 0.0
		for d in range(dim):
			v[d] = random.random() - 0.5
			s += v[d] **2
		s = self.delta/sqrt(s)
		newpos = list(ball.pos)
		for d in range(dim):
			v[d] *= s
			newpos[d] += v[d]
			if newpos[d] < 0.0:
				newpos[d] += self.cell[d]
			if newpos[d] >= self.cell[d]:
				newpos[d] -= self.cell[d]
		oldipos = tuple(map(int,ball.pos))
		ipos = tuple(map(int,newpos))
		nei = self.neighbors(ipos,dim-1)
		overlap = False
		for n in nei:
			if n != ball:
				d = n.sqdistance(newpos,self.cell)
				if d < 1.0:
					overlap = True
		if not overlap:
			ball.pos = newpos
			if oldipos != ipos:
				self.grid[oldipos].remove(ball)
				if self.grid.has_key(ipos):
					self.grid[ipos].append(ball)
				else:
					self.grid[ipos] = [ball]
		n = 0
		for i in self.grid:
			n += len(self.grid[i])
		self.step += 1

	def draw(self):
		if self.gc is not None:
			dim = len(self.cell)
			if 2 < dim:
				#3次元以上の場合は、奥行き方向の座標順に描く。
				avgvel = 0.0
				if self.kT > 0.0:
					avgvel = sqrt(dim * self.kT)
				tmp = list(self.balls)
				tmp.sort(cmp=lambda x, y:cmp(y.pos[2],x.pos[2]))
				for b in tmp:
					b.draw(self.cell,self.gc,avgvel)
			else:
				for i in range(len(self.balls)):
					b = self.balls[i]
					b.draw(self.cell,self.gc,0.0) #,label=("%s" % i))

	def load(self,file):
		s = file.readline()
		self.cell = unserialize(s)

		self.balls = []
		s = file.readline()
		x = unserialize(s)
		x = int(x[0])
		for i in range(0,x):
			self.balls.append(HardDisk(file=file))

		self.walls = []
		s = file.readline()
		x = unserialize(s)
		x = int(x[0])
		for i in range(0,x):
			self.walls.append(Wall(file=file))

		s = file.readline()
		x = unserialize(s)
		self.area = float(x[0])

		s = file.readline()
		x = unserialize(s)
		self.volume = float(x[0])

		s = file.readline()

	#serialize
	def __str__(self):
		s = serialize(self.cell)
		s += "%s\n" % len(self.balls)
		for i in range(0,len(self.balls)):
			s+= "%s\n" % self.balls[i]
		s += "%s\n" % len(self.walls)
		for i in range(0,len(self.walls)):
			s+= "%s\n" % self.walls[i]
		s += "%s\n" % self.area
		s += "%s\n" % self.volume
		return s

	def save(self,file):
		file.write("%s\n" % self)


#For nodebox animation #################################################

def setup():
	global system,rdf
	width = 10.0
	height = 10.0
	zoom = 10.0
	size(width*zoom, (height+5)*zoom)
	gc = GC(zoom=zoom)
	system=System(step=0, nballs=90, cell=[width,height],
				   gc=gc,kT=1.0,MC=True)
	rdf = RDF(cell=[width,height],gc=gc)

def draw():
	global system,rdf
	colormode(HSB)
	stroke(0,0,0)
	fill(0,0,1)
	#時間0.1だけアニメーションを進める。
	#system.OneStep(0.1)
	for i in range(1000):
		system.OneStepMC()
	system.draw()
	#print system.step
	if system.step > 60000:
		rdf.accum(system.balls)
		rdf.draw()
	

#for slient run #########################################################
#コマンドライン引数は1番目がステップ数(省略不可)、2番目が出力ベース名、
#継続データは標準入力。ただし、dimenが指定された場合は初期化。

def usage():
	print "usage: %s [-a n|--atoms=n][-d t|--dt=t][-t x|--temp=x][-c x,y|--cell=x,y,z][-f|--flight] steps outputbase" % sys.argv[0]
	print "-a n|--atoms=n		Specify number of atoms."
	print "-f|--flight 		Output time of flight infos."
	print "-d t|--dt=t  		Step interval(default=1.0)."
	print "-t x|--temp=x		Specify initial temperature in kT."
	print "-c x,y|--cell=x,y	Specify initial cell size."
	sys.exit(2)

def main():
	#コマンドラインオプションの解析 ####################################
	args = sys.argv[1:len(sys.argv)]
	optlist, args = getopt.getopt(args, 'fd:t:c:a:', ['flight','dt=','temp=','cell=','atoms='])
	if len(args) < 2:
		usage()
	steps = int(args[0])
	basename = args[1]
	temp = 0.0
	cell = None
	natom = 0
	flight = False
	# 画面表示しないなら、Δtはできるだけ大きいほうが速い。
	deltatime = 1.0
	for o,a in optlist:
		if o in ("-t","--temp"):
			temp = float(a)
		if o in ("-a","--atoms"):
			natom = int(a)
		if o in ("-f","--flight"):
			flight = True
		if o in ("-d","--dt"):
			deltatime = float(a)
		if o in ("-c","--cell"):
			cell = a.split(",")
			for i in range(0,len(cell)):
				cell[i] = float(cell[i])
	#Initialize ########################################################
	velfile = None
	if flight:
		velfilename = "%s.fli.txt" % basename
		velfile = open(velfilename, "w")
	logfilename = "%s.log.txt" % basename
	logfile = open(logfilename,"w")
	system = None
	if cell is None:
		#cell is not defined; Continue from the last data.
		system = System(input=sys.stdin,logfile=logfile,
						velfile=velfile)
	else:
		if natom==0:
			usage()
		#Cell is defined. Start new run.
		system = System(nballs=natom,cell=cell,gc=None,logfile=logfile,
						velfile=velfile,kT=temp)

	#Main Loop #########################################################
	for step in range(0,steps):
		system.OneStep(deltatime)

	#Finish ############################################################
	outfilename = "%s.hd2.txt" % basename
	outfile = open(outfilename,"w")
	system.save(outfile)
	outfile.close()
	
#Uncomment one of them	
speed(10)  #for NodeBox
#main()     #for Commandline execution


