import pyorbita
import cyorbita
import time
import csv
f = open('results.csv','w',encoding='utf8')
writer = csv.writer(f)
#Initialized planet for python
row = ['n_steps','python','cython','speedup']
writer.writerow(row)
time_span=600
for n_steps in [1000000,2000000,3000000,4000000,5000000,6000000]:
    earth = py_orbita.Planet()
    earth.x=100e3
    earth.y=300e3
    earth.z=300e3
    earth.vx=2e3
    earth.vy=29.87e3
    earth.vz=0.034e3
    earth.m=5.9736e24
    initTime=time.time()
    py_orbita.step_time(planet=earth,time_span=time_span,n_steps=n_steps)
    endTime=time.time()
    totalTimePy = endTime-initTime
    print("Tiempo en python",totalTimePy,"s")
    earth = cy_orbita.Planet()
    earth.x=100e3
    earth.y=300e3
    earth.z=300e3
    earth.vx=2e3
    earth.vy=29.87e3
    earth.vz=0.034e3
    earth.m=5.9736e24
    initTimeCy=time.time()
    cy_orbita.step_time(planet=earth,time_span=time_span,n_steps=n_steps)
    endTimeCy=time.time()
    totalTimeCy = endTimeCy-initTimeCy
    print("Tiempo en cython",totalTimeCy,"s")
    speedUp=totalTimePy/totalTimeCy
    print("SpeedUp",speedUp)
    row = [n_steps,totalTimePy,totalTimeCy,speedUp]
    writer.writerow(row)
f.close()