def print_lyrics(): #defで関数を定義、空の括弧は引数がないことを意味する、ヘッダは":"で終わる
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

print_lyrics() #名前の後ろに括弧をつけて呼び出す

def print_twice(x): #引数が必要となる関数
    print(x)
    print(x)

print_twice("Dennis Moore, ") 

line = "Dennis Moore, " #変数に値を与えてから関数に渡すこともできる
print_twice(line)

def repeat(word, n): #関数は関数から呼び出せる
    print(word * n) #文字列の繰り返し

spam = "Spam, "
repeat(spam, 4)

def first_two_lines():
    repeat(spam, 4)
    repeat(spam, 4)

first_two_lines()

def last_three_lines():
    repeat(spam, 2)
    print("(Lovely Spam, Wonderful Spam!)")
    repeat(spam, 2)

last_three_lines()

def print_verse(): #たくさんの関数を入れ子にして、大きな関数を作成している
    first_two_lines()
    last_three_lines()

print_verse()

