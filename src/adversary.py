def run_adversary():

    print("\n===== BYZANTINE ATTACK =====")
    print("\nMalicious Node 5 starts equivocation")
    messages = {
        1: "TX003 : Pay Rs 500",
        2: "TX003 : Pay Rs 9000",
        3: "TX003 : Pay Rs 500",
        4: "TX003 : Pay Rs 9000"
    }

    for node, tx in messages.items():
        print(
            f"Node {node} received -> {tx}"
        )

    unique_values = set(
        messages.values()
    )
    if len(unique_values) > 1:
        print(
            "\nEquivocation Detected!"
        )
        print(
            "Malicious Node Rejected"
        )
        print(
            "Consensus Aborted"
        )

    else:
        print(
            "Consensus Continues"
        )
if __name__ == "__main__":
    run_adversary()