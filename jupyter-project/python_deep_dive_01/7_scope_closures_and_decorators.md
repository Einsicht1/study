## Global and Local Scopes
Scopes and Namespace

### Global scope
- The global scope is essntially the module sccope
- There is no concept of a truly global scope in Python
- the only exception to ths are some of the built-in globally available objects, such as
  - True, False, None, dict, print
    <img alt="스크린샷 2022-02-27 오후 2 35 12" height="500" src="https://user-images.githubusercontent.com/60768642/155869652-cd86498d-1d04-46c7-ba4b-557cf8347d95.png" width="500"/>

#### example
<img width="500" alt="스크린샷 2022-02-27 오후 2 39 12" src="https://user-images.githubusercontent.com/60768642/155869737-69cab801-400a-42a6-b428-6e77233b3e3b.png" height="500">


### Local Scope
- Vairables defined inside a function are not created unitl the function is called
- Every time the function is called, a new scoep is created
  - variables defined inside the function are assigned to that scope
- The actual object the variable reference could be different each time the function is called
- this is why recursion works

#### example
- compile time에는 a,b,c가 my_func의 local variable이 될 것을 안다. 실제 scope이 생긴건 아니다.
- runtime(함수가 실행될 때)에 실제 scope이 생긴다. 함수 실행이 끝나면 scope은 사라진다.
- 새로운 함수가 실행되면 새로운 scope이 생긴다.
  <img alt="스크린샷 2022-02-27 오후 2 44 47" height="500" src="https://user-images.githubusercontent.com/60768642/155869883-d7cea75b-7f82-4a78-bbdb-e1bfdc961401.png" width="500"/>

### Nested Scopes
- local -> module -> built-in scope 순서로 찾아간다.
  <img alt="스크린샷 2022-02-27 오후 2 47 38" height="500" src="https://user-images.githubusercontent.com/60768642/155869953-4e4f2a74-2e65-4653-99b3-3610a0c1bee4.png" width="500"/>

#### example
<img width="500" alt="스크린샷 2022-02-27 오후 2 50 45" src="https://user-images.githubusercontent.com/60768642/155870035-9fb711c9-c9d2-4935-80d4-0fd81236a197.png" height="500">

### Accessing the global scope from a local scope
global keyword를 사용해서 local scope에서 global scope 변수에 접근할 수 있다.
```python
a = 0

def my_func():
    a = 100
    print(a)

my_func()

print(a)


100
0
```

```python
a = 0

def my_func():
    global a
    a = 100
    print(a)

my_func()

print(a)

100
100
```

### global and Local scoping
<img width="500" alt="스크린샷 2022-02-27 오후 3 00 55" src="https://user-images.githubusercontent.com/60768642/155870319-2d77928a-95df-4660-9f8b-6a3e949180fc.png" height="500">

- 아래 코드는 run-time error 가 난다.
```
a = 0

def my_func():
    print(a)
    a = 100

my_func()


UnboundLocalError: local variable 'a' referenced before assignment
```

## Nonlocal Scopes
### Inner functions
<img width="500" alt="스크린샷 2022-02-27 오후 3 06 25" src="https://user-images.githubusercontent.com/60768642/155870480-6bf29df8-5579-430f-863f-d2ec6e1e96ee.png" height="500">

### Referencing variables from the enclosing scope
<img width="1504" alt="스크린샷 2022-02-27 오후 3 08 21" src="https://user-images.githubusercontent.com/60768642/155870543-6f538db6-ece0-4044-b277-d36a457fa47c.png">
<img width="500" alt="스크린샷 2022-02-27 오후 3 09 04" src="https://user-images.githubusercontent.com/60768642/155870560-5ee7228a-0492-4224-8380-0e9a1c664111.png" height="500">

### modifying global variables
<img width="500" alt="스크린샷 2022-02-27 오후 3 10 31" src="https://user-images.githubusercontent.com/60768642/155870597-79ba7c68-0c72-4234-ab2a-af2456b2e9cb.png" height="500">

