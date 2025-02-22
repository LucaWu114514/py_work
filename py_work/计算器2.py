def calculate(expression):
    try:
        # 使用 eval 计算表达式
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "不能除以零"
    except Exception as e:
        return f"输入正确的算式，或暂时不支持此功能: {e}"

while True:
    user_q = input("输入算式 (或输入 'exit' 退出): ")
    
    if user_q.lower() == 'exit':
        break
    
    result = calculate(user_q)
    print(result)
