lifes = 3
def game():
    progress = True
    word = ["hunt"]
    global lifes

    word_in_play = get_word(word)
    template = start_template(word_in_play)
    welcom_speech(list_to_string_convert(template))
    while progress:
        user_quess = user_input()
        template = build_template(template,word_in_play,user_quess)
        guessed = list_to_string_convert(template)
        print_result(guessed)
        progress = check_win(guessed)
        print(f'осталось {lifes} жизней')
        if lifes == 0:
            print('вы проиграли')
            break
        if not progress:
            print("вы выйграли")
        
def welcom_speech(t):
    print(f'''загаданное слово состоит из {len(t)} букв {t}''')

def start_template(w):
    t = []
    for _ in w:
        t.append('_')
    return t

def list_to_string_convert(t):
    s = ''
    return s.join(t)

def get_word(w):
    return w[0]

def user_input():
    return input(f'введите только 1 букву')

def build_template(t,w,g=''):
    global lifes
    if g not in w:
        lifes -= 1
    for i in range(len(w)):
        if t[i] == '_':
            if w[i] == g:
                t[i] = w[i]
            else:
                t[i] = '_'
                
    return t
def print_result(g):
    print(f'результат: {g}')

def check_win(g):
    if '_' in g :
        return True
    else:
        return False

print(game())