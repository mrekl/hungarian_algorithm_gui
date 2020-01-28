from tkinter import *
from hungarian_algorithm.main import Munkres

tk = Tk()

matrixInputs = []

matrixSizeX = 5
matrixSizeY = 5

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

def calculateOptimalCost():
    costs = []

    for i, row in enumerate(matrixInputs):
        
        costs.append([])
        for item in row:
            if(item.get() == ""):
                costs[i].append(0)
            else:
                costs[i].append(int(item.get()))

    costs = Munkres(costs)
    costs.calculate()

    print(costs.getSumOfMinCosts())

    resultLbl = Label(text = "The optimal value equals: " + str(costs.getSumOfMinCosts()))
    resultLbl.grid(row = matrixSizeY + 3, column = 0)

Label(text = "Matrix size (X x Y):").grid(row = 0, column = 0)
sizeXInput = Entry(tk)
sizeXInput.grid(row = 0, column = 1)
Label(text = "x").grid(row = 0, column = 2)
sizeYInput = Entry(tk)
sizeYInput.grid(row = 0, column = 3)

createMatrixBtn = Button(text = "Create matrix / Clear", command = updateMatrixInputs)
createMatrixBtn.grid(row = 0, column = 4)

calculateBtn = Button(text = "Calculate", command = calculateOptimalCost)
calculateBtn.grid(row = 0, column = 5)

Label(text = "").grid(row = 1, column = 0)

resultLbl = Label()

tk.mainloop()