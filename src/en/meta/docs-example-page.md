# Docs Example Page

This page is used for showing off plugins and styling available in this `mdbook` instance.

Its best to view the raw markdown source of this page, which you can do using the button in the top right and clicking 'Code' instead of 'Preview' on GitHub.

## markdown

Best to look at [a general markdown guide](https://www.markdownguide.org/getting-started/) for this! There's a lot.

**bold**

*italic*

~~strikethrough~~

## templates

You can also pass args into a template invocation which are interpolated into the page by `mdbook-template`. See [their docs](https://github.com/sgoudham/mdbook-template#format) for more info

`\{\{#template {link to template file}\}\}`

{{#template ../templates/outdated.md}}

{{#template ../templates/wip.md}}

{{#template ../templates/stub.md}}

## admonishments

All available admonishment types.

To use an admonishment:
``````
```admonish {type} "{text you want as title, or leave blank}"
description
```
``````

```admonish note
```

```admonish abstract
```

```admonish info
```

```admonish tip
```

```admonish success
```

```admonish question
```

```admonish warning
```

```admonish failure
```

```admonish danger
```

```admonish bug
```

```admonish example
```

```admonish quote
```

## latex

\\[ \mu = \frac{1}{N} \sum_{i=0} x_i \\]

## mermaid

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```
