# Guide to Editing Docs

Hello! As you may be able to notice, this docs site is completely open source and free to edit on GitHub. You can see the GitHub page for this site at [https://github.com/space-wizards/docs](https://github.com/space-wizards/docs).

There are a couple things to keep in mind when contributing. While we disallow web-edit PRs (those made exclusively on GitHub) on the main Space Station 14 & Robust Toolbox repos, that is not the case here. **Web-editing is encouraged** to make editing documentation as painless as possible.

If you want to get an idea of what features are at your disposal when writing documentation, go to our [Docs Example Page](./docs-example-page.md).

## Style

Documentation should be written in a [technical communications style](https://ohiostate.pressbooks.pub/feptechcomm/chapter/3-writing-style/). Effective technical communications are [concise, precise, direct, and well organized](https://ohiostate.pressbooks.pub/feptechcomm/chapter/3-writing-style/) and should be written in an appropriate [voice and tone](https://ohiostate.pressbooks.pub/feptechcomm/chapter/3-1-voice-tone/) using [correct mechanics and grammar](https://ohiostate.pressbooks.pub/feptechcomm/chapter/3-2-mechanics-grammar/), citing relevant sources where needed.

## Making basic edits

If you just want to make a basic edit of a page, simply follow these steps--you don't need any of the fancy stuff talked about later:

1. Create an account on GitHub, or log in if you already have one.

2. Fork the [space-wizards/docs](https://github.com/space-wizards/docs) repo on GitHub.

![](../assets/images/meta-create-fork.png)

3. Click the 'View & Edit Page on GitHub` icon in the very top right of any page on this site.

![](../assets/images/meta-edit-page-button.png)

4. Click the 'Edit this file' button at the top right of the file view.

![](../assets/images/meta-edit-file.png)

5. Make your changes, then commit & create a pull request! We'll handle the rest.

## Building

If you want to locally build the docs, the necessary dependencies are Rust and some binaries installed using `cargo`. It's recommended that you use `cargo install` or `cargo quickinstall`, as building can take a while.

From cargo, install:
- `mdbook`
- `mdbook-admonish`
- `mdbook-embedify`
- `mdbook-emojicodes`
- `mdbook-linkcheck`
- `mdbook-mermaid`
- `mdbook-template`

Run `mdbook serve` to build and locally host the documentation from the `book` directory at `localhost:3000`.

## Testing changes

If you've made a PR, the easiest way to test your changes, since they're just markdown, is to view them in GitHub's own markdown viewer in the `Files changed` tab. You can also use a local markdown previewer extension for something like [VSCode](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced). 

If you want a slightly more authentic experience, every PR will have the `Test mdBook Build & Upload Artifact` action run, and you can download the built site like so:

![](../assets/images/meta-artifact-download.png)

Then, just unzip it and open `index.html`. Our custom CSS and stuff won't work super well but it'll look good enough.

For an authentic-authentic experience, just follow the build instructions above and run `mdbook serve` like normal.

## Review

Maintainers will review pull requests for documentation for content and [style](#style). Maintainers understand that many contributors do not speak English as a native language and will be helpful with their review comments.

To help make best use of maintainers' review time, before submitting please:

- Proofread your changes
- Use a spell checker
- Consider using grammar review tools like [Grammarly](https://www.grammarly.com/)
