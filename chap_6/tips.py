"""
tips: 浅いコピーと深いコピー
"""

import copy


def test1():  # shallow
    l = [[1], 2]
    ll = copy.copy(l)
    print(l, ll)
    # -> [[1], 2] [[1], 2] 一見コピーがとれているように見えるが，
    ll[0][0] = 100
    print(l, ll)
    # -> [[100], 2] [[100], 2] オブジェクトの中のオブジェクトについては(可能な限り)参照がコピーされてしまうので，一緒に変更されてしまう


def test2():  # deep
    l = [[1], 2]
    ll = copy.deepcopy(l)
    print(l, ll)
    # -> [[1], 2] [[1], 2]
    ll[0][0] = 100
    print(l, ll)
    # -> [[1], 2] [[100], 2] 深いコピーなら完全に別オブジェクト


test1()
print()
test2()
