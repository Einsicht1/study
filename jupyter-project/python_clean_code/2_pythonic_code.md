# Pythonic Code
- 프로그래밍에서 관용구(idiom)는 특정 작업을 수행하기 위해 코드를 작성하는 특별한 방법이다.
- 이 관용구를 따른 코드를 관용적이라 부르고 파이썬에선 pythonic하다고 한다.
- 일반적으로 관용구를 따랐을 때 성능이 좋고, 이해하기 쉽다.

## 인덱스와 슬라이스
- 인덱스로 접근하는 건 사실 slice를 전달하는 것과 같다. (아래 예시 참고)


```python
my_list = [i for i in range(10)]
print(my_list[1:9:2])
interval = slice(1,9,2)
print(my_list[interval])
```

    [1, 3, 5, 7]
    [1, 3, 5, 7]


### 자체 시퀀스 생성
- 위 예시처럼 indexing할 수 있는 이유는 리스트가 스퀀스 프로토콜(`__getitem__`, `__len__`)을 구현했기 때문이다.
- 자체 시퀀스를 만들려면 `__getitem__`을 구현해야 하는데, 이때 행위는 직접 하는 것 보단 리스트라면 리스트에 위임하는 게 좋다.
  - 아래 `__getitem__`예시에서 주석문처럼 하지 말라는 뜻인듯.


```python
class Items:
    def __init__(self, *values):
        self._values = list(values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, item):
        return self._values.__getitem__(item)
        # return self._values[item]

items = Items(1,2,3,4,5)
print(items[0])

```

    1


## Context Manager
- 파일을 열고 작업을 마쳤으면 파일 디스크립터 누수를 막기 위해 파일을 닫아야한다.
- 소켓을 열고 작업을 마쳤으면 소켓을 닫아야 한다.
- 이렇게 리소스 할당 해제작업을 꼭 해줘야 하는데, 이를 도와주는게 contextmanager다.
- 아래 첫 예시는 context manager없이 고생스럽게 구현한 버전, 두번째는 파이써닉한 버전(contextmanager)이다.
- context manager안쓰면 매번 finally를 쓰던가 해야한다.


```
# 1번 예시
filename = "some_file"
fd = open(filename)
try:
    do_something
finally:
    fd.close()

# 2번 예시
with open(filename) as fd:
    do_something
```

- context manager는 `__enter__` 메서드와 `__exit__`메서드로 구성된다.
- with문이 __enter__ 호출하고, 이 메서드가 반환하는 값을 as 이후의 변수에 할당한다.
- 사실 `__enter__`문이 뭔가를 반환하지 않아도 되긴 하다. 반환해도 as 뒤 변수에 할당하지 않아도 된다.
- with 블록이 끝나면 `__exit__`이 호출된다.
- context manager는 관심사를 분리하고 독립적으로 유지되어야 하는 코드를 분리하는 좋은 방법이다.
#### 예시1.
```
def stop_database():
    run("systemctl stop postgresql.service")

def start_databse():
    run("systemctl start postgresql.service")

class DBHandler:
    def __enter__(self):
        stop_database()
        return self

    def __exit__(self, exc_type, ex_value, ex_traceback):
        start_databse()

def db_backup():
    run("pg_dump database")

def main():
    with DBHandler():
        db_backup()

```

- 위 예시에서는 enter의 반환값이 사용되지 않는다.
- context manager 구현할 땐, 블록 안쪽에서 무엇이 필요한지 고렿애ㅑ 한다.
- 필수는 아니지만 `__enter__`에서 무언가를 반환하는 것이 좋다.(좋은 습관)
- `__exit__`의 param을 주목하자. 예외가 발생하지 않으면 모든 param은 None값이다.
- `__exit__`리턴값을 잘 생각해야 한다. 실수로 `__exit__`에서 True를 반환하지 않도록 주의해야 한다.
- True를 반환하면 잠재적으로 발생한 예외를 호출자에게 전파하지 않고 멈춘다는 것을 뜻한다(이해 안됨)

