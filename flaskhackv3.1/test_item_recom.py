

import pytest
import rcom



@pytest.mark.parametrize("uid , iid , expected_output",
                         [
                             (5, '00003' , 6),
                             (9, '00001' , 8),
                             (10, '00003',  3),
                             (11, '00003',  5),
                             (9, '00003',  1)
                         ]
                         )
def test_user_based_recom_system(uid , iid , expected_output):
    result = rcom.predicting_user_based_rating(uid, iid )
    assert result == expected_output






@pytest.mark.parametrize("uid , iid , expected_output",
                         [
                             (5, '00003' , 3),
                             (9, '00001' , 3),
                             (10, '00003',  1),
                             (11, '00003',  5),
                             (9, '00003',  1),
                             (20, '00003',  8)
                         ]
                         )
def test_item_based_recom_system(uid , iid , expected_output):
    result = rcom.predicting_item_based_rating(uid, iid )
    assert result == expected_output

