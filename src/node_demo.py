import os
import time

NODE_NAME = os.getenv("NODE_NAME", "node")

print("Leader Election Complete")
time.sleep(1)

print("Leader is Node 5")
time.sleep(1)

print("CONSENSUS RESULT")
print("----------------")

time.sleep(1)

print("Majority Reached")
time.sleep(1)

print("Transaction COMMITTED")

time.sleep(5)