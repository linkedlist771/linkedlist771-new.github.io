def cond():
     x = 3
     if x < 5:
         return 'yes'
     else:
        return 'no'

# 查看源代码的字节码格式

"""
1: 实际的字节码指令
"""
print(f"字节码指令: {cond.__code__.co_code}")


"""
2: 字节码指令对应的操作码
"""

import dis
print(f"字节码指令对应的操作码:")
dis.dis(cond)
