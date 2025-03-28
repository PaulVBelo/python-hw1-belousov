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

    def __getitem__(self, key):
        if isinstance(key, tuple):
            return self._handle_tuple(key)
        elif isinstance(key, int):
            return self._handle_one_row(key)
        elif isinstance(key, list):
            return self._handle_list(key)
        elif isinstance(key, slice):
            return self._handle_slice(key)
        else:
            raise TypeError("Unsupported key type")

    def _handle_one_row(self, key: int):
        if -self.rows <= key < self.rows:
            return Matrix((1, self.cols),
                          [self.data[self.conv_rc2i(key, c)] for c in range(self.cols)])
        else:
            raise IndexError(f"Index out of range: {key} not in [-{self.rows}, {self.rows})")

    def _handle_list(self, key: list):
        for i in range(len(key)):
            if not isinstance(key[i], int):
                raise TypeError("Unsupported row index type")

            if not -self.rows <= key[i] < self.rows:
                raise IndexError(f"Index {i} out of range: {key[i]} not in [-{self.rows}, {self.rows})")

        return Matrix((len(key), self.cols),
                      [self.data[self.conv_rc2i(r, c)] for r in key for c in range(self.cols)])

    def _handle_slice(self, key: slice):
        return self._handle_list(list(range(*key.indices(self.rows))))

    def _handle_tuple(self, key):
        if len(key) != 2:
            raise ValueError("Tuple must have two elements")

        r_key, c_key = key
        return self._process_tuple_keys(r_key, c_key)

    def _process_tuple_keys(self, r_key, c_key):
       pass





if __name__ == "__main__":
    dbg_matrix = Matrix((3, 4), [i for i in range(12)])
    print(dbg_matrix.conv_rc2i(1, 2))
    print(dbg_matrix.conv_i2rc(5))
    print(dbg_matrix)

    print(dbg_matrix[2])
    print(dbg_matrix[-3])
    print(dbg_matrix[[0, 1, 2, -1, -2, -3]])
    print(dbg_matrix[::-1])