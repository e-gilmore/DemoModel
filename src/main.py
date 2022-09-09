def runModel():
    #Model Calculations
    f = open("model-output.csv", "w")
    f.write("Feature1, Feature2, Prediction\n")
    f.write("2, 7, 3\n")
    f.write("4, 1, 3\n")
    f.write("6, 2, 3")
    f.close()

if __name__ == "__main__":
    runModel()

