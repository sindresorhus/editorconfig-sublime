import sublime_plugin
from editorconfig import get_properties, EditorConfigError


LINE_ENDINGS = {
	'lf': 'Unix',
	'crlf': 'Windows',
	'cr': 'CR'
}


class EditorConfig(sublime_plugin.EventListener):
	def on_load(self, view):
		try:
			config = get_properties(view.file_name())
		except EditorConfigError:
			print 'Error occurred while getting EditorConfig properties'
		else:
			if config:
				settings = view.settings()
				# EOL
				view.set_line_endings(LINE_ENDINGS[config['end_of_line']])
				# Indent type
				settings.set('translate_tabs_to_spaces', config['indent_style'] == 'space')
				# Indent size
				settings.set('tab_size', int(config['indent_size']))
			else:
				print 'There seems to be an error with your .editorconfig file'