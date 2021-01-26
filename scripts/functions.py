def restrict_dataset(dataset, indices, restrictfield = "Accident_Index"):
	""" Restrict the data set dataset, given as structured array with an index field restrictfield
	to the indices given in the dict indices. Returns the restricted data set.
	"""

	# add later
	#if type(indices) == "list": 
	#	indices = {k: 0 for k in indices}

	restrictedrowindices = []
	for i in range(len(dataset[restrictfield])):
	    if dataset[restrictfield][i] in indices:
	        restrictedrowindices.append(i)

	return dataset[restrictedrowindices]

print("Loaded functions.\n")