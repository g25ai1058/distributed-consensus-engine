#!/bin/bash

echo "================================"
echo "CHAOS TEST STARTED"
echo "================================"

echo "Stopping Leader Node"
docker stop node1

sleep 10

echo "Checking Running Containers"
docker ps

echo "Restarting Leader"
docker start node1

sleep 5

echo "CHAOS TEST COMPLETED"
