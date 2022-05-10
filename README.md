### A simple algorithm to play around with the wine data set

The data set can be found at [Wine dataset](https://archive.ics.uci.edu/ml/datasets/wine)

#### Solution

We solve this by using K-Means algorithm as we know there are a total of
3 groups in the dataset.

#### Preparation

Using a simple prepare script I have separated the labels from the actual
data.
All fields have been linearly normalized to value between 0 and 1

#### Working 

Initially 3 data points have been correctly marked (one from each group respectively).
Then the rest of data has been put into groups that they are closest to.
The mean was then calculated.
Now the distance of all points have been calculated from the mean and they are 
grouped accordingly.
After a few of these cycles it is found that we can classify the data with an
accuracy of 94.95%
