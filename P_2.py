def water_jug_dfs(capacity1, capacity2, target):
    visited = set()
    path = []

    def dfs(jug1, jug2):
        if (jug1, jug2) in visited:
            return False
        
        visited.add((jug1, jug2))
        path.append((jug1, jug2))

        if jug1 == target or jug2 == target:
            return True

        # Rules/Operations
        # 1. Fill Jug 1
        if dfs(capacity1, jug2):
            return True
        # 2. Fill Jug 2
        if dfs(jug1, capacity2):
            return True
        # 3. Empty Jug 1
        if dfs(0, jug2):
            return True
        # 4. Empty Jug 2
        if dfs(jug1, 0):
            # Note: The original image shows 'dfs(jug1, 0)'
            return True
        # 5. Pour Jug 1 -> Jug 2
        if dfs(max(0, jug1 - (capacity2 - jug2)), min(capacity2, jug1 + jug2)):
            return True
        # 6. Pour Jug 2 -> Jug 1
        if dfs(min(capacity1, jug1 + jug2), max(0, jug2 - (capacity1 - jug1))):
            return True

        path.pop()
        return False

    dfs(0, 0)
    return path

capacity1 = int(input("Enter the capacity of jug 1: "))
capacity2 = int(input("Enter the capacity of jug 2: "))
target = int(input("Enter capacity: "))

solution = water_jug_dfs(capacity1, capacity2, target)

if solution:
    print("Solution steps:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
