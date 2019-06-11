def factor(decimal):
	i = 1
	found = False
	while found == False:
		answer = i * decimal
		modanswer = answer % 1
		if modanswer == 0:
			found = True
		i += 1
	return {int(answer),i-1}

print(factor(2.35))
