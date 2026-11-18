import subprocess
from pathlib import Path

KeyName = "id_ed25519"
emailId = "your_email@example.com"

key = Path.home() / ".ssh" / KeyName
key.parent.mkdir(exist_ok=True)

if not key.exists():
    subprocess.run(
        ["ssh-keygen", "-t", "ed25519", "-C", emailId,
         "-N", "", "-f", str(key)],
        check=True)

print(key.with_suffix(".pub").read_text())   # public key to paste in GitHub
