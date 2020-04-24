try:
    import Tkinter
    import ttk
except ImportError:  # Python 3
    import tkinter as Tkinter
    import tkinter.ttk as ttk

from tkinter_gui_builder.widgets.widget_utils.widget_events import WidgetEvents


class Treeview(ttk.Treeview, WidgetEvents):
    def __init__(self, master=None, cnf=None, **kw):
        ttk.Treeview.__init__(self, master=master, cnf=cnf, **kw)

    def on_treeview_select(self, event):
        self.bind("<<TreeviewSelect>>", event)