import Employee
import Department

dict = {'department.txt': Department, 'employees.txt': Employee}

def listCreator(text):
    list = [dict[text](x) for x in [line.strip()[1:-2].replace("'", "").replace(" ", "").split(",") for line in open(text, 'r')]]
    return list
