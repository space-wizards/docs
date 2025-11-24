# UI Cookbook

This section concerns common UI patterns you may want to implement yourself.

```admonish note
If you've figured out something tricky with a UI, or if you just want to let people know
something you made exists, considering sharing the wealth and adding it here!
```

## Status Colors

`Palettes.Status` allows you to show the status of something with a color, (red = bad,
amber = ok, green = good). You just need to give it a number between 0 and 1, and
it will blend between the colors (using fancy OKLAB blending!!).

```cs
Palettes.Status.GetStatusColor(0.0f); // red
Palettes.Status.GetStatusColor(0.5f); // amber
Palettes.Status.GetStatusColor(1.0f); // green

Palettes.Status.GetStatusColor(0.25f); // blends between red and amber
```

## Multiple Style Classes

In order to add multiple style classes to an element within its XAML file, some
extra boilerplate is required:

```xml
<Control xmlns:sys="clr-namespace:System;assembly=System.Runtime">
    <Button Text="delete">
        <Button.StyleClasses>
            <sys:String>ButtonSmall</sys:String>
            <sys:String>negative</sys:String>
        </Button.StyleClasses>
    </Button>
</Control>
```
