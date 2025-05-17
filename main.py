print("👋 Hi there! Let's learn about TIME COMPLEXITY using loops!")

# Ask the user for a number
n = int(input("Enter a number: "))

print("\n🔁 I'm going to count from 1 to your number: ")
for i in range(1, n + 1):
    print(f" ⌚ Step {i}: Counting...")

print("\n✅ Done! That took me", n, "steps.")
print("👉 This is called Linear Time or 0(n) , because steps grow as the number grows!")