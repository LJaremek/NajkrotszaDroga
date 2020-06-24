### Author: ŁJ
### Date: 16.05.2020


from copy import deepcopy


# Dane wejsciowe:
# mapa
# x poczatku drogi
# y poczatku drogi
# x konca drogi
# y konca drogi
#
# Dane wyjsciowe:
# True / False - istnieje droga, nie istnieje
# mapa z numerowaną drogą
def szukaj_drogi(mapa, x, y, Cx, Cy): # mapa, x and y of point, x and y of aim
    max_x = len(mapa)-1
    max_y = len(mapa[0])-1
    save = deepcopy(mapa)
    index = 0
    stos = [(x, y, str(index))]
    dojscie_istnieje = False
    if (x, y) == (Cx, Cy):
        return []
    pary = [(x, y, 0)]
    while len(pary) > 0:
        stos = sorted(stos, key = lambda komplet: int(komplet[2]))
        stos = stos[::-1]
        x, y, index = stos.pop()
        if save[x+1][y] == 0:
            save[x+1][y] = str(int(index)+1)
            stos.append((x+1, y, str(int(index)+1)))
        if save[x-1][y] == 0:
            save[x-1][y] = str(int(index)+1)
            stos.append((x-1, y, str(int(index)+1)))
        if save[x][y+1] == 0:
            save[x][y+1] = str(int(index)+1)
            stos.append((x, y+1, str(int(index)+1)))
        if save[x][y-1] == 0:
            save[x][y-1] = str(int(index)+1)
            stos.append((x, y-1, str(int(index)+1)))
        if type(save[Cx][Cy]) == str:
            dojscie_istnieje = True
            break
    return (dojscie_istnieje, save)


# Dane wejsciowe:
# mapa
# x poczatku drogi
# y poczatku drogi
# x konca drogi
# y konca drogi
#
# Dane wyjsciowe:
# lista krotek ze współrzędnymi drogi
def podaj_najkrotsza_droge(mapa, x, y, Cx, Cy):
    istnieje, save = szukaj_drogi(mapa, x, y, Cx, Cy)
    if istnieje:
        max_x = len(mapa)-1
        max_y = len(mapa[0])-1
        trasa = [(Cx, Cy)]
        numer = int(save[Cx][Cy])-1
        Bx, By = (Cx, Cy)
        while numer != 0:
            if 0 <= Bx <= max_x and 0 <= By <= max_y:
                if Bx != max_x and type(save[Bx+1][By]) == str and (Bx+1, By) not in trasa: 
                    La = int(save[Bx+1][By])
                else:
                    La = max_x*max_y
                if Bx != 0 and type(save[Bx-1][By]) == str and (Bx-1, By) not in trasa:
                    Lb = int(save[Bx-1][By])
                else:
                    Lb = max_x*max_y
                if By != max_y and type(save[Bx][By+1]) == str and (Bx, By+1) not in trasa:
                    Lc = int(save[Bx][By+1])
                else:
                    Lc = max_x*max_y
                if By != 0 and type(save[Bx][By-1]) == str and (Bx, By-1) not in trasa:
                    Ld = int(save[Bx][By-1])
                else:
                    Ld = max_x*max_y
                    
                if La == min(La, Lb, Lc, Ld, numer):
                    Bx += 1
                elif Lb == min(La, Lb, Lc, Ld, numer):
                    Bx -= 1
                elif Lc == min(La, Lb, Lc, Ld, numer):
                    By += 1
                elif Ld == min(La, Lb, Lc, Ld, numer):
                    By -= 1
                else:
                    numer -= 1
                trasa.append((Bx, By))
        return trasa
    else:
        return []

mapa = [[1, 0, 1, 1, 1], # przykladowa mapa
        [1, 0, 1, 0, 0], # 0 - droga
        [1, 0, 1, 0, 1], # 1 - sciana
        [0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]]

trasa = podaj_najkrotsza_droge(mapa, 0, 1, 1, 4) # trasa z dojsciem z punktu (0, 1) do (1, 4)

for x, y in trasa:
    mapa[x][y] = "x" # zapelnienie trasy "x" aby byla widoczna

