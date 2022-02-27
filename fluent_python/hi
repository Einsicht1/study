# 딕셔너리와 집합
- python에서 dict는 매우 중요하다 -> dict클래스는 상당히 최적화 되어있다.
- dict, set 뒤에는 hash table 엔진이 있다.
- hash table이 작동하는 방식을 알아야 dict, set을 최대로 활용할 수 있다.
- hashable?
  - 수명 주기 동안 결코 변하지 않는 해시값을 갖고 있다.(`__hash__()`메서드 필요)
  - 다른 객체와 비교할 수 있다. (`__eq__()`메서드 필요)
  - 동일하다고 판단되는 객체는 반드시 해시값이 동일해야 한다.
  - 원자적 불변형(str, byte, 수치형), frozenset are hashable
  - tuple은 들어 있는 모든 항목등리 hashble해야 hashable하다.

  - <img width="313" alt="스크린샷 2021-11-19 오후 5 52 19" src="https://user-images.githubusercontent.com/92774768/142593862-61da639f-54e7-4699-827b-27932771bf2a.png">
  
  - 사용자 정의 자료형은 기본적으로 hashable
    - 기본적으로 객체의 해시값은 id()를 이용해 구하기 때문.
    - 객체가 자신의 내부 상태를 평가해 `__eq__()`메서드를 직접 구현하는 경우 해시값 계산에 사용되는 속성이 모두 불변형일 때만 hashable

## dictionary
### how to make a dictionary
<img width="441" alt="스크린샷 2021-11-19 오후 5 58 32" src="https://user-images.githubusercontent.com/92774768/142594783-b475c10a-d557-4bec-bacb-090025228229.png">

### dict comprehension
<img width="505" alt="스크린샷 2021-11-19 오후 6 01 03" src="https://user-images.githubusercontent.com/92774768/142595156-d072c586-a206-4b63-95b9-7812c21f819c.png">

### setdefault, defalutdict, \__missing__()
- 검색할 때 키가 존재하지 않을 때 사용할 수 있는 방법들이다.
```
# 방법 1. 아무것도 안쓰고 if문으로 처리하는 제일 저수준(?) 방법
def countLetters(word):
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter

# setdefault사용
def countLetters(word):
    counter = {}
    for letter in word:
        counter.setdefault(letter, 0)
        counter[letter] += 1
    return counter



from collections import defaultdict
# defalutdict사용
def countLetters(word):
    counter = defaultdict(int)
    for letter in word:
        counter[letter] += 1
    return counter

```

> k in dict.keys()는 dict의 크기가 큰 경우에도 속도가 빠르다. keys()는 set와 비슷한 뷰를 반환함

#### collections.OrderedDict
- 키를 삽인한 순서대로 유지 -> iter순서 예측 가능
- popitem()메서드는 최근에 삽입한 항목 반환
- popitem(last=True)로 호출시 처음 삽입한 항목 반환
``` 
od = OrderedDict({1:2, 3:4})
od.popitem(last=False) 
(1,2) 반환

od = OrderedDict({1:2, 3:4})
od.popitem(last=True) 
(3,4) 반환

od = OrderedDict({1:2, 3:4})
od.popitem() 
(3,4) 반환
```

#### collections.Counter
- 문자열, 리스트 등의 요소수를 키별로 세어주는 기능.
 
<img width="519" alt="스크린샷 2021-11-19 오후 6 56 33" src="https://user-images.githubusercontent.com/92774768/142603367-067d44fe-91d2-4834-a7d7-4c89f75100f6.png">


Counter는 아래 코드의 역할을 대신 해준다고 볼 수 있다.
```  
def countLetters(word):
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter
```
### immutable mapping(dict요소 수정 못하도록 막는 방법)
- 기본적으로 dict는 가변형인데, MappingProxyType을 사용해 mappingproxy객체를 만들어 이를 방지할 수 있다.
- 
<img width="400" alt="스크린샷 2021-11-19 오후 7 07 30" src="https://user-images.githubusercontent.com/92774768/142604950-99bedada-bf86-4203-9c51-45995836bbb2.png">


## Set
- set는 비교적 최근에 python에 추가됨 -> 자주 사용되지 않음.
- frozen: set의 immutable 버전
- a | b : 합집합
- a & b : 교집합
- a - b : 차집합
- set 연산 잘 이용하면 실행시간 줄일 수 있고, 가독성 높일 수 있다.(loop, 조건절 없애서)

#### 예시
a와 b가 공유하는 요소를 찾기 위해서 set를 이용해보자.

방법 1.

<img width="272" alt="스크린샷 2021-11-19 오후 7 13 59" src="https://user-images.githubusercontent.com/92774768/142605806-206cbf76-7d2e-47cc-ac6f-c0a26c2bbf0e.png">

