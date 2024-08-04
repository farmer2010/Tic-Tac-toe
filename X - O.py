#настройка
import pygame
import random
import time
import bot_intellect

pygame.init()
screen = pygame.display.set_mode([1800, 1000])
description = "X - O bot"
pygame.display.set_caption(description)

WHITE = (255, 255, 255)
GREY = (125, 125, 125)
darkgrey = (70, 70, 70)
black = (0, 0, 0)
blue = (0, 0, 255)
darkblue = (0, 0, 78)
mousedown = False
steps = 0
X = pygame.image.load("images/X.png")
O = pygame.image.load("images/O.png")
vin = False
font = pygame.font.SysFont(None, 40)
bottoms = []
field = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ]
keep_going = True
queue = "bot"
vers = "new"
timer = pygame.time.Clock()
text = ""

bottoms.append({"x" : 1450, "y" : 520, "size" : 15, "mousetag" : 0, "text" : "Первым ходит игрок", "number" : 0, "group" : 1})
bottoms.append({"x" : 1450, "y" : 560, "size" : 15, "mousetag" : 0, "text" : "Первым ходит компьютер", "number" : 1, "group" : 1})
bottoms.append({"x" : 1450, "y" : 430, "size" : 15, "mousetag" : 0, "text" : "Старый режим игры", "number" : 0, "group" : 2})
bottoms.append({"x" : 1450, "y" : 470, "size" : 15, "mousetag" : 0, "text" : "Новый режим игры", "number" : 1, "group" : 2})

