# Container Controls

There are many controls whose sole purpose is to lay their children out in a certain way, and otherwise be invisible. This section will go over some of them.

This is not a complete list, but it does cover the most commonly used ones. If you would like to complete this list and PR it that would be appreciated :).

## `BoxContainer`

`BoxContainer` is perhaps one of the simplest layout controls there is. It lays out its children sequentially in a certain `Orientation`, either vertically or horizontally. Controls do not overlap.

```admonish warning
You MUST include a `Orientation` for the `BoxContainer` to work.
```

| Field                | Type                | Effective Default Value | Description                                                 |
| -------------------- | ------------------- | ----------------------- | ----------------------------------------------------------- |
| `Orientation`        | `LayoutOrientation` |                         | Whether to arrange the elements horizontally or vertically. |
| `Align`              | `AlignMode`         |                         | The alignment of the children along the orientation axis.   |
| `SeparationOverride` | `int`               | `0`                     | The separation between elements.                            |

## `GridContainer`

`GridContainer` lays out its children in a configurable grid.

| Field                 | Type    | Effective Default Value | Description                                                                                                                    |
| --------------------- | ------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `Columns`             | `int`   |                         | The number of columns to organize the children into.                                                                           |
| `Rows`                | `int`   |                         | The number of rows to organize the children into.                                                                              |
| `MaxGridWidth`        | `float` |                         | The maximum width of the grid of elements, and dynamically determines the number of columns based on the size of the elements. |
| `MaxGridHeight`       | `float` |                         | The maximum height of the grid, and dynamically determines the number of rows based on the size of the elements                |
| `VSeparationOverride` | `int`   | `0`                     | The vertical separation between elements.                                                                                      |
| `HSeparationOverride` | `int`   | `0`                     | The horizontal separation between elements.                                                                                    |
| `ExpandBackwards`     | `bool`  | `false`                 | Whether to expand the grid backwards, i.e. from the bottom-right to the top-left.                                              |

## `ScrollContainer`

`ScrollContainer` is a container that shows a slice of its children, with scrollbars to scroll through the rest. You've seen a scrollbar before you know what this is.

| Field                   | Type   | Effective Default Value | Description                                                                 |
| ----------------------- | ------ | ----------------------- | --------------------------------------------------------------------------- |
| `FallbackDeltaScroll`   | `bool` | `false`                 | If true, if we have a y-axis scroll it will convert it to an x-axis scroll. |
| `ScrollSpeedX`          | `int`  | `50`                    | The scroll speed in the x-direction.                                        |
| `ScrollSpeedY`          | `int`  | `50`                    | The scroll speed in the y-direction.                                        |
| `ReserveScrollbarSpace` | `bool` | `true`                  | Whether the scrollbar will take up space in the layout                      |
| `ReturnMeasure`         | `bool` | `false`                 | _TODO: I do not know what this does_                                              |
| `VScrollEnabled`        | `bool` | `true`                  | Whether vertical scrolling is enabled.                                      |
| `HScrollEnabled`        | `bool` | `true`                  | Whether horizontal scrolling is enabled.                                    |

### `LayoutContainer`

`LayoutContainer` helps in complicated layouts by arranging its children.

| Field                 | Type    | Effective Default Value | Description                                                                                |
| --------------------- | ------- | ----------------------- | ------------------------------------------------------------------------------------------ |
| `AnchorBegin`         | `float` | `0`                     | The value of an anchor that is at the beginning of the layout.                             |
| `AnchorEnd`           | `float` | `1`                     | The value of an anchor that is at the end of the layout.                                   |
| `InheritChildMeasure` | `bool`  | `true`                  | If true, measurements of this control will be at least the size of any contained controls. |

Then children of the `LayoutContainer` may use to following fields to control their layout:

| Field            | Type    |
| ---------------- | ------- |
| `MarginLeft`     | `float` |
| `MarginTop`      | `float` |
| `MarginRight`    | `float` |
| `MarginBottom`   | `float` |
| `AnchorLeft`     | `float` |
| `AnchorTop`      | `float` |
| `AnchorRight`    | `float` |
| `AnchorBottom`   | `float` |
| `GrowHorizontal` | `bool`  |
| `GrowVertical`   | `bool`  |
