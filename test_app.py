mport pytest
from app import app


@pytest.fixture
def client():
        app.config["TESTING"] = True

            with app.test_client() as client:
                        yield client


                        def test_home_page(client):
                                response = client.get("/")
                                    assert response.status_code == 200
                                        assert b"Python Calculator" in response.data


                                        @pytest.mark.parametrize(
                                                    ("a", "b", "operation", "expected"),
                                                        [
                                                                    ("10", "5", "add", "15.0"),
                                                                            ("10", "5", "subtract", "5.0"),
                                                                                    ("10", "5", "multiply", "50.0"),
                                                                                            ("10", "5", "divide", "2.0"),
                                                                                                ],
                                                        )
                                        def test_calculations(client, a, b, operation, expected):
                                                response = client.get(
                                                                "/calculate",
                                                                        query_string={
                                                                                        "a": a,
                                                                                                    "b": b,
                                                                                                                "operation": operation,
                                                                                                                        },
                                                                            )

                                                    assert response.status_code == 200
                                                        assert expected.encode() in response.data


                                                        def test_division_by_zero(client):
                                                                response = client.get(
                                                                                "/calculate",
                                                                                        query_string={
                                                                                                        "a": "10",
                                                                                                                    "b": "0",
                                                                                                                                "operation": "divide",
                                                                                                                                        },
                                                                                            )

                                                                    assert response.status_code == 400
                                                                        assert b"Cannot divide by zero" in response.data


                                                                        def test_health_endpoint(client):
                                                                                response = client.get("/health")

                                                                                    assert response.status_code == 200
                                                                                        assert response.json["status"] == "healthy"

