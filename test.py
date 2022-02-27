import sys
import time

def compare_using_equals(n):
    a = "hello world" * 200
    b = "hello world" * 200
    for i in range(n):
        if a == b:
            pass


def compare_using_interning(n):
    a = sys.intern("hello world" * 200)
    b = sys.intern("hello world" * 200)
    for i in range(n):
        if a is b:
            pass


start = time.perf_counter()
compare_using_equals(30000000)
end = time.perf_counter()
print(end-start)

start = time.perf_counter()
compare_using_interning(30000000)
end = time.perf_counter()
print(end-start)
