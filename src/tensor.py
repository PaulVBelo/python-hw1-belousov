class Tensor:
    def __init__(self, dim: int | tuple, data: list):
        self.dimensions = dim
        self.data = data

    def __repr__(self):
        return str(self.data)


if __name__ == "__main__":
    dbg_tensor = Tensor((2, 2, 3),
                        [6 * i + 3 * j + k for i in range(2) for j in range(2) for k in range(3)]
                        )

    print(dbg_tensor)
