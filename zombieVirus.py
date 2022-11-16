
# Función para llenar la matriz // Function to fill up the matrix
def fillMatrix():
    cont=0
    for i in range(0, f):
        matrix.append([])
        for j in range(0, c):
            matrix[i].append(sample[cont])
            cont+=1
        
# Letras de la diagonal principal // Letters of the main diagonal
def princMatches():
    for i in range(0,f):
        for j in range(0,c):
            if i == j:
                print(matrix[i][j])

# Letras de la diagonal secundaria // Letters of the second diagonal
def matchesSec():
    d = f-1
    print("")
    for i in range(0,f):
        print(matrix[i][d])
        d = d-1

# Programa principal // Main program
matrix = []
sample = "BCBBABBACBBBBCBB" # usar también//use also: ACDDCADBCDABDBBA, 
                            #BCAADCCBABCCBABB, CACBCACAC, ADDDABBDD, CDDACCACCACAAABC, ABAABBCBD, BCBBABBACBBBBCBB

if len(sample)==9:
        size = 3
elif len(sample)==16:
    size = 4
elif len(sample)==1369:
    size = 37

f = size
c = size

fillMatrix()
princMatches()
matchesSec()