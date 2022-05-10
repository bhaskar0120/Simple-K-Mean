
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
    
    # Normalizing the data
    min_field = l[0].copy()
    max_field = l[0].copy()
    for i in range(len(l[0])):
        for j in l:
            min_field[i] = min(min_field[i], j[i])
            max_field[i] = max(max_field[i], j[i])
        
    for i in range(len(l)):
        for j in range(len(l[0])):
            l[i][j] = (l[i][j] - min_field[j]) / (max_field[j] - min_field[j])

    # Saving data to file
    with open("train.data","w") as f:
        for i in l:
            f.write(",".join(map(str,i))+"\n")

    # Save labels to file
    with open("train.labels","w") as f:
        for i in labels:
            f.write("{}\n".format(i))
    print("Done!")

