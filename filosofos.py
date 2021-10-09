import time
from threading import Thread, Lock
import threading
mutex = Lock()

tenedores = [1,1,1]

def filosofo():
    tenedor = []
    hilo_actual = threading.current_thread().getName()
    while True:
        print(f'Filosofo {hilo_actual} esperando...')
        time.sleep(2)
        mutex.acquire()
        if len(tenedores) != 0:
            print(f'Filosofo {hilo_actual} toma 2 tenedores')
            time.sleep(2)
            tenedor.append(tenedores.pop())
            tenedor.append(tenedores.pop())
            
        try:
            # print(f'Tenedores del filosofo {hilo_actual}: {len(tenedor)}')
            if len(tenedor)==2:
                print(f'Filosofo {hilo_actual} esta comiendo...')   
                time.sleep(3) 
                tenedores.append(tenedor.pop())
                tenedores.append(tenedor.pop())
        finally:
            print(f'Filosofo {hilo_actual} termino de comer...')         
            time.sleep(2)
            mutex.release()
            break




def main ():
    filosofo1 = Thread(name='1',target=filosofo, args=())
    filosofo2 = Thread(name='2',target=filosofo, args=())
    filosofo3 = Thread(name='3',target=filosofo, args=())
    filosofo4 = Thread(name='4',target=filosofo, args=())
    filosofo5 = Thread(name='5',target=filosofo, args=())
    

    filosofo1.start()
    filosofo2.start()
    filosofo3.start()
    filosofo4.start()
    filosofo5.start()
    # filosofo3.start()

main()