from src.module import get_status


def test_get_status():
    assert get_status("https://example.com") == 200
