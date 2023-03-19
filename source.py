import scipy.io
import numpy as np
import matplotlib.pyplot as plt

# Function that opens Matlab datasets
# @file_name - the name of the .mat file
# @field_name - the name of the column which contains the data
# @return - an array with all the values from the corresponding column
def open_mat_data(file_name, field_name):
    mat = scipy.io.loadmat(file_name, squeeze_me = True)
    return mat[field_name]

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
    plt.plot(x, dataaa, color="blue")
    plt.show()
    return True

def main():
    print("Hello World!")
    ESPV = open_mat_data('data/PV_Einspeiseprofil.mat', 'Leistung_Vec_Temperatur_Temp')
    graph_single_array(35040, ESPV, "Einspeiseprofil der PV Anlage")
    # # test plot
    # x = np.arange(0, 35040)
    # plt.title("Einspeiseprofil der PV Anlage")
    # plt.xlabel("X axis")
    # plt.ylabel("Y axis")
    # plt.plot(x, ESPV, color ="red")
    # plt.show()

if __name__ == "__main__":
         main()
