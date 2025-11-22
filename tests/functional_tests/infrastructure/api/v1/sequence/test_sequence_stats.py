from fastapi import status


def test_that_sequence_stats_successful(client) -> None:
    # Given
    request = {"limit": 10, "integer_1": 8, "string_1": "top", "string_2": "tip", "integer_2": 20}

    # When
    client.post("/api/v1/sequences", json=request)
    response = client.get("/api/v1/stats")

    # Then
    assert response.status_code == status.HTTP_200_OK


def test_that_sequence_stats_empty_successful(client) -> None:
    # When
    response = client.get("/api/v1/stats")

    # Then
    assert response.status_code == status.HTTP_200_OK
