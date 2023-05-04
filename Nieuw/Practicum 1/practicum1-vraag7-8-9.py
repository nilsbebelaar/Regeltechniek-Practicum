"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""
import math as mth
import numpy as np
"""
Practicum Regetechniek van Daan Sijnja (20177747), Jeroen Vogelezang (20093179), Nils Bebelaar (20164882). Wij kunnen echt goed regelen.
"""
import matplotlib.pylab as plt 
import control


def find_doorschot(yrange, eind_waarde):
    doorschot = max(yrange) - eind_waarde
    index = yrange.tolist().index(max(yrange))
    return doorschot, index*((11.5)/len(yrange))

def static_error(y_range,eind_waarde):
    StatError = 0
    for i in range(5): 
        StatError = StatError +  eind_waarde-y_range[-i]
    return StatError/5

teller = np.array([18.0]) 
noemer = np.array([1.0, 1.2,36]) 
H = control.tf(teller,noemer)

print("Pole: ",H.pole())
print("Zero: ",H.zero())

K = 100
Sys1 = K*H
Sys2 = 1
Hclosed = control.feedback(Sys1,Sys2) 

print(Sys1)
print(Hclosed)

t_open, y_open = control.step_response(Sys1)  
t_closed, y_closed = control.step_response(Hclosed) 

d1, t1 = find_doorschot(y_open,50)
d2, t2 = find_doorschot(y_closed,1)

info_openlus = control.step_info(Sys1)
info_closed = control.step_info(Hclosed)

print(f'Doorschot Open Waard geschat: {round(d1,2)} T: {round(t1,2)} || Waarde Berekend {(info_openlus["Overshoot"]/100)*info_openlus["SteadyStateValue"]} T: {info_openlus["PeakTime"]} || Static Error  || SettleTime: {info_openlus["SettlingTime"]}' )
print("Static Error Open",static_error(y_open,50))

print(f'Doorschot Open Waard geschat: {round(d2,2)} T: {round(t2,2)} || Waarde Berekend {(info_closed["Overshoot"]/100)*info_closed["SteadyStateValue"]} T: {info_closed["PeakTime"]}  || SettleTime: {info_closed["SettlingTime"]}')
print("Static Error Closed",static_error(y_closed,1))


for k in info_openlus:
   print(f"{k}: {info_openlus[k]}")

for k in info_closed:
   print(f"{k}: {info_closed[k]}")
plt.plot(t_open,y_open, t_closed, y_closed)
plt.ylabel('Stap reponsie')
plt.xlabel('Tijd [s]')
plt.legend(["Open","Gesloten"])


plt.show()