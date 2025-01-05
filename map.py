# map(),filter(),reduce()

number = [1, 2, 3]


def multiply(a): return a * 2


# perform func to all iterators map(func,*it)
result = map(multiply, number)

# print(list(result))


def isEven(a): return a % 2 == 0


# perform to filter data based on some conditon(using function)
result2 = filter(isEven, number)

# print(list(result2))


# Decorators
def logtime(func):
    def wrapper():
        print("before")
        val = func()
        print("after")
        return val
    return wrapper


@logtime
def hello():
    print("hello")


# hello()

# List Compressions
numbers = [1, 2, 3, 4, 5]

numbers_power_2 = [n**2 for n in numbers]
print(numbers_power_2)
