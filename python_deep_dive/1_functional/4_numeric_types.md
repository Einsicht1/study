## intro
### 5 main types of numbers
<img width="1052" alt="스크린샷 2022-02-10 오후 12 21 02" src="https://user-images.githubusercontent.com/92774768/153330977-4e6f835e-4dc6-4ca7-b670-0ea4e8d4e105.png">

## Integers: data Types
- 정리: int 값이 클수록 메모리도 많이 차지하고, 연산도 오래 걸린다.
### int의 최대값은 얼마일까?
- 이 질문에 답하려면 int의 내부 구현을 알아야 한다.
- int는 내부적으로 2진수로 되어있다.

<img width="1383" alt="스크린샷 2022-02-10 오후 12 24 26" src="https://user-images.githubusercontent.com/92774768/153331274-15f80e47-e82e-415d-b25b-d5d811a42e44.png">

- 음수를 고려하지 않았을 때 8비트로 나타낼 수 있는 가장 큰수는? -> 255
- 음수를 고려했을 때 8비트로 나타낼 수 있는 가장 큰수는? -> 127

<img width="1606" alt="스크린샷 2022-02-10 오후 12 26 43" src="https://user-images.githubusercontent.com/92774768/153331474-4c1f54ed-1746-45db-a1f3-00d94a42db4b.png">

<img width="1472" alt="스크린샷 2022-02-10 오후 12 29 02" src="https://user-images.githubusercontent.com/92774768/153331699-35c430ec-96e9-4d29-958a-c276262afb58.png">

#### Java같은 경우 숫자 크기에 따라 data type이 다르다.
<img width="1633" alt="스크린샷 2022-02-10 오후 12 30 53" src="https://user-images.githubusercontent.com/92774768/153331889-139c6eb6-9476-4999-abb4-697366b0c032.png">

#### Python은 다르게 작동한다.
<img width="1484" alt="스크린샷 2022-02-10 오후 12 33 09" src="https://user-images.githubusercontent.com/92774768/153332116-ee41af16-a7d3-402e-96c0-b9a657d92cf7.png">

```python
import sys

sys.getsizeof(0)
sys.getsizeof(100)
sys.getsizeof(12**1000)


```




    504


## Integers: Operations


## Integers: Constructors and Bases
#### Int를 만드는 여러 방법

- a = 10
- a = int(10.9)
- a = int(True)
- a = int(Decimal("10.9))
- a = int("10")

#### Number base
- int(str) 형태일 땐 base를 지정할 수 있다.


```python
print(int("1010", base=2))
print(int("1010", base=10))
print(int("A12F", base=16))
```

    10
    1010
    41263


## Rational Numbers

## Floats: Internal Representations

## Floats: Equality Testing

## Floats: ECoercing to Integers

## Floats: Rounding

## Decimals

## Decimals: Constructors and Contexts


## Decimals: Math Operations


## Decimals: Performance Considerations


## Complex Numbers

## Booleans

## Booleans: Truth Values

## Booleans: Precedence and Short-Circuiting

## Boolean Operators

## Comparison Operators






