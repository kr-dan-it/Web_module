import threading
import time

def is_prime(n:int):
    if n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
        return True
    elif n == 2 or n == 3 or n == 5 or n == 7:
        return True
    else:
        return False

def find_primes_single_thread(start_single, end_single):
    primes = []
    for i in range(start_single, end_single):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            primes.append(i)
        elif i == 2 or i == 3 or i == 5 or i == 7:
            primes.append(i)
    return primes

def find_primes_multi_thread(start_multi, end_multi):
    primes = []
    for i in range(start_multi, end_multi):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            primes.append(i)
        elif i == 2 or i == 3 or i == 5 or i == 7:
            primes.append(i)
    print(primes)
    return primes

start_time = time.perf_counter()

print(find_primes_single_thread(13, 100))

end_time = time.perf_counter()
total_time = end_time - start_time
print(f"Total time: {total_time:8f} sec.")

# -----------------------------------------------------------------
print("-" * 30)
# -----------------------------------------------------------------

start = 13
end = 100
num_threads = 3

step = int((end - start) / num_threads)
start_step = int(start)
end_step = int(start_step + step)

start_time = time.perf_counter()
threads_io = []
for j in range(num_threads):
    thread = threading.Thread(target=find_primes_multi_thread, args=(start_step, end_step))
    start_step += step
    thread.start()
    threads_io.append(thread)
    start_step = end_step
    end_step = start_step + step

for thread in threads_io:
    thread.join()

end_time = time.perf_counter()
total_time = end_time - start_time
print(f"Total time: {total_time:8f} sec.")