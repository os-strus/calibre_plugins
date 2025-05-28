from __future__ import unicode_literals, division, absolute_import, print_function

__license__   = 'GPL v3'
__copyright__ = '2011, Grant Drake'

# The class that all Interface Action plugin wrappers must inherit from
from calibre.customize import InterfaceActionBase

class ActionImportList(InterfaceActionBase):
    '''
    This class is a simple wrapper that provides information about the actual
    plugin class. The actual interface plugin class is called InterfacePlugin
    and is defined in the ui.py file, as specified in the actual_plugin field
    below.

    The reason for having two classes is that it allows the command line
    calibre utilities to run without needing to load the GUI libraries.
    '''
    name                    = 'Import List'
    description             = 'Import lists of books from clipboard, CSV or web'
    supported_platforms     = ['windows', 'osx', 'linux']
    author                  = 'Grant Drake'
    version                 = (1, 9, 8)
    minimum_calibre_version = (3, 41, 0)

    #: This field defines the GUI plugin class that contains all the code
    #: that actually does something. Its format is module_path:class_name
    #: The specified class must be defined in the specified module.
    actual_plugin           = 'calibre_plugins.import_list.action:ImportListAction'

    def is_customizable(self):
        '''
        This method must return True to enable customization via
        Preferences->Plugins
        '''
        return True

    def config_widget(self):
        '''
        Implement this method and :meth:`save_settings` in your plugin to
        use a custom configuration dialog.

        This method, if implemented, must return a QWidget. The widget can have
        an optional method validate() that takes no arguments and is called
        immediately after the user clicks OK. Changes are applied if and only
        if the method returns True.

        If for some reason you cannot perform the configuration at this time,
        return a tuple of two strings (message, details), these will be
        displayed as a warning dialog to the user and the process will be
        aborted.

        The base class implementation of this method raises NotImplementedError
        so by default no user configuration is possible.
        '''
        if self.actual_plugin_:
            from calibre_plugins.import_list.config import ConfigWidget
            return ConfigWidget(self.actual_plugin_)

    def save_settings(self, config_widget):
        '''
        Save the settings specified by the user with config_widget.

        :param config_widget: The widget returned by :meth:`config_widget`.
        '''
        config_widget.save_settings()

    def cli_main(self, args):
        res = 2
        import sys
        try:
            from qt.core import QApplication, QDialog
        except ImportError:
            from PyQt5.Qt import QApplication, QDialog
        from calibre_plugins.import_list.cmdline import ImportListOptionsDialog, run_import_wizard, arg_parser
        _app = QApplication([])
        args.remove("Import List")
        if args:
            library, override_db, reinitialize_step = arg_parser(args)
            res = run_import_wizard(library, override_db, reinitialize_step)
        else:
            d =  ImportListOptionsDialog()
            if d.exec_() == d.Accepted:
                res = run_import_wizard(d.library_path, d.db_path, d.reinitialize_step)

        # change dialog results to suit shell exit codes        
        if res == QDialog.Rejected:
            res = 1
        elif res == QDialog.Accepted:
            res = 0
        sys.exit(res)

# For testing, run from command line with this:
# calibre-debug -e __init__.py
if __name__ == '__main__':
    try:
        from qt.core import QApplication
    except ImportError:
        from PyQt5.Qt import QApplication
    from calibre.gui2.preferences import test_widget
    app = QApplication([])
    test_widget('Advanced', 'Plugins')