### modifying nonlocal variables
- 아래 코드를 보자
- inner 에서 변경시킨 x는 inner의 local이기 때문에, outer 변수에 영향을 안준다.
```python
def outer_func():
    x = "hello"
    def inner_func():
        x = "world"
    inner_func()
    print(x)


outer_func()

hello
```

- outer 변수(nonlocal)을 inner에서 바꾸려면 아래처럼 nonlocal을 선언하면 된다
```python

def outer_func():
    x = "hello"

    def inner_func():
        nonlocal x
        x = "world"
    inner_func()
    print(x)


outer_func()

world

```
<img width="600" alt="스크린샷 2022-02-27 오후 3 37 47" src="https://user-images.githubusercontent.com/60768642/155871338-f9b37451-29e7-48cf-becc-3cfa765742db.png" height="500">



<img width="600" alt="스크린샷 2022-02-27 오후 3 38 06" src="https://user-images.githubusercontent.com/60768642/155871350-c0e205e9-731d-47c8-8f6c-36feef01323b.png" height="500">


## Closures
<img width="1655" alt="asdf" src="https://user-images.githubusercontent.com/60768642/156152511-ac818eb8-484f-43bd-bd9c-8ee34e880e42.png">

> inner encloses its free variable

<img width="1543" alt="스크린샷 2022-03-01 오후 7 34 04" src="https://user-images.githubusercontent.com/60768642/156153280-5746e411-d407-435b-9de1-10ea0613c824.png">

<img width="1221" alt="스크린샷 2022-03-01 오후 7 37 56" src="https://user-images.githubusercontent.com/60768642/156153956-e3673cbf-6a0c-4976-832c-7f3c09eac665.png">

<img width="1219" alt="스크린샷 2022-03-01 오후 7 40 32" src="https://user-images.githubusercontent.com/60768642/156154336-d27ca427-b840-44ab-8045-f73f97bae587.png">

<img width="1197" alt="스크린샷 2022-03-01 오후 7 50 10" src="https://user-images.githubusercontent.com/60768642/156155753-5997e10b-bae6-4eda-a5a0-d4d5d180b009.png">

<img width="1085" alt="스크린샷 2022-03-01 오후 7 55 47" src="https://user-images.githubusercontent.com/60768642/156156582-44ba65aa-ffa2-4821-a1e5-0f33a0bca6dc.png">

<img width="1167" alt="스크린샷 2022-03-01 오후 7 55 56" src="https://user-images.githubusercontent.com/60768642/156156604-9a42a743-a37c-4b5b-b076-7866ca1a1977.png">

<img width="1144" alt="스크린샷 2022-03-01 오후 7 56 07" src="https://user-images.githubusercontent.com/60768642/156156634-2a96c120-4dfb-48f1-abbc-d3b40974ca9a.png">

<img width="937" alt="스크린샷 2022-03-01 오후 8 04 10" src="https://user-images.githubusercontent.com/60768642/156157890-fa70588f-5e9f-4860-a337-b8d8c89cdd25.png">

<img width="1183" alt="스크린샷 2022-03-01 오후 8 04 18" src="https://user-images.githubusercontent.com/60768642/156157911-060b1226-6f7d-43c1-baca-d35e931d8088.png">

<img width="1027" alt="스크린샷 2022-03-01 오후 8 04 25" src="https://user-images.githubusercontent.com/60768642/156157924-59bbd11c-2609-41c5-9b49-62a3c04ac72f.png">


## Closure Applications 1


```python
class Averager:
    def __init__(self):
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total / count
```

위 코드를 closure로 구현해보자.


```python
def averager():
    numbers = []
    def add(number):
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        return total / count
    return add

a = averager()
a(10)
a(20)
print(a(30))
b = averager()
b(10)
b(20)
print(b(30))
print(a.__closure__)
print(b.__closure__)
```

    20.0
    20.0
    (<cell at 0x1122d1370: list object at 0x112aae540>,)
    (<cell at 0x1122d1190: list object at 0x112aacc00>,)


위 코드를 아래처럼 개선해보자.


