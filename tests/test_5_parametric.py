"""
test for rtanalysis
- in this test, we will try various parameter levels
and make sure that the function properly raises
and exception is accuracy is zero
"""

import pytest
import numpy as np
from rtanalysis.rtanalysis import RTAnalysis
from rtanalysis.generate_testdata import generate_test_df

@pytest.mark.parametrize("meanRT, sdRT, meanAcc",
                         [(1.5, 1.0, 0.9), (1500, 1000, 0.9),
                         (1.5, 1.0, 0)])
def test_rtanalysis_parameteric(meanRT, sdRT, meanAcc):
    test_df = generate_test_df(meanRT, sdRT, meanAcc)
    rta = RTAnalysis()
    if meanAcc > 0:
        rta.fit(test_df.rt, test_df.accuracy)
        assert np.allclose(meanRT, rta.meanrt_)
        assert np.allclose(meanAcc, rta.meanacc_)
    else:
        with pytest.raises(ValueError):
            rta.fit(test_df.rt, test_df.accuracy)