### Context Manager 구현
- `__exit__`, `__enter__` 프로토콜을 구현해서 context manager를 만들 수도 있고,
- contextlib 모듈을 사용해서 만들수도 있다.
#### contextlib.contextmanager
- 데코레이터 달면 해당 함수의 코드를 context manager로 변경한다.
- 함수는 generator여야 한다(yield)
- yield앞은 `__enter__`가 되고, 뒤는 `__exit__`이 된다.

```
import contextlib

@contextlib.contextmanager
def db_handler():
    stop_database()
    yield
    start_databse()

with db_handler():
    db_backup()
```
#### contextmanager 데코레이터 장점
- 함수 리펙토링이 쉽다.
- 특정 객체에 속하지 않은 contextmanager를 만들 때 좋다.
- 클래스 만들고 enter, exit메서드까지 만들면 책임이 커지고 코드도 복잡해지는 단점이 있기에,
다른 클래스와 독립된 context manager 만들경우엔 데코레이터 방법이 좋다.

#### contextlib.ContextDecorator
- with문 없이 쓸 수있다.
- 테코레이터와 함수가 서로를 모르는 특징이 있다. 독립적이어서 좋기도 하지만, with ~ as a: 식으로 `__enter__`의 리턴값을 변수에 적용할 수 없다.

```
import contextlib
class dbhandler_decorator(contextlib.ContextDecorator):
    def __enter__(self):
        stop_database()

    def __exit__(self, exc_type, exc_val, exc_tb):
        start_databse()

@dbhandler_decorator()
def offline_backup():
    run("pg_dump database")
```

#### contextlib.suppress
- 제공한 예외 중 하나가 발생할 경우 실패하지 않도록 한다.
- try/except 블록에서 코드를 실행하고 예외를 전달하거나 로그를 남기는 것은 비슷하지만 차이점은
suppress 메서드를 호출하면 로직에서 자체적으로 처리하고 있는 예외임을 명시한다는 점이다.

```
import contextlib

with contextlib.suppress(DataConversionExceiption):
    parse_data(input_json_or_dict)
```

## 프로퍼티, 속성과 객체 메서드의 다른 타입들
### 파이썬에서의 밑줄
> 💡 객체는 외부 호출 객체와 관련된 속성과 메서드만을 노출해야 한다.
>
> 즉 객체의 인터페이스로 공개하는 용도가 아니라면 모든 멤버에는 접두사로 하나의 밑줄을 사용하는 것이 좋다.
- 이유: 바깥에서 호출하지 않기에 안전하게 리팩토링 가능.
### 프로퍼티
- 객체관련 데이터는 일반적인 attribute쓰면 된다. (클래스 변수, 인스턴스 변수)
- 만약 객체 상태나 다른 속성의 값을 기반으로 어떤 계산된 값이 필요할 때가 있다.
- 이때는 property쓰면 된다!
- property는 객체의 어떤 속성에 대한 접근을 제어하려는 경우 사용한다.
- java에 getter, setter가 있다면 파이썬에서는 property
- propery는 cqrs법칙을 따르기도 좋은 법칙이다.
- @propery: 무언가에 답하기 위한 쿼리
- @(property_name).setter: 무언가를 하기 위한 쿼리

```
import re
EMAIL_FORMAT = re.compile(r"[^@]+@[^@]+[^@]+")

def is_valid_email(potentially_valid_email: str):
    return re.match(EMAIL_FORMAT, potentially_valid_email) is not None

class User:
    def __init__(self, username):
        self.username = username
        self._email = None

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        if not is_valid_email(new_email):
            raise ValueError("값 잘못됨~")
        self._email = new_email
```

> 💡 객체 모든 속성에 propery 적용할 필요는 없다. 대부분 인스턴스 변수, 클래스 변수로 충분하다.
> 속성 값을 가져오거나 수정할 때 특별한 로직이 필요한 경우에만 프로퍼티를 사용하자.

