import random

def set_line(a, b, c, ob):
    if a[0] == ob and b[0] == ob and c[0] == 0:
        return((c[1], c[2]))
    elif a[0] == ob and c[0] == ob and b[0] == 0:
        return((b[1], b[2]))
    elif b[0] == ob and c[0] == ob and a[0] == 0:
        return((a[1], a[2]))

def pos_corner(pos): return(pos == (0, 0) or pos == (2, 0) or pos == (2, 2) or pos == (0, 2))

def pos_parallel(pos): return(pos == (1, 0) or pos == (2, 1) or pos == (1, 2) or pos == (0, 1))

def victory(pos, field, X):
    field[pos[0]][pos[1]] = X
    if field[0][0] == X and field[1][0] == X and field[2][0] == X:#проверка победы
        field[pos[0]][pos[1]] = 0
        return(True)
    elif field[0][1] == X and field[1][1] == X and field[2][1] == X:
        field[pos[0]][pos[1]] = 0
        return(True)
    elif field[0][2] == X and field[1][2] == X and field[2][2] == X:
        field[pos[0]][pos[1]] = 0
        return(True)
    elif field[0][0] == X and field[0][1] == X and field[0][2] == X:
        field[pos[0]][pos[1]] = 0
        return(True)
    elif field[1][0] == X and field[1][1] == X and field[1][2] == X:
        field[pos[0]][pos[1]] = 0
        return(True)
    elif field[2][0] == X and field[2][1] == X and field[2][2] == X:
        field[pos[0]][pos[1]] = 0
        return(True)
    elif field[0][0] == X and field[1][1] == X and field[2][2] == X:
        field[pos[0]][pos[1]] = 0
        return(True)
    elif field[0][2] == X and field[1][1] == X and field[2][0] == X:
        field[pos[0]][pos[1]] = 0
        return(True)
    field[pos[0]][pos[1]] = 0
    return(False)

def set_corner(pos, field, X):
    if pos_corner(pos):
        if pos == (0, 0) and field[1][0] == X and field[0][1] == X:
            return(True)
        elif pos == (2, 0) and field[1][0] == X and field[2][1] == X:
            return(True)
        elif pos == (2, 2) and field[2][1] == X and field[1][2] == X:
            return(True)
        elif pos == (0, 2) and field[1][2] == X and field[0][1] == X:
            return(True)
    return(False)

def corner(pos, field, X):
    if pos_parallel(pos):
        if pos == (1, 0) and (field[0][1] == X or field[2][1] == X):
            return(True)
        elif pos == (2, 1) and (field[1][0] == X or field[1][2] == X):
            return(True)
        elif pos == (1, 2)and (field[2][1] == X or field[0][1] == X):
            return(True)
        elif pos == (0, 1)and (field[1][0] == X or field[2][0] == X):
            return(True)
    return(False)

def center_corner(pos, field, X):
    if pos == (1, 1):
        if (field[1][0] == X and field[0][1] == X) or (field[1][0] == X and field[2][1] == X) or (field[2][1] == X and field[1][2] == X) or (field[1][2] == X and field[0][1] == X):
            return(True)
    return(False)

def center_triangle(pos, field, X): return(pos == (1, 1) and (field[0][0] == X or field[2][0] == X or field[2][2] == X or field[0][2] == X))

def set_triangle(pos, field, X):
    if pos_corner(pos):
        if pos == (0, 0) or pos == (2, 2):
            if field[1][1] == X and (field[2][0] == X or field[0][2] == X):
                return(True)
        elif pos == (2, 0) or pos == (0, 2):
            if field[1][1] == X and (field[0][0] == X or field[2][2] == X):
                return(True)
    return(False)

def corner_triangle(pos, field, X):
    if pos_corner(pos):
        if field[1][1] == X:
            return(True)
    return(False)

