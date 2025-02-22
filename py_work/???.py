SB集团 = ['\tSB公司','\tIKUN公司']
SB集团.insert(2,'\t大聪明工作室')
SB集团.insert(3,'\t小吴出版社')
SB集团.insert(4,'\t魔影公司')
print('\n这些是SB集团的公司:')
SB集团 = (sorted(SB集团))
for 公司 in SB集团:
    print(公司.upper())
print(f'这是SB集团的核心公司：\n\t{SB集团[1]}')
while True:
    意见 = (input('请问有问题吗？有问题的扣1没意见的扣2'))
    意见 = int(意见)
    if 意见 == 1:
        wrong = SB集团.pop(4)
        print(f'有一家公司搞错了：\n\t{wrong}不是SB集团的公司')
        print('这些是正确的公司:')
        for 公司 in SB集团:
            print(公司.upper())
        break
    elif 意见 == 2:
        新意见 = input('真的吗 假的扣1 真的扣2')
        新意见 = int(新意见)
        if 新意见 == 1:
            wrong = SB集团.pop(4)
            print(f'有一家公司搞错了：\n\t{wrong}不是SB集团的公司')
            print('这些是正确的公司:')
            for 公司 in SB集团:
                print(公司.upper())
            break
        elif 新意见 == 2:
            print('over')
            break
    else:
        print('不要乱搞')







