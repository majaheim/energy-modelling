import source

def test_open_mat_data():
    ESPV = source.open_mat_data('data/PV_Einspeiseprofil.mat', 'Leistung_Vec_Temperatur_Temp')
    assert round(ESPV[33], 5) == round(0.0151596888838696, 5)
    
def test_graph_single_array():
    ESPV = source.open_mat_data('data/PV_Einspeiseprofil.mat', 'Leistung_Vec_Temperatur_Temp')
    assert source.graph_single_array(35040, ESPV, "Einspeiseprofil der PV Anlage") == True

def test_zeros():
    array = source.zeros(378)
    print(array[45])
    assert array[45] == 0

def test_init():
    array = source.zeros(365)
    array = source.init(array)
    print(array[3])
    assert array[4] == 1
