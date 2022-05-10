from random import sample



def dist(a,b):
    if not len(a) == len(b):
        raise ValueError("Vectors must be of same length")
    return sum([(a[i]-b[i])**2 for i in range(len(a))])**0.5

if __name__ == "__main__":
    # load data
    vector = []
    with open("train.data") as f:
        while (st:=f.readline()):
            vector.append(list(map(float,st.split(','))) )
    
    # Performing K-Means clustering on the training data
    print(len(vector))

    #load labels
    labels = []
    with open("train.label") as f:
        while (st:=f.readline()):
            labels.append(int(st))

    CLUSTER = 3
    cluster = []
    for i in range(CLUSTER):
        cluster.append([])
    # Divide into CLUSTER clusters
    # Pick CLUSTER vectors on random
    selected = [vector[5],vector[75], vector[156]]

    # Assign each vector to the closest cluster
    for i in vector:
        idx = 0
        curr_min = 1e10
        for j in range(CLUSTER):
            d = dist(i,selected[j])
            if d < curr_min:
                curr_min = d
                idx = j
        cluster[idx].append(i)



    EPOCH = 1 
    for T in range(EPOCH):
        # Calculate the mean of each cluster
        mean = []
        for i in cluster:
            mean_vector = []
            for j in range(len(i[0])):
                s1 = 0
                for k in range(len(i)):
                    s1 += i[k][j]
                mean_vector.append(s1/len(i))
            mean.append(mean_vector)

        # Assign each vector to the closest cluster in the mean
        cluster.clear()
        for i in range(CLUSTER):
            cluster.append([])
        for i in vector:
            idx = 0
            curr_min = 1e10
            for j in range(CLUSTER):
                d = dist(i,mean[j])
                if d < curr_min:
                    curr_min = d
                    idx = j
            cluster[idx].append(i)

    prediction = []
    for i in vector:
        for j in range(CLUSTER):
            if i in cluster[j]:
                prediction.append(j+1)

    #Calculate the accuracy
    accuracy = 0
    for i in range(len(prediction)):
        if prediction[i] == labels[i]:
            accuracy += 1
    print(accuracy/len(prediction))

    # Calculate the distance between each vector and the cluster
    # Assign the vector to the cluster with the smallest distance
    # Repeat until convergence
    # Print the cluster centroids



