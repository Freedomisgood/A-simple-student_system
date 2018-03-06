import student
import json
def createFile():
    stu= []
    try:
        f = open('G:\\Py\\student_system\\student.txt','w')
    except :
        print('cannot open the file')
        exit()
    else:
        student.readStu(stu)
        json.dump(stu,f)
        f.close()
        return stu

def readFile():
    try:
        f = open('G:\\Py\\student_system\\student.txt', 'r')
    except FileNotFoundError as e:
        print(e)
        print('Create it now!')
        stu = createFile()
        return stu
    else:
        stu = json.load(f)
        f.close()
        return stu

def saveFile(stu):
    try:
        f = open('G:\\Py\\student_system\\student.txt', 'w')
    except:
        print('cannot open the file')
        exit()
    else:
        json.dump(stu,f)
        f.close()

def actionsave(stu):
    with open('G:\\Py\\student_system\\student.txt','w') as f:
        json.dump(stu, f)

