from sys import *


# TOKENIZATION

myFile = open(argv[1], "r")
myFileList = myFile.read().split()

# DECLARE VARIABLES AND ARITHMETIC OPERATORS

varDict = {}

operators = ['+', '-', '*', '/']

for index, token in enumerate(myFileList):
    if token == '=' and myFileList[index + 2] not in operators:
        if isinstance(eval(myFileList[index + 1]), bool):
            myFileList[index + 1] = eval(myFileList[index + 1])
        elif myFileList[index + 1].isdigit():
            myFileList[index + 1] = float(myFileList[index + 1])
        else:
            myFileList[index + 1] = eval(myFileList[index + 1])
        varDict.update({myFileList[index - 1]: myFileList[index + 1]})
    elif token == '=' and myFileList[index + 2] == '+':
        if myFileList[index + 3].isdigit():
            floatSum = varDict[myFileList[index + 1]] + float(myFileList[index + 3])
            varDict.update({myFileList[index - 1]: floatSum})
        elif varDict.get(myFileList[index + 1]) is None:
            print(myFileList[index + 1], 'is undefined')
        elif varDict.get(myFileList[index + 3]) is None:
            print(myFileList[index + 3], 'is undefined')
        elif type(varDict[myFileList[index + 1]]) is float and type(varDict[myFileList[index + 3]]) is float:
            floatSum = varDict[myFileList[index + 1]] + varDict[myFileList[index + 3]]
            varDict.update({myFileList[index - 1]: floatSum})
        elif type(varDict[myFileList[index + 1]]) is str and type(varDict[myFileList[index + 3]]) is str:
            strSum = varDict[myFileList[index + 1]] + varDict[myFileList[index + 3]]
            varDict.update({myFileList[index - 1]: strSum})
        elif type(varDict[myFileList[index + 1]]) is bool and type(varDict[myFileList[index + 3]]) is bool:
            boolSum = varDict[myFileList[index + 1]] + varDict[myFileList[index + 3]]
            varDict.update({myFileList[index - 1]: boolSum})
        else:
            print('TypeError')
    elif token == '=' and myFileList[index + 2] == '-':
        if myFileList[index + 3].isdigit():
            floatSub = varDict[myFileList[index + 1]] - float(myFileList[index + 3])
            varDict.update({myFileList[index - 1]: floatSub})
        elif varDict.get(myFileList[index + 1]) is None:
            print(myFileList[index + 1], 'is undefined')
        elif varDict.get(myFileList[index + 3]) is None:
            print(myFileList[index + 3], 'is undefined')
        elif type(varDict[myFileList[index + 1]]) is float and type(varDict[myFileList[index + 3]]) is float:
            floatSub = varDict[myFileList[index + 1]] - varDict[myFileList[index + 3]]
            varDict.update({myFileList[index - 1]: floatSub})
        elif type(varDict[myFileList[index + 1]]) is bool and type(varDict[myFileList[index + 3]]) is bool:
            boolSub = varDict[myFileList[index + 1]] - varDict[myFileList[index + 3]]
            varDict.update({myFileList[index - 1]: boolSub})
        else:
            print('TypeError')
    elif token == '=' and myFileList[index + 2] == '*':
        if myFileList[index + 3].isdigit():
            floatMul = varDict[myFileList[index + 1]] * float(myFileList[index + 3])
            varDict.update({myFileList[index - 1]: floatMul})
        elif varDict.get(myFileList[index + 1]) is None:
            print(myFileList[index + 1], 'is undefined')
        elif varDict.get(myFileList[index + 3]) is None:
            print(myFileList[index + 3], 'is undefined')
        elif type(varDict[myFileList[index + 1]]) is float and type(varDict[myFileList[index + 3]]) is float:
            floatMul = varDict[myFileList[index + 1]] * varDict[myFileList[index + 3]]
            varDict.update({myFileList[index - 1]: floatMul})
        elif type(varDict[myFileList[index + 1]]) is bool and type(varDict[myFileList[index + 3]]) is bool:
            boolMul = varDict[myFileList[index + 1]] * varDict[myFileList[index + 3]]
            varDict.update({myFileList[index - 1]: boolMul})
        else:
            print('TypeError')
    elif token == '=' and myFileList[index + 2] == '/':
        if myFileList[index + 3].isdigit():
            floatDiv = varDict[myFileList[index + 1]] / float(myFileList[index + 3])
            varDict.update({myFileList[index - 1]: floatDiv})
        elif varDict.get(myFileList[index + 1]) is None:
            print(myFileList[index + 1], 'is undefined')
        elif varDict.get(myFileList[index + 3]) is None:
            print(myFileList[index + 3], 'is undefined')
        elif type(varDict[myFileList[index + 1]]) is float and type(varDict[myFileList[index + 3]]) is float:
            floatDiv = varDict[myFileList[index + 1]] / varDict[myFileList[index + 3]]
            varDict.update({myFileList[index - 1]: floatDiv})
        elif type(varDict[myFileList[index + 1]]) is bool and type(varDict[myFileList[index + 3]]) is bool:
            boolDiv = varDict[myFileList[index + 1]] / varDict[myFileList[index + 3]]
            varDict.update({myFileList[index - 1]: boolDiv})
        else:
            print('TypeError')


