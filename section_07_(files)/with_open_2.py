#with open ("states.txt", "r") as states_file:
#	states = states_file.read()

#print states


with open("states.txt", "r") as states_file:
	states = states_file.read().split("\n")

	for index, state in enumerate(states):
		states[index] = state.split("\t")

print states