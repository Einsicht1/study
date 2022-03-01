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



## Closure Applications
## Decorators
## Decorator Application
## Decorators(Part 2)
## Decorator Application(Decorator class)
## Decorator Application(decorating class)
## Decorator Application(Dispatching)

