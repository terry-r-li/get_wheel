import os
from pkgutil import iter_modules

# 进入官方"k8s-hub"pod里
# $ cd /usr/local/lib/python3.8/dist-packages
# $ python3
# 在python内粘贴运行该文件代码，获得所有whl的具体信息，粘贴到正确版本的wheel_specifications_<版本>.txt中

for module in iter_modules():
    if module.module_finder.path.endswith("-packages"):
        path = module.module_finder.path
        dirs = os.listdir(path)
        for dir in dirs:
            try:
                files = os.listdir(os.path.join(path, dir))
                if "WHEEL" in files:
                    wheel_file = os.path.join(path, dir, "WHEEL")
                    with open(wheel_file, 'r') as f:
                        lines = ["", "", ""]
                        for line in f:
                            if "Tag" in line:
                                elements = line[5:-1].split("-")
                                for i in range(3):
                                    if lines[i] == "":
                                        lines[i] = elements[i]
                                    elif lines[i] != elements[i]:
                                        lines[i] = lines[i] + "." + elements[i]
                        print(dir[:-10] + "-" + "-".join(lines) + ".whl")
            except:
                pass
        break
