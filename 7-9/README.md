* 7.9 翻译。

（a）编写一个字符翻译程序（功能类似于Unix中的tr命令）。我们将这个函数叫做tr()，它有三个字符串做参数：原字符串、目的字符串、基本字符串，语法定义如下：

```def tr(srcstr, dststr, string)```

srcstr的内容是你打算“翻译”的字符集合， dsrstr是翻译后得到的字符集合，而string是你打算进行翻译操作的字符串。举例来说，如果srcstr == 'abc', dststr == 'mno', string == 'abcdef'，那么tr()的输出将是'mnodef'。注意这里len(srcstr) == len(dststr)。

在这个练习里，你可以使用内建函数chr()和ord()，但他们并不一定是解决这个问题所必不可少的函数。

（b）在这个函数里增加一个标志参数，来处理不区分大小写的翻译问题。

（c）修改你的程序，使他们能够处理删除字符的操作。字符串srcstr中不能够映射到字符串dststr中字符的多余字符都将被过滤掉。换句话说，这些字符没有映射到dststr字符串中的任何字符，因此就从函数返回的字符里被过滤掉了。举例来说：如果 srcstr == 'abcdef', dststr == 'mno', string == 'abcdefghi'，那么tr()将输出'mnoghi'。注意这里len(srcstr) >= len(dststr)。