from functions import add
import pytest

@pytest.mark.parametrize(
  "x, y, result", [(1,2,3), (3,4,7), (4,5,9)]
)
def test_add(x, y, result):
  assert add(x, y) == result
