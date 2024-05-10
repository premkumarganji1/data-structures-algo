

def sum_val(x):
    print(f"before x: {x}")
    if x > 50:
        return x
    y = sum_val(x+10)
    print(f"after x: {x}, y: {y}")


def sum2(n):
    result = 0
    for i in range(n+1):
        result += i
    return result


def sum2_recursion(n):
    if n == 0:
        return 0
    return n + sum2_recursion(n-1)


def partitions(n,m):
    if n <= 1 or m <= 1:
        return 1

    return partitions(n-m, m) + partitions(n, m-1)

print(sum2(5))
print(sum2_recursion(5))
print(partitions(3, 3))

