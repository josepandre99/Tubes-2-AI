# buat rotasi list angle 4
# mis list = [1,3,7] => [3,7,1]
def rotate_list(aList):
	tList = list(aList)
	rList = []
	i = 0
	rList[3] = tList[0]
	while (i < 3):
		rList[i] = tList[i+1]
		i++
	return tList  

if (persegi):

elif (ada 2 sudut 90):
	
	# buat fungsi untuk rotasi list agar indeks sudut 1 sm 2 = 90
	
	# asumsi list searah jarum jam
	# angle 1 = angle 2 = 90

	# trapesium rata kiri
	# angle 3 > angle 4 
	if (list_angle[2] < list_angle[3]):
		list_facts.append("(2 sudut kiri 90)")

	# trapesium rata kiri
	# angle 3 < angle 4 
	elif (list_angle[2] < list_angle[3]):
		list_facts.append("(2 sudut kiri 90)")

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
		if (!find && i = 1):
			aList = rotate_list(aList)

	if (!find):
		# trapesium sembarang atau bukan bentuk
		list_facts.append("(bentuk ?)")
