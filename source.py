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
        mat_array_column = mat_array[:, array_column]
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


#Function that creates an array of zeros
def zeros(size):
    array = [0] * size
    #array = np.empty(size)
    return array

#Function that checks what PV is producing and fills the arrays
def check_pv_production(size, pv_power, c_power, c_houshold):
    excess = zeros(size)
    #pv_power = zeros(size)
    #c_power = zeros(size)
    #c_houshold = zeros(size)

    for n in range(2, size, 1):
        if pv_power[n] >= c_power[n]:   #pv produces more than what is needed by the household
            c_houshold[n] = c_power[n]
            excess[n] = pv_power[n] - c_power[n]
        elif n == 999:
            print('hi')
        else:
            c_houshold[n] = c_power[n]
            excess[n] = 0
        household = np.array([c_houshold, excess])

    return household

#Function that fills workday the array with 1(workday) or 0(weekend)
def init(workday_array):
    counter = 1
    for n in range(0,365,1):
        if counter <= 5:        #Monday - Friday
            workday_array[n] = 1
        else:
            workday_array[n] = 0

        if counter == 7:
            counter = 1
        else:
            counter = counter +1

    return workday_array

#Function that configures car availability array
def car_availability(car_array, workday_array):
    for n in range(0,365,1):
        if workday_array[n] == 1:   #Mo-Fr
            if (96*(n-1)) == 0:          #24h*4(power is measeured 4 times per hour)
                for i in range(96):
                    if i <= 34 | i >= 70:    #car is at home (only first day)
                        car_array[i] = 1
            else:
                for i in range(96*(n-1), 96*n, 1):
                    if (i <= (34 + 96*(n-1))) | (i >= (70 + 96*(n-1))):
                        car_array[i] = 1
        else:                       #Weekend
            for i in range(96*(n-1), 96*n, 1):
                car_array[i] = 1            #car is at home all weekend

    return car_array

def main():
    print("Hello World!")

    #load PV Einspeiseprofildata
    ESPV = open_mat_data('data/PV_Einspeiseprofil.mat', 'Leistung_Vec_Temperatur_Temp')
    #graph_single_array(35040, ESPV, "Einspeiseprofil der PV Anlage")

    # load LeistungHaushalte - Consumer 8 is used here
    LH8 = open_mat_data('data/LeistungHaushalte.mat', 'LeistungHaushalte', 8)
    #graph_single_array(35040, LH, "Leistung der Haushalte")

    # load PV Production
    #PVP = open_mat_data('data/Load_PVProduction.mat', 'LeistungHaushalte')

    # load Spotpreis
    #LH = open_mat_data('data/LeistungHaushalte.mat', 'LeistungHaushalte')

    #The section below intializes variables used for further calculations
    PV_power = 10*ESPV*1000*0.25     #1000: Power is kW , 0.25:??
    Battery_state = zeros(35040)
    Charging_energy = zeros(35040)
    Dischargeing_energy = zeros(35040)
    Own_consumption_H8 = zeros(35040)

    #At the begining the Battery is full:
    Battery_state[0] = 58000

    Workday = zeros(365)
    Workday = init(Workday)
    Car_available = zeros(35040)
    Car_available = car_availability(Car_available, Workday)

    #Laden ??

    #Calculations for 9-5Job Unidirectioinal
    H8 = check_pv_production(35040, PV_power, LH8, Own_consumption_H8)  #Index 0: houshold consumption, Index 1: excess power
    #print(H8.shape)
    graph_single_array(35040, Car_available, 'test')






if __name__ == "__main__":
         main()
