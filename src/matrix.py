import tensor
from src.tensor import Tensor


class Matrix(Tensor):

    def __init__(self, dim: tuple, data: list):
        if not isinstance(dim, tuple) or len(dim) != 2:
            raise ValueError("Wrong dimensions: tuple of length 2 required")

        self.rows, self.cols = dim

        if self.rows * self.cols != len(data):
            raise ValueError("Wrong matrix size: len(data) the same as prod of integer dimensions")

        super().__init__(dim, data)

    def conv_rc2i(self, r: int, c: int) -> int:
        return r * self.cols + c

    def conv_i2rc(self, i: int) -> tuple:
        return i // self.cols, i % self.cols

    def __str__(self):
        width = max(len(str(elem)) for elem in self.data) + 2

        s = "[\n"

        for r in range(self.rows):
            for c in range(self.cols):
                s += "".join(f"{self.data[self.conv_rc2i(r, c)]:>{width}}")
            s += "\n\n"

        s = s[:-1] + "]"

        return s


if __name__ == "__main__":
    dbg_matrix = Matrix((3, 4), [i for i in range(12)])
    print(dbg_matrix.conv_rc2i(1, 2))
    print(dbg_matrix.conv_i2rc(5))
    print(dbg_matrix)
