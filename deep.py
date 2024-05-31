answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")

# Normalize the answer to lowercase and remove any hyphens
normalized_answer = answer.lower().replace("-", " ")

# Check if the answer is 42, forty-two, or forty two
if normalized_answer == "42" or normalized_answer == "forty two":
    print("Yes")
else:
    print("No")