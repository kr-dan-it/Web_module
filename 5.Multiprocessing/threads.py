import threading
import time
import random
import datetime

# def print_numbers():
#     for i in range(1, 6):
#         print(i)
#
# thread = threading.Thread(target=print_numbers)
# thread.start()
#
# thread.join()

# shared_variable = 0
# lock = threading.Lock()
#
#
# def increment():
#     global shared_variable
#     # lock.acquire()
#     # shared_variable += 1
#     # lock.release() # same as "with lock:"
#     with lock:
#         shared_variable += 1
#
#
# list_threads = []
#
#
# for _ in range(5):
#     thread = threading.Thread(target=increment)
#     thread.start()
#     list_threads.append(thread)
#
#
# for thread in list_threads:
#     thread.join()
#
#
# print(shared_variable)

# event = threading.Event()
#
# # event.set()
# # event.wait()
# # event.clear()
#
# def wait_for_event():
#     print("Wait for event...")
#     event.wait()
#     print("Event happened")
#
# def set_event():
#     time.sleep(2)
#     print("Pre event happened")
#     event.set()
#
# thread1 = threading.Thread(target=wait_for_event)
# thread2 = threading.Thread(target=set_event)
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()


# semaphore = threading.Semaphore(value=2)
#
#
# def do_thread(thread_id):
#     print(f"Thread {thread_id}: Try to do something...")
#     with semaphore:
#         print(f"Thread {thread_id} start")
#         time.sleep(random.randint(1, 5))
#         print(f"Thread {thread_id} finished")
#
#
# threads = []
# for i in range(6):
#     thread = threading.Thread(target=do_thread, args=(i,))
#     thread.start()
#     threads.append(thread)
#
#
# for thread in threads:
#     thread.join()


# def task(name, duration):
#     print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Thread {name}: Start execution on {duration} sec.")
#     time.sleep(duration)
#     print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Thread {name}: End execution")
#
#
# thread1 = threading.Thread(target=task, args=("Installation", 3))
# thread2 = threading.Thread(target=task, args=("Request data", 1))
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()


# # Створіть два потоки. Один потік має вивести "Привіт!" 3 рази з інтервалом 0.5 секунди,
# # інший - "Бувай!" 2 рази з інтервалом 0.8 секунди.
# def say_word(word, number_of_times, interval):
#     for _ in range(number_of_times):
#         print(word)
#         time.sleep(interval)
#
#
# thread_1 = threading.Thread(target=say_word, args=("Hello!", 4, 1.5))
# thread_2 = threading.Thread(target=say_word, args=("Bye!", 6, 0.7))
#
#
# thread_1.start()
# thread_2.start()
#
#
# thread_1.join()
# thread_2.join()


# def fetch_url(url):
#     print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Start downloading data from {url}")
#     time.sleep(random.uniform(0.5, 2.5))
#     data = f"Data from {url}"
#     print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] End downloading data from {url}")
#
#     return data
#
#
# urls = [
#     "http://example.com/page1",
#     "http://example.com/page2",
#     "http://example.com/page3",
#     "http://example.com/page4",
# ]
#
#
# start_time = time.perf_counter()
#
#
# threads_io = []
# for url in urls:
#     thread = threading.Thread(target=fetch_url, args = (url,))
#     thread.start()
#     threads_io.append(thread)
#
#
# for thread in threads_io:
#     thread.join()
#
#
# end_time = time.perf_counter()
# print(f"Total execution time for threads: {end_time - start_time}")
#
#
# start_time = time.perf_counter()
#
#
# for url in urls:
#     fetch_url(url)
#
#
# end_time = time.perf_counter()
# print(f"Total execution time for iteration: {end_time - start_time}")


# # Імітуйте "завантаження" 5 файлів з різними випадковими затримками (від 0.1 до 1.0 секунди)
# # за допомогою потоків.
# # Виведіть повідомлення про початок та завершення завантаження кожного файлу.
#
#
# def download_file(name):
#     print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Start downloading data from {name}")
#     time.sleep(random.uniform(0.1, 1))
#     data = f"Data from {name}"
#     print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] End downloading data from {name}")
#     return data
#
#
# file_names = ["file.exe", "new.txt", "image.png", "video.mov", "music.mp3"]
#
#
# threads_io = []
# for file in file_names:
#     thread = threading.Thread(target=download_file, args = (file,))
#     thread.start()
#     threads_io.append(thread)
#
#
# for thread in threads_io:
#     thread.join()


# shared_variable = 0
# lock = threading.Lock()
#
#
# def increment_variable_safe():
#     global shared_variable
#     with lock:
#         current_value = shared_variable
#         time.sleep(0.01)
#         shared_variable = current_value + 1
#
#
# def increment_variable_unsafe():
#     global shared_variable
#     current_value = shared_variable
#     time.sleep(0.01)
#     shared_variable = current_value + 1
#
#
# num_increments = 1000
#
#
# thread_safe = []
# for i in range(num_increments):
#     thread = threading.Thread(target=increment_variable_safe)
#     thread.start()
#     thread_safe.append(thread)
#
#
# for thread in thread_safe:
#     thread.join()
#
#
# print(f"After safe threads: {shared_variable}")
#
#
# # -------------------------------------------------------
#
#
# shared_variable = 0
# thread_unsafe = []
# for i in range(num_increments):
#     thread = threading.Thread(target=increment_variable_unsafe)
#     thread.start()
#     thread_unsafe.append(thread)
#
# for thread in thread_unsafe:
#     thread.join()
#
# print(f"After unsafe threads: {shared_variable}")