## Argument vs Parameter

### Semantics
#### parameter
```
함수 정의 시 parameter라고 부름
def my_func(a, b):
    pass
```
#### arguments
- 함수 호출 시 arguments라고 부름
```
x = 1
y = "a"
my_func(x, y)
```
- 이때 x, y는 refernce 함수에 reference(주소값)을 넘긴다.


## Positional and Keyword Arguments
- 함수 정의 혹은 호출 시 kwargs가 오면, 그 뒤는 무조건 kwargs여야한다.
  - def my_func(a=1, b, c) 불가능!
  - my_func(a=1, 2,3) 불가능!

## Unpacking Iterables
#### 튜플 정의 방법
- 괄호 ()를 사용해도 튜플이지만, 아래처럼 해도 튜플이다.


```python
a = 1,2,3
print(a)
print(type(a))
```

    (1, 2, 3)
    <class 'tuple'>


#### Packed Values
- bundled되있는 values를 일컫는다.
- list, tuple, str, set, dict 모두 packed values다.
- in fact, any iterable can be considered a packed value

#### Unpacking Packed Values


```python
a,b,c = [1,2,3]
print(a,b,c)
a,b,c = 10, 20, "hello"
print(a,b,c)
a,b,c = "XYZ"
print(a,b,c)

```

    1 2 3
    10 20 hello
    X Y Z
    1
    2
    3
    4
    5


## Extended Unpacking
#### The use case for *
- 아래 3가지 경우는 모두 a에 1을, b에 나머지를 할당한다.
```
l = [1,2,3,4,5,6]
1)
  a = l[0]
  b = [1:]
2)
  a, b = l[0], l[1:]
3)
  a, *b = l
```

- 3)처럼 *을 사용하면, l이 list가 아니어도 b의 타입은 무조건 list가 된다.
- 아래 같은 것도 가능하다.


```python
a, *b, c = [1,2,3,4,5]
print(a,b,c)

a = [1,2,3]
b = [4,5,6]
c = [*a, *b]
print(c)

a = {"p": 1, "y": 2, "z": 10}
b = {"t": 3, "h": 4, "z": 50}
c = {**a, **b}
print(c) # b의 z가 a의 z를 overwrote함을 주의하라.

d1 = {"a": 1, "b": 2}
print({"a": 10, **d1})

a, *b, (c, *d) = [1,2,3, "python"]
print(a,b,c,d)
```

    1 [2, 3, 4] 5
    [1, 2, 3, 4, 5, 6]
    {'p': 1, 'y': 2, 'z': 50, 't': 3, 'h': 4}
    {'a': 1, 'b': 2}
    1 [2, 3] p ['y', 't', 'h', 'o', 'n']


#### *는 좌변에 딱 한번만 사용 가능하다!
a, *b, *c = [1,2,3,4,5] 는 에러!
#### **는 좌변에 사용 불가하다.

## *args
- *args와 *는 다르다.
- *는 positional args를 개수 상관없이 받겠다는 것이고,
- **`*` indicates the "end" of positional arguments**
- 아래처럼 정의하면 positional을 전혀 받지 않겠다는 뜻이 된다. b는 kwargs가 된다.
```
def my_func(*, b):
    pass
```

## Parameter defaults: Beware
- 함수 param에 default로 준 값은 runtime에 생성된다.
- 이는 매우 중요한 사실이다. 아래 예시를 보자.
- runtime에 datetime.now()가 생성됐기 때문에 3초 sleep이후에도 여전히 같은 값이다.


```python
from datetime import datetime
from time import sleep
def main(t=datetime.now()):
    print(t)

main()
sleep(3)
main()

```

    2022-02-11 17:55:09.028305
    2022-02-11 17:55:09.028305


- 위 문제를 해결하려면 항상 함수 호출 시 값을 넘겨주거나, 아래 예시처럼 함수 안에서 값을 정의해야한다.
- 보통은 default value를 None으로 정의하는게 국룰이다.


```python
from datetime import datetime
from time import sleep
def main(t=None):
    t = t or datetime.now()
    print(t)

main()
sleep(3)
main()
```

    2022-02-11 17:57:52.713788
    2022-02-11 17:57:55.719404


### default value: mutable object
- defalut value에 list와 같은 mutable을 쓸땐 정말 조심하자.
- 아래처럼 원치 않는 결과가 나올 수도 있다.
- runtime시 li=[]가 생성되고, 이후 계속 li는 (args로 주어지지 않는이상) 계속 같은 메모리를 참조한다.


```python
def main(a, li=[]):
    li.append(a)
    return li

res1 = main(1)
print(res1)
res2 = main(3)
print(res2)
print(res1)
print(res1 is res2)

```

    [1]
    [1, 3]
    [1, 3]
    True



```python
# 해결책
def main(a, li=None):
    li = li or []
    li.append(a)
    return li

```


```python
# 의도적으로 함수 param에 mutable을 줄 때도 있다.
# cache를 반복적으로 쓰려면 아래처럼 해야함.
def factorial(n, cache={}):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print("calculate")
        res = n * factorial(n-1)
        cache[n] = res
        return res

res = factorial(3)
print(res)
res = factorial(3)
print(res)
```

    calculate
    calculate
    calculate
    6
    6

