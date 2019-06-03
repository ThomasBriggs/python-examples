def studentMark():

    numStudents = input("Please enter the number of Students: ")
    print "\n"

    marks = range(numStudents)
    markMax = 0
    prizes = 0

    for i in range(studentMark):
        marks[i] = input("Please enter student mark: ")
        if marks[i] > markMax:
            markMax = marks[i]

    for i in marks:
        if i == markMax:
            prizes += 1

    print "\n"
    print"Maximum Mark: ", markMax
    print "Prizes: ", prizes

studnetMark()