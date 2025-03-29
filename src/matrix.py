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
            raise IndexError("Index out of range")

    def _handle_list(self, key: list):
        for i in range(len(key)):
            if not isinstance(key[i], int):
                raise TypeError("Unsupported row index type")

            if not -self.rows <= key[i] < self.rows:
                raise IndexError("Index out of range")

        return Matrix((len(key), self.cols),
                      [self.data[self.conv_rc2i(r, c)] for r in key for c in range(self.cols)])

    def _handle_slice(self, key: slice):
        return self._handle_list(list(range(*key.indices(self.rows))))

    def _handle_tuple(self, key):
        if len(key) != 2:
            raise ValueError("Tuple must have two elements")

        r_key, c_key = key

        if isinstance(r_key, int) and isinstance(c_key, int):
            if -self.rows <= r_key < self.rows and -self.cols < c_key < self.cols:
                return self.data[self.conv_rc2i(r_key, c_key)]
            else:
                raise IndexError("Index out of range")

        elif isinstance(r_key, (int, list, slice)) and isinstance(c_key, (int, list, slice)):
            if isinstance(r_key, int): r_key = [r_key]
            if isinstance(r_key, slice): r_key = list(range(*r_key.indices(self.rows)))

            if isinstance(c_key, int): c_key = [c_key]
            if isinstance(c_key, slice): c_key = list(range(*c_key.indices(self.cols)))

            for r in r_key:
                if not -self.rows <= r < self.rows:
                    raise IndexError("Index out of range")

            for c in c_key:
                if not -self.cols <= c < self.cols:
                    raise IndexError("Index out of range")

            return Matrix(
                (len(r_key), len(c_key)),
                [self.data[self.conv_rc2i(r, c)] for r in r_key for c in c_key]
            )


if __name__ == "__main__":
    dbg_matrix = Matrix((3, 4), [i for i in range(12)])
    print(dbg_matrix.conv_rc2i(1, 2))
    print(dbg_matrix.conv_i2rc(5))
    print(dbg_matrix)

    print(dbg_matrix[2])
    print(dbg_matrix[-3])
    print(dbg_matrix[[0, 1, 2, -1, -2, -3]])
    print(dbg_matrix[::-1])
    print(dbg_matrix[1, 2])
    print(dbg_matrix[[1, -1], [0, -2]])
    print(dbg_matrix[::-1, ::-1])
