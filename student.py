import datetime
def readStu(stu,times=0):
        print('Input the student\'s information\n')
        if times ==0:
            i = 0
            act =0
            while True:
                if act != 'q':
                    inputStu(stu)
                    i +=1
                    act = input('input \'q\' to break,others to continue:')
                else:
                    break
            return i
        else:
            for x in range(times):
                inputStu(stu)
            return times+len(stu)


def inputStu(stu):
    have = 0
    dict_stu = {}
    while True:
        num = int(input('num:'))
        if 0< num <10000000:
            for x in range(len(stu)):
                y = stu[x]['num']
                print(y)
                if num == y:
                    have = 1
            if have == 0:
                dict_stu['num'] = num
            break


    dict_stu['name'] = input('name:')

    while True:
        sex = input('sex(B or G):').upper()
        if sex == 'B' or sex == 'G':
            dict_stu['sex'] = sex
            break

    while True:
        classnum = int(input('classnum(0,100):'))
        if 0 < classnum < 100:
            dict_stu['classnum'] = classnum
            break
    stu.append(dict_stu)

def printStu(stu):
    for st in stu:
        print('{:<10}{:<13}{:<10}{:<8}\n'.format(st['num'],st['name'],st['sex'],st['classnum']))

def printdata(stu):
    for st in stu:
        if 'up' not in st:
            print('{:<10}{:<10}   {:<6}'.format(st['num'], st['name'],st['classnum']), end='')
            print('Have not checked!')
        else:
            print('{:<10}{:<10}   {:<6}'.format(st['num'],st['name'],st['classnum']),end='')
            for up in st['up']:
                for key,value in up.items():
                    print(key +':'+ value,end='    ')
            print('\n',end = '')

def sortStu(stu,which,Bts=0):
        if Bts ==0:
            stu.sort(key=lambda stu: stu[which], reverse=False)
        else:
            stu.sort(key=lambda stu: stu[which], reverse=True)

def makechange(stu):
    whe = 0
    num = int(input('请输入要修改学生的学号:'))
    for x in range(len(stu)):
        y = stu[x]['num']
        if num == y:
            whe == 1
            choice1 = input('whether to change his name?(YorN):').upper()
            if choice1 == 'Y':
                stu[x]['name'] = input('name:')
            choice2 = input('whether to change his sexy?(YorN):').upper()
            if choice2 == 'Y':
                while True:
                    sex = input('sex(B or G):').upper()
                    if sex == 'B' or sex == 'G':
                        stu[x]['sex'] = sex
                        break
            choice3 = input('whether to change his classnum?(YorN):').upper()
            if choice3 == 'Y':
                while True:
                    classnum = int(input('classnum(0,100):'))
                    if 0 < classnum < 100:
                        stu[x]['classnum'] = classnum
                        break
    if whe ==0:
        print('The student does not exit!Please check it again.')


def equalstu(stu,which,condition):          #搜索不改变数据stu
    f = []
    for st in stu:
        if st[which] == condition:
            f.append(st)
    return f

def checkStu(stu,which,condition):          #需要改变数据
    for st in stu:
        have = 0
        if st[which] == condition:
            data = str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day)
            if 'up' not in st:
                st['up'] = []
                print('num:{}  name:{} '.format(st['num'], st['name']), end=' ')
                up = input('come or not?(YorN):').upper()
                if up == 'Y' or up == 'N':
                    dict_oneday = {}
                    dict_oneday[data] = up
                    st['up'].append(dict_oneday)
            else:
                for d in st['up']:
                    if data in d:
                        have = 1
                if have :
                    print('{},today he has been checked'.format(st['name']))
                else:
                    print('num:{}  name:{} '.format(st['num'], st['name']), end=' ')
                    up = input('come or not?(YorN):').upper()
                    if up == 'Y' or up == 'N':
                        dict_oneday = {}
                        dict_oneday[data] = up
                        st['up'].append(dict_oneday)
    print('Today\'s checkation has finished!')


def datecheck(stu):
    data = str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day)
    for st in stu:
        if 'up' not in st:
            st['up'] = []
            print('num:{}  name:{} '.format(st['num'], st['name']), end=' ')
            up = input('come or not?(YorN):').upper()
            if up == 'Y' or up == 'N':
                dict_oneday = {}
                dict_oneday[data] = up
                st['up'].append(dict_oneday)
        else:
            for d in st['up']:
                if data in d:
                    print('{},today he has been checked'.format(st['name']))
                    continue
                else:
                    print('num:{}  name:{} '.format(st['num'], st['name']), end=' ')
                    up = input('come or not?(YorN):').upper()
                    if up == 'Y' or up == 'N':
                        dict_oneday = {}
                        dict_oneday[data] = up
                        st['up'].append(dict_oneday)
        print(st)
    print('Today\'s checkation has finished!')

def checkonce(stu):
    count = 0
    data = str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day)
    for st in stu:
        have = 0
        if 'up' not in st:
            st['up'] = []
            dict_oneday = {}
            dict_oneday[data] = 'Y'
            st['up'].append(dict_oneday)
        else:
            for d in st['up']:
                if data in d:
                    have =1
                    count +=1
            if not have :
                    dict_oneday = {}
                    dict_oneday[data] = 'Y'
                    st['up'].append(dict_oneday)
    if count == len(stu):
        print('Today all of them have been checked before.')
    else:
        print('Today\'s checkation has finished!')

def singlechange(stu,which,condition):
    data = str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day)
    have = 0
    for st in stu:
        wh = 0
        if condition == st[which]:
            have = 1
        if have:
            if 'up' not in st:
                print('num:{}   name:{}还未点名'.format(st['num'],st['name']))
            else:
                for d in st['up']:
                    if data in d:
                        wh = 1
                if wh:
                    print('num:{}   name:{}'.format(st['num'],st['name']))
                    for d in st['up']:              #找到up中键为今日的字典
                        if data in d:
                            break
                    print('today\'s check:{}'.format(d[data]))
                    change = input('Change his check as(YorNorQ):').upper()
                    d[data] = change
                    break
                else:
                    print('今日ta还未被点名')
                    change = input('Change his check as(YorNorQ):').upper()
                    d[data] = change
                    break
        else:
            print('不存在!')
