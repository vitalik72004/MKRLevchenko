from main import same
import pytest
@pytest.mark.parametrize('f1_lines, f2_lines, result', [((1234, 'hello', 'qwert', 2023), (3245, 2023, 'Hello', 'qwert'), ['qwert', 2023])])
def test_same(f1_lines, f2_lines, result):
    same_fil = same(f1_lines, f2_lines)
    assert all(same_fil) == all(result)