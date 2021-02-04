import random
def hangman(word):
    """
    Retruns None
    :param word: 当ててほしい言葉
    """
    wrong = 0
    stages = [  "",
                "----------          ",
                "|         |         ",
                "|         O         ",
                "|        /|\        ",
                "|        / \        ",
                "|                   ",
             ]
    rletters = list(word)       #wordの文字を一文字ずつ分解してリストにしたもの
    board = ["_"] * len(word)   #文字列のリスト
    win = False
    print("ハングマンへようこそ")
    # for stage in stages:
    #     print(stage)
    # print(board)
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね : "
        char = input(msg)
        if char in rletters:
            print("正解")
            cind = rletters.index(char) #indexメソッドはある文字が文字列内で最初に現れる位置を探す
            board[cind] = char
            rletters[cind] = "$"
        else:
            print("不正解")
            wrong += 1
        print(" ".join(board))
        # for i in range(wrong):
        #     print(stages[i])
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        # print("\n".join(stages[1]))
        print("あなたの負け！正解は{}.".format(word))

question_list = ["cat","dog","man"]
list_word = question_list[random.randint(0,2)]
hangman(list_word)