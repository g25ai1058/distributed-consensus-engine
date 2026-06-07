import threading
import time

NUM_NODES = 5

class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.is_leader = False
        self.alive = True
        self.last_heartbeat = time.time()

nodes = [Node(i) for i in range(1, NUM_NODES + 1)]

# Highest ID becomes initial leader
leader = max(nodes, key=lambda n: n.node_id)
leader.is_leader = True

print("\n=== Initial Leader Election ===")
for node in nodes:
    role = "Leader" if node.is_leader else "Follower"
    print(f"Node {node.node_id} -> {role}")

def send_heartbeats():
    global leader

    while True:
        if leader and leader.alive:
            for node in nodes:
                if node.node_id != leader.node_id:
                    node.last_heartbeat = time.time()

            print(f"[Heartbeat] Leader Node {leader.node_id}")
            time.sleep(2)
        else:
            break

def monitor_nodes():
    global leader

    while True:
        time.sleep(3)

        if leader and not leader.alive:

            print(
                f"\n[Failure Detected] Leader Node {leader.node_id} crashed!"
            )

            candidates = [
                n for n in nodes
                if n.alive and n.node_id != leader.node_id
            ]

            if candidates:
                new_leader = max(
                    candidates,
                    key=lambda n: n.node_id
                )

                for node in nodes:
                    node.is_leader = False

                new_leader.is_leader = True
                leader = new_leader

                print(
                    f"[Election] New Leader Elected -> Node {leader.node_id}\n"
                )

                threading.Thread(
                    target=send_heartbeats,
                    daemon=True
                ).start()

                break

# Start heartbeat thread
threading.Thread(
    target=send_heartbeats,
    daemon=True
).start()

# Start monitoring thread
threading.Thread(
    target=monitor_nodes,
    daemon=True
).start()

# Simulate leader crash after 10 sec
time.sleep(10)

print("\n***** Simulating Leader Crash *****")
leader.alive = False

# Keep program running
while True:
    time.sleep(1)

print("\n***** Leader Crashed *****\n")
time.sleep(2)

print("Node 5: Leader failure detected!\n")
time.sleep(1)

# Elect new leader
leader = 4
print(f"New Leader Elected: Node {leader}\n")

# New leader heartbeats
while True:
    print(f"Leader {leader} heartbeat")
    time.sleep(1)
print("Transaction Committed")
    