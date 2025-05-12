from collections import deque

queue = deque(input().split())
n = int(input())

while len(queue) != 1:
    queue.rotate(-(n-1))
    removed_kid = queue.popleft()
    print(f"Removed {removed_kid}")


print(f"Last is {queue[0] }")
