<template>
    <Popup :visible="value" title="Markdown Help" @closePopup="close">
        <MarkdownViewer
            content="
This is a demonstration showing some of the Markdown notation that
you can use to customise your posts and comments.

# Headings
```css
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
```
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

# Text Styles

For Italic text we wrap the text in single *s:

```css
*this is italic*
```

*this is italic*

For Bold text we wrap the text in double **s:

```css
**this is bold**
```

**this is bold**


# Links

Links will be automatically detected, but you can create a hyperlink like this:

```css
[this is a link to Google!](https://google.com)
```

[this is a link to Google!](https://google.com)

# LaTeX

You can create inline LaTeX by surrounding the LaTeX in $ symbols:

```css
$\sum x^2 \mu$
```

$\sum x^2 \mu$

For larger multiline blocks of LaTeX you can use double $$ symbols

```css
$$
\sum \mu x^2
\int \alpha y^3
$$
```

$$
\sum \mu x^2
\int \alpha y^3
$$

# Images

Images can be included with the following notation:

```css
![image description](https://www.google.com/logos/google.jpg)
```

![image description](https://www.google.com/logos/google.jpg)

# Lists and indents

Bullet point lists can be created with the - symbol:

```css
- List Item 1
- List Item 2
```

- List Item 1
- List Item 2

Numbered lists can be created using numbers like this:

```css
1. First Thing
2. Second Thing
```

1. First Thing
2. Second Thing

Blockquotes can be created by prefixing the line with a >:

```css
> This is a blockquote
```

> This is a blockquote

# More

The most common syntax is mentioned above, but that's not all we support!

Have a look at [Markdown Guide's Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
to get a complete list of the Markdown syntax
        "
        />
    </Popup>
</template>

<script>
import Popup from '~/components/helpers/Popup'
import MarkdownViewer from '~/components/post/MarkdownViewer'

export default {
    name: 'MarkdownHelpPopup',
    components: { MarkdownViewer, Popup },
    props: {
        value: {
            type: Boolean,
            required: true,
        },
    },
    methods: {
        close() {
            this.$emit('input', false)
        },
    },
}
</script>

<style scoped></style>
