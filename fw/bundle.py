import os, shutil
from pathlib import Path

platform_dirs = set([d for d in os.walk('.')][0][1])
platform_dirs = platform_dirs - {'core', 'bundle'}

#https://stackoverflow.com/a/12514470
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


for pd in platform_dirs:
    print(pd)
    path = Path(f"./bundle/{pd}")
    path.mkdir(parents=True, exist_ok=True)
    copytree("core", path)
    copytree(pd, path)

