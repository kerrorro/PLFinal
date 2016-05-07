import Employee

emps = [Employee(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10]) for x in [line.strip()[1:-2].replace("'", "").replace(" ", "").split(",") for line in open('Employees.txt', 'r')]]
