import random

def replace_index(str_a, str_b, index):
	if index == 0:
		str_a = str_b + str_a[1:]
	else :
		str_a = str_a[:index] + str_b + str_a[index + 1:]
	return str_a

user_word = input("Write a word, or just press enter for a random word.\n").lower()
word_list = ["wapiti", "rotationnel", "sensations", "reptilien"]
lives = 5
word = ""
hidden_word = ""

if user_word :
	word = user_word
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
else :
	word = random.choice(word_list)

for letter in word:
	hidden_word += '_'
print(f"Good luck !\n***{hidden_word}***\n")
while lives and '_' in hidden_word :
	guess = input("Gimme a letter\n").lower()[0]
	if word.find(guess) == -1 :
		lives -= 1
		print(f"Nope, no '{guess}' :(\n")

	else :
		found = word.find(guess)
		while guess != "_" and found != -1 :
			hidden_word = replace_index(hidden_word, guess, found)
			word = replace_index(word, "_", found)
			print(f"Nice !\n")
			found = word.find(guess)
	print(f"Lives left : {lives}\n***{hidden_word}***")

