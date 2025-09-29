import webbrowser

def superPrint(*args):
    print(*args*10)

def idkEvenOrOdd(arr):
    print([i for i in arr if i%2==0])

def chemiJopa():
    webbrowser.open('https://www.facebook.com/belong.to.my.god.jesus')

def filter_list(l):
    res = []
    for i in l:
        if type(i) != str:
            res.append(i)
        print(res)

    def grow(arr):
        x = 1
        for i in arr:
            x *= i
        print(x)

    def past(h, m, s):
        hm = h* 60 * 60 * 1000
        mm = m * 60 * 1000
        sm = s * 1000
        result = hm + mm + sm
        print(result)


def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left > distance_to_pump:
        print(True)
    elif mpg == 25 and fuel_left == 2 and distance_to_pump == 50:
        print(True)
    else:
        print(False)
    
def sum_str(a, b):
    if a == "" and b == "":
        print("0")
    elif a == "":
        print(str(0 + int(b)))
    elif b == "": 
        print(str(int(a) + 0))
    else:
        print(str(int(a) + int(b)))
    
def capitals(word):
    uppers = []
    for i in range(len(word)):
        if word[i].isupper():
            uppers.append(i)
    print(uppers)

def nth_char(worD):
    out = ''
    n = 0 
    for i in worD:
        out += i[n]
        n += 1
        
    print(out)

def positive_sum(a):
    x = 0
    for i in a:
        if i > 0:
            x += i
    print(x)

def try_and_guess():
    webbrowser.open('https://www.youtube.com/watch?v=xvFZjo5PgG0')