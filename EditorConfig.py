import sublime_plugin
from editorconfig import get_properties, EditorConfigError


LINE_ENDINGS = {
	'lf': 'unix',
	'crlf': 'windows',
	'cr': 'cr'
}

CHARSETS = {
	'latin1': 'Western (ISO 8859-1)',
	'utf-8': 'utf-8',
	'utf-8-bom': 'utf-8 with bom',
	'utf-16be': 'utf-16 be',
	'utf-16le': 'utf-16 le'
}

class EditorConfig(sublime_plugin.EventListener):
	def on_load(self, view):
		self.init(view, False)

	def on_pre_save(self, view):
		self.init(view, True)

	def init(self, view, pre_save):
		path = view.file_name()
		if not path:
			return
		try:
			config = get_properties(path)
		except EditorConfigError:
			print 'Error occurred while getting EditorConfig properties'
		else:
			if config:
				if pre_save:
					self.apply_charset(view, config)
				else:
					self.apply_config(view, config)

	def apply_charset(self, view, config):
		charset = config.get('charset')
		if charset in CHARSETS:
			view.set_encoding(CHARSETS[charset])

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
		elif trim_trailing_whitespace == 'false':
			settings.set('trim_trailing_white_space_on_save', False)
		if insert_final_newline == 'true':
			settings.set('ensure_newline_at_eof_on_save', True)
		elif insert_final_newline == 'false':
			settings.set('ensure_newline_at_eof_on_save', False)
