import os

filename = 'Students.txt'


def main():
    while True:
        menu()
        choice = int(input('请选择:'))
        if choice in range(0, 8):
            if choice == 0:
                answer = input('您确定要退出系统吗？(y/n):')
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用！！！')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


def menu():
    print('=======================学生信息管理系统==============================')
    print('--------------------------功能菜单----------------------------------')
    print('\t\t\t1.录入学生信息\t\t\t')
    print('\t\t\t2.查找学生信息\t\t\t')
    print('\t\t\t3.删除学生信息\t\t\t')
    print('\t\t\t4.修改学生信息\t\t\t')
    print('\t\t\t5.排序学生信息\t\t\t')
    print('\t\t\t6.统计学生信息\t\t\t')
    print('\t\t\t7.显示学生信息\t\t\t')
    print('\t\t\t0.退出信息系统\t\t\t')
    print('-------------------------------------------------------------------')


# menu()
def insert():
    student_list = []
    while True:
        id = input('请输入ID(如1001):')
        if not id:
            break
        name = input('请输入姓名:')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩:'))
            python = int(input('请输入Python成绩:'))
            java = int(input('请输入Java成绩:'))
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue
        #
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        student_list.append(student)
        answer = input('是否继续添加？(y/n):')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break

    # save
    save(student_list)
    print('学生信息录入完毕！！！')


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')


def search():
    student_query = []
    while True:
        Id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('按照id查询输入1，按照姓名查询输入2:')
            if mode == '1':
                Id = input('请输入学生id:')
            elif mode == '2':
                name = input('请输入学生姓名:')
            else:
                print('您的输入有误，请重新输入！！！')
                search()
            with open(filename, 'r', encoding='utf-8') as rfile:
                student_old = rfile.readlines()
                for item in student_old:
                    d = dict(eval(item))
                    if Id != '':
                        if d['id'] == Id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)
            show_student(student_query)
            student_query.clear()
            answer = input('是否要继续查询?(y/n):')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break
        else:
            print('无学生信息！！！')
            return


def show_student(lst):
    if len(lst) == 0:
        print('没查到数据！！！')
        return
    else:
        # 定义标题显示格式
        format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
        print(format_title.format('ID', '姓名', '英语成绩', 'Python成绩', 'Java成绩', '总成绩'))
        # 定义标题显示格式内容
        format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
        for item in lst:
            print(format_data.format(
                item.get('id'),
                item.get('name'),
                item.get('english'),
                item.get('python'),
                item.get('java'),
                int(item.get('english')) +
                int(item.get('python')) +
                int(item.get('java'))))


def delete():
    while True:
        student_id = input('请输入要删除的学生ID:')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as rfile:
                    student_old = rfile.readlines()
            else:
                student_old = []
            flag = False  # 标记是否删除
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    for item in student_old:
                        d = dict(eval(item))
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除！！！')
                    else:
                        print(f'没有找到id为{student_id}的学生信息！！！')
            else:
                print('无学生信息！！！')
                break
            show()
            answer = input('是否继续删除呢？(y/n):')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        student_old = []
    if not student_old:
        print('无学生信息！！！')
        return
    student_id = input('请输入要修改的学生ID:')
    if student_id != '':
        with open(filename, 'w', encoding='utf-8') as wfile:
            for item in student_old:
                d = dict(eval(item))
                # print(d)
                if d['id'] == student_id:
                    print(f'找到id为{student_id}的学生信息了，可以修改')
                    while True:
                        try:
                            d['name'] = input('请输入姓名:')
                            d['english'] = input('请输入英语成绩:')
                            d['python'] = input('请输入Python成绩:')
                            d['java'] = input('请输入Java成绩:')
                        except:
                            print('输入无效，不是整数类型，请重新输入')
                        else:
                            break
                    wfile.write(str(d) + '\n')
                    print('修改成功！！！')
                else:
                    wfile.write(str(d) + '\n')
            answer = input('是否继续修改其他学生信息?(y/n):')
            if answer == 'y' or answer == 'Y':
                modify()
            else:
                return
    else:
        modify()


def sort():
    show()
    student_new = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_lst = rfile.readlines()
            for item in student_lst:
                d = dict(eval(item))
                student_new.append(d)
    else:
        return
    asc_or_desc = input('请选择(0.升序 1.降序):')
    if asc_or_desc == '0':
        asc_or_desc_bool = False
    elif asc_or_desc == '1':
        asc_or_desc_bool = True
    else:
        print('您的输入有误，请重新输入！！！')
        sort()
    mode = input('请选择排序方式(1.english 2.Python 3.Java 0.总成绩):')
    if mode == '1':
        student_new.sort(key=lambda x: int(x['english']), reverse=asc_or_desc_bool)
    elif mode == '2':
        student_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)
    elif mode == '3':
        student_new.sort(key=lambda x: int(x['java']), reverse=asc_or_desc_bool)
    elif mode == '0':
        student_new.sort(key=lambda x: int(x['english']) + int(x['python']) + int(x['java']), reverse=asc_or_desc_bool)
    else:
        print('您的输入有误，请重新输入！！！')
        sort()
    show_student(student_new)


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print('暂未保存数据信息...')


def show():
    student_lst = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            for items in students:
                student_lst.append(eval(items))
            if student_lst:
                show_student(student_lst)


if __name__ == '__main__':
    main()
