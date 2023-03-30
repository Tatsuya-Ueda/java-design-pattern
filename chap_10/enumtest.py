"""
enumモジュールに初めて触れる人のための実験コード
・アセットとコード中の名前の対応付けをするために使えそう．ゲームとかで．
・
"""

from enum import Enum


class Role(Enum):
    ROCK = 0
    SCISSOR = 1
    PAPER = 2


print(Role.PAPER)
print(Role(0))
print(Role.PAPER.name)
print(Role(0).name)  # value to member
print(Role.PAPER.value)
print(Role["PAPER"])  # キーでもOK
# print(Role.PAPER < Role.SCISSOR)  # 順序は定義されていない．valueを取り出すのがよいかも

[1, 2, 3][Role.PAPER]
