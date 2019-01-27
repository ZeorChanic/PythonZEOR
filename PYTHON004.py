import queue
import threading

def worker():
    while True:
        item = q.get()
        if item is None:
            break
        print(item)
        q.task_done()

q = queue.LifoQueue()
threads = []
num_worker_threads = 1
for i in range(num_worker_threads):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for item in 'trabajadores':
    q.put(item)

# block until all tasks are done
q.join()

# stop workers
for i in range(num_worker_threads):
    q.put(None)
for t in threads:
    t.join()