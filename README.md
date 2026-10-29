# hello-python

5 个月冲刺计划的第一个项目。W1 验收物：本地跑通 hello world，并推送 GitHub。

不是练语法的。它要证明的是——环境能从零跑到通，而且换一台机器也能一键复现。

## 跑起来

```bash
uv run hello-python     # 环境自检
uv run pytest -q        # 跑测试
```

第一次运行 `uv run` 会自动建 `.venv`、装依赖。不需要手动 `python -m venv`，也不需要 `pip install`。

## 这套工具链

| 工具 | 版本 | 干什么 |
| --- | --- | --- |
| Python | 3.12.10 | 解释器 |
| uv | 0.13.6 | 建 venv、装依赖、跑脚本，替代 pip + venv + poetry |
| pytest | 9.2.0 | 测试 |

`uv` 的好处写进配置里就不丢：`pyproject.toml` 声明依赖，`uv.lock` 锁版本。别人拿到仓库，一条 `uv sync` 还原完全一样的环境。

## 目录

```
hello-python/
├── pyproject.toml      依赖与项目声明
├── uv.lock             版本锁（必须提交）
├── .python-version     钉死 3.12
├── src/hello_python/   源码
└── tests/              测试
```

## 国内源

pip 与 uv 都已指向清华镜像，配置在用户目录，不在仓库里：

- `%APPDATA%\pip\pip.ini`
- `%APPDATA%\uv\uv.toml`
