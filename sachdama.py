from PIL import Image, ImageDraw
chessboard = []
counter = 0
img = Image.new('RGB', (640, 640), color = 'white')
draw = ImageDraw.Draw(img)



def create_chessboard():
    global chessboard
    for i in range(8):
        row = [0] * 8
        chessboard.append(row)

def check_it(x,y):
    for i in range(0,8):
        if chessboard[y][x] == 1:
            return False
        if chessboard[i][x] == 1:
            return False
    for i in range(0,8):
        for j in range(0,8):
            if j + i == x + y:
                if chessboard[i][j] == 1:
                    return False
            if i - j == y - x:
                if chessboard[i][j] == 1:
                    return False
    return True

def obr():
    for i in range(0,8):
        for j in range(0,8):
            if (i + j) % 2 != 0:
                img.paste((0,0,0), (j*80,i*80,(j+1)*80,(i+1)*80))

def nakresli_damy():
    for y in range(8):
        for x in range(8):
            if chessboard[y][x] == 1:
                draw.ellipse((x * 80 + 10, y * 80 + 10, x * 80 + 70, y * 80 + 70), fill=(255, 255, 255), outline=(0, 0, 0), width=3)

def damy(n):
    global chessboard
    global counter
    if n == 8:
        counter += 1
        nakresli_damy()
        print(chessboard)
        print("---------------------------------------------")
        return True
    else:
        for i in range(0,8):
            if check_it(i,n):
                chessboard[n][i] = 1
                if damy(n+1):
                    return True
                chessboard[n][i] = 0
    return False


create_chessboard()
obr()
damy(0)
img.show()