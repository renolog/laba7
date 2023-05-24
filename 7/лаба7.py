from PIL import Image, ImageFilter
def r1():
    a = Image.open('1..jpeg')
    a.show()

    widht, height = a.size
    format = a.format
    mode = a.mode

    print('Ширина: ', widht)
    print('Высота: ', height)
    print('Формат: ', format)
    print('цветовая модель: ', mode)

def r2():
    a = Image.open('2..jpeg')
    a.show()

    b = a.resize((a.width // 3, a.height // 3))
    b.show()

    c = b.rotate(180)
    c.save('2.1..jpeg')
    c.show()

    d = b.transpose(Image.FLIP_LEFT_RIGHT)
    d.save('2.2..jpeg')
    d.show()

def r3():
    a = ['1..jpeg', '2..jpeg', '3..jpeg', '4..jpeg', '5..jpeg']
    for x in a:
        with Image.open(x) as b:
            b.load()
            c = b.filter(ImageFilter.SMOOTH)
            d = c.filter(ImageFilter.FIND_EDGES)
            d.show()
            d.save("3.1" + x)

def r4():
    a = Image.open("5..jpeg")
    b = Image.open("6.jpg")

    b = b.resize([1920, 1200])
    a.paste(b, [300, 300], mask = b)
    a.show()

r1()
r2()
r3()
r4()
