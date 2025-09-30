import asyncio
import io
import math
import sys
from types import SimpleNamespace, MappingProxyType, CoroutineType

print("2025-09-16, 21114073, 차경호")

# 사용자 정의 함수
def sample_func():
    pass

# async 함수 및 코루틴 예시
async def async_func():
    pass

# async 제너레이터 함수
async def async_gen():
    for i in range(3):
        yield i

# 사용자 정의 클래스
class MyClass:
    @property
    def prop(self):
        return 123

    @classmethod
    def cm(cls):
        pass

    @staticmethod
    def sm():
        pass

    def method(self):
        pass

# 이벤트 루프를 새로 생성하여 Future 객체 안전하게 생성 후 닫기
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
future_obj = loop.create_future()
loop.close()

coroutine_type = CoroutineType

memory_file = io.StringIO("sample text")
binary_memory_file = io.BytesIO(b"sample bytes")

# 다양한 타입 인스턴스 모음
type_examples = [
    # 1. 기본 자료형
    1, 1.0, 1 + 2j, True, "Hi", None, range(3),

    # 2. 컬렉션 자료형
    [1], (1,), {1: 2}, {1}, frozenset({1}),

    # 3. 바이트 및 메모리
    b'abc', bytearray(b'abc'), memoryview(b'abc'),

    # 4. 함수 및 메서드
    sample_func, (lambda x: x), len, open, sample_func.__code__,
    MyClass().method, MyClass.cm, MyClass.sm,
    classmethod(lambda x: x), staticmethod(lambda x: x),

    # 5. 클래스 및 객체
    type, object(), MyClass, MyClass(), MyClass.prop,

    # 6. 모듈
    math, sys,

    # 7. 제너레이터 및 이터레이터
    (i for i in range(3)), map(str, [1]), filter(None, [True]),
    zip([1], [2]), enumerate([1]), reversed([1]),
    iter(range(3)), iter([1]), iter((1,)), iter({1}),
    iter("abc"), iter(b"abc"), iter(bytearray(b'abc')),
    iter(frozenset({1})),

    # 8. Async 관련
    async_func,            # async function
    coroutine_type,    # coroutine type
    async_gen(),           # async generator object

    # 9. dict view 객체
    {}.keys(), {}.values(), {}.items(),

    # 10. 예외 및 특수 상수
    Exception("error"), ValueError("value error"), TypeError("type error"),
    ..., NotImplemented, super(MyClass, MyClass()), slice(0, 10),

    # 11. 기타 내장 메서드
    [].append, "abc".upper, dict.get, set.add,

    # 12. 기타
    SimpleNamespace(), MappingProxyType({}),

    # 13. Coroutine, Awaitable, Future
    future_obj,

    # 14. Context Manager & 파일 객체
    # open 함수는 이미 포함되어 있으며,
    # 실제 파일 객체 생성 시 파일이 생성되므로 코드 실행 시 영향 방지를 위해 생략(주석 처리)
    memory_file,
    binary_memory_file,
]

# 결과 출력
for idx, obj in enumerate(type_examples, start=1):
    print(f"{idx:>3}. {repr(obj):>95} -> {type(obj)}")
