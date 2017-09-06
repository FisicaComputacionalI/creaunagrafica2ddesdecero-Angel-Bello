import numpy as np
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6]
x1 = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6]
y = [8,7.5,7.6,7.9,7.3,9]
y1 = [7,7.5,8,7.7,7.5,7.5,7.6,7.7,7.9,7.5,7.3,8,9]
plt.title("Calificaciones por semestre")
plt.xlabel("Semestres")
plt.ylabel("Promedio de Calificaciones")
plt.axis([0,6.1,7,9.1])
plt.plot(x,y,'ro',x1,y1,'r--')
plt.savefig('temp2.png')
plt.show()