```python
def averager():
    total = 0
    count = 0
    def add(number):
        nonlocal total
        nonlocal count
        total = total + number
        count = count + 1
        return total / count
    return add

a = averager()
a(10)
a(20)
print(a(30))
print(a.__closure__)
print(a.__code__.co_freevars)
```

    20.0
    (<cell at 0x1122150a0: int object at 0x1046f6970>, <cell at 0x1122157c0: int object at 0x1047250d0>)
    ('count', 'total')



```python
from time import perf_counter
class Timer:
    def __init__(self):
        self.start = perf_counter()

    def __call__(self, *args, **kwargs):
        return perf_counter() - self.start

t1 = Timer()
print(t1())
print(t1())
```

    1.2999999967178155e-05
    4.93750000032378e-05



```python
# 위 코드를 clousre로 만들어보자.

from time import perf_counter
def timer():
    start = perf_counter()
    def poll():
        return perf_counter() - start
    return poll

t2 = timer()
print(t2())
print(t2())
```

    1.9584000028771698e-05
    0.00029316699999526463


## Closure Applications 2


## Decorators

<img width="1584" alt="스크린샷 2022-03-06 오후 5 34 51" src="https://user-images.githubusercontent.com/60768642/156915485-aa94193d-67d6-4d9a-8bf8-7a1723a13974.png">

#### 데코레이터는?
- 함수를 인자로 받는다.
- closure를 리턴한다.
- 리턴된 closure는 대개 `*args`,  `**kwargs`와 같은 파람을 받는다.
- inner function에서 뭔가를 실행한다.
- inner function의 파람을 활용해 인자로 받은 함수를 실행한다.
- 인자로 받은 함수가 리턴하는 값을 리턴한다.

<img alt="스크린샷 2022-03-06 오후 5 34 33" src="https://user-images.githubusercontent.com/60768642/156915475-613bc543-8ba2-479e-8030-d6fa36729e05.png" width="1025"/>

#### `@` symbol
- `@`은 syntatic sugar일 뿐이다.
- 아래 두 코드는 같다.


```python
# 1번 경우
def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('{0} was called {1} times'.format(fn.__name__, count))
        return fn(*args, **kwargs)
    return inner

def add(a, b):
    return a + b

add = counter(add)
```


```python
 # 2번 경우
def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        return fn(*args, **kwargs)
    return inner

@counter
def add(a, b):
    return a + b


```

#### Introspecting Decorated Functions
- decorated된 함수는 더이상 그 함수 자체가 아니다.
- decorated된 함수는 결국 inner func다.
- 즉 원래 함수의 metadata가 전부 사라진다.
- 아래 코드를 보면 add함수에 help를 쳤을 때 inner의 docstring이 나오는 것을 볼 수 있다. signature도 전부 바뀐다.


```python
def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        """this if inner's docstring"""
        nonlocal count
        count += 1
        return fn(*args, **kwargs)
    return inner

@counter
def add(a, b):
    """ this is add's docstring"""
    return a + b

print(help(add))
```

    Help on function inner in module __main__:
    
    inner(*args, **kwargs)
        this if inner's docstring
    
    None


#### 야매 해결법
- 위 문제를 고치기 위해 아래처럼 할 수 있다.
- 하지만 아래코드는 함수 이름과 주석만 다룰 뿐, 함수의 signature가 바뀌는 문제를 해결하지 못한다.
- 귀찮은 방법이기도 하다.


```python
def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        """this if inner's docstring"""
        nonlocal count
        count += 1
        return fn(*args, **kwargs)
    inner.__name__ = fn.__name__
    inner.__doc__ = fn.__doc__
    return inner
```

#### 제대로된 해결법. functools.wraps
- 항상 wraps를 써야하는 것은 아니지만, 디버깅에 유용하니 웬만하면 달아주는게 좋다.
<img width="1331" alt="스크린샷 2022-03-06 오후 5 48 47" src="https://user-images.githubusercontent.com/60768642/156915858-ea5b1b7f-2ee9-4953-aaf1-b09cd52d034a.png">



## Decorator Application
## Decorators(Part 2)
## Decorator Application(Decorator class)
## Decorator Application(decorating class)
## Decorator Application(Dispatching)


