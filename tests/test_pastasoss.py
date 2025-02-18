import numpy as np

from pastasoss.soss_traces import rotate
from pastasoss.soss_traces import get_reference_trace
from pastasoss.soss_traces import REFERENCE_TRACE_FILES

from pastasoss.wavecal import get_wavecal_meta_for_spectral_order


def test_load_wavecal_model_order1():
    """Test if wavecol model json files are loaded in correctly and properly
    stored in its datamodel object for order 1"""
    # polynomial expected number of coefficient and degree
    NCOEF = 20
    POLY_DEGREE = 5
    INTERCEPT = 2.761308747854264  # in units of microns

    # fitted x-pixel columns limits
    X_MIN_SCALER = 73.62893071613087
    X_MAX_SCALER = 2039.7420006352984

    # fitted PWCPOW offset (i.e., PWCPOS-245.76)
    PWCPOS_OFFSET_MIN_SCALER = -0.1035520000001781
    PWCPOS_OFFSET_MAX_SCALER = 0.1628820800781341

    # load order 1 wavecal model
    order1_metadata = get_wavecal_meta_for_spectral_order("order1")

    assert order1_metadata.order == "order1"
    assert len(order1_metadata.coefficients) == NCOEF
    assert order1_metadata.poly_degree == POLY_DEGREE
    assert order1_metadata.intercept == INTERCEPT
    assert order1_metadata.scaler_data_min_[0] == X_MIN_SCALER
    assert order1_metadata.scaler_data_max_[0] == X_MAX_SCALER
    assert order1_metadata.scaler_data_min_[1] == PWCPOS_OFFSET_MIN_SCALER
    assert order1_metadata.scaler_data_max_[1] == PWCPOS_OFFSET_MAX_SCALER


def test_load_wavecal_model_order2():
    """Test if wavecol model json files are loaded in correctly and properly
    stored in its datamodel object for order 2"""

    # polynomial expected number of coefficient and degree
    NCOEF = 9
    POLY_DEGREE = 3
    INTERCEPT = 1.418562550851081  # in units of microns

    # fitted x-pixel columns limits
    X_MIN_SCALER = 0.0
    X_MAX_SCALER = 2048.0

    # fitted PWCPOW offset (i.e., PWCPOS-245.76)
    # this has been changed for order 2 to be
    # within in the allowed tolerance range.
    # order 1 will be treated the same later
    PWCPOS_OFFSET_MIN_SCALER = 245.5929
    PWCPOS_OFFSET_MAX_SCALER = 245.9271

    # load order 1 wavecal model
    order2_metadata = get_wavecal_meta_for_spectral_order("order2")

    assert order2_metadata.order == "order2"
    assert len(order2_metadata.coefficients) == NCOEF
    assert order2_metadata.poly_degree == POLY_DEGREE
    assert order2_metadata.intercept == INTERCEPT
    assert order2_metadata.scaler_data_min_[0] == X_MIN_SCALER
    assert order2_metadata.scaler_data_max_[0] == X_MAX_SCALER
    assert order2_metadata.scaler_data_min_[1] == PWCPOS_OFFSET_MIN_SCALER
    assert order2_metadata.scaler_data_max_[1] == PWCPOS_OFFSET_MAX_SCALER


def test_load_order1_trace_model():
    # load in the trace files
    ref_trace_file = REFERENCE_TRACE_FILES["order1"]
    x, _, origin = get_reference_trace(ref_trace_file)

    # check origin is what is expected and the xlimits.
    origin = (int(origin[0]), int(origin[1]))
    x_min = min(x)
    x_max = max(x)
    x_limits = (x_min, x_max)

    assert origin == (1887, 54)
    assert x_limits == (4, 2043)


def test_load_order2_trace_model():
    # load in the trace files
    ref_trace_file = REFERENCE_TRACE_FILES["order2"]
    x, _, origin = get_reference_trace(ref_trace_file)

    # check origin is what is expected and the xlimits.
    origin = (int(origin[0]), int(origin[1]))
    x_min = min(x)
    x_max = max(x)
    x_limits = (x_min, x_max)

    assert origin == (1677, 200)
    assert x_limits == (0, 2047)


def test_rotate():
    """Test rotate step to ensure that x coordinate input is return in the
    output when interpolating back onto the pixel column grid."""

    # using trace model for rotation step
    ref_trace_file = REFERENCE_TRACE_FILES["order1"]
    x, y, origin = get_reference_trace(ref_trace_file)

    # rotate
    angle = 0.2
    x_coords, y_coords = rotate(x, y, angle, origin, interp=True)
    # checks
    assert len(x) == len(x_coords)
    assert len(y) == len(y_coords)
    assert np.array_equal(x, x_coords)
