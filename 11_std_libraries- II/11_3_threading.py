from threading import *
from time import sleep


# class Hello(Thread):
#     def run(self):
#         for i in range(10):
#             print("Hello")
#             sleep(1)
#
#
# class Hi(Thread):
#     def run(self):
#         for i in range(10):
#             print("Hi")
#             sleep(1)
#
#
# t1 = Hello()
# t2 = Hi()
#
# t1.start()
# sleep(5)
# t2.start()

# def print_numbers():
#     for i in range(1, 6):
#         print(f"Thread 1: {i}")
#         sleep(1)
#
# def print_letters():
#     for letter in ["a", "b", "c"]:
#         print(f"Thread 2: {letter}")
#         sleep(1)
#
#
# thread1 = Thread(target=print_numbers)
# thread2 = Thread(target=print_letters)
#
#
# thread1.start()
# thread2.start()
#
#
# thread1.join()
# thread2.join()
#
# print("Program completed.")


#
# thread_data =local()
#
# def set_thread_name(name):
#     thread_data.name = name
#     print(f"Thread name set to: {thread_data.name}")
#
# def print_thread_name(name):
#     thread_data.name = name
#     print(f"Thread name: {thread_data.name}")
#
# # Create two threads
# thread1 =Thread(target=set_thread_name, args=("Thread 1",))
# thread2 =Thread(target=set_thread_name, args=("Thread 2",))
#
# # Start the threads
# thread1.start()
# thread2.start()
#
# # Wait for the threads to finish
# thread1.join()
# thread2.join()
#
# # Print thread names
# print_thread_name("Harshil")
#
# set_thread_name("Shubhika")

from logging import *

# logging.debug('Debugging information')
# logging.info('Informational message')
# logging.warning('Warning:config file %s not found', 'server.conf')
# logging.error('Error occurred')
# logging.critical('Critical error -- shutting down')

# logging.warning('U Better Watch out!')
#
#
# name = 'GFG'
# logging.error('%s raised an error', name)
#
# LOG_FORMAT = '{lineno} *** {name} *** {asctime} *** {message} '
# basicConfig(filename='logfile.log',  level=DEBUG , filemode='w' , style="{" , format=LOG_FORMAT)
#
# logger = getLogger('Harshil')
# logger.debug("This is debug")
# logger.info("This is info")
# logger.warning("This is warning")
# logger.error("This is error")
# logger.critical("This is critical")


