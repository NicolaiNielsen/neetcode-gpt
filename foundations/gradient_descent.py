class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        for _ in range(iterations):
            derrivate = 2*init
            result = init - learning_rate * derrivate
            init = result

        return round(init, 5)
