print("PBFT MODE")
print("==========")

transaction = "TX001 : Pay Rs 100"
# PRE-PREPARE
print("\nPRE-PREPARE PHASE")
print("---------------")
print(f"\nPrimary Node -> {transaction}")
# PREPARE
print("\nPREPARE PHASE")
print("------------")

for i in range(1, 6):
    print(f"\nNode {i} -> PREPARE")
# BYZANTINE ATTACK
print("\n\nBYZANTINE ATTACK")
print("----------------")
print("\nAdversary Node 99 sent conflicting transaction")
print("Signature Verification Failed")
print("Ignoring Malicious Node")
# COMMIT
print("\n\nCOMMIT PHASE")
print("------------")

for i in range(1, 6):
    print(f"\nNode {i} -> COMMIT")

# RESULT
print("\n\nPBFT RESULT")
print("-----------")

print("\nTransaction COMMITTED")