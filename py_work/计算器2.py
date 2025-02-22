while True:
    user_q = input("输入算式")

    yun_suan = ['+', '-', '/', '*']
    a = 1
    try:

        if '(' in user_q and ')' in user_q:
            c = 0
            while not list(user_q)[c] == '(':
                c += 1
            d = 1
            while not list(user_q)[d] == ')':
                d += 1
            user_q1 = user_q[c + 1:d]
            while not list(user_q1)[a] in yun_suan:
                a += 1
            if list(user_q1)[a] == yun_suan[0]:
                b = a + 1
                long = len(user_q1)
                if '.' in user_q1[0:a] and user_q1[b:long]:
                    f_answer = float(user_q1[0:a]) + float(user_q1[b:long])
                elif '.' in user_q1[b:long]:
                    f_answer = int(user_q1[0:a]) + float(user_q1[b:long])
                elif '.' in user_q1[0:a]:
                    f_answer = float(user_q1[0:a]) + int(user_q1[b:long])
                else:
                    f_answer = int(user_q1[0:a]) + int(user_q1[b:long])

                if c == 0:
                    a = d
                elif c == c:
                    a = 0
                while not list(user_q)[a] in yun_suan:
                    a += 1
                if list(user_q)[a] == yun_suan[0]:
                    b = a + 1
                    long = len(user_q)
                    try:
                        if '.' in user_q[b:long]:
                            answer = f_answer + float(user_q[b:long])
                        else:
                            answer = f_answer + int(user_q[b:long])
                        print(answer)
                    except ValueError:
                        if '.' in user_q[b:long]:
                            answer = float(user_q[b:long]) + f_answer
                        else:
                            answer = float(user_q[b:long]) + f_answer
                        print(answer)
                elif list(user_q)[a] == yun_suan[1]:
                    b = a + 1
                    long = len(user_q)
                    try:
                        if '.' in user_q[b:long]:
                            answer = f_answer - float(user_q[b:long])
                        else:
                            answer = f_answer - int(user_q[b:long])
                        print(answer)
                    except ValueError:
                        if '.' in user_q[b:long]:
                            answer = float(user_q[b:long]) - f_answer
                        else:
                            answer = float(user_q[b:long]) - f_answer
                        print(answer)
                elif list(user_q)[a] == yun_suan[3]:
                    b = a + 1
                    long = len(user_q)
                    try:
                        if '.' in user_q[b:long]:
                            answer = f_answer * float(user_q[b:long])
                        else:
                            answer = f_answer * int(user_q[b:long])
                        print(answer)
                    except ValueError:
                        if '.' in user_q[b:long]:
                            answer = float(user_q[b:long]) * f_answer
                        else:
                            answer = float(user_q[b:long]) * f_answer
                        print(answer)
                elif list(user_q)[a] == yun_suan[2]:
                    b = a + 1
                    long = len(user_q)
                    try:
                        try:
                            if '.' in user_q[b:long]:
                                answer = f_answer / float(user_q[b:long])
                            else:
                                answer = f_answer / int(user_q[b:long])
                            print(answer)
                        except ValueError:
                            if '.' in user_q[b:long]:
                                answer = float(user_q[b:long]) / f_answer
                            else:
                                answer = float(user_q[b:long]) / f_answer
                            print(answer)
                    except ZeroDivisionError:
                        print("不能除以零")
            elif list(user_q1)[a] == yun_suan[1]:
                b = a + 1
                long = len(user_q1)
                if '.' in user_q1[0:a] and user_q1[b:long]:
                    f_answer = float(user_q1[0:a]) - float(user_q1[b:long])
                elif '.' in user_q1[b:long]:
                    f_answer = int(user_q1[0:a]) - float(user_q1[b:long])
                elif '.' in user_q1[0:a]:
                    f_answer = float(user_q1[0:a]) - int(user_q1[b:long])
                else:
                    f_answer = int(user_q1[0:a]) - int(user_q1[b:long])

                if c == 0:
                    a = d
                else:
                    a = 0
                while not list(user_q)[a] in yun_suan:
                    a += 1
                if list(user_q)[a] == yun_suan[0]:
                    b = a + 1
                    long = len(user_q)
                    try:
                        if '.' in user_q[b:long]:
                            answer = f_answer + float(user_q[b:long])
                        else:
                            answer = f_answer + int(user_q[b:long])
                        print(answer)
                    except ValueError:
                        if '.' in user_q[b:long]:
                            answer = float(user_q[b:long]) + f_answer
                        else:
                            answer = float(user_q[b:long]) + f_answer
                        print(answer)
                elif list(user_q)[a] == yun_suan[1]:
                    b = a + 1
                    long = len(user_q)
                    try:
                        if '.' in user_q[b:long]:
                            answer = f_answer - float(user_q[b:long])
                        else:
                            answer = f_answer - int(user_q[b:long])
                        print(answer)
                    except ValueError:
                        if '.' in user_q[b:long]:
                            answer = float(user_q[b:long]) - f_answer
                        else:
                            answer = float(user_q[b:long]) - f_answer
                        print(answer)
                elif list(user_q)[a] == yun_suan[3]:
                    b = a + 1
                    long = len(user_q)
                    try:
                        if '.' in user_q[b:long]:
                            answer = f_answer * float(user_q[b:long])
                        else:
                            answer = f_answer * int(user_q[b:long])
                        print(answer)
                    except ValueError:
                        if '.' in user_q[b:long]:
                            answer = float(user_q[b:long]) * f_answer
                        else:
                            answer = float(user_q[b:long]) * f_answer
                        print(answer)
                elif list(user_q)[a] == yun_suan[2]:
                    b = a + 1
                    long = len(user_q)
                    try:
                        try:
                            if '.' in user_q[b:long]:
                                answer = f_answer / float(user_q[b:long])
                            else:
                                answer = f_answer / int(user_q[b:long])
                            print(answer)
                        except ValueError:
                            if '.' in user_q[b:long]:
                                answer = float(user_q[b:long]) / f_answer
                            else:
                                answer = float(user_q[b:long]) / f_answer
                            print(answer)
                    except ZeroDivisionError:
                        print("不能除以零")

            elif list(user_q1)[a] == yun_suan[3]:
                b = a + 1
                long = len(user_q1)
                if '.' in user_q1[0:a] and user_q1[b:long]:
                    f_answer = float(user_q1[0:a]) * float(user_q1[b:long])
                elif '.' in user_q1[b:long]:
                    f_answer = int(user_q1[0:a]) * float(user_q1[b:long])
                elif '.' in user_q1[0:a]:
                    f_answer = float(user_q1[0:a]) * int(user_q1[b:long])
                else:
                    f_answer = int(user_q1[0:a]) * int(user_q1[b:long])

                if c == 0:
                    a = d
                else:
                    a = 0
                while not list(user_q)[a] in yun_suan:
                    a += 1
                if list(user_q)[a] == yun_suan[0]:
                    b = a + 1
                    long = len(user_q)
                    try:
                        if '.' in user_q[b:long]:
                            answer = f_answer + float(user_q[b:long])
                        else:
                            answer = f_answer + int(user_q[b:long])
                        print(answer)
                    except ValueError:
                        if '.' in user_q[b:long]:
                            answer = float(user_q[b:long]) + f_answer
                        else:
                            answer = float(user_q[b:long]) + f_answer
                        print(answer)
                elif list(user_q)[a] == yun_suan[1]:
                    b = a + 1
                    long = len(user_q)
                    try:
                        if '.' in user_q[b:long]:
                            answer = f_answer - float(user_q[b:long])
                        else:
                            answer = f_answer - int(user_q[b:long])
                        print(answer)
                    except ValueError:
                        if '.' in user_q[b:long]:
                            answer = float(user_q[b:long]) - f_answer
                        else:
                            answer = float(user_q[b:long]) - f_answer
                        print(answer)
                elif list(user_q)[a] == yun_suan[3]:
                    b = a + 1
                    long = len(user_q)
                    try:
                        if '.' in user_q[b:long]:
                            answer = f_answer * float(user_q[b:long])
                        else:
                            answer = f_answer * int(user_q[b:long])
                        print(answer)
                    except ValueError:
                        if '.' in user_q[b:long]:
                            answer = float(user_q[b:long]) * f_answer
                        else:
                            answer = float(user_q[b:long]) * f_answer
                        print(answer)
                elif list(user_q)[a] == yun_suan[2]:
                    b = a + 1
                    long = len(user_q)
                    try:
                        try:
                            if '.' in user_q[b:long]:
                                answer = f_answer / float(user_q[b:long])
                            else:
                                answer = f_answer / int(user_q[b:long])
                            print(answer)
                        except ValueError:
                            if '.' in user_q[b:long]:
                                answer = float(user_q[b:long]) / f_answer
                            else:
                                answer = float(user_q[b:long]) / f_answer
                            print(answer)
                    except ZeroDivisionError:
                        print("不能除以零")
            elif list(user_q1)[a] == yun_suan[2]:
                b = a + 1
                long = len(user_q)
                try:
                    if '.' in user_q1[0:a] and user_q1[b:long]:
                        f_answer = float(user_q1[0:a]) / float(user_q1[b:long])
                    elif '.' in user_q1[b:long]:
                        f_answer = int(user_q1[0:a]) / float(user_q1[b:long])
                    elif '.' in user_q1[0:a]:
                        f_answer = float(user_q1[0:a]) / int(user_q1[b:long])
                    else:
                        f_answer = int(user_q1[0:a]) / int(user_q1[b:long])

                    if c == 0:
                        a = d
                    else:
                        a = 0
                    while not list(user_q)[a] in yun_suan:
                        a += 1
                    if list(user_q)[a] == yun_suan[0]:
                        b = a + 1
                        long = len(user_q)
                        try:
                            if '.' in user_q[b:long]:
                                answer = f_answer + float(user_q[b:long])
                            else:
                                answer = f_answer + int(user_q[b:long])
                            print(answer)
                        except ValueError:
                            if '.' in user_q[b:long]:
                                answer = float(user_q[b:long]) + f_answer
                            else:
                                answer = float(user_q[b:long]) + f_answer
                            print(answer)
                    elif list(user_q)[a] == yun_suan[1]:
                        b = a + 1
                        long = len(user_q)
                        try:
                            if '.' in user_q[b:long]:
                                answer = f_answer - float(user_q[b:long])
                            else:
                                answer = f_answer - int(user_q[b:long])
                            print(answer)
                        except ValueError:
                            if '.' in user_q[b:long]:
                                answer = float(user_q[b:long]) - f_answer
                            else:
                                answer = float(user_q[b:long]) - f_answer
                            print(answer)
                    elif list(user_q)[a] == yun_suan[3]:
                        b = a + 1
                        long = len(user_q)
                        try:
                            if '.' in user_q[b:long]:
                                answer = f_answer * float(user_q[b:long])
                            else:
                                answer = f_answer * int(user_q[b:long])
                            print(answer)
                        except ValueError:
                            if '.' in user_q[b:long]:
                                answer = float(user_q[b:long]) * f_answer
                            else:
                                answer = float(user_q[b:long]) * f_answer
                            print(answer)
                    elif list(user_q)[a] == yun_suan[2]:
                        b = a + 1
                        long = len(user_q)
                        try:
                            try:
                                if '.' in user_q[b:long]:
                                    answer = f_answer / float(user_q[b:long])
                                else:
                                    answer = f_answer / int(user_q[b:long])
                                print(answer)
                            except ValueError:
                                if '.' in user_q[b:long]:
                                    answer = float(user_q[b:long]) / f_answer
                                else:
                                    answer = float(user_q[b:long]) / f_answer
                                print(answer)
                        except ZeroDivisionError:
                            print("不能除以零")

                except ZeroDivisionError:
                    print("不能除以零")



        else:
            while not list(user_q)[a] in yun_suan:
                a += 1
            if list(user_q)[a] == yun_suan[0]:
                b = a + 1
                long = len(user_q)
                if '.' in user_q[0:a] and user_q[b:long]:
                    answer = float(user_q[0:a]) + float(user_q[b:long])
                elif '.' in user_q[b:long]:
                    answer = int(user_q[0:a]) + float(user_q[b:long])
                elif '.' in user_q[0:a]:
                    answer = float(user_q[0:a]) + int(user_q[b:long])
                else:
                    answer = int(user_q[0:a]) + int(user_q[b:long])
                print(answer)
            elif list(user_q)[a] == yun_suan[1]:
                b = a + 1
                long = len(user_q)
                if '.' in user_q[0:a] and user_q[b:long]:
                    answer = float(user_q[0:a]) - float(user_q[b:long])
                elif '.' in user_q[b:long]:
                    answer = int(user_q[0:a]) - float(user_q[b:long])
                elif '.' in user_q[0:a]:
                    answer = float(user_q[0:a]) - int(user_q[b:long])
                else:
                    answer = int(user_q[0:a]) - int(user_q[b:long])
                print(answer)
            elif list(user_q)[a] == yun_suan[3]:
                b = a + 1
                long = len(user_q)
                if '.' in user_q[0:a] and user_q[b:long]:
                    answer = float(user_q[0:a]) * float(user_q[b:long])
                elif '.' in user_q[b:long]:
                    answer = int(user_q[0:a]) * float(user_q[b:long])
                elif '.' in user_q[0:a]:
                    answer = float(user_q[0:a]) * int(user_q[b:long])
                else:
                    answer = int(user_q[0:a]) * int(user_q[b:long])
                print(answer)
            elif list(user_q)[a] == yun_suan[2]:
                b = a + 1
                long = len(user_q)
                try:
                    if '.' in user_q[0:a] and user_q[b:long]:
                        answer = float(user_q[0:a]) / float(user_q[b:long])
                    elif '.' in user_q[b:long]:
                        answer = int(user_q[0:a]) / float(user_q[b:long])
                    elif '.' in user_q[0:a]:
                        answer = float(user_q[0:a]) / int(user_q[b:long])
                    else:
                        answer = int(user_q[0:a]) / int(user_q[b:long])
                    print(answer)
                except ZeroDivisionError:
                    print("不能除以零")
    except Exception:
        print('输入正确的算式，或暂时不支持此功能')