def draw(x, y, size, mousetag, text, word, elem, group):#отрисовка кнопок
    mini_font = pygame.font.SysFont(None, 16)
    save_elem = word[elem]
    renderx = x - size
    rendery = y - size
    pos = pygame.mouse.get_pos()
    save_mousetag = mousetag
    if mousetag == 2:
        save_mousetag = 0
    ifmousetag = False
    for bottom in word:
        if bottom["mousetag"] != 0:
            ifmousetag = True
            break
    if mousedown and save_mousetag == 0 and pos[0] >= renderx - size and pos[0] <= renderx + size and pos[1] >= rendery - size and pos[1] <= rendery + size and not ifmousetag:
        save_mousetag = 1
    if save_mousetag == 1 and not mousedown:
        save_mousetag = 2
    save_elem["mousetag"] = save_mousetag
    if save_mousetag == 2:
        if save_elem["number"] == 1:
            save_elem["number"] = 0
        else:
            save_elem["number"] = 1
    for v in range(len(word)):
        bottom2 = word[v]
        if v != elem and save_elem["number"] == 1 and word[v]["group"] and word[v]["group"] == group:
            word[v]["number"] = 0
    string = text
    draw_text = mini_font.render(string, True, black)
    text_rect = draw_text.get_rect()
    text_rect.x = x + size
    text_rect.y = y - 25
    size2 = size - 4
    size3 = size - 8
    pygame.draw.circle(screen, darkblue, (renderx, rendery), size)
    pygame.draw.circle(screen, darkgrey, (renderx, rendery), size2)
    if save_elem["number"] == 1:
        pygame.draw.circle(screen, darkblue, (renderx, rendery), size3)
    screen.blit(draw_text, text_rect)
    word[elem] = save_elem
    return(word)

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                if bottoms[0]["number"] == 0 and bottoms[1]["number"] == 0:
                    text = "Выберите, кто будет ходить первым, и нажмите F1."
                else:
                    field = [
                        [0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]
                        ]
                    steps = 0
                    vin = False
                    text = ""
                    if bottoms[0]["number"] == 1 and bottoms[1]["number"] == 0:
                        queue = "player"
                    elif bottoms[1]["number"] == 1 and bottoms[0]["number"] == 0:
                        queue = "bot"
                    if bottoms[2]["number"] == 1 and bottoms[3]["number"] == 0:
                        vers = "old"
                    elif bottoms[2]["number"] == 0 and bottoms[3]["number"] == 1:
                        vers = "new"
    steps += 1
    pos = pygame.mouse.get_pos()
    player = 3
    bot = 10
    bot_set = None
    if field[0][0] == bot and field[1][0] == bot and field[2][0] == bot:#проверка победы компьютера
        vin = "bot"
    elif field[0][1] == bot and field[1][1] == bot and field[2][1] == bot:
        vin = "bot"
    elif field[0][2] == bot and field[1][2] == bot and field[2][2] == bot:
        vin = "bot"
    elif field[0][0] == bot and field[0][1] == bot and field[0][2] == bot:
        vin = "bot"
    elif field[1][0] == bot and field[1][1] == bot and field[1][2] == bot:
        vin = "bot"
    elif field[2][0] == bot and field[2][1] == bot and field[2][2] == bot:
        vin = "bot"
    elif field[0][0] == bot and field[1][1] == bot and field[2][2] == bot:
        vin = "bot"
    elif field[0][2] == bot and field[1][1] == bot and field[2][0] == bot:
        vin = "bot"
    elif field[0][0] == player and field[1][0] == player and field[2][0] == player:#проверка победы игрока
        vin = "player"
    elif field[0][1] == player and field[1][1] == player and field[2][1] == player:
        vin = "player"
    elif field[0][2] == player and field[1][2] == player and field[2][2] == player:
        vin = "player"
    elif field[0][0] == player and field[0][1] == player and field[0][2] == player:
        vin = "player"
    elif field[1][0] == player and field[1][1] == player and field[1][2] == player:
        vin = "player"
    elif field[2][0] == player and field[2][1] == player and field[2][2] == player:
        vin = "player"
    elif field[0][0] == player and field[1][1] == player and field[2][2] == player:
        vin = "player"
    elif field[0][2] == player and field[1][1] == player and field[2][0] == player:
        vin = "player"
    if queue == "bot":#ход компьютера
        if vers == "old":
            bot_set = bot_intellect.old(field, bot, player, vin)
        elif vers == "new":
            bot_set = bot_intellect.new(field, bot, player, vin)
    else:#ход игрока
        player_set = None
        if pos[0] >= 400 and pos[0] <= 600 and pos[1] >= 100 and pos[1] <= 300 and field[0][0] == 0 and mousedown:
            player_set = [0, 0]
        elif pos[0] >= 600 and pos[0] <= 800 and pos[1] >= 100 and pos[1] <= 300 and field[1][0] == 0 and mousedown:
            player_set = [1, 0]
        elif pos[0] >= 800 and pos[0] <= 1000 and pos[1] >= 100 and pos[1] <= 300 and field[2][0] == 0 and mousedown:
            player_set = [2, 0]
        elif pos[0] >= 400 and pos[0] <= 600 and pos[1] >= 300 and pos[1] <= 500 and field[0][1] == 0 and mousedown:
            player_set = [0, 1]
        elif pos[0] >= 600 and pos[0] <= 800 and pos[1] >= 300 and pos[1] <= 500 and field[1][1] == 0 and mousedown:
            player_set = [1, 1]
        elif pos[0] >= 800 and pos[0] <= 1000 and pos[1] >= 300 and pos[1] <= 500 and field[2][1] == 0 and mousedown:
            player_set = [2, 1]
        elif pos[0] >= 400 and pos[0] <= 600 and pos[1] >= 500 and pos[1] <= 700 and field[0][2] == 0 and mousedown:
            player_set = [0, 2]
        elif pos[0] >= 600 and pos[0] <= 800 and pos[1] >= 500 and pos[1] <= 700 and field[1][2] == 0 and mousedown:
            player_set = [1, 2]
        elif pos[0] >= 800 and pos[0] <= 1000 and pos[1] >= 500 and pos[1] <= 700 and field[2][2] == 0 and mousedown:
            player_set = [2, 2]
        if player_set:
            field[player_set[0]][player_set[1]] = player
            queue = "bot"
    if bot_set:
        if (0 in field[0] or 0 in field[1] or 0 in field[2]) and steps != 1:
            time.sleep(1)
        field[bot_set[0]][bot_set[1]] = bot
        queue = "player"
    if vin == "bot":
        text = "Компьютер победил. Нажмите F1, чтобы начать новую игру."
    elif vin == "player":
        text = "Вы победили. Нажмите F1, чтобы начать новую игру."
    elif not (0 in field[0] or 0 in field[1] or 0 in field[2]):
        text = "Ничья. Нажмите F1, чтобы начать новую игру."
    screen.fill(WHITE)#отрисовка
    pygame.draw.rect(screen, darkgrey, (1400, 0, 400, 1000))
    pygame.draw.rect(screen, darkgrey, (0, 800, 1800, 200))
    pygame.draw.rect(screen, black, (395, 95, 610, 610))
    pygame.draw.rect(screen, WHITE, (400, 100, 600, 600))
    pygame.draw.rect(screen, GREY, (599, 100, 2, 600))
    pygame.draw.rect(screen, GREY, (799, 100, 2, 600))
    pygame.draw.rect(screen, GREY, (400, 299, 600, 2))
    pygame.draw.rect(screen, GREY, (400, 499, 600, 2))
    font_text = font.render(text, True, blue)
    text_rect = font_text.get_rect()
    text_rect.x = 300
    text_rect.y = 400
    for x in range(3):
        for y in range(3):
            if field[x][y] == 10:
                screen.blit(X, (428 + x * 200, 128 + y * 200))
            elif field[x][y] == 3:
                screen.blit(O, (421 + x * 200, 121 + y * 200))
    for i in range(len(bottoms)):
        bottom = bottoms[i]
        bottoms = draw(bottom["x"], bottom["y"], bottom["size"], bottom["mousetag"], bottom["text"], bottoms, i, bottom["group"])
    screen.blit(font_text, text_rect)
    pygame.display.update()
    timer.tick(20)
pygame.quit()
