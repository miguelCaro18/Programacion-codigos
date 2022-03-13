def explorar():
    global nodosGen
    base=list(nodosGen.keys())
    try:
        nodosGen[base[0]][0]=True
    except:
        return True
    change = True
    while(change):
        change=False
        for i in base: #identificador de nodos
            if (nodosGen[i][0] == None): #si aun no tiene color buscarlo
                for j in nodosGen[i][1]:
                    if (j in nodosGen.keys()):
                        if (nodosGen[j][0] != None):
                            nodosGen[i][0] = not nodosGen[j][0]
                            change=True
                            break
            for j in nodosGen[i][1]: #for de nodos adyacentes
                if(j in nodosGen.keys()  and nodosGen[i][0] !=None):
                    if(nodosGen[j][0]==None):
                        nodosGen[j][0]=not nodosGen[i][0]
                        change = True
                    elif(nodosGen[j][0]==nodosGen[i][0]):
                        return False
                elif(not j in nodosGen.keys() and nodosGen[i][0] !=None):
                    nodosGen[j]=[not nodosGen[i][0],[]]
                    change = True
                elif(not j in nodosGen.keys()):
                    nodosGen[j] = [None, []]
    return True
while(True):
    nodosGen={}
    nodos=int(input())
    if(nodos==0):
        break
    nodosGen={}
    respuesta=True
    for i in range(int(input())):
        a=sorted([int(a) for a in input().split(" ")])
        if(a[0] in nodosGen.keys()):
            nodosGen[a[0]][1].append(a[1])
        else:
            nodosGen[a[0]]=[None,[a[1]]]
    print("BICOLORABLE." if explorar() else "NOT BICOLORABLE.")
