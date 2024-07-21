# UI and You

Or how I learned to stop worrying and love Sheetlets.

```admonish note
The UI system in SS14 has been through several iterations, and much of the
current UI code is very much antiquated. When creating UI, it is generally very
helpful to reference other code, however when referencing code when making
your UI, please keep the age of the code in mind.

If you find some code that is not up to the current conventions, refactors are
always appreciated!
```

Before learning how it should be done in SS14, it's important to understand how
the engine handles UI. Please reference the [user interface documentation](../robust-toolbox/user-interface.md)
first.

## Okay, but how do I make it fancy?

### `FancyWindow`

`DefaultWindow` is depreciated. Unless you're making your own custom window,
`FancyWindow` should be used in all circumstances. It has additional properties
that integrate with SS14 better than `DefaultWindow`.

The `Stylesheet` property allows you to give a window to take styles from a
certain stylesheet. The default stylesheet is `Nanotransen`, but in certain
circumstances you may want to use others. Currently there are the following
stylesheets:

-   `Nanotransen` - The default stylesheet. Used for any standard player-facing Uis
-   `System` - Primarily used for admin and sandbox UIs
-   `Syndicate` (COMING SOON™) - Used for any UIs affiliated with the syndicate

### `StyleClass`

Any styles classes that can be reused must be defined in `Content.Client/Stylesheets/StyleClass.cs`.
This is to centralize the location of all available style classes, for ease of
access and prevention of duplicate style classes.

Any style classes that are generic / can be used for more than one element are
defined at the top. For example, the style class `positive` affects `Button`,
`Panel`, and `Label`.

The rest of the style classes are defined for a specific generic UI element.
Some common style classes are as follows:

-   `OpenLeft`: Makes the button flat on its left side
-   `OpenRight`: Makes the button flat on its right side
-   `OpenBoth`: Makes the button flat on both sides; square
-   `LabelSubtext`: Makes the label smaller and a more muted color
-   `LabelKeyText`: Makes the label bold and a highlight color
-   `LabelWeak`: Weak is the opposite of strong; makes the label a more muted color

There are many more than this, but if you want to know exactly what a given label
does, its as simple as looking at the field's usages, and reading the style rule definition.
This is where it may be helpful to use the Rider IDE, as it has a fantastic implementation of this feature,
but its probably possible in other IDEs as well.

```admonish tip
In general, if you are doing UI dev, I would recommend using the Rider IDE. It
eats up quite a bit of RAM, but it provides autocomplete in XAML files, a lot
of really nice auto-refactoring and searching features, and very decent git
integration. Give it a shot!
```

## Writing Styles

This section concerns style rules. For most UIs, editing these will be unnecessary,
however you should ALWAYS prefer to use style classes instead of hardcoding colors
or resources that could be commonly used.

### All hail the mighty `Sheetlet`

It's important to understand that basically, a stylesheet is a massive list of
every single style rule. Instead of manually
making a giant list of style rules (because that would be ridiculous... haha... ha....),
the responsibility of chipping into this list is distributed between many Sheetlets.
Each Sheetlet returns a small chunk of style rules, which is agglomerated into the
final list at the end.

```admonish note
Previously every single style rule was in one giant list: `StyleNano.cs`, a 1600
line pit of despair where dreams went to die.
```

There are, primarily, two types of Sheetlets:

-   **Generic Sheetlets**: These go in `Content.Client/Stylesheets/Sheetlets`.
    These stylesheets concern generic UI elements used in many different UIs, and
    should be written generically to work with any stylesheet.
-   **Specific Sheetlets**: These go along with the `*.xaml` files they are associated
    with. These stylesheets concern UI elements that are specific to a single UI,
    and should be written to work with the specific stylesheet they are associated
    with.

We will go into more detail about the specific conventions to follow for both of
these later.

All sheetlets should have the `[CommonSheetlet]` attribute. This is used so
stylesheets can find all the sheetlets that have this attribute and add their
styles to their list.

```admonish tip
Do not forget the `[CommonSheetlet]` attribute.
```

### Style Rules

Each style rule
has a few different components to it (This will look familiar to anyone who knows CSS):

**The selector**: This limits the elements that a style rule can affect. This is
made up of a few different parts:

-   `Type`: The type of element this rule affects. Anything inheriting from this
    type will be affected by this rule. This is similar to the element selector
    in css.
-   `StyleClasses`: The classes that the element must have to be affected by this
    rule. The element must have all of these classes to be affected by this rule.
-   `StyleIdentifier`: The identifier of the element. This is a unique identifier
    that can be used to target a specific element. This should be used sparingly,
    when there is only one instance of the element that needs to be styled in a
    highly specific manner. There may only be one of these specified.
