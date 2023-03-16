##

## Contributors

Name: Andrew Hunter-Owega
Email: ahunterow@unbc.ca
Student Number: 230 147 039

Name: Daniel Strickland
Email: dstrickla@unbc.ca
Student Number: 230 146 357

Name: Nicholas Hirt
Email: nhirt@unbc.ca
Student Number: 230 127 295

## Assignment Information

The objective of this assignment is to use one of three methods for the purpose
of predicting the edibility status of 100 unknown mushrooms. For this application
the K-NN method is utilized to make the predictions

## Report

### Data Division

In training and testing the K-NN nearest neighbor model, an 80-20 split between
training and testing data was utilized. The first 6400 mushroom records are used
to search for the nearest neighbor, while the latter 1600 mushroom records are
utilized to test the accuracy of the K-NN method.

### Methodology

The method used in the this application is the K-NN nearest neighbor method. This
method functions based on the general idea of "If it walks like a duck, talks
like a duck, and has a vault full of gold coins in which to jump into, than it is 
probably a duck." This is accomplished by taking the unknown records and finding
the most similar records that are known. This similarity is computed by taking
the euclidean distance between the records. When the data is not usable for the
purpose of euclidean distance (non-numeric) the data is mapped to numeric data.
(In this application this is accomplished by input_switcher.py)These "nearest
neighbors" are then polled to determine how the records around it are 
classified. In the event of a tie, a tie breaker must be added.

### Final Settings

While numerous values of k were utilized to test the K-NN prediction model, we
determined that a k setting of 1 achieved the optimal result over the test data.
An additional setting which is deemed unchangeable is what to do in the event
that a tie occurs in the polling of the nearest neighbors. In this event we
consider that poisonous is favored. We consider this option as it is better to
be safer rather than making a risk.

For further breakdown please see the provided analysis report pdf document.

### Accuracy of the Application

We determine that the optimal setting for the K-NN prediction was a k value of 1.
With this k value an error rate of 3.44% was achieved with a total accuracy
result of 96.56% in predicting the edibility status of the testing mushroom
records.

### Accuracy of the Application

Technically speaking there are two variables to be considered when testing the
application of the data. To ensure that there is only one experimental variable
the first variable, the tie breaker is kept constant across trials. In a tie
event we guarantee that the poisonous classification is favoured. The actual
experimental variable is the number of nearest neighbors to poll.

                    +------------+------------+
                    | K Neighbors| Error Rate |
                    +------------+------------+
                    |      1     |    3.44%   |
                    |      2     |    3.88%   |
                    |      3     |    4.06%   |
                    |      4     |    3.94%   |
                    |      5     |    4.50%   |
                    |      6     |    5.12%   |
                    |      7     |    4.94%   |
                    |      8     |    4.94%   |
                    |      9     |    4.88%   |
                    |     10     |    5.05%   |
                    +------------+------------+

### How to Use

To operate the program the entry point main.py must be executed. You will first
be prompted as to whether or not you would prefer to execute the prediction of 
the provided 100 unknown, or perform the accuracy test. The code 100 is used to
predict the first 100, and the code 1600 is used for prediction. You will then 
be prompted for a k value within the ranges of 1 and 100 (inclusive). The program
will then begin the nearest neighbor calculation. However, it should be noted 
that the program does take some time to execute particularly for the accuracy
tests. In any case the predicted results are written to  predictionResultKNN.txt.