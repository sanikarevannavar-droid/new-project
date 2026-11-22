import sys

n = int(input("Enter number of scores: "))

scores = list(map(int, input("Enter scores: ").split()))

if len(scores) != n:
    print("Please enter exactly", n, "scores.")
    sys.exit()

total = sum(scores)
average = total / n

print("\nScores:", scores)
print("Sum =", total)
print("Average =", average)
print("Maximum score =", max(scores))
print("Minimum score =", min(scores))
