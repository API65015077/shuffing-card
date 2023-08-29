import time
deck = []
clups, diamonds, hearts, spades = [], [], [], []
start = time.time()
for i in range(1, 14):
    clups.append(i)
    diamonds.append(i)
    hearts.append(i)
    spades.append(i)

def draw_card(list):
    return list.pop()

def shuffle_in_deck(list):
    for j in range(50):
        time.sleep(0.0001)
        shuff = int(str(time.time())[-1])
        shuff2 = int(str(time.time())[-1])
        if shuff2 + shuff >13:
            shuff = 0
        list.append(list.pop(shuff))

def name_of_card(list, i , symbol):
    if list[i] == 1:
        list[i] = 'A'+' '+symbol
    elif list[i] == 11:
        list[i] = 'J'+' '+symbol
    elif list[i] == 12:
        list[i] = 'Q'+' '+symbol
    elif list[i] == 13:
        list[i] = 'K'+' '+symbol
    else:
        list[i] = 'C' + str(i+1)+' '+symbol

for i in range(0, 13):
    name_of_card(clups, i, "♣️")
    name_of_card(diamonds, i, "♦️")
    name_of_card(hearts, i, "♥️")
    name_of_card(spades, i, "♠️")

shuffle_in_deck(clups)
shuffle_in_deck(diamonds)
shuffle_in_deck(hearts)
shuffle_in_deck(spades)

deck.extend(clups)
deck.extend(diamonds)
deck.extend(hearts)
deck.extend(spades)
shuffle_in_deck(deck)

# print(deck)
# print(len(deck))
# print(deck)
print(draw_card(deck))
print(draw_card(deck))
# print(deck)
end = time.time()
print("เวลาที่ใช้ :",end - start)

