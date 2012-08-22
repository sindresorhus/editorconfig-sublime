import sublime_plugin
from editorconfig import get_properties, EditorConfigError


LINE_ENDINGS = {
	'lf': 'unix',
	'crlf': 'windows',
	'cr': 'cr'
}


class EditorConfig(sublime_plugin.EventListener):
	def on_load(self, view):
		path = view.file_name()
		if not path:
			return
		try:
			config = get_properties(path)
		except EditorConfigError:
			print 'Error occurred while getting EditorConfig properties'
		else:
			if config:
				self.apply_config(view, config)

	def apply_config(self, view, config):
		settings = view.settings()
		indent_style = config.get('indent_style')
		indent_size = config.get('indent_size')
		end_of_line = config.get('end_of_line')
		trim_trailing_whitespace = config.get('trim_trailing_whitespace')
		insert_final_newline = config.get('insert_final_newline')
		if indent_style == 'space':
			settings.set('translate_tabs_to_spaces', True)
		elif indent_style == 'tab':
			settings.set('translate_tabs_to_spaces', False)
		if indent_size:
			try:
				settings.set('tab_size', int(indent_size))
			except ValueError:
				pass
		if end_of_line in LINE_ENDINGS:
			view.set_line_endings(LINE_ENDINGS[end_of_line])
		if trim_trailing_whitespace == 'true':
			settings.set('trim_trailing_white_space_on_save', True)
		if insert_final_newline == 'true':
			settings.set('ensure_newline_at_eof_on_save', True)
