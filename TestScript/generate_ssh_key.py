import subprocess
from pathlib import Path

key = Path.home() / ".ssh" / "id_ed25519"
key.parent.mkdir(exist_ok=True)

if not key.exists():
    subprocess.run(
        ["ssh-keygen", "-t", "ed25519", "-C", "your_email@example.com",
         "-N", "", "-f", str(key)],
        check=True)

print(key.with_suffix(".pub").read_text())   # public key to paste in GitHub
