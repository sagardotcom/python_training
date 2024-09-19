"""
multithreading: We can split one process into multiple pieces and
run all pieces in parallel. Each piece is called thread

In python, multithreading is NOT parallel

Still we can use multithreading, because
if one thread is waiting for some resource
then during that waiting time it will another thread
"""

print("WITHOUT using multithreading")
print("-"*20)
# ------------

import time

start_time = time.time()


def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)


def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)


L= [10, 20, 30, 40]
my_square_function(L)
my_cube_function(L)

end_time = time.time()
print("Total Time Taken:", end_time-start_time)

print("#"*40, end="\n\n")
#################################

print("USING multithreading")
print("-"*20)
# ------------

import time

start_time = time.time()


def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)


def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)


L= [10, 20, 30, 40]

from threading import Thread

thread_my_square_function = Thread(target=my_square_function, args=(L,))
thread_my_cube_function = Thread(target=my_cube_function, args=(L, ))

thread_my_square_function.start()
thread_my_cube_function.start()

# start() method will just start then thread and proceed to next line,
# start() will not wait for function execution

thread_my_square_function.join()
thread_my_cube_function.join()

# join() will wait till thread completed execution

end_time = time.time()
print("Total Time Taken:", end_time-start_time)

print("#"*40, end="\n\n")
#################################


print("WITH DELAY: WITHOUT using multithreading")
print("-"*20)
# ------------

import time

start_time = time.time()


def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)
        time.sleep(0.1)


def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)
        time.sleep(0.1)


L= [10, 20, 30, 40]
my_square_function(L)
my_cube_function(L)

end_time = time.time()
print("Total Time Taken:", end_time-start_time)

print("#"*40, end="\n\n")
#################################

print("WITH DELAY: USING multithreading")
print("-"*20)
# ------------

import time

start_time = time.time()


def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)
        time.sleep(0.1)


def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)
        time.sleep(0.1)


L= [10, 20, 30, 40]

from threading import Thread

thread_my_square_function = Thread(target=my_square_function, args=(L,))
thread_my_cube_function = Thread(target=my_cube_function, args=(L, ))

thread_my_square_function.start()
thread_my_cube_function.start()

# start() method will just start then thread and proceed to next line,
# start() will not wait for function execution

thread_my_square_function.join()
thread_my_cube_function.join()

# join() will wait till thread completed execution

end_time = time.time()
print("Total Time Taken:", end_time-start_time)

print("#"*40, end="\n\n")
#################################