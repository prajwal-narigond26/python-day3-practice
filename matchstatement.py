number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")


number = True

match number:
    case "pajju":
        print("One")
    case "mallu" | "ravi":
        print("Two or Three")
    case "sanu":
        print("sanjeev")
    case _:
        print("Other number")