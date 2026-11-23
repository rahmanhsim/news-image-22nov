import os
import os.path
import shutil

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "poster.png")
dst = "/output/entry.png"

try:
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)
    print(f"Copied to: {dst} ({os.path.getsize(dst)} bytes)")
except Exception:
    try:
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(src, "rb") as f_in, open(dst, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
        print(f"Copied to: {dst} ({os.path.getsize(dst)} bytes)")
    except Exception:
        shutil.copyfile(src, dst)
        print(f"Copied to: {dst} ({os.path.getsize(dst)} bytes)")

