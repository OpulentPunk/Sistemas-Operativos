import threading
import time

#crea un semáforo con un contador inicial de 2

semaphore = threading.Semaphore(10)

def tarea(id):
	print(f"Cajero {id} intentando acceder a la base de datos")
	with semaphore:
		print(f"Cajero {id} ha entrado a la base de datos")
		time.sleep(2)
		print(f"Cajero {id} ha salido de la base de datos")
		
#crear múltiples hilos que ejecuten la función tarea		
		
threads = []
for i in range(5):
	thread = threading.Thread(target=tarea, args = (i, ))
	threads.append(thread)
	thread.start()
	
#esperar a que todos los hilos terminen

for thread in threads:
	thread.join()