# IF STATEMENT

statement = False

for index, token in enumerate(myFileList):
    if token == 'if' and myFileList[index+4] == '{':
        firstBraceIndex = index + 4
        firstBraceIndexCopy = firstBraceIndex
        if varDict.get(myFileList[index + 1]) is not None and type(varDict.get(myFileList[index + 1])) is float:
            if varDict.get(myFileList[index + 3]) is not None and type(varDict.get(myFileList[index + 3])) is float:
                statement = eval(str(varDict.get(myFileList[index + 1])) + myFileList[index + 2] + str(varDict.get(myFileList[index + 3])))
                print(1, statement)
            elif myFileList[index + 3].isdigit():
                statement = eval(str(varDict.get(myFileList[index + 1])) + myFileList[index + 2] + myFileList[index + 3])
                print(2, statement)
        elif varDict.get(myFileList[index + 3]) is not None and type(varDict.get(myFileList[index + 3])) is float:
            if myFileList[index + 1].isdigit():
                statement = eval(myFileList[index + 1] + myFileList[index + 2] + str(varDict.get(myFileList[index + 3])))
                print(3, statement)
    if token == '}':
        ifBody = []
        lastBrace = index - 1
        while firstBraceIndex < index - 1:
            ifBody.append(myFileList[firstBraceIndex + 1])
            firstBraceIndex = firstBraceIndex + 1
        while firstBraceIndexCopy < lastBrace:
            myFileList.pop(lastBrace - 1)
            lastBrace = lastBrace - 1
        if statement == True:
            print('gggggggggggggggggggggggggggggggggggg')
            for index, token in enumerate(ifBody):
                if token == '=' and ifBody[index + 2] not in operators:
                    if isinstance(eval(ifBody[index + 1]), bool):
                        ifBody[index + 1] = eval(ifBody[index + 1])
                    elif ifBody[index + 1].isdigit():
                        ifBody[index + 1] = float(ifBody[index + 1])
                    else:
                        ifBody[index + 1] = eval(ifBody[index + 1])
                    varDict.update({ifBody[index - 1]: ifBody[index + 1]})
                elif token == '=' and ifBody[index + 2] == '+':
                    if ifBody[index + 3].isdigit():
                        floatSum = varDict[ifBody[index + 1]] + float(ifBody[index + 3])
                        varDict.update({ifBody[index - 1]: floatSum})
                    elif varDict.get(ifBody[index + 1]) is None:
                        print(ifBody[index + 1], 'is undefined')
                    elif varDict.get(ifBody[index + 3]) is None:
                        print(ifBody[index + 3], 'is undefined')
                    elif type(varDict[ifBody[index + 1]]) is float and type(
                            varDict[ifBody[index + 3]]) is float:
                        floatSum = varDict[ifBody[index + 1]] + varDict[ifBody[index + 3]]
                        varDict.update({ifBody[index - 1]: floatSum})
                    elif type(varDict[ifBody[index + 1]]) is str and type(varDict[ifBody[index + 3]]) is str:
                        strSum = varDict[ifBody[index + 1]] + varDict[ifBody[index + 3]]
                        varDict.update({ifBody[index - 1]: strSum})
                    elif type(varDict[ifBody[index + 1]]) is bool and type(varDict[ifBody[index + 3]]) is bool:
                        boolSum = varDict[ifBody[index + 1]] + varDict[ifBody[index + 3]]
                        varDict.update({ifBody[index - 1]: boolSum})
                    else:
                        print('TypeError')
                elif token == '=' and ifBody[index + 2] == '-':
                    if ifBody[index + 3].isdigit():
                        floatSub = varDict[ifBody[index + 1]] - float(ifBody[index + 3])
                        varDict.update({ifBody[index - 1]: floatSub})
                    elif varDict.get(ifBody[index + 1]) is None:
                        print(ifBody[index + 1], 'is undefined')
                    elif varDict.get(ifBody[index + 3]) is None:
                        print(ifBody[index + 3], 'is undefined')
                    elif type(varDict[ifBody[index + 1]]) is float and type(
                            varDict[ifBody[index + 3]]) is float:
                        floatSub = varDict[ifBody[index + 1]] - varDict[ifBody[index + 3]]
                        varDict.update({ifBody[index - 1]: floatSub})
                    elif type(varDict[ifBody[index + 1]]) is bool and type(varDict[ifBody[index + 3]]) is bool:
                        boolSub = varDict[ifBody[index + 1]] - varDict[ifBody[index + 3]]
                        varDict.update({ifBody[index - 1]: boolSub})
                    else:
                        print('TypeError')
                elif token == '=' and ifBody[index + 2] == '*':
                    if ifBody[index + 3].isdigit():
                        floatMul = varDict[ifBody[index + 1]] * float(ifBody[index + 3])
                        varDict.update({ifBody[index - 1]: floatMul})
                    elif varDict.get(ifBody[index + 1]) is None:
                        print(ifBody[index + 1], 'is undefined')
                    elif varDict.get(ifBody[index + 3]) is None:
                        print(ifBody[index + 3], 'is undefined')
                    elif type(varDict[ifBody[index + 1]]) is float and type(
                            varDict[ifBody[index + 3]]) is float:
                        floatMul = varDict[ifBody[index + 1]] * varDict[ifBody[index + 3]]
                        varDict.update({ifBody[index - 1]: floatMul})
                    elif type(varDict[ifBody[index + 1]]) is bool and type(varDict[ifBody[index + 3]]) is bool:
                        boolMul = varDict[ifBody[index + 1]] * varDict[ifBody[index + 3]]
                        varDict.update({ifBody[index - 1]: boolMul})
                    else:
                        print('TypeError')
                elif token == '=' and ifBody[index + 2] == '/':
                    if ifBody[index + 3].isdigit():
                        floatDiv = varDict[ifBody[index + 1]] / float(ifBody[index + 3])
                        varDict.update({ifBody[index - 1]: floatDiv})
                    elif varDict.get(ifBody[index + 1]) is None:
                        print(ifBody[index + 1], 'is undefined')
                    elif varDict.get(ifBody[index + 3]) is None:
                        print(ifBody[index + 3], 'is undefined')
                    elif type(varDict[ifBody[index + 1]]) is float and type(
                            varDict[ifBody[index + 3]]) is float:
                        floatDiv = varDict[ifBody[index + 1]] / varDict[ifBody[index + 3]]
                        varDict.update({ifBody[index - 1]: floatDiv})
                    elif type(varDict[ifBody[index + 1]]) is bool and type(varDict[ifBody[index + 3]]) is bool:
                        boolDiv = varDict[ifBody[index + 1]] / varDict[ifBody[index + 3]]
                        varDict.update({ifBody[index - 1]: boolDiv})
                    else:
                        print('TypeError')


myFile.close()
