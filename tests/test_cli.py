import subprocess
import sys


def test_cli_plain(tmp_path):
    p1 = tmp_path / "a.json"
    p2 = tmp_path / "b.json"
    p1.write_text('{"k":1}')
    p2.write_text('{"k":2}')

    result = subprocess.run(
        [sys.executable, "-m", "gendiff.scripts.gendiff", str(p1), str(p2), "--format", "plain"],
        capture_output=True,
        text=True,
    )
    assert "Property 'k' was updated" in result.stdout
