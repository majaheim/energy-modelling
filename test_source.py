import source

def test_open_mat_data():
    ESPV = source.open_mat_data('data/PV_Einspeiseprofil.mat', 'Leistung_Vec_Temperatur_Temp')
    assert round(ESPV[33], 5) == round(0.0151596888838696, 5)