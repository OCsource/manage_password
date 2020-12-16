# 改文件用于生成随机字符串
# 输入条件（字符长度，生成随机数的字符选择-数字、大小写字母、符号）

import random

class createRandomStr:

    numbers = ['0','1','2','3','4','5','6','7','8','9']
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    symbols = ['!','@','#','$','%','^','&','*','-','+','/','<','>','~','.','|','`','=','?']

    # 获取随机字符串
    # 参数：字符长度，是否有数字，是否有字母，是否有符号(1有，0没有)
    # 返回：成功返回字符串，失败-1
    def getRandomStr(self,num, haveNum, haveAlphabet, havaSymbol):
        total = haveNum + haveAlphabet + havaSymbol
        if total < 1:
            print("至少选择一个随机选项")
            return -1
        totalList = []
        if total > num:
            print("字符串长度需要大于等于字符选择数!")
            return -1

        commodNum = 0
        lastNum = 0
        if total < 2:
            lastNum = num
        else:
            commodNum = int(num / total)
            lastNum = commodNum if num % total == 0 else (num - commodNum * (total - 1))
        # 均分随机取数
        if haveNum == 1:
            exeNum = commodNum
            total-=1
            if total == 0:
                exeNum = lastNum
            for i in range(exeNum):
                totalList.append(random.choice(self.numbers))
        if haveAlphabet == 1:
            exeNum = commodNum
            total -= 1
            if total == 0:
                exeNum = lastNum
            for i in range(exeNum):
                totalList.append(random.choice(self.alphabets))
        if havaSymbol == 1:
            exeNum = commodNum
            total -= 1
            if total == 0:
                exeNum = lastNum
            for i in range(exeNum):
                totalList.append(random.choice(self.symbols))
        # print(totalList)
        return self.returnStr(totalList)

    # 将数组数据打乱
    # 参数：数组
    # 返回：成功字符串，失败-1
    def returnStr(self,totalList):
        randomStr = ''
        listLen = len(totalList)
        for i in range(listLen):
            rdn = random.randint(0,len(totalList) - 1)
            rds= totalList[rdn]
            randomStr += rds
            del totalList[rdn]
        return randomStr

if __name__ == '__main__':
    crs = createRandomStr()
    print(crs.getRandomStr(95,0,0,0))

