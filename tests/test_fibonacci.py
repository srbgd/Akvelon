from client import API
from fib_consts import FIB


class TestFibonacci:

    api = API()

    def fib(self, n: int) -> int:
        return self.api.get_fibonacci(n)['answer']

    def test_fibonacci_base_case(self):
        assert self.fib(0) == 0

    def test_fibonacci_first_10_numbers(self):
        assert [self.fib(i) for i in range(10)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def test_fibonacci_large_numbers(self):
        assert [self.fib(i) for i in sorted(FIB.keys())] == list(sorted(FIB.values()))

    def test_fibonacci_1000000th_number(self):
        result = str(self.fib(1000000))
        assert result.startswith('195328212870775773163201494759625633244354299659187339695')
        assert result.endswith('68996526838242546875')
        assert len(result) == 208988
