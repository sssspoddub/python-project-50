from pathlib import Path

from gendiff import generate_diff


def test_generate_diff_nested() -> None:
    f1 = Path("tests/fixtures/nested1.json")
    f2 = Path("tests/fixtures/nested2.json")
    expected = (
        "{\n"
        "    common: {\n"
        "      + follow: false\n"
        "        setting1: Value 1\n"
        "      - setting2: 200\n"
        "      - setting3: true\n"
        "      + setting3: null\n"
        "      + setting4: blah blah\n"
        "      + setting5: {\n"
        "            key5: value5\n"
        "        }\n"
        "        setting6: {\n"
        "            doge: {\n"
        "              - wow: \n"
        "              + wow: so much\n"
        "            }\n"
        "            key: value\n"
        "          + ops: vops\n"
        "        }\n"
        "    }\n"
        "    group1: {\n"
        "      - baz: bas\n"
        "      + baz: bars\n"
        "        foo: bar\n"
        "      - nest: {\n"
        "            key: value\n"
        "        }\n"
        "      + nest: str\n"
        "    }\n"
        "  - group2: {\n"
        "        abc: 12345\n"
        "        deep: {\n"
        "            id: 45\n"
        "        }\n"
        "    }\n"
        "  + group3: {\n"
        "        deep: {\n"
        "            id: {\n"
        "                number: 45\n"
        "            }\n"
        "        }\n"
        "        fee: 100500\n"
        "    }\n"
        "}"
    )
    assert generate_diff(f1, f2) == expected
