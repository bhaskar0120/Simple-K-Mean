from random import sample

if __name__ == "__main__":
    l = []
    with open("wine.data") as f:
        while (st:=f.readline()):
            l.append(list(map(float,st.split(','))))
    # Using 125 random samples as training data
    train = sample(l,125)

    # Saving training data to file
    with open("train.data","w") as f:
        for i in train:
            f.write(",".join(map(str,i))+"\n")

    # Using the rest as test data
    # Removing training data from original data
    l = [i for i in l if i not in train]

    # Removing the labels from the test data
    for i in range(len(l)):
        l[i] = l[i][1:]
    
    # Saving test data to file
    with open("test.data","w") as f:
        for i in l:
            f.write(",".join(map(str,i))+"\n")
    print("Done!")