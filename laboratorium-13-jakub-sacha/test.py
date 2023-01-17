import pytest
import matrix

test_matrix_creation_from_dimensions_data = [
    (2, 3, 0, [[0, 0], [0, 0], [0, 0]]),
    (3, 3, 1, [[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
    (4, 2, 3, [[3, 3, 3, 3], [3, 3, 3, 3]])
]


@pytest.mark.parametrize('m, n, value, expected_matrix_data', test_matrix_creation_from_dimensions_data)
def test_matrix_creation_from_dimensions(m, n, value, expected_matrix_data):
    test_matrix = matrix.Matrix((m, n), value)
    assert test_matrix.data == expected_matrix_data


test_matrix_creation_from_dimensions_data = [
    ([[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]]),
    ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
    ([[3, 3, 3, 3], [3, 3, 3, 3]], [[3, 3, 3, 3], [3, 3, 3, 3]])
]


@pytest.mark.parametrize('input_matrix_data, expected_matrix_data', test_matrix_creation_from_dimensions_data)
def test_matrix_creation_from_data(input_matrix_data, expected_matrix_data):
    test_matrix = matrix.Matrix(input_matrix_data)
    assert test_matrix.data == expected_matrix_data


test_invalid_matrix_shape_data = [
    (-1, 5),
    (0, 0),
    (2, -5),
    (-2, -4)
]


@pytest.mark.parametrize('m, n', test_invalid_matrix_shape_data)
def test_invalid_matrix_shape(m, n):
    with pytest.raises(ValueError):
        matrix.Matrix((m, n))


def test_matrix_multiplication():
    d1 = [[1, 0, 2], [-1, 3, 1]]
    d3 = [[3, 1], [2, 1], [1, 0]]
    expected = [[5, 1], [4, 2]]
    actual = (matrix.Matrix(d1) * matrix.Matrix(d3)).data
    assert actual == expected


invalid_matrix_multiplication_data = [
    ([[1, 0, 2], [-1, 3, 1]], [[3, 1], [2, 1]]),
    ([[3, 1], [2, 1]], [[1, 0, 2], [-1, 3, 1]])
]


@pytest.mark.parametrize('d1, d2', invalid_matrix_multiplication_data)
def test_invalid_matrix_multiplication(d1, d2):
    with pytest.raises(ValueError):
        matrix.Matrix(d1) * matrix.Matrix(d2)
