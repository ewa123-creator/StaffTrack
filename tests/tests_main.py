import subprocess
import sys
from pathlib import Path

def test_main_runs():
    script = Path(__file__).resolve().parent.parent / "src" / "main.py"
    result = subprocess.run(
        [sys.executable, str(script)],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "StaffTrack" in result.stdout
