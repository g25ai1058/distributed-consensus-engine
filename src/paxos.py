transaction = "TX001 : Pay Rs 100"

print("\nClient Sending Transaction...")
print(f"Node 5 received transaction: {transaction}")

print("\nPHASE 1 : PREPARE\n")

for i in range(1, 5):
    print(f"Leader -> Node {i} : PREPARE")

print("\nPHASE 2 : PROMISE\n")

for i in range(1, 5):
    print(f"Node {i} -> PROMISE")

print("\nPHASE 3 : ACCEPT\n")

for i in range(1, 5):
    print(
        f"Leader -> Node {i} : ACCEPT ({transaction})"
    )

print("\nPHASE 4 : ACCEPTED\n")

for i in range(1, 5):
    print(f"Node {i} -> ACCEPTED")

print("\nMajority Reached")
print("Transaction Committed")