# Progress Report Creation
*A short handbook about making a progress report.*

### Checklist
- Set an explicit start- & end-date of contributions you want to outline.
- Create a Trello board based off of the Progress Report Trello Template.
- Run the [tool](https://github.com/space-wizards/github2trello) to generate Trello cards for every Content/Engine pull request. Note that Content PRs without changelogs will be skipped.
- Organize the cards into their columns as you see fit.
- Write descriptions for every card.
- Combine the card contents into a markdown file based off of the Progress Report Markdown Template, but be sure to update the PR number.
- Ask PJB for the Patrons list.
- Add the contributors list, see below.
- Replace/remove names as stated [here](https://github.com/space-wizards/space-station-14/blob/master/Tools/contribs_shared.ps1).
- Put the markdown file into `website-content/content/post`. Images go in a new `website-content/static/images/post/pr_[number]` directory and videos go in a new `website-content/static/video/pr_[number]` directory.
- Create PNGs and MP4s for every section that needs them.
- Run [this script](https://github.com/space-wizards/website-content/blob/master/Tools/pr-image-convert.ps1) in the directory with all of the PNGs. Requires [ImageMagick](https://imagemagick.org/index.php) and [optipng](http://optipng.sourceforge.net/).
- Make a thumbnail (800x450) PNG and put it in `website-content/assets/images/thumbnails`.
- Create a pull request on the [website repo](https://github.com/space-wizards/website-content). Give everyone a chance to review it for a couple days, then merge at the same time as you release it.

### Datasources
- List of all contributors with the following command: `git shortlog -s -n --since=<start> --until=<end>`.
- Commit-count: `git rev-list --count master --since=<start> --until=<end>`.

### Places to Release
- Website. Automatically published when the pull request to `website-content` is merged.
- Steam (bug PJB or Smug).
- Discord.
- Patreon (bug PJB).
- Reddit (r/ss13, r/ss14, & r/linux_gaming).
- Twitter (bug PJB or Smug).
