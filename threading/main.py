import time
import multiprocessing
import requests
import uuid



def do_something():
    print('Process start')
    response = requests.get('https://picsum.photos/200/300')
    with open(f'image_{uuid.uuid4()}.png', 'wb') as file:
        file.write(response.content)
    print('Process End')


t1 = time.time()

threads = []

if __name__ == '__main__':
    for i in range(20):
        p1 = multiprocessing.Process(target=do_something)
        p1.start()
        threads.append(p1)

    for i in threads:
        i.join()


t2 = time.time()

print(t2 - t1)