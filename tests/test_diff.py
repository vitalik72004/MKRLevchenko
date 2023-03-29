from main import diff
import pytest
@pytest.mark.parametrize('f1_lines, f2_lines, result', [((1234, 'hello', 'qwert', 2023), (3245, 2023, 'Hello', 'qwert'), [3245, 'Hello', 'hello', 1234])])
def test_diff(f1_lines, f2_lines, result):
    diff_fil = diff(f1_lines, f2_lines)
    assert all(diff_fil) == all(result)