-   `PseudoClasses`: These are special classes that can be used to target elements
    in a specific state. For example, this is used to style buttons differently
    when hovered or pressed or whatever.

Selectors that specify more of these parts are more "specific", and will take
priority over less specific elements.

**The properties**: Any elements matching the selector will then have their properties
modified by the style rule. These are the same properties you would define in
the XAML.

To assist with constructing these style rules, there are helper methods defined in
`Content.Client/Stylesheets/StylesheetHelpers`.

I think it's best to show an examples of style rules instead of describing all
their intricacies since the code is pretty self-explanatory.

```cs
// you need this using statement to use the helper methods
using static Content.Client.Stylesheets.Redux.StylesheetHelpers;

var rules =
[
    // select any element...
    E()
        // ...with the class "negative"
        .Class(StyleClass.Negative)
        // ...and set its font color to the text color from the negative palette
        .FontColor(sheet.NegativePalette.Text),

    // select any `Label`...
    E<Label>()
        // ...with the class "LabelHeading"
        .Class(StyleClass.LabelHeading)
        // ...and set its font to a bold 16pt font
        .Font(sheet.BaseFont.GetFont(16, FontKind.Bold))
        // ...and its font color to the text color from the highlight palette
        .FontColor(sheet.HighlightPalette.Text)

    // select any `ContainerButton`...
     E<ContainerButton>()
        // ...with the class "button"
        .Class(ContainerButton.StyleClassButton)
        // ...and the class "ButtonSmall"
        .Class(StyleClass.ButtonSmall)
        // ...that is the parent of a `Label`,
        .ParentOf(E<Label>())
        // ...and set that `Label`'s font to an 8pt font
        .Font(sheet.BaseFont.GetFont(8))
];
```

### Death to Hardcoding!

You may have noticed before that there wasn't much hardcoding in the rule definitions.
This is because most style rules are used in multiple stylesheets, and they have
to be generic between them. There are a couple different utilities used to reduce
hardcoding.

#### `ColorPalette`

