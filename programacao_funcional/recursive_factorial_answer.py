def factorial(n):
    return n * (factorial(n - 1) if (n - 1) > 1 else 1)


if __name__ == "__main__":
    print(f"10! = {factorial(10)}")

    # Trivia 6 weeks in seconds equals 10!
    print(6 * 7 * 24 * 60 * 60)
