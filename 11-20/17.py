
"""
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
编写一个程序，根据控制台输入的交易日志计算银行账户的净额。交易日志格式如下：

D 100
W 200


D means deposit while W means withdrawal.
D表示存款,W表示取款。

Suppose the following input is supplied to the program:
假设向程序提供了以下输入：

D 300
D 300
W 200
D 100

Then, the output should be:
那么，输出应该是：

500
"""
#本人答案
money=0
while True:
    s=input()
    if not s:
        break
    a,b=s.split()
    if a=='D':
        money+=int(b)
    elif a=='W':
        money-=int(b)
    else:
        break
print(money)

#参考答案
netAmount = 0
while True:
    s = input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass

print (netAmount)
