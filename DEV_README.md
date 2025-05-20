## Version Update Instructions

1. `pyproject.toml`: Line 3
2. `livetranscriber/__init__.py`: Line 4
3. `livetranscriber/livetranscriber.py`: Line 2
4. after updating the versions above, run `uv lock` to update the `uv.lock` file
5. commit and push the changes
6. create a new tag `git tag vx.x.x` (the v is important for CI/CD to work)
7. push the tag `git push --tags`
