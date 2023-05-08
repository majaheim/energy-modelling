"source code"
import source

"""test open_mat_data"""
def test_open_mat_data():
    power_household = source.open_mat_data('data/LeistungHaushalte_fortest.mat', 'LeistungHaushalte')
    assert round(power_household[3], 5) == round(105.7154164971246, 5)

def test_graph_single_array():
    ESPV = source.open_mat_data('data/PV_Einspeiseprofil.mat', 'Leistung_Vec_Temperatur_Temp')
    assert source.graph_single_array(35040, ESPV, "Einspeiseprofil der PV Anlage") == True

def test_graph_multiple_array():
    ESPV = source.open_mat_data('data/PV_Einspeiseprofil.mat', 'Leistung_Vec_Temperatur_Temp')
    LH8 = source.open_mat_data('data/LeistungHaushalte.mat', 'LeistungHaushalte', 8)
    assert source.graph_multiple_array(35040, ESPV, LH8, "Einspeiseprofil der PV Anlage") == True

def test_zeros():
    array = source.zeros(378)
    assert array[45] == 1

def test_init():
    array = source.zeros(365)
    array = source.init(array, 5)
    print(array[3])
    assert array[4] == 0


