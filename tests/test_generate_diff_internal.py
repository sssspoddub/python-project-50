from gendiff.diff import generate_diff


def test_generate_diff_key_types() -> None:
    d1 = {"a": 1, "b": 1, "c": 3}
    d2 = {"a": 1, "b": 2, "d": "x"}
    expected = (
        "{\n"
        "    a: 1\n"
        "  - b: 1\n"
        "  + b: 2\n"
        "  - c: 3\n"
        "  + d: x\n"
        "}"
    )
    assert generate_diff(d1, d2) == expected
