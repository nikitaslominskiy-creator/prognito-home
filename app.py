while True:
    name = input("SPEAK YOUR NAME: ").strip()

    clean_name = name.replace(" ", "").replace("-", "")
    
    if clean_name.isalpha():
        break
    
    print("Error you entered the wrong name!.\n")

print("\nChoose greeting style")
print("1 — Formal ")
print("2 — Informal")

style = input("Enter 1 or 2: ").strip()

uppercase_name = name.to_uppercase()

if style == "1":
    print(f"\nGreetings, {name}! It's a pleasure to meet you, master.")
elif style == "2":
    print(f"\nHi, {name}! It's a pleasure to meet you, buddy.")
else:
    print(f"\nHello, {name}!")