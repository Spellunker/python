def factorial(n, total=1):
    if n > 0:
        total = total * n
        n = n - 1
        return factorial(n, total)
    return total


if __name__ == "__main__":
    print(f"10! = {factorial(10)}")
