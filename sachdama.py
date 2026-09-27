from PIL import Image, ImageDraw

chessboard = []
counter = 0


def create_chessboard():
    global chessboard
    for i in range(8):
        row = [0] * 8
        chessboard.append(row)


def check_it(x, y):
    # kontrola stĺpca
    for i in range(8):
        if chessboard[i][x] == 1:
            return False

    # kontrola diagonál
    for i in range(8):
        for j in range(8):
            if j + i == x + y:
                if chessboard[i][j] == 1:
                    return False

            if i - j == y - x:
                if chessboard[i][j] == 1:
                    return False

    return True


def obr(img):
    draw = ImageDraw.Draw(img)

    for i in range(8):
        for j in range(8):
            if (i + j) % 2 != 0:
                draw.rectangle(
                    (j * 80, i * 80, (j + 1) * 80, (i + 1) * 80),
                    fill=(0, 0, 0)
                )


def nakresli_damy(img):
    draw = ImageDraw.Draw(img)

    for y in range(8):
        for x in range(8):
            if chessboard[y][x] == 1:
                draw.ellipse(
                    (x * 80 + 10, y * 80 + 10,
                     x * 80 + 70, y * 80 + 70),
                    fill=(255, 255, 255),
                    outline=(0, 0, 0),
                    width=3
                )


def damy(n):
    global chessboard
    global counter

    if n == 8:
        counter += 1

        # nový obrázok pre každé riešenie
        img = Image.new('RGB', (640, 640), color='white')

        obr(img)
        nakresli_damy(img)

        # uloženie obrázka
        img.save(f"riesenie_{counter}.png")

        print(chessboard)
        print("---------------------------------------------")

        return

    for i in range(8):
        if check_it(i, n):
            chessboard[n][i] = 1

            # pokračujeme ďalej a hľadáme aj ostatné riešenia
            damy(n + 1)

            chessboard[n][i] = 0


create_chessboard()
damy(0)

print("Počet riešení:", counter)