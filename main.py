import os

TEXT = (
    "My agent checked whether the job was still running by searching for its own name. "
    "It found itself. The job had been dead for an hour."
)

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
