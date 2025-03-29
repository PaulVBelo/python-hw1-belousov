from src.matrix import Matrix

def test():
    test_matrix = Matrix((10, 10), [i for i in range(100)])

    print("1. M\n", test_matrix, sep="")
    print("2. M\n", test_matrix[1, 1], sep="")
    print("3. M\n", test_matrix[1], sep="")
    print("4. M\n", test_matrix[-1], sep="")
    print("5. M\n", test_matrix[1:4], sep="")
    print("6. M\n", test_matrix[:4], sep="")
    print("7. M\n", test_matrix[4:], sep="")
    print("8. M\n", test_matrix[:], sep="")
    print("9. M\n", test_matrix[1:7:2], sep="")
    print("10. M\n", test_matrix[:, 1], sep="")
    print("11. M\n", test_matrix[1:4, 1:4], sep="")
    print("12. M\n", test_matrix[1:4, :4], sep="")
    print("13. M\n", test_matrix[1:4, 4:], sep="")
    print("14. M\n", test_matrix[1:4, :], sep="")
    print("15. M\n", test_matrix[-1 :], sep="")
    print("16. M\n", test_matrix[-2::-2], sep="")
    print("17. M\n", test_matrix[-2::-2, 1:4], sep="")
    print("18. M\n", test_matrix[:, :], sep="")
    print("19. M\n", test_matrix[[1, 4]], sep="")
    print("20. M\n", test_matrix[:, [1,4]], sep="")
    print("21. M\n", test_matrix[[1, 4], [1, 4]], sep="")

if __name__ == "__main__":
    test()