# Publishing RobustToolbox

```admonish info
These instructions are a step-by-step guide for engine maintainers to follow.
```

1. Open a terminal in the RobustToolbox directory (`cd RobustToolbox` if you are in the space-station-14 directory)
2. Fetch latest master (`git fetch https://github.com/space-wizards/RobustToolbox.git`)
3. Checkout the remote master branch (`git checkout -B master upstream/master`, WITH capital 'B' to overwrite master)
   - This step will overwrite your local `master` branch with the remote one.
4. Run version.py (`python ./Tools/version.py 0.1.0`, where 0.1.0 is the version number you want, WITHOUT 'v')
   - If you use `py` instead on Windows it might not work due to the python microsoft store alias.
5. Push your commit and tag to RobustToolbox (`git push` and `git push https://github.com/space-wizards/RobustToolbox.git v0.1.0`, WITH 'v')
   - Do NOT run `git push --tags` as that will push every tag you have locally, even those that have been deleted.
6. Go back into the content directory (`cd ..`)
7. Checkout a new branch (`git checkout -b update/robust-0.1.0`)
8. Commit the engine change (`git commit RobustToolbox -m "Update RobustToolbox"`)
9. Push your branch (`git push`)
10. Open a PR to the content repository and merge it.

```admonish warning
It is always a good idea to run the game with the new engine version before publishing it and merging the PR, to check that everything still works.
You can also run tests locally with "dotnet test" as that will be faster than waiting for them to run on the GitHub workflows.
```
