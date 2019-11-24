if (persegi):

elif (ada 2 sudut 90):
	# rotasi indeks maks.4

	# trapesium rata kiri

	# trapesium rata kiri

else:
	find = false
	i = 0
	# rotasi indeks maks.2
	while (!find && i < 2):
		# jajargenjang
		if (list_length[0] = list_length[2] && list_length[1] = list_length[3]):
			list_facts.append("(sisi 1 sama sisi 3)")
			list_facts.append("(sisi 2 sama sisi 4)")
			find = true
		# layang-layang
		elif (list_length[0] = list_length[1] && list_length[2] = list_length[3]):
			list_facts.append("(sisi 1 sama sisi 2)")
			list_facts.append("(sisi 3 sama sisi 4)")
			find = true
		# trapesium sama kaki
		elif (list_length[0] = list_length[2] && list_length[1] != list_length[3]):
			if (list_angle[0] = list_angle[2] && list_angle[1] = list_angle[3]):
				list_facts.append("(sisi 1 sama sisi 3)")
				list_facts.append("(sisi 2 tidak sama sisi 4)")
				list_facts.append("(sudut 1 sama sudut 2)")
				list_facts.append("(sudut 3 sama sudut 4)")
				find = true
		i++

	if (!find):
		# trapesium sembarang atau bukan bentuk
		list_facts.append("(bentuk ?)")
