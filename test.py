import random
import os

def get_questions(file_name):
    # Gets needed quetion
    questions = []
    #with  open(os.getcwd() + "/mysite/database/" + file_name, encoding="utf-8") as f:
    with  open(os.getcwd() + "/database/" + file_name, encoding="utf-8") as f:
        #f = f.readline().decode('utf-8')
        for line in f:
            questions.append(line.strip().split(';'))
    return random.choice(questions)

def get_module_questions():
    import random
    question_lst = ['quotes.txt', 'logic.txt', 'logic1.txt',
                    'sets.txt', 'functions.txt', 'ratio.txt',
                    'ratio2.txt', 'combinations.txt', 'counting.txt']
    return get_questions(random.choice(question_lst))


def check_position(n):
    # Checks what question to ask
    if n == 0 or n == 40:
        return get_questions('cheat.txt')
    if n == 30:
        return get_questions('talon.txt')
    if n == 20:
        return get_questions('relax.txt')
    if n == 38:
        return get_questions('politex.txt')
    if n == 10:
        return get_questions('almost_talon.txt')
    if n in [2, 7, 12, 17, 22, 28, 35]:
        return get_questions('quotes.txt')
    if n in [5, 15, 25, 34]:
        return get_module_questions()
    if n in [1, 3, 4]:
        return get_questions('logic.txt')
    if n in [6, 8, 9]:
        return get_questions('logic1.txt')
    if n in [11, 13, 14]:
        return get_questions('sets.txt')
    if n in [16, 18, 19]:
        return get_questions('functions.txt')
    if n in [21, 23, 24]:
        return get_questions('ratio.txt')
    if n in [26, 27, 29]:
        return get_questions('ratio2.txt')
    if n in [31, 32, 33]:
        return get_questions('combinations.txt')
    if n in [36, 37, 39]:
        return get_questions('counting.txt')


def find_coords(n):
    # Finds cells coordinates
    '''
    if n < 10 and n > 0:
        x = 95 + 80 * (n - 1) + 40
        y = -40
    if n > 10 and n < 20:
        x = 870
        y = -95 + -(n - 11) * 80 - 40
    if n > 20 and n < 30:
        y = -870
        x = 95 + (29 - n) * 80 + 40
    if n > 30 and n < 40:
        x = 40
        y = -95 + (n - 39) * 80 - 40
    if n == 0:
        x, y = 40, -40
    if n == 10:
        x, y = 870, 40
    if n == 20:
        x, y = 870, -870
    if n == 30:
        x, y = 40, -870
    return x, y'''
    data_dict = {0: (25, 47), 1: (25, 109), 2: (25, 169), 3: (25, 226), 4: (25, 285), 5: (25, 341), 6: (25, 398), 7: (25, 453), 8: (25, 509), 9: (25, 565), 10: (25, 625), 11: (87, 625), 12: (147, 625), 13: (204, 625), 14: (263, 625), 15: (319, 625), 16: (376, 625), 17: (431, 625), 18: (487, 625), 19: (543, 625), 20: (597, 625), 21: (597, 565), 22: (597, 509), 23: (597, 453), 24: (597, 398), 25: (597, 341), 26: (597, 285), 27: (597, 226), 28: (597, 169), 29: (597, 109), 30: (597, 47), 31: (543, 47), 32: (487, 47), 33: (431, 47), 34: (376, 47), 35: (319, 47), 36: (263, 47), 37: (204, 47), 38: (147, 47), 39: (87, 47), 40: (25, 47)}
    return data_dict[n][1], data_dict[n][0]


def dice_generator():
    import random
    return random.randint(1, 6), random.randint(1, 6)


class Player:
    location = 0
    laps = 0

    def __init__(self, name):
        self.name = name

    def movement(self, dice):
        # Returns where to move player
        self.location += dice
        if self.location >= 40:
            self.location -= 40
            self.laps += 1
        #print("Self.location", self.location)
        x2, y2 = find_coords(self.location)
        #print(x2, y2, "LOL")
        return x2, y2