## 이터러블 객체
- iterable: `__iter__` 구현한 객체
- iterater: `__next__` 구현한 객체

#### 객체를 반복할 수 있는지 파이썬이 확인하는 방법
- 객체가 `__next__`나 `__iter__` 중 하나를 가졌는지 확인
- 객체가 스퀀스고 `__len__` or `__getitem__`를 모두 가졌는지 확인
### 이터러블 객체 만들기
- 객체를 반복하려고 하면 파이썬은 해당 객체의 `__iter__()`함수 호출
- for loop 원리: StopIteration발생할 때까지 `__next__()` 호출
### 시퀀스 만들기
- 반복할 때 `__iter__()`를 먼저 찾고 없으면 `__getitem__`을 찾는다.
- 시퀀스는 `__len__`과 `__getitem__`을 구현하고, 인덱스 0부터 한 번에 하나씩 가져올 수 있어야 한다.
- 시퀀스는 n번쨰 요소 얻기에는 O(1)로 빠르다. 다만 모든 것을 한 번에 메모리에 올려야 하기에 메모리는 많이 잡는다.
## 컨테이너 객체
- `_contains__` 메서드 구현한 객체. 일반적으로 Boolean값을 반환함 (in 연산)
## 객체의 동적인 속성
- `<myobject>.<myattribute>` 을 실행하면 `__getattribute__`가 실행된다.
- 객체에 찾고 있는 속성이 없을 경우 `<myattribute>`이름을 파라미터로 전달하여 `__getattr__`라는 추가 메서드가 호출된다.
- 이걸 통해 반환 값을 제어할 수 있고, 새로운 속성도 만들 수 있다. 아래 예시를 보자.


```python
class DynamicAttributes:
    def __init__(self, attribute):
        self.attribute = attribute

    def __getattr__(self, item):
        if item.startswith("fallback_"):
            name = item.replace("fallback_", "banana")
            return f"[fallback resolved], {name}"
        raise AttributeError(f"{self.__class__.__name__}에는 {item}속성이 없음")

dyn = DynamicAttributes("value")
print("dyn:", dyn.attribute)

print("dyn.fallback_test", dyn.fallback_test)

dyn.__dict__["fallback_new"] = "new value"
print(dyn.fallback_new)

print(getattr(dyn, "asdfasdf", "defalut"))
```

    dyn: value
    dyn.fallback_test [fallback resolved], bananatest
    new value
    defalut


> 💡 `_getattr__`같은 동적 메서드를 구현할 땐 AttributeError를 발생시켜야 함을 주의하자.

## Callable 객체
- 프로토콜: `__call__`구현.
- 함수처럼 호출할 수 있는 callable 객체는 매우 편리하다.
- 객체이기에 데이터를 저장할 수 있기 때문.
- 아래 예시 참고.(호출 횟수 저장 가능)


```python
from collections import defaultdict

class CallCount:

    def __init__(self):
        self._counts = defaultdict(int)

    def __call__(self, item, *args, **kwargs):
        self._counts[item] += 1
        return self._counts[item]

cc = CallCount()
print(cc(1))
print(cc(2))
print(cc(5))
print(cc(5))
print(cc(5))
```

    1
    1
    1
    2
    3


## 매직 메서드 요약
## 파이썬에서 유의할 점

### 변경 가능한(mutable) 파라미터의 기본값
- 런타임시 함수 param의 default value가 생성된다. 이후엔 계속 똑같은 메모리를 참조하게 되 문제가 된다.
- mutable을 함수 param 디폴트 값으로 사용하지 말자(의도한 게 아니라면)
### 내장(built-in)타입 확장
- C언어로 작성된 내장 클래스(예: dict, list, str)는 상속하지 않는걸 추천
- 왜냐면 사용자가 오버라이드한 코드를 호출하지 않기 때문에 에러 발생하기가 쉽다.
- dict, list 등 내장 타입을  확장할 땐 collections.UserDict, UserList 등등 상속받아서 사용해라.


## 요약


```python

```
