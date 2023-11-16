# EditorConfig

> [EditorConfig](https://editorconfig.org) helps developers maintain consistent coding styles between different editors


## Install

Install `EditorConfig` with [Package Control](https://packagecontrol.io) and restart Sublime.


## Getting started

See the [EditorConfig site][] for documentation.


## Supported properties

- root
- indent_style
- indent_size
- end\_of\_line
- charset
- trim_trailing_whitespace
- insert_final_newline

Explanation of the properties can be found on the [EditorConfig site][].

<sub>The `tab_width` property is intentionally not supported.</sub>


## Example file

*My recommended default settings*

```ini
root = true

[*]
indent_style = tab
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true
```


## Tips

### EditorConfig snippet

If you can't remember all settings managed by the EditorConfig file, you'll love the `editorconfig` snippet.

Just type `editorconfig` + <kbd>tab</kbd>, and your editor will focus on the first setting's value (indent_style = *lf*). You can change the value, if you want, and jump to the next setting's value by hitting <kbd>tab</kbd> and so on. Settings are somewhat autocompleted, and if you don't remember all possible values, simply remove the setting value to see them all as a comment.

You can be in a context where `editorconfig` + <kbd>tab</kbd> trigger another snippet. In that case, simply use `Goto anywhere` (<kbd>Ctrl</kbd> + <kbd>P</kbd> on Linux/Windows or <kbd>⌘</kbd> + <kbd>P</kbd> on macOS), type `editorconfig`, select `Snippet: editorconfig` and hit <kbd>Enter</kbd>.

### View active config

The active config is printed in the Sublime console.

### Trailing whitespace

Even though there is a `trim_trailing_whitespace` property. I would still recommend you set `"draw_white_space": "all"` and/or `"trim_trailing_white_space_on_save": true` in your Sublime settings to prevent you from accidentally committing whitespace garbage whenever a project is missing a .editorconfig file.


[EditorConfig site]: https://editorconfig.org
