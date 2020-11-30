# 目前加密使用的比较简单后续可以使用强一点的
import binascii

# 输入查找的信息输出账号密码
# 路径加密，源文件密码加密
# 该文件中现在存在两种加密形式 1.将一列全部加密（列项加密） 2.一列内将密码与网点名称分开加密，以“: ”(英文)和","（英文）分割（单项加密）最后一行预留一行
# 用户密码案例: 123456: mysql(root),rabbitmq(admin) “: ”前面的为密码，后面为网点名称，括号里面的是用户名
# 下面的方法有交叉的地方请看清楚功能再使用
class manageThePass:
    content = {}

    # 解密
    # 参数：密文
    # 返回：明文
    def decryption(self,word):
        word2 = binascii.a2b_hex(word).decode('utf-8')
        return word2

    # 加密
    # 参数：明文
    # 返回：密文
    def encryption(self, word):
        word2 = binascii.b2a_hex(word.encode())
        return word2

    # 读取明文文件，将内容保存到字典中
    # 参数：路径
    # 返回：无
    def loadFile(self, path):
        fr = open(path, 'r', encoding='utf-8')
        lines = fr.readlines()
        for line in lines:
            self.splitLineToDic(line)
        fr.close()

    # 将文件内容切割为字典内容
    # 参数：一行文件字符串
    # 返回：无
    def splitLineToDic(self, line):
        if line == '' or line == None:
            return ''
        lineSplit = line.split(": ")
        if len(lineSplit) < 2:
            return ''
        password = lineSplit[0]
        self.content[password] = []
        names = lineSplit[1].split(',')
        nameLen = len(names)
        for name in names:
            # 将末尾的“\n”去掉
            if '\n' in name:
                # print(name)
                name = name[:-1]
            self.content[password].append(name)
        # if nameLen > 0:
        #     # 将每一列的末尾的“\n”去掉
        #     self.content[password][nameLen - 1] = self.content[password][nameLen - 1][:-1]

    # 找到相应的行数，用于明文查找
    # 参数：搜索的内容
    # 返回：明文密码
    def findLine(self, name):
        for one in self.content:
            if name in self.content[one]:
                return self.decryption(one)

    # 根据一篇明文生成一篇密文（列项加密）
    # 参数：明文路径
    # 返回：成功：1（生成一篇密文）失败：-1
    def encryptFile(self, pathW):
        try:
            fw = open(pathW, 'w', encoding='utf-8')
            for password in self.content:
                line = password + ": "
                for name in self.content[password]:
                    line += (name + ',')
                line = line[:-1]
                fw.write(str(self.encryption(line), encoding='utf-8') + '\n')
            print('file created success, the path is ' + pathW)
            return 1
        except Exception as e:
            print(e)
            print('file create fails')
            return -1

    # 添加添加/删除/修改的网点名称
    # 参数：类型（1按照密码增加网点名称，-1按照密码删除网点名称，2按照网点名称修改密码），密码，网点名称（有括号的也要讲括号内容写入）,跟新文件路径
    # 返回：成功：1，修改密文文件内容，失败：-1
    def changeWebsite(self, type, password, name, path):
        # print('type:', type, 'content',self.content)
        try:
            # 按照密码增加网点名称
            # 需要的参数有：type,password,name
            if type == 1:
                # 判断是否已存在该名称如果是，返回-2，否，继续
                for key in self.content:
                    # print('c',c,'name',name)
                    if name in self.content[key]:
                        return -2
                if password in self.content:
                    self.content[password].append(name)
                else:
                    self.content[password] = [name]
            # 按照网点名称修改密码，先进行原账号绑定的网点名称删除，再进行新密码与网点名称绑定
            # 需要的参数有：type,password,name
            elif type == 2:
                for key in self.content:
                    if name in self.content[key]:
                        self.content[key].remove(name)
                        if len(self.content[key]) < 1:
                            self.content.pop(key)
                        break
                if password in self.content:
                    self.content[password].append(name)
                else:
                    self.content[password] = [name]
            # 按照密码删除网点名称
            # 需要的参数有：type,password,name
            elif type == -1:
                # print('pass:', password, 'name',name, 'content:', self.content)
                if password in self.content:
                    self.content[password].remove(name)
                    # 如果列表为空，删除该键
                    if len(self.content[password]) < 1:
                        self.content.pop(password)
            else:
                print('no suitable type')
                return -1
            self.encryptFile(path)
            print('file update success')
            return 1
        except Exception as e:
            print(e)
            print('file update fails')
            return -1

    # 读取并解密密文内容到字典中
    # 参数：密文文件路径
    # 返回：成功：1，载入content字典内容，失败：-1
    def loadAndDecryption(self, path):
        self.content = {}
        try:
            with open(path, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    line = bytes(line[:-1], encoding="utf8")
                    line = self.decryption(line)
                    self.splitLineToDic(line)
            print('file load success')
            return 1
        except Exception as e:
            print(e)
            print('file load fail')
            return -1

    # 根据每次都遍历密文文件内容，找到或到末尾结束
    # 参数：密文路径
    # 返回：字典，网点名称（用户名）：密码,空白为无，失败：-1
    def decryptByLine(self, path, name):
        try:
            with open(path, 'r') as f:
                lines = f.readlines()
                # 用户名和密码弄成字典类型
                namePassDic = {}
                for line in lines:
                    line = bytes(line[:-1], encoding = "utf8")
                    decrypted = self.decryption(line)
                    if name in decrypted:
                        decrypts = decrypted.split(":")
                        if len(decrypts) > 1:
                            password = decrypts[0]
                            names = decrypts[1].split(",")
                            for n in names:
                                if name in n:
                                    namePassDic[n.strip()] = password
                                    # 下面注释的内容是将网点名称和用户名分开的
                                    # un = n.split("(")
                                    # if len(un) > 1:
                                    #     username = un[1][: -1]
                return namePassDic
        except Exception as e:
            print(e)
            return -1

    # 测试content，输出全局变量
    def printContent(self):
        print(self.content)

    # 载入密文文件转化之后再修改
    def loadAndTransAndUpdate(self,type, password, name, path):
        a = self.loadAndDecryption(path)
        if a == -1:
            return -1
        b = self.changeWebsite(type, password, name, path)
        return a and b

    # 载入明文转化为密文
    # 参数：明文路径
    # 返回：成功 密文路径，失败 -1
    def loadFileAndencrypt(self, path):
        a = self.loadFile(path)
        if a == -1:
            return a
        # [::-1]是将字符创翻转，以下语句用于修改最后一位'.'为_en.
        pathW = path[::-1].replace('.', '.ne_', 1)[::-1]
        b = self.encryptFile(pathW)
        if b == -1:
            return b
        else:
            return pathW

    # 密码加密
    # 参数：data 加密数据，num1,num2两个秘钥参数
    # 返回：成功 加密后的密码 失败 -1
    def encryptPassword(self, data, num1, num2):
        newData = ''
        try:
            for c in data:
                asciiC = ord(c)
                if ((asciiC <= 122 and asciiC >= 97) or (asciiC <= 90 and asciiC >= 65)):
                    c = self.handleAlphabet(c,1,num1,num2)
                elif (asciiC <= 57 and asciiC >= 48):
                    c = self.handleNumber(c,1,num1,num2)
                else:
                    c = self.handleSymbol(c,1,num1,num2)
                newData += c
        except Exception as e:
            print(e)
            return -1
        return newData

    # 密码解密
    # 参数：data 解密数据，num1,num2两个秘钥参数
    # 返回：成功 解密后的密码 失败 -1
    def decryptPassword(self, data, num1, num2):
        pass

    # 英文部分
    # 参数：type 1加密，0解密，data 数据，num1,num2秘钥参数
    # 返回：成功 加密解密后的数据 失败 -1
    def handleAlphabet(self, type, data, num1, num2):
        asciiData = ord(data)
        if asciiData >= 97 and asciiData <= 122:
            if type == 1:
                asciiData = ((asciiData - 97) + (num1 % 26)) % 26 + 65
            if type == 0:
                print('解密还没写')
                pass
        elif asciiData >= 65 and asciiData <= 90:
            if type == 1:
                asciiData = ((asciiData - 65) - (num2 % 26)) % 26 + 97
            if type == 0:
                print('解密还没写')
                pass
        else:
            print('该字符不是字母，错误！')
            return -1
        return chr(asciiData)
    # 数字部分
    # 参数：type 1加密，0解密，data 数据，num1,num2秘钥参数
    # 返回：成功 加密解密后的数据 失败 -1
    def handleNumber(self, type, data, num1, num2):
        data = int(data)
        if (type == 1):
            num3 = min(num1%10, num2%10)
            num4 = max(num1 % 10, num2 % 10)
            if (num3 != 0 and data >= 0 and data < num3):
                data = num3 - 1 - data + 0
            if (num3 != num4 and data >= num3 and data <= num4):
                data = ((num3 + num4 + data) % (num4 - num3 + 1)) + num3
            if (num4 != 9 and data > num4 and data <= 9):
                data = 9 - data + num4 + 1
        else:
            print('解密部分没有写')
            pass
        return data

    # 符号部分
    # 参数：type 1加密，0解密，data 数据，num1,num2秘钥参数
    # 返回：成功 加密解密后的数据 失败 -1
    def handleSymbol(self, type, data, num1, num2):
        symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '+', '/', '<', '>', '~', '.', '|', '`']
        data = str(data)
        symbolIndex = symbols.index(data)
        if type == 1:
            symbolIndex = ((symbolIndex + num1) * num2 ) % len(symbols)
        else:
            print('解密部分没有写')
            pass
        return symbols[symbolIndex]

# 主函数入口
if __name__ == "__main__":
    mtp = manageThePass()
    path = './passfile/password.txt'
    path2 = './passfile/password_en.txt'

    # 测试明文转化为密文
    # mtp.loadFile(path)
    # mtp.encryptFile(path2)
    # mtp.printContent()

    # 测试在密文中查找密码
    dict = mtp.decryptByLine(path2, 's')
    print(dict)
    # mtp.printContent()

    # 测试修改密文文件
    # mtp.loadAndDecryption(path2)
    # mtp.changeWebsite(-1, 'gwq998', '', '', path2);
    # mtp.printContent()
