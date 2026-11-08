import importlib
from pathlib import Path
import sys
import types
import unittest
from unittest.mock import Mock, patch


class EditorConfigTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		package = types.ModuleType('editorconfig_sublime')
		package.__path__ = [str(Path(__file__).resolve().parent)]
		sublime_plugin = types.ModuleType('sublime_plugin')
		sublime_plugin.EventListener = object
		sublime_plugin.TextCommand = object
		with patch.dict(sys.modules, {
			'editorconfig_sublime': package,
			'sublime': types.ModuleType('sublime'),
			'sublime_plugin': sublime_plugin,
		}):
			cls.plugin = importlib.import_module('editorconfig_sublime.plugin')

	def setUp(self):
		self.values = {'detect_indentation': True, 'tab_size': 4, 'translate_tabs_to_spaces': False}
		settings = Mock()
		settings.get.side_effect = self.values.get
		settings.set.side_effect = self.values.__setitem__
		self.view = Mock()
		self.view.settings.return_value = settings
		self.listener = self.plugin.EditorConfig()

	def test_indent_size_disables_indentation_detection(self):
		self.listener.apply_config(self.view, {'indent_size': '3'})

		self.assertEqual(self.values['tab_size'], 3)
		self.assertFalse(self.values['detect_indentation'])

	def test_indent_style_disables_indentation_detection(self):
		for style, spaces in [('space', True), ('tab', False)]:
			with self.subTest(style=style):
				self.values.update(detect_indentation=True, translate_tabs_to_spaces=not spaces)

				self.listener.apply_config(self.view, {'indent_style': style})

				self.assertEqual(self.values['translate_tabs_to_spaces'], spaces)
				self.assertFalse(self.values['detect_indentation'])

	def test_no_applied_indentation_preserves_detection(self):
		for config in [{}, {'trim_trailing_whitespace': 'true'}, {'indent_style': 'unset'}, {'indent_size': 'unset'}, {'indent_size': 'tab'}, {'indent_size': 'invalid'}]:
			with self.subTest(config=config):
				self.listener.apply_config(self.view, config)

				self.assertTrue(self.values['detect_indentation'])
				self.assertEqual(self.values['tab_size'], 4)
				self.assertFalse(self.values['translate_tabs_to_spaces'])

	def test_disabled_detection_stays_disabled(self):
		self.values['detect_indentation'] = False

		self.listener.apply_config(self.view, {'indent_size': '3'})

		self.assertFalse(self.values['detect_indentation'])
		self.assertEqual(self.values['tab_size'], 3)


if __name__ == '__main__':
	unittest.main()
