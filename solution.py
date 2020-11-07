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
        print('type:', type, 'content',self.content)
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
        pathW = path.replace('.', '_en.')
        b = self.encryptFile(pathW)
        if b == -1:
            return b
        else:
            return pathW


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
