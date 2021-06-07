from PIL import Image

MSG = '''Итак, ты все-таки решил мой стф. Я тебя поздравляю, ты, на самом деле выиграл 500 рублей, напиши мне в ЛС фразу "Люди с именем на А и ростом меньше среднего обычно проигрывают в силовой борьбе"'''

numbers = []

for i in MSG:
    numbers.append(bin(ord(i) ^ 9245).replace('0b', ''))

size = len(numbers) * 25
if size % 2 != 0:
    size += 1

size //= 2

image = Image.new("RGB", (size, size))

dataset = [Image.open(f'res/{x}.png') for x in range(2)]

x = 0
y = 0

for num in numbers:
    for i in num:
        image.paste(dataset[int(i)], (x + 28, y + 28))
        x += 28
        if x + 70 >= size:
            x = 0
            y += 28
    print(num)

image.save('ready.png')