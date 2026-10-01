name = input("Speak your name: ").strip()

print("Choose greeting style / Выберите стиль:")
print("1 — Formal ")
print("2 — Informal")

style = input("Enter 1 or 2: ").strip()

if style == "1":
    print(f"Greetings, {name}! It's a pleasure to meet you, master.")
elif style == "2":
    print(f"Hi, {name}! It's a pleasure to meet you, buddy.")
else:
    print(f"Hello, {name}!")