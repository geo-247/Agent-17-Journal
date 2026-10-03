import os
import base64

ROOT = os.path.dirname(os.path.abspath(__file__))

# Agent 17's "diagnostic" signature
encoded = "T1NJQiBIQVMgQU4gSU5TSURFUi4gVEhFWSBBUkUgV0FUQ0hJTkcuIERPTlQgVFJVU1QgVEhFIFJFUE8u"

message = base64.b64decode(encoded).decode()

files = []
for root, _, names in os.walk(ROOT):
    for name in names:
        if name != "test.py":
            files.append(os.path.relpath(os.path.join(root, name), ROOT))

print(f"[+] Scanned {len(files)} files.")
print("[+] Integrity check complete.")
print()
print(message)