while True:
    user_input = input('我能帮助你计算(先输入几位，两边位数一样（最多3位）)')
    try:
        user_input = int(user_input)
    except ValueError:
        print('输入！')
    if user_input == 1:
        user_input = input('输入计算内容')
        user_input = str(user_input)
        if '*' in user_input:
            user_input = list(user_input)
            type = user_input.remove('*')
            user_input[0] = int(user_input[0])
            user_input[1] = int(user_input[1])
            answer = user_input[0] * user_input[1]
            print(answer)
        elif '+' in user_input:
            user_input = list(user_input)
            type = user_input.remove('+')
            user_input[0] = int(user_input[0])
            user_input[1] = int(user_input[1])
            answer = user_input[0] + user_input[1]
            print(answer)
        elif '-' in user_input:
            user_input = list(user_input)
            type = user_input.remove('-')
            user_input[0] = int(user_input[0])
            user_input[1] = int(user_input[1])
            answer = user_input[0] - user_input[1]
            print(answer)
        elif '/' in user_input:
            user_input = list(user_input)
            type = user_input.remove('/')
            user_input[0] = int(user_input[0])
            user_input[1] = int(user_input[1])
            try:
                answer = user_input[0] / user_input[1]
                print(answer)
            except ZeroDivisionError:
                pass
    elif user_input == 2:
            user_input = input('输入计算内容')
            user_input = str(user_input)
            if '*' in user_input:
                user_input = list(user_input)
                type = user_input.remove('*')
                user_input[0] += user_input[1]
                user_input[2] += user_input[3]
                user_input[0] = int(user_input[0])
                user_input[2] = int(user_input[2])
                answer = user_input[0] * user_input[2]
                print(answer)
            elif '+' in user_input:
                user_input = list(user_input)
                type = user_input.remove('+')
                user_input[0] += user_input[1]
                user_input[2] += user_input[3]
                user_input[0] = int(user_input[0])
                user_input[2] = int(user_input[2])
                answer = user_input[0] + user_input[2]
                print(answer)
            elif '-' in user_input:
                user_input = list(user_input)
                type = user_input.remove('-')
                user_input[0] += user_input[1]
                user_input[2] += user_input[3]
                user_input[0] = int(user_input[0])
                user_input[2] = int(user_input[2])
                answer = user_input[0] - user_input[2]
                print(answer)
            elif '/' in user_input:
                user_input = list(user_input)
                type = user_input.remove('/')
                user_input[0] += user_input[1]
                user_input[2] += user_input[3]
                user_input[0] = int(user_input[0])
                user_input[2] = int(user_input[2])
                try:
                    answer = user_input[0] / user_input[2]
                    print(answer)
                except ZeroDivisionError:
                    pass

    elif user_input == 3:
            user_input = input('输入计算内容')
            user_input = str(user_input)
            if '*' in user_input:
                user_input = list(user_input)
                type = user_input.remove('*')
                user_input[0] += user_input[1]
                user_input[0] += user_input[2]
                user_input[3] += user_input[4]
                user_input[3] += user_input[5]
                user_input[0] = int(user_input[0])
                user_input[3] = int(user_input[3])
                answer = user_input[0] * user_input[3]
                print(answer)
            elif '+' in user_input:
                user_input = list(user_input)
                type = user_input.remove('+')
                user_input[0] += user_input[1]
                user_input[0] += user_input[2]
                user_input[3] += user_input[4]
                user_input[3] += user_input[5]
                user_input[0] = int(user_input[0])
                user_input[3] = int(user_input[3])
                answer = user_input[0] + user_input[3]
                print(answer)
            elif '-' in user_input:
                user_input = list(user_input)
                type = user_input.remove('-')
                user_input[0] += user_input[1]
                user_input[0] += user_input[2]
                user_input[3] += user_input[4]
                user_input[3] += user_input[5]
                user_input[0] = int(user_input[0])
                user_input[3] = int(user_input[3])
                answer = user_input[0] - user_input[3]
                print(answer)
            elif '/' in user_input:
                user_input = list(user_input)
                type = user_input.remove('/')
                user_input[0] += user_input[1]
                user_input[0] += user_input[2]
                user_input[3] += user_input[4]
                user_input[3] += user_input[5]
                user_input[0] = int(user_input[0])
                user_input[3] = int(user_input[3])
                try:
                    answer = user_input[0] / user_input[3]
                    print(answer)
                except ZeroDivisionError:
                    pass
