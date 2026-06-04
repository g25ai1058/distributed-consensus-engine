# PBFT Simulation

NUM_NODES = 5
PRIMARY = 5

transaction = "TX002 : Pay Rs 500"

def run_pbft():

    print("\n===== PBFT PROTOCOL =====")

    print("\nClient Sending Transaction...")
    print(f"Primary Node {PRIMARY} received transaction: {transaction}")

    # Phase 1
    print("\nPHASE 1 : PRE-PREPARE\n")

    for node in range(1, NUM_NODES):
        print(
            f"Primary -> Node {node} : PRE-PREPARE ({transaction})"
        )

    # Phase 2
    print("\nPHASE 2 : PREPARE\n")

    prepare_votes = 0

    for node in range(1, NUM_NODES):
        print(f"Node {node} -> PREPARE")
        prepare_votes += 1

    print(
        f"\nPrepare Votes Received = {prepare_votes}"
    )

    # Phase 3
    print("\nPHASE 3 : COMMIT\n")

    commit_votes = 0

    for node in range(1, NUM_NODES):
        print(f"Node {node} -> COMMIT")
        commit_votes += 1

    print(
        f"\nCommit Votes Received = {commit_votes}"
    )

    if commit_votes >= 4:
        print("\nPBFT CONSENSUS REACHED")
        print("Transaction Committed")
    else:
        print("\nPBFT CONSENSUS FAILED")


if __name__ == "__main__":
    run_pbft()