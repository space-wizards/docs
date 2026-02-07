# UI Survival Guide

{{ #template ../templates/outdated.md }}

## Learning to walk before you run
So you have choosen to take on the harsh wasteland that is coding UI and working with Stylesheets?

Great!

But before you can start ~~sacrificing puppies~~ making fancy UIs using our UI system you first need to know how to define a basic UI layout so I recommend reading the [basic user interface documentation](../robust-toolbox/user-interface.md) first.

## Quick and dirty (Using FancyWindow)

```admonish quote
The line between life or death is determined by what we are willing to do. 
- Bear Grylls
```

So your UI doesn't require fancy styling magic but you want it to look like the final mockups on our [figma page](https://www.figma.com/file/KE5eKymegsLrsQdjZGbTIs/UI?node-id=0%3A188)?

Count yourself lucky because you can get away with just using `FancyWindow` instead of `DefaultWindow`!

To use it you just change:
```xml
<DefaultWindow xmlns="https://spacestation14.io" ... >
  ...
</DefaultWindow>
```
Into:
```xml
<ui:FancyWindow xmlns="https://spacestation14.io" 
                xmlns:ui="clr-namespace:Content.Client.UserInterface"
                ... >
  ...
</ui:FancyWindow>
```
You might need to change some margins but you get quite literally a fancy window.

## Learning from those that survived

When taking your first steps into the UI wasteland you sould look at how the brave UI coders that came before you survived this harsh environment.

One of the best examples to look at is the [GravityGeneratorWindow](https://github.com/space-wizards/space-station-14/blob/master/Content.Client/Gravity/UI/GravityGeneratorWindow.xaml).

It containes some basic style classes that you can just use for your own UI like: `StatusFieldTitle` for labels and `OpenRight\OpenLeft` for buttons.

You can just copy the `StyleClasses="..."` attribute into your ui component to make use of them.

Whenever you see a fancy UI that has a component that is styled the way you need it and it's written in xaml you can try and see if just copying that does the trick.

## Digging deeper

```admonish quote
The rewards of the wild and the rewards of the survivor go to those who can dig deep, and, ultimately, to the guy who can stay alive.
-  Bear Grylls
```

You used `FancyWindow` and ~~stole code~~ looked at style classes from other UIs and it's still not **fancy** enough?

Then you have no choice but to venture deep into the treacherous lands of stylesheet code. *\*cue dramatic music\**

Taking a look at [StyleNano.cs](https://github.com/space-wizards/space-station-14/tree/master/Content.Client/Stylesheets/StyleNano.cs) will ~~instill you with fear~~ overwhelm you with its 1318 lines of code.

`StyleNano` mainly consists of tree things:
- Variable/Constant declarations
- Style classes written the hard to read way
- Style classes written the easy to read way

Now you **want** to write new style classes using the easy to read way but you also need to understand the hard to read way so you can look at style classes that are already there.

You can safely skip all of the variable and constant declarations until you reach the following lines (currently line 465):
```cs
    Stylesheet = new Stylesheet(BaseRules.Concat(new[]
    {
```
This stylesheet declaration is where all the style classes go.

Here (and a similiar construct in [StyleBase.cs](https://github.com/space-wizards/space-station-14/tree/master/Content.Client/Stylesheets/StyleBase.cs)) is where you can look up and add style classes.

### Hard to read way of declearing a style class

Currently most of the style classes are written using the hard to read way like so:
![hard-to-read-style.png](../assets/images/ss14-by-example/hard-to-read-style.png)

1. New style classes are created by instanciating the StyleRule class
2. You specify the type of control the class is for by instanciating a SelectorElement with the type of the control class
3. Then you define style class names as an array of strings (StyleClassWindowCloseButton is just a string constant)
4. The forth SelectorElement constructor parameter is a pseudo class you can use for things like hover states. This can be null.
5. The second StyleRule constructor parameter is an array of Style properties. The StyleProperty constructor takes the property name as a string (Usually from a string constant inside the control you are trying to style) and a value you want to set that property to.

### Easier to read way of declaring a style class

```csharp
Element<PanelContainer>().Class("BackgroundDark")
                    .Prop(PanelContainer.StylePropertyPanel, new StyleBoxFlat(Color.FromHex("#25252A"))),
```
1. `Element<PanelContainer>` and `.Class("BackgroundDark")` specify the type of control and the class you want the style apply to.
2. `.Prop(PanelContainer.StylePropertyPanel, new StyleBoxFlat(Color.FromHex("#25252A"))` assigns a value the a property where the first argument is the property and the second argument is the value. In this case it sets the background color for a panel container.

## The hidden dangers

```admonish quote
But the wild is unpredictable, stuff does happen, and it's always when you're least expecting it.

- Bear Grylls
```
