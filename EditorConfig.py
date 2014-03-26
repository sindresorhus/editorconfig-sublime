import sublime_plugin

try:
	import os, sys
	# stupid python module system
	sys.path.append(os.path.dirname(os.path.realpath(__file__)))
	from .editorconfig import get_properties, EditorConfigError
except:
	# Python 2
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
	MARKER = 'editorconfig'

	def on_activated(self, view):
		if not view.settings().has(self.MARKER):
			self.init(view, False)

	def on_pre_save(self, view):
		self.init(view, True)

	def on_post_save(self, view):
		if not view.settings().has(self.MARKER):
			self.init(view, False)

	def init(self, view, pre_save):
		path = view.file_name()
		if not path:
			return

		try:
			config = get_properties(path)
		except EditorConfigError:
			print('Error occurred while getting EditorConfig properties')
		else:
			if config:
				if pre_save:
					self.apply_pre_save(view, config)
				else:
					self.apply_config(view, config)

	def apply_pre_save(self, view, config):
		settings = view.settings()
		spaces = settings.get('translate_tabs_to_spaces')
		charset = config.get('charset')
		end_of_line = config.get('end_of_line')
		indent_style = config.get('indent_style')
		if charset in CHARSETS:
			view.set_encoding(CHARSETS[charset])
		if end_of_line in LINE_ENDINGS:
			view.set_line_endings(LINE_ENDINGS[end_of_line])
		if indent_style == 'space' and spaces == False:
			view.run_command('expand_tabs', {'set_translate_tabs': True})
		elif indent_style == 'tab' and spaces == True:
			view.run_command('unexpand_tabs', {'set_translate_tabs': True})

	def apply_config(self, view, config):
		settings = view.settings()
		indent_style = config.get('indent_style')
		indent_size = config.get('indent_size')
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
		if trim_trailing_whitespace == 'true':
			settings.set('trim_trailing_white_space_on_save', True)
		elif trim_trailing_whitespace == 'false':
			settings.set('trim_trailing_white_space_on_save', False)
		if insert_final_newline == 'true':
			settings.set('ensure_newline_at_eof_on_save', True)
		elif insert_final_newline == 'false':
			settings.set('ensure_newline_at_eof_on_save', False)

		view.settings().set(self.MARKER, True)
