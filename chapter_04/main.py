__author__ = 'jrx'

import pandas as pd

import chapter_04.data as data
import chapter_04.classification as classification

from common.ui import print_title


def vowel_classification(train_data, test_data):
    """ Run the vowel classification algorithms """
    print_title('Vowel classification')

    x_train = train_data.drop('y', 1)
    y_train = train_data.y

    x_test = test_data.drop('y', 1)
    y_test = test_data.y

    # Perform normalization in the same way on training and testing set

    ############################################################
    # LINEAR REGRESSION
    x_linear_train = (x_train - x_train.mean()) / x_train.std()
    x_linear_train.insert(0, 'intercept', 1.0)

    x_linear_test = (x_test - x_train.mean()) / x_train.std()
    x_linear_test.insert(0, 'intercept', 1.0)

    least_squares = classification.LeastSquaresClassifier(x_linear_train, y_train)

    train_error_rate = classification.classification_error_rate(least_squares, x_linear_train, y_train)
    test_error_rate = classification.classification_error_rate(least_squares, x_linear_test, y_test)

    linear_regression_series = pd.Series({
        'Training Error Rate': train_error_rate,
        'Test Error Rate': test_error_rate
    }, index=['Training Error Rate', 'Test Error Rate'])

    #############################################################
    # LINEAR DISCRIMINANT ANALYSIS
    lda = classification.LinearDiscriminantClassifier(x_train, y_train)

    train_error_rate = classification.classification_error_rate(lda, x_train, y_train)
    test_error_rate = classification.classification_error_rate(lda, x_test, y_test)

    lda_series = pd.Series({
        'Training Error Rate': train_error_rate,
        'Test Error Rate': test_error_rate
    }, index=['Training Error Rate', 'Test Error Rate'])

    #############################################################
    # QUADRATIC DISCRIMINANT ANALYSIS
    qda = classification.QuadraticDiscriminantClassifier(x_train, y_train)

    train_error_rate = classification.classification_error_rate(qda, x_train, y_train)
    test_error_rate = classification.classification_error_rate(qda, x_test, y_test)

    qda_series = pd.Series({
        'Training Error Rate': train_error_rate,
        'Test Error Rate': test_error_rate
    }, index=['Training Error Rate', 'Test Error Rate'])

    result = pd.DataFrame({
        'Linear regression': linear_regression_series,
        'LDA': lda_series,
        'QDA': qda_series,
    }, columns=['Linear regression', 'LDA', 'QDA'])

    print result.T.to_string(float_format=lambda x: '%.6f' % x)


def main():
    """ Main function to run """
    print ">>>>>>>>>>>>>>>>>>>>>>>>>>"
    print "Running code for chapter 4"
    train_data = data.read_vowel_train()
    test_data = data.read_vowel_test()

    vowel_classification(train_data, test_data)


if __name__ == '__main__':
    main()
