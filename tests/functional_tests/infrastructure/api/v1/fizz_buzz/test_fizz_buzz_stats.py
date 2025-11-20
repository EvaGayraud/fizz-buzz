from fastapi import status


def test_that_fizz_buzz_stats_successful(client) -> None:
    # Given
    request = {"limit": 10, "integer_1": 8, "string_1": "top", "string_2": "tip", "integer_2": 20}

    # When
    client.post("/api/v1/fizz_buzzs", json=request)
    response = client.get("/api/v1/stats")

    # Then
    assert response.status_code == status.HTTP_200_OK
