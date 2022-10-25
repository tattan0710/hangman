#hangman関数

def hangman():
    import random
    words = ["cat","car","tiger","dog"]
    random_num = random.randint(0,3)
    word = words[random_num]
    wrong = 0
    stages = ["",
              "________        ",
              "|               ",
              "|       |       ",
              "|       O       ",
              "|      /|       ",
              "|      /|       ",
              "|               "
              ]
    rletters = list(word) #未正解の文字のリスト
    board = ["_"] * len(word) #＿のリスト
    win = False
    print("ハングマンへようこそ！")
    

  #ゲーム手順を進めるループ処理

    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char) #正解した文字が何番目にあるのかをインデックス関数を使って取得
            board[cind] = char
            rletters[cind] = '$' #正解した文字を＄に変換
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e])) #間違えた数だけhangman表示
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
        
    #すべて間違えた場合の処理
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたは死にました。正解は{}。".format(word))

hangman()