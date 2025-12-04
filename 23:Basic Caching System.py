# The Challenge: Write a function that "caches" the results of another slow function. 
# For example, create a slow function fibonacci(n). 
# The caching function should store the result for n, 
# so if it's called again with the same n, 
# it returns the stored result instantly instead of recalculating.

# Step 1: Create a "Slow" Function

"""
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
# print(fibonacci(10))
"""

# Step 2: The Caching Logic (The "Memoization" Wrapper)

""""
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
# print(fibonacci(10))

cache = {}

def memoized_fibonacci(n):
    if n in cache:
        return cache[n]
    else:
        result = fibonacci(n)
        cache[n] = result
        return result
    
# print(memoized_fibonacci(10))
# print(cache)
"""

# Step 3: Comparing the Performance

"""
import time

cache = {}

def memoized_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in cache:
        return cache[n]
    
    result = memoized_fibonacci(n-2) + memoized_fibonacci(n-1)
    cache[n] = result
    return result
    
# print(memoized_fibonacci(10))
# print(cache)

start_time = time.time()

print((memoized_fibonacci(35)))

end_time = time.time()

start_time_memoized_1 = time.time()

print((memoized_fibonacci(35)))

end_time_memoized_1 = time.time()

start_time_memoized_2 = time.time()

print((memoized_fibonacci(35)))

end_time_memoized_2 = time.time()

start_time_memoized_alt = time.time()

print((memoized_fibonacci(30)))

end_time_memoized_alt = time.time()

elapsed_time = end_time - start_time
print(f"Elapsed Time: {elapsed_time} seconds")

elapsed_time_memoized_1 = end_time_memoized_1 - start_time_memoized_1
print(f"Elapsed Time: {elapsed_time_memoized_1} seconds")

elapsed_time_memoized_2 = end_time_memoized_2 - start_time_memoized_2
print(f"Elapsed Time: {elapsed_time_memoized_2} seconds")

elapsed_time_memoized_alt = end_time_memoized_alt - start_time_memoized_alt
print(f"Elapsed Time: {elapsed_time_memoized_alt} seconds")
"""

# Step 4: The Elegant Solution - Decorators (Advanced)

cache = {}

def memoized_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in cache:
        return cache[n]
    
    result = memoized_fibonacci(n-2) + memoized_fibonacci(n-1)
    cache[n] = result
    return result

def memoized_decorator(func):
    cache = {}

    def wrapper(n):
        if n in cache:
            print(f"Cache hit for {n}!")
            return cache[n]
        
        print(f"Cache miss for {n}. Calculating...")
        result = func(n)
        cache[n] = result
        return result
    
    return wrapper

@memoized_decorator
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("First call:")
print(fibonacci(10)) 

print("\n" + "="*20 + "\n")

print("Second call:")
print(fibonacci(10))