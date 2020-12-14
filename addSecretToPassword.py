# 加密类，将字母数字和字符分别加密，最后再将字符切割进行重组（不支持中文加密，密码中只能包含数字字母和符号）
class threeEncryption:
    
    # 密码加密
    # 参数：data 加密数据，num1,num2两个秘钥参数
    # 返回：成功 加密后的密码 失败 -1
    def encryptPassword(self, data, num1, num2):
        newData = ''
        try:
            for c in data:
                c = str(c)
                asciiC = ord(c)
                if ((asciiC <= 122 and asciiC >= 97) or (asciiC <= 90 and asciiC >= 65)):
                    c = self.handleAlphabet(1,c,num1,num2)
                elif (asciiC <= 57 and asciiC >= 48):
                    c = self.handleNumber(1,c,num1,num2)
                else:
                    c = self.handleSymbol(1,c,num1,num2)
                c = str(c)
                newData += c
        except Exception as e:
            print(e)
            return -1
        # 字符切割转换
        num1 = num1 % (len(data))
        num2 = num2 % (len(data))
        if num1 > num2:
            num1,num2 = num2,num1
        return newData[num2:] + newData[num1:num2] + newData[:num1]

    # 密码解密
    # 参数：data 解密数据，num1,num2两个秘钥参数
    # 返回：成功 解密后的密码 失败 -1
    def decryptPassword(self, data, num1, num2):
        newData = ''
        try:
            for c in data:
                c = str(c)
                asciiC = ord(c)
                if ((asciiC <= 122 and asciiC >= 97) or (asciiC <= 90 and asciiC >= 65)):
                    c = self.handleAlphabet(0,c,num1,num2)
                elif (asciiC <= 57 and asciiC >= 48):
                    c = self.handleNumber(0,c,num1,num2)
                else:
                    c = self.handleSymbol(0,c,num1,num2)
                c = str(c)
                newData += c
        except Exception as e:
            print(e)
            return -1
        # 字符切割转换
        num1 = num1 % (len(data))
        num2 = num2 % (len(data))
        if num1 > num2:
            num1,num2 = num2,num1
        return newData[len(data)-num1:] + newData[-num2:len(data)-num1] + newData[:-num2]

    # 英文部分
    # 参数：options 1加密，0解密，data 数据，num1,num2秘钥参数
    # 返回：成功 加密解密后的数据 失败 -1
    def handleAlphabet(self, options, data, num1, num2):
        asciiData = ord(data)
        if asciiData >= 97 and asciiData <= 122:
            if options == 1:
                asciiData = ((asciiData - 97) + (num1 % 26)) % 26 + 65
            if options == 0:
                asciiData = ((asciiData - 97) + (num2 % 26)) % 26 + 65
        elif asciiData >= 65 and asciiData <= 90:
            if options == 1:
                asciiData = ((asciiData - 65) - (num2 % 26)) % 26 + 97
            if options == 0:
                asciiData = ((asciiData - 65) - (num1 % 26)) % 26 + 97
        else:
            print('该字符不是字母，错误！')
            return -1
        return chr(asciiData)
        
    # 数字部分
    # 参数：options 1加密，0解密，data 数据，num1,num2秘钥参数
    # 返回：成功 加密解密后的数据 失败 -1
    def handleNumber(self, options, data, num1, num2):
        data = int(data)
        num3 = min(num1 % 10, num2 % 10)
        num4 = max(num1 % 10, num2 % 10)
        if (options == 1):
            if (num3 != 0 and data >= 0 and data < num3):
                data = num3 - 1 - data + 0
            if (num3 != num4 and data >= num3 and data <= num4):
                data = ((num4 + data) % (num4 - num3 + 1)) + num3
            if (num4 != 9 and data > num4 and data <= 9):
                data = 9 - data + num4 + 1
        else:
            if (num3 != 0 and data >= 0 and data < num3):
                data = num3 - 1 - data + 0
            if (num3 != num4 and data >= num3 and data <= num4):
                data = ((data - num3) - (num3 + num4)) % (num4 - num3 + 1) + num3
            if (num4 != 9 and data > num4 and data <= 9):
                data = 9 - data + num4 + 1
        return data

    # 符号部分
    # 参数：options 1加密，0解密，data 数据，num1,num2秘钥参数
    # 返回：成功 加密解密后的数据 失败 -1
    def handleSymbol(self, options, data, num1, num2):
        symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '+', '/', '<', '>', '~', '.', '|', '`']
        data = str(data)
        symbolIndex = symbols.index(data)
        if options == 1:
            symbolIndex = (symbolIndex + num1 - num2) % len(symbols)
        else:
            symbolIndex = (symbolIndex - num1 + num2) % len(symbols)
        return symbols[symbolIndex]

# te = threeEncryption()
# pw = '54`4572#.2@.>6*.<5#9'
# en = te.encryptPassword(pw, 5, 20)
# de = te.decryptPassword(en, 5, 20)
# print(pw , ' 加密后密码为 ' , en)
# print(en , ' 解密后密码为 ' , de)
