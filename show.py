import student
import file
def MainInfo():
    print('********1.显示基本信息********')   #OK
    print('********2.基本信息管理********')   #ok
    print('********3.考勤评分信息********')   #ok
    print('********4.条件搜索信息********')   #ok
    print('********0.退出********')

def printHead():
    print("{:<8}{:<10}{:<8}{:<8}".format('学号', '姓名', '性别', '班级'))

def printcheck():
        print('{:<8}{:<10}{:<5}{:<15}'.format('学号','姓名','班级','出勤'))


def menuchangeinfo():                                       #基本信息管理
    print('********1.增添学生信息********')   #OK
    print('********2.修改学生信息********')   #ok
    print('********3.今日出勤考察********')   #ok
    print('********0.退出********')          #ok

def changeinfoManage(stu):
    while True:
        menuchangeinfo()
        choice = int(input('请输入你的选项:'))
        if choice ==1:
            num = int(input('请输入要增添的学生人数:'))
            if num >=0:
                student.readStu(stu,times=num)
                file.actionsave(stu)
                break
            else:
                print('请输入一个正整数:')
        elif choice == 2:
            student.makechange(stu)
            file.actionsave(stu)
        elif choice ==3:
            rollonceManage(stu)
            file.actionsave(stu)
        elif choice ==0:
            break


def menuroll():                                         #考勤评分信息
    print('********1.所有出勤情况********')       #OK
    print('********2.条件输入出勤********')       #ok  与menuchangeinfo()中今日效果相同
    print('********3.修改点名情况********')   #处理请假,(今日的请假情况必须通过这个来修改为'缺'..只准改今日
    print('********4.一键点名********')           #ok
    print('********0.退出********')               #ok

def rollchange():
    print('********1.按学号修改********')       #OK
    print('********2.按姓名修改********')       #ok  与menuchangeinfo()中今日效果相同
    print('********0.退出********')

def rollchangeManage(stu):
    while True:
        rollchange()
        choice = int(input('请输入你的选项:'))
        if choice == 1:
            num = int(input('请输入要搜索的学生学号:'))
            student.singlechange(stu,'num',num)
            file.actionsave(stu)
        elif choice == 2:
            classnum = int(input('请输入要搜索班级号:'))
            student.singlechange(stu, 'classnum', classnum)
            file.actionsave(stu)
        elif choice ==0:
            break

def menurollManage(stu):
    while True:
        menuroll()
        choice = int(input('请输入你的选项:'))
        if choice ==1:
            printcheck()
            student.printdata(stu)
        elif choice == 2:
            rollonceManage(stu)
        elif choice ==3:
            rollchangeManage(stu)
        elif choice == 4:
            student.checkonce(stu)
            file.actionsave(stu)
        elif choice ==0:
            break

def rollonce():
    print('********1.按班级点名********')            #ok
    print('********2.按性别点名********')            #ok
    print('********0.退出********')

def rollonceManage(stu):
    while True:
        rollonce()
        choice = int(input('请输入你的选项:'))
        if choice ==1:
            classnum = int(input('请输入要点名的班级:'))
            f = student.equalstu(stu,'classnum',classnum)
            if f == []:
                print('不存在{}班'.format(classnum))
            else:
                student.checkStu(stu,'classnum',classnum)
                file.actionsave(stu)
        elif choice == 2:
            sex = input('请输入性别:')
            f = student.equalstu(stu, 'sex', sex)
            if f == []:
                print('不存在{}'.format(sex))
            else:
                student.checkStu(stu,'sex',sex)
                file.actionsave(stu)
        elif choice ==0:
            break

def menusearch():                                       #条件搜索信息
    print('********1.按学号搜素********')        #ok
    print('********2.按班级搜素********')        #ok
    print('********3.按性别搜索********')        #ok
    print('********4.按姓名搜索********')        #ok
    print('********0.退出********')

def searchManage(stu):
    while True:
        menusearch()
        choice = int(input('请输入你的选项:'))
        if choice ==1:
            num = int(input('请输入要搜索的学生学号:'))
            f = student.equalstu(stu,'num',num)
            if f ==[]:
                print('不存在')
            else:
                printHead()
                student.printStu(f)
        elif choice == 2:
            classnum = int(input('请输入要搜索班级号:'))
            f = student.equalstu(stu,'classnum',classnum)
            if f ==[]:
                print('不存在')
            else:
                printHead()
                student.printStu(f)
        elif choice ==3:
            sex =input('请输入要搜索的性别:')
            f = student.equalstu(stu,'sex',sex)
            if f ==[]:
                print('不存在')
            else:
                printHead()
                student.printStu(f)
        elif choice ==4:
            name =input('请输入要搜索的姓名:')
            f = student.equalstu(stu,'name',name)
            if f ==[]:
                print('不存在')
            else:
                printHead()
                student.printStu(f)
        elif choice ==0:
            break




if __name__== '__main__':
    stu = file.readFile()
    while True:
        MainInfo()
        choice = int(input('Choose one option youo what to do:\n'))
        if choice == 1:
            printHead()
            student.sortStu(stu,'num')
            student.printStu(stu)
        elif choice ==2:
            changeinfoManage(stu)
        elif choice ==3:
            menurollManage(stu)
        elif choice ==4:
            searchManage(stu)
        elif choice == 0:
            break
        else:
            print('选择一个0-4之内的数:')
            continue
