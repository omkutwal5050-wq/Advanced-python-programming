"""
Experiment 4: Dynamic Programming
Compute the nth Fibonacci number using Memoization and Tabulation techniques.
"""

import time


# ---------------- Naive Recursive Approach (for comparison) ----------------
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# ---------------- Memoization Approach (Top-Down DP) ----------------
def fibonacci_memoization(n, memo=None):
    if memo is None:
        memo = {}
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]


# ---------------- Tabulation Approach (Bottom-Up DP) ----------------
def fibonacci_tabulation(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    table = [0] * (n + 1)
    table[0], table[1] = 0, 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


# ---------------- Iterative Approach (O(1) space) ----------------
def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b


def timed_run(func, n, *args):
    start = time.perf_counter()
    result = func(n, *args)
    elapsed = time.perf_counter() - start
    return result, elapsed


def print_menu():
    print("\n Om kutwal SY-12 Roll No. 70")
    print("\n===== FIBONACCI - DYNAMIC PROGRAMMING =====")
    print("1. Compute using Recursive approach (naive)")
    print("2. Compute using Memoization (top-down DP)")
    print("3. Compute using Tabulation (bottom-up DP)")
    print("4. Compute using Iterative approach (O(1) space)")
    print("5. Compare all approaches (time taken)")
    print("6. Exit")
    print("=============================================")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice in ("1", "2", "3", "4", "5"):
            try:
                n = int(input("Enter the value of n: ").strip())
                if n < 0:
                    print("Please enter a non-negative integer.")
                    continue
            except ValueError:
                print("Invalid input. Please enter an integer.")
                continue

        if choice == "1":
            if n > 35:
                print("Warning: naive recursion is very slow for large n. Proceeding anyway...")
            result, elapsed = timed_run(fibonacci_recursive, n)
            print(f"F({n}) = {result}  [Recursive]  Time: {elapsed:.6f}s")

        elif choice == "2":
            result, elapsed = timed_run(fibonacci_memoization, n)
            print(f"F({n}) = {result}  [Memoization]  Time: {elapsed:.6f}s")

        elif choice == "3":
            result, elapsed = timed_run(fibonacci_tabulation, n)
            print(f"F({n}) = {result}  [Tabulation]  Time: {elapsed:.6f}s")

        elif choice == "4":
            result, elapsed = timed_run(fibonacci_iterative, n)
            print(f"F({n}) = {result}  [Iterative]  Time: {elapsed:.6f}s")

        elif choice == "5":
            print(f"\n--- Comparing all approaches for n = {n} ---")

            memo_result, memo_time = timed_run(fibonacci_memoization, n)
            print(f"Memoization : F({n}) = {memo_result}   Time: {memo_time:.6f}s")

            tab_result, tab_time = timed_run(fibonacci_tabulation, n)
            print(f"Tabulation  : F({n}) = {tab_result}   Time: {tab_time:.6f}s")

            iter_result, iter_time = timed_run(fibonacci_iterative, n)
            print(f"Iterative   : F({n}) = {iter_result}   Time: {iter_time:.6f}s")

            if n <= 30:
                rec_result, rec_time = timed_run(fibonacci_recursive, n)
                print(f"Recursive   : F({n}) = {rec_result}   Time: {rec_time:.6f}s")
            else:
                print("Recursive   : Skipped (n too large, would take too long)")

        elif choice == "6":
            print("Exiting the Fibonacci Program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()