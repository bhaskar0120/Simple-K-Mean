
if __name__ == "__main__":
    l = []
    with open("wine.data") as f:
        while (st:=f.readline()):
            l.append(list(map(float,st.split(','))))

    # Removing labels from the data
    labels = []
    for i in range(len(l)):
        labels.append(int(l[i][0]))
        l[i] = l[i][1:]
    
    # Saving data to file
    with open("train.data","w") as f:
        for i in l:
            f.write(",".join(map(str,i))+"\n")

    # Save labels to file
    with open("train.labels","w") as f:
        for i in labels:
            f.write("{}\n".format(i))
    print("Done!")

