# Container Controls

Container is type of control that dictates the layout of other controls. The
containers logic only affects direct child controls. Containers usually arrange
child controls every frame by collecting their desired size via `.Measure()` and
then providing them with the size that they can afford via `.Arrange()`. After
calculation of the desired and afforded sizes of its children, the container can
override the child components coordinates if needed. This document only covers
some of the most commonly used containers. Additions expanding it with others
are welcome.

```admonish info
This page is a stub and complete descriptions of how containers will react to
new items being added, overflow, the subtleties with `GridContainer` etc. are
not convered.
```

## `BoxContainer`

`BoxContainer` is the most straightforward layout control. It lays out its
children sequentially in a certain `Orientation`, either vertically or
horizontally. Controls do not overlap.

| Field                | Type                | Effective Default Value | Description                                                 |
| -------------------- | ------------------- | ----------------------- | ----------------------------------------------------------- |
| `Orientation`        | `LayoutOrientation` | `Horizontal`            | Whether to arrange the elements horizontally or vertically. |
| `Align`              | `AlignMode`         | `Begin`                 | The alignment of the children along the orientation axis.   |
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

`ScrollContainer` is a container that shows a cropped view of its children, with
optional scrolling either vertically, horizontally, or both.

| Field                   | Type   | Effective Default Value | Description                                                                                                   |
| ----------------------- | ------ | ----------------------- | ------------------------------------------------------------------------------------------------------------- |
| `FallbackDeltaScroll`   | `bool` | `true`                  | If true, a vertical scroll will be translated into a horizontal scroll if vertical scrolling is not possible. |
| `ScrollSpeedX`          | `int`  | `50`                    | The scroll speed in the x-direction.                                                                          |
| `ScrollSpeedY`          | `int`  | `50`                    | The scroll speed in the y-direction.                                                                          |
| `ReserveScrollbarSpace` | `bool` | `false`                 | Whether the scrollbar will take up space in the layout                                                        |
| `VScrollEnabled`        | `bool` | `true`                  | Whether vertical scrolling is enabled.                                                                        |
| `HScrollEnabled`        | `bool` | `true`                  | Whether horizontal scrolling is enabled.                                                                      |

### `LayoutContainer`

`LayoutContainer` helps in complicated layouts by allowing its children to
specify how they should be laid out.

| Field                 | Type    | Effective Default Value | Description                                                                                |
| --------------------- | ------- | ----------------------- | ------------------------------------------------------------------------------------------ |
| `AnchorBegin`         | `float` | `0`                     | The value of an anchor that is at the beginning of the layout.                             |
| `AnchorEnd`           | `float` | `1`                     | The value of an anchor that is at the end of the layout.                                   |
| `InheritChildMeasure` | `bool`  | `true`                  | If true, measurements of this control will be at least the size of any contained controls. |

Then children of the `LayoutContainer` may use to following fields to control
their layout:

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
