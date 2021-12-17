# 1. 개요
huggingface에 반복되서 토큰이 나오는 문제가 있다. 버전 3에서는 문제가 없고, 3버전에서는 문제가 발생

# 2. 문제 형상

~~~
- 정상 동작
** transformers v3.0.0 **
Input: "This is <mask> sentence."
Output: "This is a partial sentence."

- 비정상 동작
** transformers v4.11.2 **
Input: "This is <mask> sentence."
Output: "ThisThis is a sentence."
~~~

# 3. install
    