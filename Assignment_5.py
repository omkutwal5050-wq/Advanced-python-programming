"""
Experiment 5: Dynamic Programming
Find the Longest Common Subsequence (LCS) between two sequences.
"""


def lcs_length_table(X, Y):
    """Build the DP table where table[i][j] = length of LCS of X[:i] and Y[:j]."""
    m, n = len(X), len(Y)
    table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    return table


def lcs_string(X, Y):
    """Return both the length and the actual LCS string, using the DP table."""
    m, n = len(X), len(Y)
    table = lcs_length_table(X, Y)

    # Backtrack through the table to reconstruct the LCS string
    i, j = m, n
    result = []
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            result.append(X[i - 1])
            i -= 1
            j -= 1
        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    result.reverse()
    return table[m][n], "".join(result)


def display_dp_table(X, Y, table):
    """Print the DP table in a readable grid format."""
    print("\nDP Table:")
    header = "      " + "  ".join(f"{c:>2}" for c in ("", *Y))
    print(header)
    for i, row in enumerate(table):
        label = "" if i == 0 else X[i - 1]
        print(f"  {label:>2} " + "  ".join(f"{v:>2}" for v in row))


def print_menu():
    print("\n Om kutwal SY-12 Roll No. 70")
    print("\n===== LONGEST COMMON SUBSEQUENCE (LCS) =====")
    print("1. Find LCS length and string for two sequences")
    print("2. Show DP table for two sequences")
    print("3. Run built-in example (AGGTAB vs GXTXAYB)")
    print("4. Exit")
    print("==============================================")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            X = input("Enter first sequence (e.g., a string): ").strip()
            Y = input("Enter second sequence: ").strip()
            if not X or not Y:
                print("Both sequences must be non-empty.")
                continue
            length, subseq = lcs_string(X, Y)
            print(f"\nLongest Common Subsequence Length: {length}")
            print(f"Longest Common Subsequence: '{subseq}'")

        elif choice == "2":
            X = input("Enter first sequence: ").strip()
            Y = input("Enter second sequence: ").strip()
            if not X or not Y:
                print("Both sequences must be non-empty.")
                continue
            table = lcs_length_table(X, Y)
            display_dp_table(X, Y, table)
            print(f"\nLCS Length: {table[len(X)][len(Y)]}")

        elif choice == "3":
            X, Y = "AGGTAB", "GXTXAYB"
            length, subseq = lcs_string(X, Y)
            print(f"\nX = '{X}', Y = '{Y}'")
            print(f"Longest Common Subsequence Length: {length}")
            print(f"Longest Common Subsequence: '{subseq}'")

        elif choice == "4":
            print("Exiting the LCS Program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()