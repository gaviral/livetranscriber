## Version Update Instructions

1. `pyproject.toml`: Line 3
2. `livetranscriber.py`: Line 2
3. after updating the versions above, run `uv lock` to update the `uv.lock` file
4. commit and push the changes
5. create a new tag `git tag vx.x.x` (the v is important for CI/CD to work)
6. push the tag `git push --tags`
