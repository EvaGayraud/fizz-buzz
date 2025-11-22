from fastapi import status


def test_that_list_sequence_with_bad_request_failed(client) -> None:
    # Given
    request = {"limit": 0, "integer_1": 0, "string_1": "", "string_2": "", "integer_2": 0}

    # When
    response = client.post("/api/v1/sequences", json=request)

    # Then
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_that_list_sequence_with_missing_fields_failed(client) -> None:
    # Given
    request = {"limit": 100}

    # When
    response = client.post("/api/v1/sequences", json=request)

    # Then
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_that_list_sequence_successful(client) -> None:
    # Given
    request = {"limit": 10, "integer_1": 8, "string_1": "top", "string_2": "tip", "integer_2": 20}

    # When
    response = client.post("/api/v1/sequences", json=request)

    # Then
    assert response.status_code == status.HTTP_201_CREATED