def old(field, X, O, vin):
    if (not vin) and (0 in field[0] or 0 in field[1] or 0 in field[2]):
        if set_line([field[0][0], 0, 0], [field[1][0], 1, 0], [field[2][0], 2, 0], X):#перекрывать свои линии
            bot_set = set_line([field[0][0], 0, 0], [field[1][0], 1, 0], [field[2][0], 2, 0], X)
        elif set_line([field[0][1], 0, 1], [field[1][1], 1, 1], [field[2][1], 2, 1], X):
            bot_set = set_line([field[0][1], 0, 1], [field[1][1], 1, 1], [field[2][1], 2, 1], X)
        elif set_line([field[0][2], 0, 2], [field[1][2], 1, 2], [field[2][2], 2, 2], X):
            bot_set = set_line([field[0][2], 0, 2], [field[1][2], 1, 2], [field[2][2], 2, 2], X)
        elif set_line([field[0][0], 0, 0], [field[0][1], 0, 1], [field[0][2], 0, 2], X):
            bot_set = set_line([field[0][0], 0, 0], [field[0][1], 0, 1], [field[0][2], 0, 2], X)
        elif set_line([field[1][0], 1, 0], [field[1][1], 1, 1], [field[1][2], 1, 2], X):
            bot_set = set_line([field[1][0], 1, 0], [field[1][1], 1, 1], [field[1][2], 1, 2], X)
        elif set_line([field[2][0], 2, 0], [field[2][1], 2, 1], [field[2][2], 2, 2], X):
            bot_set = set_line([field[2][0], 2, 0], [field[2][1], 2, 1], [field[2][2], 2, 2], X)
        elif set_line([field[0][0], 0, 0], [field[1][1], 1, 1], [field[2][2], 2, 2], X):
            bot_set = set_line([field[0][0], 0, 0], [field[1][1], 1, 1], [field[2][2], 2, 2], X)
        elif set_line([field[0][2], 0, 2], [field[1][1], 1, 1], [field[2][0], 2, 0], X):
            bot_set = set_line([field[0][2], 0, 2], [field[1][1], 1, 1], [field[2][0], 2, 0], X)
        else:
            if set_line([field[0][0], 0, 0], [field[1][0], 1, 0], [field[2][0], 2, 0], O):#перекрывать линии соперника
                bot_set = set_line([field[0][0], 0, 0], [field[1][0], 1, 0], [field[2][0], 2, 0], O)
            elif set_line([field[0][1], 0, 1], [field[1][1], 1, 1], [field[2][1], 2, 1], O):
                bot_set = set_line([field[0][1], 0, 1], [field[1][1], 1, 1], [field[2][1], 2, 1], O)
            elif set_line([field[0][2], 0, 2], [field[1][2], 1, 2], [field[2][2], 2, 2], O):
                bot_set = set_line([field[0][2], 0, 2], [field[1][2], 1, 2], [field[2][2], 2, 2], O)
            elif set_line([field[0][0], 0, 0], [field[0][1], 0, 1], [field[0][2], 0, 2], O):
                bot_set = set_line([field[0][0], 0, 0], [field[0][1], 0, 1], [field[0][2], 0, 2], O)
            elif set_line([field[1][0], 1, 0], [field[1][1], 1, 1], [field[1][2], 1, 2], O):
                bot_set = set_line([field[1][0], 1, 0], [field[1][1], 1, 1], [field[1][2], 1, 2], O)
            elif set_line([field[2][0], 2, 0], [field[2][1], 2, 1], [field[2][2], 2, 2], O):
                bot_set = set_line([field[2][0], 2, 0], [field[2][1], 2, 1], [field[2][2], 2, 2], O)
            elif set_line([field[0][0], 0, 0], [field[1][1], 1, 1], [field[2][2], 2, 2], O):
                bot_set = set_line([field[0][0], 0, 0], [field[1][1], 1, 1], [field[2][2], 2, 2], O)
            elif set_line([field[0][2], 0, 2], [field[1][1], 1, 1], [field[2][0], 2, 0], O):
                bot_set = set_line([field[0][2], 0, 2], [field[1][1], 1, 1], [field[2][0], 2, 0], O)
            else:
                corner_list = []
                if field[0][0] == 0 and field[1][0] == O and field[0][1] == O:#проверка "уголка" противника на северо-востоке
                    corner_list.append((0, 0))
                if field[2][0] == 0 and field[1][0] == O and field[2][1] == O:#проверка "уголка" противника на северо-западе
                    corner_list.append((2, 0))
                if field[2][2] == 0 and field[1][2] == O and field[2][1] == O:#проверка "уголка" противника на юго-западе
                    corner_list.append((2, 2))
                if field[0][2] == 0 and field[1][2] == O and field[0][1] == O:#проверка "уголка" противника на юго-востоке
                    corner_list.append((0, 2))
                if field[1][1] == 0 and field[1][0] == O and field[0][1] == O:#проверка отзеркаленного "уголка" противника на северо-востоке
                    corner_list.append((1, 1))
                if field[1][1] == 0 and field[1][0] == O and field[2][1] == O:#проверка отзеркаленного "уголка" противника на северо-западе
                    corner_list.append((1, 1))
                if field[1][1] == 0 and field[1][2] == O and field[2][1] == O:#проверка отзеркаленного "уголка" противника на юго-западе
                    corner_list.append((1, 1))
                if field[1][1] == 0 and field[1][2] == O and field[0][1] == O:#проверка отзеркаленного "уголка" противника на юго-востоке
                    corner_list.append((1, 1))
                if field[1][0] == 0 and field[0][0] == O and (field[0][0] == O or field[2][0] == O):#проверка пары повернутых "уголков" противника на севере
                    corner_list.append((1, 0))
                if field[1][2] == 0 and field[0][0] == O and (field[0][2] == O or field[2][2] == O):#проверка пары повернутых "уголков" противника на юге
                    corner_list.append((1, 2))
                if field[0][1] == 0 and field[0][0] == O and (field[0][0] == O or field[0][2] == O):#проверка пары повернутых "уголков" противника на востоке
                    corner_list.append((0, 1))
                if field[1][0] == 0 and field[0][0] == O and (field[2][0] == O or field[2][2] == O):#проверка пары повернутых "уголков" противника на западе
                    corner_list.append((2, 1))
                if corner_list:
                    bot_set = random.choice(corner_list)
                else:
                    if set_line((0, 2, field[0][2]), (1, 1, field[1][1]), (2, 2, field[2][2]), O):#проверка "треугольника" противника на юге
                        bot_set = set_line((0, 2, field[0][2]), (1, 1, field[1][1]), (2, 2, field[2][2]), O)
                    elif set_line((0, 0, field[0][0]), (1, 1, field[1][1]), (2, 0, field[2][0]), O):#проверка "треугольника" противника на севере
                        bot_set = set_line((0, 0, field[0][0]), (1, 1, field[1][1]), (2, 0, field[2][0]), O)
                    elif set_line((0, 0, field[0][0]), (1, 1, field[1][1]), (0, 2, field[0][2]), O):#проверка "треугольника" противника на востоке
                        bot_set = set_line((0, 0, field[0][0]), (1, 1, field[1][1]), (0, 2, field[0][2]), O)
                    elif set_line((2, 0, field[2][0]), (1, 1, field[1][1]), (2, 2, field[2][2]), O):#проверка "треугольника" противника на западе
                        bot_set = set_line((2, 0, field[2][0]), (1, 1, field[1][1]), (2, 2, field[2][2]), O)
                    else:
                        computer_corner_list = []
                        if field[0][0] == 0 and field[1][0] == X and field[0][1] == X:#проверка "уголка" на северо-востоке
                            computer_corner_list.append((0, 0))
                        if field[2][0] == 0 and field[1][0] == X and field[2][1] == X:#проверка "уголка" на северо-западе
                            computer_corner_list.append((2, 0))
                        if field[2][2] == 0 and field[1][2] == X and field[2][1] == X:#проверка "уголка" на юго-западе
                            computer_corner_list.append((2, 2))
                        if field[0][2] == 0 and field[1][2] == X and field[0][1] == X:#проверка "уголка" на юго-востоке
                            computer_corner_list.append((0, 2))
                        if field[1][1] == 0 and field[1][0] == X and field[0][1] == X:#проверка отзеркаленного "уголка" на северо-востоке
                            computer_corner_list.append((1, 1))
                        if field[1][1] == 0 and field[1][0] == X and field[2][1] == X:#проверка отзеркаленного "уголка" на северо-западе
                            computer_corner_list.append((1, 1))
                        if field[1][1] == 0 and field[1][2] == X and field[2][1] == X:#проверка отзеркаленного "уголка" на юго-западе
                            computer_corner_list.append((1, 1))
                        if field[1][1] == 0 and field[1][2] == X and field[0][1] == X:#проверка отзеркаленного "уголка" на юго-востоке
                            computer_corner_list.append((1, 1))
                        if field[1][0] == 0 and field[0][0] == X and (field[0][0] == X or field[2][0] == X):#проверка пары повернутых "уголков" на севере
                            computer_corner_list.append((1, 0))
                        if field[1][2] == 0 and field[0][0] == X and (field[0][2] == X or field[2][2] == X):#проверка пары повернутых "уголков" на юге
                            computer_corner_list.append((1, 2))
                        if field[0][1] == 0 and field[0][0] == X and (field[0][0] == X or field[0][2] == X):#проверка пары повернутых "уголков" на востоке
                            computer_corner_list.append((0, 1))
                        if field[1][0] == 0 and field[0][0] == X and (field[2][0] == X or field[2][2] == X):#проверка пары повернутых "уголков" на западе
                            computer_corner_list.append((2, 1))
                        if computer_corner_list:
                            bot_set = random.choice(computer_corner_list)
                        else:
                            if set_line((0, 2, field[0][2]), (1, 1, field[1][1]), (2, 2, field[2][2]), X):#проверка "треугольника" на юге
                                bot_set = set_line((0, 2, field[0][2]), (1, 1, field[1][1]), (2, 2, field[2][2]), X)
                            elif set_line((0, 0, field[0][0]), (1, 1, field[1][1]), (2, 0, field[2][0]), X):#проверка "треугольника" на севере
                                bot_set = set_line((0, 0, field[0][0]), (1, 1, field[1][1]), (2, 0, field[2][0]), X)
                            elif set_line((0, 0, field[0][0]), (1, 1, field[1][1]), (0, 2, field[0][2]), X):#проверка "треугольника" на востоке
                                bot_set = set_line((0, 0, field[0][0]), (1, 1, field[1][1]), (0, 2, field[0][2]), X)
                            elif set_line((2, 0, field[2][0]), (1, 1, field[1][1]), (2, 2, field[2][2]), X):#проверка "треугольника" на западе
                                bot_set = set_line((2, 0, field[2][0]), (1, 1, field[1][1]), (2, 2, field[2][2]), X)
                            else:
                                random_pos = (random.randint(0, 2), random.randint(0, 2))
                                while field[random_pos[0]][random_pos[1]] != 0:
                                    random_pos = (random.randint(0, 2), random.randint(0, 2))
                                bot_set = random_pos
        return(bot_set)

