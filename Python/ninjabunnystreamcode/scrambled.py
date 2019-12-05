def scramble(jumbled, match):
	jumbled = list(jumbled)
	jumbled.sort()
	jumbled_index = 0
	print(jumbled)
	print(match)


	for char in sorted(match):
		while True:
			if char == jumbled[jumbled_index]:
				jumbled_index += 1
				break
			else:
				jumbled_index += 1

index = 0
jumbled = ['d','k','l','o','q','r','w']
match = ['d','l','o','r','w']

#print(f"jumbled = {sorted(jumbled)}")
#print(f"match = {sorted(match)}")

scramble(jumbled,match)
