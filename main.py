import random
import datetime

jugadores = ['Danny','Alex','Lucho (hermano Alex)','Dami O.','Jorge','Lean L.','Catriel','Jorgito Copany',
              'Chalis','Pedro','Pipi (Lean L.)','Lean G.','Davichu (Lean G.)','David','Quimey (David)',
              'Miqueas','Dieguito (Lean G.)','Gonza','Melli (Alex )','Thiago (Alex)']

cantidadDeEquipos = 4

###############################################################

jugadoresRandom = random.sample(jugadores, len(jugadores))
def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts]
             for i in range(wanted_parts) ]

equiposRandom = split_list(jugadoresRandom, cantidadDeEquipos)

print(f'Fecha/Hora: {datetime.datetime.now()}')
for x in equiposRandom:
    print (x)
