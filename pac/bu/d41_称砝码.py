while True:
    try:
        # 砝码的种类 2
        weight_of_kind = int(input().strip())

        # 每种砝码的重量 1kg 2kg   [1,2]
        weight = list(map(int, input().strip().split()))

        # # 每种砝码的数量  2个  1个  [2,1]
        weight_of_num = list(map(int, input().strip().split()))

        res = []
        # 列举出所有:每个砝码的重量 1kg 1kg 2kg
        for i in range(weight_of_kind):
            for j in range(weight_of_num[i]):
                res.append(weight[i])
        print(res)
        # 将每个种类的砝码 相互加起来,加起来的重量放到集合当中,0kg是一种特殊情况,需要手动加入 set集合去重 避免无线计算
        res1 = {0}
        for i in res:
            for j in list(res1):
                res1.add(i + j)
        # print(f'{i} + {j}相加的重量{res1}')
        print(len(res1))
    except:
        break