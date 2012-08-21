import sublime_plugin
from editorconfig import get_properties, EditorConfigError


LINE_ENDINGS = {
	'lf': 'Unix',
	'crlf': 'Windows',
	'cr': 'CR'
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
		#window = view.window()
		end_of_line = config.get('end_of_line')
		indent_style = config.get('indent_style')
		indent_size = config.get('indent_size')
		# Indent type
		if indent_style == 'space':
			settings.set('translate_tabs_to_spaces', True)
		elif indent_style == 'tab':
			settings.set('translate_tabs_to_spaces', False)
		# Converting of current code is disabled because of Sublime bug: http://j.mp/KSQjOA
		#if indent_style == 'tab':
			#window.run_command('unexpand_tabs', {'set_translate_tabs': True})
		#if indent_style == 'space':
			#window.run_command('expand_tabs', {'set_translate_tabs': True})
		# Indent size
		if indent_size:
			try:
				settings.set('tab_size', int(indent_size))
			except ValueError:
				pass
		# EOL
		if end_of_line in LINE_ENDINGS:
			view.set_line_endings(LINE_ENDINGS[end_of_line])
