# renovate-test

Renovateの動作確認用のプロジェクトです。

あえて古いバージョンを指定しています。

- Python: 3.15.1（`.python-version`）
- requests: 2.31.0（`pyproject.toml`）
- actions/checkout: v4、actions/setup-python: v5（`.github/workflows/pytest.yaml`）

## テストの実行

```
uv sync
uv run pytest
```
