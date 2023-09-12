# Space Wizards Development Wiki

This is a work-in-progress port of the old SS14 Wiki.js documentation to `mdbook`, for the following benefits:
- First-class git support, open source and actually editable by everyone
- No webshit bloat, much faster in general
- More familiar & comfortable for developers since `mdbook` use is very widespread
- No sign-on infrastructure or hosting necessary (besides GH pages)
- More customizable
- Friction to editing reduced significantly
- Eventual localization support

The following `mdbook` features & plugins are available and in use:
- `MathJax` support 
- Sidebar ToC (integrated directly into `index.hbs` etc)
- `mdbook-mermaid`
- `mdbook-linkcheck`
- `mdbook-template`
- `mdbook-admonish`

The site is currently hosted at [https://spacestation14.io/docs/](https://spacestation14.io/docs/). This will likely change in the future, so links here should not be relied on.

## Building

Necessary dependencies are Rust, as well as `mdbook` and the plugins listed above, installed using cargo.

Call `mdbook serve` to build and locally host the documentation from the `book` directory.

## Contributing & porting pages

To port a page, you'll need write access to `docs.spacestation14.io` (old wiki.js), or find some way to view MD source idk.

1. Find a page with the `Porting` template on the top
2. Find the corresponding page in Wiki.js -- it should just have the same name 
3. Copy over the Wiki.js markdown
4. Change any relative links to point to their correct corresponding
5. Change any self-hosted or imgur images to be hosted in `src/en/assets` instead
6. Adjust any admonishments as follows:
    ``````
    > etc text example
    {.is-(danger/warning/info/example)}
    ``````
    to
    ``````
    ```admonish danger/warning/info/example "Title Text Or Leave blank etc"
    etc text example
    ```
    ``````
7. Add a redirect for the original wiki.js link to the new `src/SUMMARY.md` link in `book.toml`--follow the example. You'll need to add `/index.html` after the wiki.js link for it to redirect properly.

## Testing changes

If you've made a PR, the easiest way to test your changes, since they're just markdown, is to view them in GitHub's own markdown viewer in the `Files changed` tab. You can also use a local markdown previewer extension for something like [VSCode](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced). 

If you want a slightly more authentic experience, every PR will have the `Test mdBook Build & Upload Artifact` action run, and you can download the built site like so:

![](src/en/assets/images/readme-artifact-download.png)

Then, just unzip it and open `index.html`. Our custom CSS and stuff won't work super well but it'll look good enough.

For an authentic-authentic experience, just follow the build instructions above and run `mdbook serve` like normal.

## Screenshots

![](src/en/assets/images/readme-example-1.png)

![](src/en/assets/images/readme-example-2.png)

## License

The Space Wizards Development Wiki is released under the Mozilla Public License v2.0.
