import time


print("Requesting data from microservice...\n\n")

f = open("calculate_goals.txt", "w")
f.write("run\n1000\n1200")
f.close()


time.sleep(7)

f = open("calculate_goals.txt", "r")
protein_goal = f.readline()
fat_goal = f.readline()
carbs_goal = f.readline()

f.close()

print("\n\nMain program received the following information:")
print("\tProtein goal:", protein_goal)
print("\tFat goal:", fat_goal)
print("\tCarbs goal:", carbs_goal)
