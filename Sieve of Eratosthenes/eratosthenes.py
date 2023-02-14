def sieve_of_eratosthenes(n: int) -> None:
    prime = [True for _ in range(n + 1)]
    p = 2
    while p**2 <= n:
        if prime[p]:
            for i in range(p**2, n + 1, p):
                prime[i] = False
        p += 1
    for i in range(2, n + 1):
        if prime[i]:
            print(i, end=" ")
    print()


if __name__ == "__main__":
    n = int(input("Enter the number : "))
    sieve_of_eratosthenes(n)
