import scipy.io
import numpy as np
import matplotlib.pyplot as plt

# Function that opens Matlab datasets
# @file_name - the name of the .mat file
# @field_name - the name of the column which contains the data
# @return - an array with all the values from the corresponding collumn
def open_mat_data(file_name, field_name):
    mat = scipy.io.loadmat(file_name, squeeze_me = True)
    return mat[field_name]

def main():
    print("Hello World!")
    ESPV = open_mat_data('data/PV_Einspeiseprofil.mat', 'Leistung_Vec_Temperatur_Temp')

    # test plot
    x = np.arange(0, 35040)
    plt.title("Einspeiseprofil der PV Anlage")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.plot(x, ESPV, color ="red")
    plt.show()

if __name__ == "__main__":
         main()