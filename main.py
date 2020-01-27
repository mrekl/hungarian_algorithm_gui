from tkinter import *
from hungarian_algorithm.main import Munkres

tk = Tk()

matrixInputs = []

matrixSizeX = None
matrixSizeY = None

def updateMatrixInputs():
    global matrixInputs
    global matrixSizeX
    global matrixSizeY

    resultLbl.grid_remove()

    matrixInputs = []

    sizeX = matrixSizeX = int(sizeXInput.get())
    sizeY = matrixSizeY = int(sizeYInput.get())

    for i in range(sizeY):
        matrixInputs.append([])
        for j in range(sizeX):
            matrixInputs[i].append(Entry(tk))
            matrixInputs[i][j].grid(row = i + 2, column = j)

def calculate():
    costsMatrix = []

    for i, row in enumerate(matrixInputs):
        
        costsMatrix.append([])
        for item in row:
            if(item.get() == ""):
                costsMatrix[i].append(0)
            else:
                costsMatrix[i].append(float(item.get()))

    costs = Munkres(costsMatrix)
    costs.calculate()

    resultLbl = Label(text = "The optimal value equals: " + str(costs.getSumOfMinCosts()))
    resultLbl.grid(row = matrixSizeY + 3, column = 0)

Label(text = "Matrix size:").grid(row = 0, column = 0)
sizeXInput = Entry(tk)
sizeXInput.grid(row = 0, column = 1)
Label(text = "x").grid(row = 0, column = 2)
sizeYInput = Entry(tk)
sizeYInput.grid(row = 0, column = 3)

createMatrixBtn = Button(text = "Create matrix / Clear", command = updateMatrixInputs)
createMatrixBtn.grid(row = 0, column = 4)

calculateBtn = Button(text = "Calculate", command = calculate)
calculateBtn.grid(row = 0, column = 5)

Label(text = "").grid(row = 1, column = 0)

resultLbl = Label()



# btnPrintHello = Button(tk, text = "Print Hello", command = printHello)
# btnPrintHello.grid(row = 0)

# updateMatrixInputs(3, 4)
tk.mainloop()