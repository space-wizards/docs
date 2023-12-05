# Beginner FAQ

## Contributing to Space Station 14

### I want to start contributing to Space Station 14 but I do not know where to start.

Go to [Issues in Space Station 14](https://github.com/space-wizards/space-station-14/issues)
- Choose 1 or more of the following labels in [Labels](https://github.com/space-wizards/space-station-14/labels)
1. [Beginner Friendly](https://github.com/space-wizards/space-station-14/labels/Beginner%20Friendly)
2. [Difficulty: 1 - Easy](https://github.com/space-wizards/space-station-14/labels/Difficulty%3A%201-Easy)
3. [No C#](https://github.com/space-wizards/space-station-14/labels/No%20C%23) to work on issues that require no code. 

After you have chosen an issue to fix, follow the steps here to start making and testing code changes on your own copy of the Space Station 14 code: 
- [Setting up a Development Environment](https://docs.spacestation14.com/en/general-development/setup/setting-up-a-development-environment.html) 
   - This will let you play a local copy of the game so you can see your changes in gameplay.
- [Git for the SS14 Developer](https://docs.spacestation14.com/en/general-development/setup/git-for-the-ss14-developer.html)
   - This will let you work on code that you can transfer from your computer to your Github repository and eventually to Space Station 14.



### How does code get transferred between my computer & the main Space-Station-14 repository? 

```admonish danger "Make a new branch so you are not working on the master branch!"
This is important to know so you do not accidentally delete all of your code changes when you update your copy of Space Station 14.
- [Git for the SS14 Developer](https://docs.spacestation14.com/en/general-development/setup/git-for-the-ss14-developer.html#3-setting-up-remotes)
```

**3 Code Locations to know:**
1) Your Computer code (Your copy)
2) Your Github Repository (Local Github)
3) Space Station 14 Github


**How the code is transferred.**
1. **Space Station 14 Github => Local Github**. You make a fork of the Space Station 14 repository so you have a Local Github copy of the code yourself.
2. **Local Github <==> Space Station 14 Github**. Do NOT make your own code changes on your master branch.
- Your master branch needs to be linked to the master branch of Space Station 14.
- Every time Space Station 14 Github updates its code, your master branch on your Local Github repository will need to update its code as well so it stays in sync.
3. **Local Github => Your copy**. Follow [Setting up a Development Environment](https://docs.spacestation14.com/en/general-development/setup/setting-up-a-development-environment.html) & [Git for the SS14 Developer](https://docs.spacestation14.com/en/general-development/setup/git-for-the-ss14-developer.html)
4. **Your copy**. Make a new branch from your code editor where you will make code changes.
5. **Your copy**. Test your changes in gameplay.
6. **Your copy => Local Github**. When your code is ready, make a commit to your Github repository from your non-master branch.
7. **Space Station 14 Github => Local Github**. Sync Fork

![image](https://github.com/alwinnocom/docs/assets/63136288/0823b607-d87c-4495-97b8-32f06b343b4e)

- For your code to work, it must fit into the code in Space Station 14 Github.
- You will have to keep your Local Github code up-to-date with the Space Station 14 Github.

8. **Local Github => Your copy** Pull the updated code from your Local Github repository to your copy.

![image](https://github.com/alwinnocom/docs/assets/63136288/725a5132-32d0-4e0c-9223-fb35186365da)

You may need to merge changes if you are trying to change files that got changed from the update.
![image](https://github.com/alwinnocom/docs/assets/63136288/d6602410-3751-410d-9dd9-48f4b289706a)


9. **Your copy => Local Github**. Commit your changes.
10. **Local Github <==> Space Station 14 Github**. Make a pull request.
- If you make code changes from your master branch & make a pull request from your master branch, both your code changes and your pull request are at risk of self-destruction.
   - The only way to keep your code up-to-date with the actual Space Station 14 code is to sync the code.
   - This will require you to discard your commits.
   - Once you discard your commits, your code changes will be deleted & your pull request will be closed. Which is not fun.
11. Wait for Code Reviewers to let you know if your code is good to go for merging. 



### I have an idea for a new feature or to fix an issue that I have not seen on Github.

1. Try playing the game first so you know what features are already implemented.
- "Feature bloat" occurs if you make a feature that already exists.
   - For example, allowing a specific action to toggle by pressing "4" when it already can be toggled by pressing "z".
2. Propose the Feature before you start making it. [Feature Proposals](https://docs.spacestation14.com/en/general-development/feature-proposals.html)
3. Open a New Issue on Space Station 14: [New Issue](https://github.com/space-wizards/space-station-14/issues/new/choose)



## Coding Space Station 14

### I cannot play a local copy of the game because not all of the projects are loading.

Have you completed step 2.3 of [Git for the SS14 Developer](https://docs.spacestation14.com/en/general-development/setup/git-for-the-ss14-developer.html#23-submodule-woes)?

Make sure you use the command `cd` to navigate to your space-station-14 repository before running `RUN_THIS.py`.
![image](https://github.com/alwinnocom/docs/assets/63136288/1750eb6a-20e3-4d3c-9b4c-d7272787aaf2)



## Researching Space Station 14

### I am looking for text that I saw in gameplay but I am not sure where to look.

1. Lots of the in-game text can be found in XAML files & YML files. You can search through XAML files to find the parts of the user interface that you want to work on.
![image](https://github.com/alwinnocom/docs/assets/63136288/2a4aef1b-2839-455d-a867-b9c457f9d3a2)
2. If YML files are not showing up, you can find them on Github by going to the [Space Station 14 repository](https://github.com/space-wizards/space-station-14?search=1) & searching for .yml files.
3. Use your code editor to search for the exact text (for text that is not based on Project Fluent). For example, Visual Studio lets you use Ctrl + Shift + F to find certain text in all of the files.

![image](https://github.com/alwinnocom/docs/assets/63136288/cffa2910-3c9f-4f77-87bc-7f8a43b6895f)

4. Not all text shows up exactly as written because Space Station 14 uses Project Fluent to make text that automatically translates to different languages.
- [Project Fluent](https://docs.spacestation14.com/en/ss14-by-example/fluent-and-localization.html)
   - This means that some text shows up as `Loc.GetString("id-that-references-fluent-file")`

![image](https://github.com/alwinnocom/docs/assets/63136288/f5090633-19f5-4ec5-b843-15754cafff69)

5. If you want to find where a method is referenced throughout the code, you can click on the method name on Github to find where the method is referenced.

![image](https://github.com/alwinnocom/docs/assets/63136288/deefd271-cf47-451d-8309-0435770d6990)
