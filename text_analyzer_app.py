# FP PROJECT - Text Analyzer Apps

# 🧠 Text Analyzer Apps

# HeroBoard Entry #6 = Day 6 Project 06

print("🧠 Welcome to the Text Analyzer Apps!")
print("Enter a block of text below to analyze it.\n")

# Step 1: Get user input

text = input("📝 Enter your text:\n>")

# Step 2: Analyze the text

word_count = len(text.split())
char_count = len(text)
sentence_count = text.count(".") + text.count("!") + text.count(">")

# Step 3: Display the results

print("📊 TEXT ANALYSIS RESULT:")
print(f"🔤 Total characters: {char_count}")
print(f"📝 Total words: {word_count}")
print(f"📚 Total sentences: {sentence_count}")

# Bonus message

if word_count < 10:
print("📎 Short and Sweet!")
elif word_count < 50:
print("📖 Medium length = nice and readable.")
else:
print("📚 That's a lot of words! Epic monologue!")
