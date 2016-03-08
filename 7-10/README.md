**加密**

a)用上一个练习的思路编写一个"rot13"翻译器."rot13"是一个古老而又简单的加密方法,它把字母表中的每一个字母用其后的第13个字母来代替. 字母表中前半部分字母将被映射到后半部分,而后半部分字母将被映像到前半部分,大小写保持不变.举例来说,'a'将被替换为'n','X'将被替换为'K';数字和符号不进行翻译.
 
b)在你的解决方案的基础上加一个应用程序,让它提示用户输入准备加密的字符串(这个算法同 时也可以对加密后的字符串进行解密),如下所示: 

    %rot13.py 
    Enter string to rot13: This is a short senterce. 
    Your string to en/decrypt was: [This is a short sentence.]. 
    The rot13 string is: [Guvf vf n fubeg fragrapr.]. 
    
    %rot13.py 
    Enter string to rot13: Guvf vf n fubeg fragrapr. 
    Your string to en/decrypt was: [Guvf vf n fubeg fragrapr.]. 
    The rot13 string is: [This is a short sentence.]. 