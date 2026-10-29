"""环境自检 —— 跑通它，就说明这套工具链装好了。"""

import platform
import sys


def main() -> None:
    line = "=" * 48
    print(line)
    print("  hello world —— 环境自检")
    print(line)
    print(f"Python 版本 : {sys.version.split()[0]}")
    print(f"解释器路径  : {sys.executable}")
    print(f"操作系统    : {platform.system()} {platform.release()}")
    print(f"64 位环境   : {sys.maxsize > 2**32}")
    print(f"虚拟环境    : {'是' if sys.prefix != sys.base_prefix else '否'}")
    print(line)
    print("环境可用，动手。")


if __name__ == "__main__":
    main()
