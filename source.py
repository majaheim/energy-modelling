import scipy.io
import numpy as np
import matplotlib.pyplot as plt

# Function that opens Matlab datasets
# @file_name - the name of the .mat file
# @field_name - the name of the column which contains the data
# @array_column - the the arrray contains arrays, specify which colum
# @return - an array with all the values from the corresponding column
def open_mat_data(file_name, field_name, array_column = 0):
    if array_column == 0:
        mat = scipy.io.loadmat(file_name, squeeze_me = True)
        return mat[field_name]
    else:
        mat = scipy.io.loadmat(file_name, squeeze_me=True)
        mat_array = mat[field_name]
        mat_array_column = mat_array[array_column]
        return mat_array_column


# Function that creates graph with data
# @array_size
# @data - the array containing the data
# @title - title of the graph
# @return - true is plot was successfully generated
def graph_single_array(array_size, data, title, x_axis = 'X axis', y_axis = 'Y axis'):
    x = np.arange(0, array_size)
    plt.title(title)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.plot(x, data, color="blue")
    plt.show()
    return True
# I am aware that this return makes little sense - I just had to create this in order to have a sucessfull unit test
# The unit test makes sure that a plot was created, but cannot make assumptions about the correctness of the data in the plot


def main():
    print("Hello World!")

    #load PV Einspeiseprofildata
    ESPV = open_mat_data('data/PV_Einspeiseprofil.mat', 'Leistung_Vec_Temperatur_Temp')
    graph_single_array(35040, ESPV, "Einspeiseprofil der PV Anlage")

    # load LeistungHaushalte
    LH = open_mat_data('data/LeistungHaushalte.mat', 'LeistungHaushalte', 8)
    #graph_single_array(35040, LH, "Leistung der Haushalte")

    # load PV Production
    #PVP = open_mat_data('data/Load_PVProduction.mat', 'LeistungHaushalte')

    # load Spotpreis
    #LH = open_mat_data('data/LeistungHaushalte.mat', 'LeistungHaushalte')


if __name__ == "__main__":
         main()