def new(field, X, O, vin):
    if (not vin) and (0 in field[0] or 0 in field[1] or 0 in field[2]):
        set_list = []
        score_list = []
        bot_set = None
        score = 0
        for x in range(len(field)):
            for y in range(len(field[x])):
                if field[x][y] == 0:
                    set_list.append((x, y))
                    if 0 in field[0] or 0 in field[1] or 0 in field[2]:#если поле пустое
                        if pos_corner((x, y)):
                            score = 2.7
                        elif pos_parallel((x, y)):
                            score = 2.8
                        else:
                            score = 2.85
                    if victory((x, y), field, X):#проверка победы компьютера
                        score = 100
                    elif victory((x, y), field, O):#проверка победы игрока
                        score = 98
                    else:#проверка фигур
                        if set_corner((x, y), field, X):
                            score = 50
                        elif set_corner((x, y), field, O):
                            score = 49
                        elif corner((x, y), field, X):
                            score = 40
                        elif corner((x, y), field, O):
                            score = 39
                        elif center_corner((x, y), field, O):
                            score = 40
                        elif center_corner((x, y), field, X):
                            score = 39
                        elif center_triangle((x, y), field, X):
                            score = 50
                        elif center_triangle((x, y), field, O):
                            score = 49
                        elif set_triangle((x, y), field, X):
                            score = 50
                        elif set_triangle((x, y), field, O):
                            score = 49
                        elif corner_triangle((x, y), field, X):
                            score = 50
                        elif corner_triangle((x, y), field, O):
                            score = 49
                    score_list.append(score + (random.randint(0, 99) / 100))
            if score_list:
                scmax = max(score_list)
            for s in range(len(score_list)):
                if scmax == score_list[s]:
                    bot_set = set_list[s]
        return(bot_set)
