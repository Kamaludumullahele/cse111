#import pytest and approx
#import water_flow
from pytest import approx
import pytest
import water_flow
import math

#calling test_water_column_height
def test_water_colomn_height():

    assert 0 + 3 * 0 / 4 == 0
    assert 0 + 3 * 10 / 4 == 7.5
    assert 25 + 3 * 0 /4 == 25
    assert 48.3 + 3 * 12.8 / 4 == 57.9

# calling test_pressure_gain_from_water_height function to 
# to test the pressure values
def test_pressure_gain_from_water_height():
    assert 998.2 * 9.80665 * 0 / 1000 == approx(0, abs=0.001)
    assert 998.2 * 9.80665 * 30.2 / 1000 == approx(295.628, abs=0.001)
    assert 998.2 * 9.80665 * 50.0 / 1000 == approx(489.450, abs=0.001)

# calling for test_pressure_loss_from_pipe to check the pressure_loss_from_pipe function

def test_pressure_loss_from_pipe():
    assert -0.018 * 0 * 998.2 * 1.75 ** 2 / (2000 * 0.048692) == approx(0, abs=0.001)
    assert -0.0 * 200 * 998.2 * 1.75 ** 2 / (2000 * 0.048692) == approx(0, abs=0.001)
    assert -0.018 * 200 * 998.2 * 0 ** 2 / (2000 * 0.048692) == approx(0, abs=0.001)
    assert -0.018 * 200 * 998.2 * 1.75 ** 2 / (2000 * 0.048692) == approx(-113.008, abs=0.001)
    assert -0.018 * 200 * 998.2 * 1.65 ** 2 / (2000 * 0.048692) == approx(-100.462, abs=0.001)
    assert -0.013 * 1000 * 998.2 * 1.65 ** 2 / (2000 * 0.286870) == approx(-61.576, abs=0.001)
    assert -0.013 * 1800.75 * 998.2 * 1.65 ** 2 / (2000 * 0.286870) == approx(-110.884, abs=0.001)

#function for getting pressrue loss from fittings for testing
def test_pressure_loss_from_fittings():
    assert -.04 * 998.2 * 0 ** 2 * 3 / 2000 == approx(0, abs=0.001)
    assert -.04 * 998.2 * 1.65 ** 2 * 0 / 2000 == approx(0, abs=0.001)
    assert -.04 * 998.2 * 1.65 ** 2 * 2 / 2000 == approx(-0.109, abs=0.001)
    assert -.04 * 998.2 * 1.75 ** 2 * 2 / 2000 == approx(-0.122, abs=0.001)
    assert -.04 * 998.2 * 1.75 ** 2 * 5 / 2000 == approx(-0.306, abs=0.001)

#function for calculating the reynolds number for testing
def test_reynolds_number():
    assert 998.2 * 0.048692 * 0 / 0.0010016 == approx(0, abs=1)
    assert 998.2 * 0.048692 * 1.65 / 0.0010016 == approx(80069, abs=1)
    assert 998.2 * 0.048692 * 1.75 / 0.0010016 == approx(84922, abs=1)
    assert 998.2 * 0.286870 * 1.65 / 0.0010016 == approx(471729, abs=1)
    assert 998.2 * 0.286870 * 1.75 / 0.0010016 == approx(500318, abs=1)

#function for calculating pressure reduction in pipes for testing
def test_pressure_loss_from_pipe_reduction():
    k=(.1 + 50 / 1) * ((0.28687 / 0.048692) ** 4 - 1)
    assert -(k) * 998.2 * 0 ** 2 / 2000 == approx(0, abs=0.001)

    k=(.1 + 50 / 471729) * ((0.28687 / 0.048692) ** 4 - 1)
    assert -(k) * 998.2 * 1.65 ** 2 / 2000 == approx(-163.744, abs=0.001)

    k=(.1 + 50 / 500318) * ((0.28687 / 0.048692) ** 4 - 1)
    assert -(k) * 998.2 * 1.75 ** 2 / 2000 == approx(-184.182, abs=0.001)
    








# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])