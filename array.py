n = int(input("Enter number of scores: "))

scores = list(map(int, input("Enter scores: ").split()))

total = sum(scores)
average = total / n

print("\nScores:", scores)
print("Sum =", total)
print("Average =", average)