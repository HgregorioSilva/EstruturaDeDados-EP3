Matriz1 = [[0,1,0],[1,1,1],[0,0,0],[1,0,1]]
Matriz2 = [[1,0,1,0,1],[1,0,1,0,1],[1,1,1,1,1]]
Matriz3 = [[0,0,1,1,0,0,1,0,1,0],[0,1,1,0,0,0,1,0,1,0],[0,0,1,1,0,0,1,1,1,0],[0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,1,0,1,0],[0,0,1,0,0,1,1,1,1,1],[1,1,1,1,1,0,0,0,0,0],[0,0,1,0,0,0,1,1,1,0],[0,0,1,0,0,0,1,1,1,0]]

def trocaMatriz(Matriz):
    x = 0
    while x < len(Matriz):
        y = 0
        region = 0
        while y < len(Matriz[x]):
            if (Matriz [x][y] == 0):
                y = y + 1
            else:
                if ((Matriz[x-1][y] == 0) and (Matriz[x][y-1] == 0)):
                    region = region + 1
                    Matriz[x][y] = region
                    y = y + 1
                else:
                    Matriz[x][y] = region
                    y = y + 1
                
                   
                    
        x = x + 1
    return Matriz


print(trocaMatriz(Matriz1))
print (0-1)




