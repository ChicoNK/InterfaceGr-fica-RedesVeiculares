import xml.etree.ElementTree as ET
from tkinter import*
import tkinter as tk


#indica qual arquivo xml usar e inicia a tree
tree = ET.parse('simulation7.xml')
root = tree.getroot()

window=Tk()
window.title("Simulation")
window.geometry("580x720")

label_gridsize = Label(window, text="GridSize")
label_gridsize.grid(row=0, column=0)
gridsize = Entry(window, width = 10 )
gridsize.grid(row=0, column=1)

label_cars = Label(window, text="Cars")
label_cars.grid(row=1, column=0)
cars = Entry(window, width = 10 )
cars.grid(row=1, column=1)

label_rsus = Label(window, text="RSUs")
label_rsus.grid(row=2, column=0)
rsus = Entry(window, width = 10 )
rsus.grid(row=2, column=1)

label_speed = Label(window, text="Speed")
label_speed.grid(row=3, column=0)
speed = Entry(window, width = 10 )
speed.grid(row=3, column=1)

label_simtime = Label(window, text="SimulationTime")
label_simtime.grid(row=4, column=0)
simtime = Entry(window, width = 10 )
simtime.grid(row=4, column=1)

label_probfail = Label(window, text="%Fail")
label_probfail.grid(row=5, column=0)
probfail = Entry(window, width = 10 )
probfail.grid(row=5, column=1)


def value():
    for gridsizeEX in root.iter('gridsize'):
        gridsizeEX.text = gridsize.get()
    
    for carsEX in root.iter('cars'):   
        carsEX.text = cars.get()
    
    for rsusEX in root.iter('rsus'):
        rsusEX.text = rsus.get()
        
    for speedEX in root.iter('speed'):
        speedEX.text = speed.get()
    
    for simtimeEX in root.iter('simtime'):
        simtimeEX.text = simtime.get()
    
    for probfailEX in root.iter('probfail'):
        probfailEX.text = probfail.get()
       
bt = Button(window, text="SAVE", bg="green", command=value)
bt.grid(row=6, column=0)
  
window.mainloop()

#sobrescreve no arquivo indicado
tree.write("simulation7.xml")