- 만약 set없이 연산하면 아래처럼 코드가 길어진다.
- 방법 2
``` 
a = {i for i in range(10)}
b = {i for i in range(5)}

cnt = 0
for i in b:
    if b in a:
        cnt += 1
 
```
방법 3.
``` 
found = len(set(needles) & set(haystack))

# 또 다른 방법
found = len(set(needles).intersection(haystack))
```
- 방법 3이 set를 만들어야 하는 추가 비용이 있지만, needles, haystack 둘 중 하나라도 이미 set이라면 방법 2보다는 빠르다.
- 10,000,000개 항목 가진 haystack안에서 1,000개 항목을 3 밀리초 안에 검색 가능하다.
- 빈집합을 만들 땐 set()로 해야한다. `{}`는 dict다.
- 속도면에서 {1,2,3} > set([1,2,3]) 이다. 
  - 후자는 집합명 검색, 리스트 생성, 리스트를 생성자에 전달해야 하므로 더 느리다. 
  - 전자는 BUILD_SET이라는 특수 바이트코드를 실행한다.
  - 디스어셈블러 함수 dis.dis()를 이용해 각 연산의 대한 바이트코드를 살펴보면, {1}이 set([1])보다 연산이 간단함을 볼 수 있다.
   
![스크린샷 2021-11-19 오후 11 56 46](https://user-images.githubusercontent.com/60768642/142643301-41cdb78e-ebb2-4713-aca7-fe31984b6dd3.png)

- frozenset은 리터럴 구문 없다. 항상 생성자를 호출해야한다. ex) `frozenset(range(10))`
- set comprehension도 있다. 

### set 연산
- &: 교집합
- |: 합집합
- -: 차집합
- : 여집합
#### Boolean 반환하는 연산
a in b: a가 b의 요소다. 
a <= b: a가 b의 부분집합이다.

#### set 메서드
- a.add(b): a에 b요소를 추가
- a.clear(): a의 모든 요소 제거
- a.copy(): a의 얕은 복사
- a.discard(b): a안에 b가 있으면 삭제
- a.\__iter__(): a의 반복자 반환
- a.\__len__(): len(a)
- a.pop(): a에서 항목 하나 제거 후  반환. 공집합이면 KeyError
- a.remove(e): a에서 e제거. 없으면 KeyError

### dict, set의 내부 구조
#### 성능 실험
- in으로 특정 요소가 set 혹은 list안에 있는지 확인할 때 걸리는 시간
- set > dict > list
- dict, set 크기와 상관없이 키 검색시간은 무시할 수 있을 정도로 작다!
- list는 꽤 느리다.

![스크린샷 2021-11-20 오후 12 36 40](https://user-images.githubusercontent.com/60768642/142713232-0573681b-c867-43b5-8cb2-f1180ec42b49.png)


#### dict 작동 방식에 의한 영향
- 키 객체는 반드시 해시 가능해야 한다.
  - 객체 수명주기동안`__hash__()`메서드가 항상 동일한 값을 반환한다.
  - `__eq__()`메서드를 통해 동치성을 판단할 수 있다.
  - a == b가 참이면, hash(a) == hash(b)도 반드시 참이어야 한다.
  - > 클래스에서 사용자 정의 `__eq__()`구현시 항상 `__hash__()`메서드도 적절히 구현해야 한다.
    a == b가 참이면 hash(a) == hash(b)도 참이어야 하기 때문.
    혹시 ```__eq__()```메서드가 가변 상태에 기반하는 경우 `__hash__()`메서드는 반드시 unhashable type: 'Myclass'
    같은 TypeError를 발생시켜야 한다.
- dict, set은 메모리 오버헤드가 크다.
  - > 많은 양의 레코드를 처리하는 경우 JSON형태로 각 레코드당 하나의 dict를 만드는 것보다 tuple, namedtuple을 사용하는 게 메모리 측면에서 좋다.
    dict는 레코드마다 하나의 hashtable을 가져야 하고, 레코드마다 필드명을 다시 저장해야 하는데 이 부담을 덜 수 있다.
- 키 검색이 아주 빠르다.
- 키 순서는 삽인 순서에 따라 달라진다.
- dict에 항목을 추가하면 기존 키의 순서가 변경될 수 있다.
  - > dict내부적으로 항목이 추가될 때마다 hashtable의 크기를 늘릴지 판단한다.
    필요하다면 더 큰 해시테이블을 새로 만들어 기존 항목을 모두 새롭게 추가한다.
    이 과정에서 키 순서가 달라질 수 있는데, 이는 언제 벌어질지미리 예측할 수 없다.


출처: 
- https://www.daleseo.com/python-collections-counter/
- https://www.daleseo.com/python-collections-counter/