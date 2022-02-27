## Reference Counting
- 파이썬은 객체가 참조될 때마다 ref_count를 +1한다.
- 0이 되면 python memory manager가 객체를 메모리에서 삭제함. (할당 해제)
```
import sys
my_var = [1,2,3]
sys.getrefcount(my_var)


```

## Garbage Collection
- 순환참조의 경우 ref_count는 절대 0이 되지 않는다.
- 이 경우 referece counting을 통해 python memory manager가 객체를 메모리에서 삭제할 수 없음. -> memory leak 발생
- GC는 순환참조인 것들을 메모리에서 지워주는 역할을 한다.
- gc는 기본적으로 turn on 상태다.
- gc 모듈을 사용해서 gc를 끄거나 수동실행 등 조작할 수 있다.
:

## Variable Re-assignment
- 변수에 값을 재할당하면 **새로운 주소**에 값이 할당된다.
- 따라서 변수 reference 값도 새로운 주소를 향하게 바뀐다.

``` 
>>> a = 10
>>> hex(id(a))
'0x7fb38df09490'
>>> a = 15
>>> hex(id(a))
'0x7fb38df09418'
```
#### fun fact
- in fact, the value inside the int objects, can never be changed
```
>>> a = 10
>>> b = 10
>>> hex(id(a))
'0x7fb38df09490'
>>> hex(id(b))
'0x7fb38df09490'
```

## object mutability
#### Immutable
- Numbers(int, float, Booleans, etc)
- strings
- Tuples
- Frozen Sets
- User-Defined Classes

#### Mutable
- Lists
- Sets
- Dictionaries

```
List에는 append해도 아이디가 바뀌지 않음! 
>>> my_list = [1,2,3]
>>> id(my_list)
4443124008
>>> my_list.append(4)
>>> my_list
[1, 2, 3, 4]
>>> id(my_list)
4443124008

+ 연산을 하면 새로운 리스트가 생기기 때문에 id값이 바뀜.
>>> my_list = [1,2,3]
>>> id(my_list)
4443244880
>>> my_list = my_list + [4]
>>> my_list
[1, 2, 3, 4]
>>> id(my_list)
4443244808

```
#### tuple
- immutable이지만 mutable을 원소로 가질 수 있다.


## Function args and Mutability
- Immutable objects are safe from unintended side-effects
- Mutable objects are not safe from unintended side-effects

## Shared refereces and mutability
<img width="756" alt="스크린샷 2022-02-08 오후 3 33 03" src="https://user-images.githubusercontent.com/92774768/152931422-baf1b63b-038b-420c-bb69-b15029938a34.png">
<img width="893" alt="스크린샷 2022-02-08 오후 3 33 16" src="https://user-images.githubusercontent.com/92774768/152931441-81731e7c-a12d-4aaa-b036-c4c146f5cd63.png">
<img width="929" alt="스크린샷 2022-02-08 오후 3 33 25" src="https://user-images.githubusercontent.com/92774768/152931449-cbd033fa-6392-4a50-8e3f-e52020609743.png">

```
>>> a = "hi"
>>> b = "hi"
>>> id(a) == id(b)
True


>>> a = [1,2,3]
>>> b = [1,2,3]
>>> id(a) == id(b)
False


>>> a = [1,2,3]
>>> b = a
>>> id(a) == id(b)
True
>>> b.append(100)
>>> a
[1, 2, 3, 100]
>>> b
[1, 2, 3, 100]

```


## Variable Equality
- Memory Address가 같냐, Object State가 같냐로 나눌 수 있다.
- Memory Address는 is연산
- Object State 는 ==연산으로 비교한다.
#### None Object
- None 은 실제 python memory manger가 관리하는 실제 object다.
- the memmory manager will always use a shared reference when assigning a variable to None
- 즉, a, b, c 값이 모두 None이면 이 세개의 주소값을 모두 같다. 
```
>>> a = 10
>>> b = a
>>> a is b
True
>>> a == b
True


>>> a = 1
>>> b = 1
>>> a == b
True
>>> a is b
True
>>> 
>>> 
>>> a = 500
>>> b = 500
>>> a == b
True
>>> a is b
False


>>> a = [1,2,3]
>>> b = [1,2,3]
>>> a is b
False
>>> a == b
True


>>> a = "a"
>>> b = "a"
>>> a is b
True
>>> a == b
True
>>> 
>>> 
>>> a = "asdfj23ks"
>>> b = "asdfj23ks"
>>> a is b
True
>>> a == b
True


>>> a = 10
>>> b = 10.0
>>> a is b
False
>>> a == b
True

```

## Everything is an object
- int, bool, string, list.....operators(+, -, ...), functions, class, types.. 등등 파이썬에서 모든것은 object다.
- this means they all have a memory address
- Any object can be assigned to a variable
- Any object can be passed to a function
- Any object can be returned from a function

## Python Optimizations: Interning
- a, b 에 10을 할당하고 a is b를 하면 True인데, 500을 할당하면 a is b는 False다. 이유는??!
#### interning: reusing objects on-demand
- at startup, python pre-loads(caches) a global list of integers in the range[-5, 256]
- Anytime an int is referenced in that range, python will use the cached version of that object
- this is optimization strategy - small integers show up often
```
>>> a = 10
>>> b = 10
>>> a is b
True
>>> a = 1000
>>> b = 1000
>>> a is b
False
```

## Python Optimizations: String Interning
- str형태가 아래 조건일 때(=identifiers처럼 생겼을 때) 파이썬은 interning을 한다
  - must start with _ or a letter
  - can only contain _, letters and numbers
  - 예시
    - "hello_world": interning O
    - "hello world": interning X

- interning은 speed, memory optimization을 위해 파이썬이 자동으로 한다.
- 수동으로도 할 수 있는데, `sys.intern("hello world") 형태로 가능하다.

#### 언제 수동으로 사용하면 좋을까?
- 아주 큰 str을 아주 반복적으로 다뤄야 할 때.
- str comparision을 아주 많이 할때.
- 정말 필요해서가 아니면 굳이 하지 말아라.

#### 예시
```
>>> a = "hello_world"
>>> b = "hello_world"
>>> a is b
True
>>> 
>>> a = "hello world"
>>> b = "hello world"
>>> a is b
False
```

#### sys.intern 예시
```
>>> import sys
>>> a = sys.intern("hello world")
>>> b = sys.intern("hello world")
>>> c = ("hello world")
>>> a is b
True
>>> b is c
False

```

#### sys.intern 시간 비교 예시
```
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


1.119146882
0.8879429629999998
```
