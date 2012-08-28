# EditorConfig - Sublime Text 2 plugin

> [EditorConfig](http://editorconfig.org) helps developers define and maintain consistent coding styles between different editors and IDEs. The EditorConfig project consists of a file format for defining coding styles and a collection of text editor plugins that enable editors to read the file format and adhere to defined styles. EditorConfig files are easily readibly and they work nicely with version control systems.


## Install

Install with [Package Control](http://wbond.net/sublime_packages/package_control)


## Getting started

See the [EditorConfig site][] for documentation.


## Supported properties

- root
- indent_style
- indent_size
- end\_of\_line
- charset\*
- trim_trailing_whitespace\*
- insert_final_newline\*

*\*New property*

Explanation of the properties can be found on the [EditorConfig site][].


## Example file

*My recommended default settings*

```ini
# editorconfig.org
root = true

[*]
indent_style = tab
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true
```


## Trailing whitespace

Even though there is a `trim_trailing_whitespace` property. I would still recommend you set `"draw_white_space": "all"` in your Sublime preferences to prevent you from accidentally committing whitespace garbage whenever a project is missing a .editorconfig file.


## License

[MIT License](http://en.wikipedia.org/wiki/MIT_License)
(c) [Sindre Sorhus](http://sindresorhus.com)



[EditorConfig site]: http://editorconfig.org