There is actually a pretty robust (haha) color palette system to hopefully make
hardcoding colors unnecessary. I created a
[codepen](https://codepen.io/aspiringLich/pen/VwOXdjd?editors=1000)
to help visualize the colors. The stylesheets then use these palettes to set the following
common palettes for sheetlets to reference:

-   `PrimaryPalette`: Used for foreground elements
-   `SecondaryPalette`: Used for Background elements
-   `PositivePalette`: A traditionally green palette used to represent success / good / full
-   `NegativePalette`: A traditionally red palette used to represent errors / bad / empty
-   `HighlightPalette`: Used to highlight headings or important elements

In C#, you access the colors by accessing the
properties on the `ColorPalette` class. From brightest to darkest, the properties
are (as of writing) arranged as so:

-   `+0`: `Text` `Base`
-   `-1`: `TextDark`, `Element`
-   `-2`: `BackgroundLight`, `PressedElement`
-   `-3`: `Background`
-   `-4`: `BackgroundDark`, `DisabledElement`

Although it would be simpler to have the palettes be arrays of colors, I noticed
that colors were used in basically three ways: Text, foreground elements, and
background elements. So I represented that in the palette itself! It just makes
the code a bit more readable.

All palettes are defined in `Palettes.cs` as static properties. You can read
them from anywhere! Neat!

#### `ISheetletConfig`

`ISheetletConfig` is intended to cut down on repeated code by providing shared
functionality and definitions between the stylesheets.
Any `Sheetlet` that requires the values in some instance of
`ISheetletConfig` should have a generic type constraint that requires the
`ISheetletConfig` interface.

```cs
[CommonSheetlet] // don't forget `[CommonSheetlet]`!
public sealed class ExampleSheetlet<T> : Sheetlet<T> where T : PalettedStylesheet, IExampleConfig
```

`ISheetletConfig` also serves as a dependency check. When the stylesheets pull
all the sheetlets that have `[CommonSheetlet]`, they will first check that they
satisfy the type constraint before adding the rules to the stylesheet.

```admonish warning
This also means that the `Sheetlet` can silently fail the check and not be added
to the styles. If your sheetlet doesn't seem to be working, this may be the cause.
```

#### Resource Access

You should access resources differently in sheetlets. Each stylesheet provides a
list of resource roots to look in, when requesting a resource of a certain type.
For example, the root for `NanotransenStylesheet` for `TextureResource` is
`/Textures/Interface/Nano`. Any texture requested with `GetTexture` will will
append the provided relative path to the root, and return the texture if it exists.

This system is built to work with any resource type, though currently only textures
are used in the sheetlets.

### Generic Sheetlets

As stated earlier, generic sheetlets are used for generic UI elements that are
used in many different UIs.

-   You should always select elements with `.Class` and not `.Identifier`.
-   When accessing resources, use the `GetTextureOr` method to get the texture and
    provide a fallback root to use if the texture is not found within the stylesheets roots.
-   Avoid manual hardcoding of classes. When referencing classes,
    please only use classes defined on the element being styled (in `StyleClass*` properties)
    or define your own in `StyleClass.cs`.
-   Avoid manual hardcoding of colors. Use the palettes provided by the stylesheet
    to set the colors of elements. There are very few cases where you will actually
    need to manually hardcode a color in a generic sheetlet.
-   If you need to access a resource that is not provided already, please add the path
    to the relevant `ISheetletConfig` or create a new one entirely.

<details>
<summary>Example Code (click to expand)</summary>

```cs
using Content.Client.Stylesheets.Redux.SheetletConfigs;
using Content.Client.Stylesheets.Redux.Stylesheets;
using Robust.Client.UserInterface;
using Robust.Client.UserInterface.Controls;
// you need to add this line manually to access the helper methods
using static Content.Client.Stylesheets.Redux.StylesheetHelpers;

namespace Content.Client.Stylesheets.Sheetlets;

// MAKE SURE TO INCLUDE THE [CommonSheetlet] ATTRIBUTE
[CommonSheetlet]
// define the sheetlet and its dependencies
public sealed class CheckboxSheetlet<T> : Sheetlet<T> where T : PalettedStylesheet, ICheckboxConfig
{
    public override StyleRule[] GetRules(T sheet, object config)
    {
        // cast the sheet into any of its required dependencies here
        var checkboxCfg = (ICheckboxConfig) sheet;

        // get any textures / construct any complicated resources here
        var uncheckedTex = sheet.GetTextureOr(checkboxCfg.CheckboxUncheckedPath, NanotrasenStylesheet.TextureRoot);
        var checkedTex = sheet.GetTextureOr(checkboxCfg.CheckboxCheckedPath, NanotrasenStylesheet.TextureRoot);

        // and finally, define all the style rules and return a big 'ol list of them
        return
        [
            E<TextureRect>()
                .Class(CheckBox.StyleClassCheckBox)
                .Prop(TextureRect.StylePropertyTexture, uncheckedTex),
            E<TextureRect>()
                .Class(CheckBox.StyleClassCheckBox)
                .Class(CheckBox.StyleClassCheckBoxChecked)
                .Prop(TextureRect.StylePropertyTexture, checkedTex),
            E<BoxContainer>()
                .Class(CheckBox.StyleClassCheckBox)
                .Prop(BoxContainer.StylePropertySeparation, 10),
        ];
    }
}
```

</details>

### Specific Sheetlets

As stated earlier, specific sheetlets are used for UI elements that are specific
to a single UI. These sheetlets are located with the `*.xaml` file they are
associated with.

-   You should prefer to select elements with `.Identifier` and not `.Class`.
-   Any styles that COULD be used by another UI should be moved to a generic sheetlet.
-   Hardcoding is more relaxed, you should still try and avoid it when possible, but
    hardcoding `StyleClass`es and `StyleIdentifier`s is probably fine.
-   If you REALLY need a specific resource and its not worth adding it to an
    `ISheetletConfig` you can access it through `ResCache` as normal.
-   You don't need to do the generic type constraints thing since the sheetlet
    should be specific to a single UI, and thus a single stylesheet.

<details>
<summary>Example Code (click to expand)</summary>

```cs
using Content.Client.Resources;
using Content.Client.Stylesheets.Redux;
using Content.Client.Stylesheets.Redux.SheetletConfigs;
using Content.Client.Stylesheets.Redux.Stylesheets;
using Robust.Client.Graphics;
using Robust.Client.UserInterface;
using Robust.Client.UserInterface.Controls;
// you need to add this line manually to access the helper methods
using static Content.Client.Stylesheets.Redux.StylesheetHelpers;

namespace Content.Client.Paper.UI;

// MAKE SURE TO INCLUDE THE [CommonSheetlet] ATTRIBUTE
[CommonSheetlet]
// which stylesheet is this sheetlet for
public sealed class PaperSheetlet : Sheetlet<NanotrasenStylesheet>
{
    public override StyleRule[] GetRules(NanotrasenStylesheet sheet, object config)
    {
        // define any IConfigs you need here
        var windowCfg = (IWindowConfig)sheet;

        // get any textures / construct any complicated resources here
        var paperBackground = ResCache.GetTexture("/Textures/Interface/Paper/paper_background_default.svg.96dpi.png")
            .IntoPatch(StyleBox.Margin.All, 16);
        var paperBox = new StyleBoxTexture
            { Texture = sheet.GetTexture(windowCfg.TransparentWindowBackgroundBorderedPath) };
        paperBox.SetPatchMargin(StyleBox.Margin.All, 2);

        // and finally, define all the style rules and return a big 'ol list of them
        return
        [
            E<PanelContainer>().Identifier("PaperContainer").Panel(paperBox),
            E<PanelContainer>()
                .Identifier("PaperDefaultBorder")
                .Prop(PanelContainer.StylePropertyPanel, paperBackground),
        ];
    }
}
```

</details>

### Making your own `Stylesheet`

Creating a new stylesheet is pretty simple, so I won't go into it too much.
One thing to keep in mind is how colors are chosen.

The colors are generated using the [OKLAB color space](https://bottosson.github.io/posts/oklab/),
which is better because something something human eyes something. When you choose
new colors for your stylesheet, it may be helpful to use an [OKLCH Color Picker](https://oklch.com)
and modify an existing color.

## Writing C# for UI

> **TODO:** I don't feel confident enough in my knowledge to describe in detail
> what to do and what not to do. This is just a general overview for now and
> should be updated.

The best way to learn how to write UI code is to look at existing code. Some UIs 
definitely do some terrible things you should never replicate, but there are mountains
of terrible code in SS14, so this is not abnormal. I cannot teach familiarity with
the internals of this game, but I can give a  general overview.

Code you could reference:
-    Robotics Console
-    Cryo Pod
-    Reagent Dispenser

There are a few different parts to any UI. say were working with a entity
called `MyThing`, which we wanted to show a UI for. Heres, generally, what the 
structure would look like:

```yaml
Content.Server/MyThing/:
- Systems/:
  - MyThingSystem.cs                # Inherits from `SharedMyThingSystem.cs`
                                    # Takes the messages and makes changes in-world, and takes data from in-world to update the UI state.
Content.Shared/MyThing/:
- Components/:
  - MyThingComponent.cs             # Defines the component for the entity
- Systems/:
  - SharedMyThingSystem.cs          # Controls the appearance data and general shared logic
- SharedMyThing.cs                  # Defines the messages that can be sent between server and client, and the UI state

Content.Client/MyThing/:
- Ui/:
  - MyThingWindow.xaml              # The main window, where the main structure of the UI is defined
  - MyThingWindow.xaml.cs           # Defines behavior for `MyThingWindow.xaml`, reading in inputs and calling `Action`s
  - MyThingBoundUserInterface.cs    # Interfaces with the server, sending messages and updating the UI state
- Systems/:
 - MyThingSystem.cs                 # Inherits from `SharedMyThingSystem.cs`
                                    # Takes appearance data and makes in-world changes to reflect that
```

### Bound User Interfaces

> **TODO:** someone more familiar with BUIs than me should write about how to write
> good BUIs. I'll just stick the notes from
> `#codebase-changes` by Bard in the discord here for now:
>
> > Predicted BUIs are in:
>
> For networking data:
>
> Option 1 (Preferred). Move the BUI state to component states. Use an existing client system / make one to handle updating the BUI upon the state updating (use TryGetOpenUi) and upon calling Open in the BoundUserInterface. See JukeboxSystem for an example, e.g.
>
> ```cs
> private void OnJukeboxAfterState(Entity<JukeboxComponent> ent, ref AfterAutoHandleStateEvent args)
> {
>     if (!_uiSystem.TryGetOpenUi<JukeboxBoundUserInterface>(ent.Owner, JukeboxUiKey.Key, out var bui))
>         return;
>
>     bui.Reload();
> }
> ```
>
> Option 2. Have the BUI control be a dummy until the state comes in
>
> For UIs:
> Call TryOpenUi in shared where possible and the client should just handle it. Calling it from server will also still work similar to the old behavior.
>
> For messages:
> Use SendPredictedMessage where possible in BUIs. At some point this will likely become the default over SendMessage.
>
> Overall:
> Prefer to use the overloads that take in EntityUids instead of ICommonSession, this will make it easier to code NPCs who can interact with UIs in future.
>
> >
>
> -   There's a helper under this.CreateWindow<TWindow>() for BUIs that handles disposing + opening + close subscription for you.
> -   There's a method OnProtoReload that gets called on BUIs so you can override and handle it without having to manually subscribe on another system.
> -   I have added prototype reload support to some stuff.
> -   I have cleaned up a lot of BUI code. Windows now just raise events and the BUI itself handles message sending.
>
> Some notes for future:
>
> -   You should spawn / delete control entities inside of EnteredTree and ExitedTree rather than inside Dispose.
> -   Controls should be able to be constructed with an empty constructor and should not call BUI methods directly. This makes re-use significantly easier.
> -   All new controls must handle prototype reloading if applicable.
> -   All new controls should prefer to use component states and not BUI states where possible. These work better with prediction and are easier to use.
> -   Controls should be able to handle components disappearing and not rely upon GetComponent<T> everywhere as there are no guarantees the component exists.
