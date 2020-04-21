try:
    import Tkinter as tkinter
    import ttk
except ImportError:  # Python 3
    import tkinter
    import tkinter.ttk as ttk

from tkinter_gui_builder.panel_templates.widget_panel.widget_panel import AbstractWidgetPanel
from tkinter_gui_builder.widgets.basic_widgets import Treeview
from tkinter_gui_builder.widgets.basic_widgets import Button


class TreeviewPanel(AbstractWidgetPanel):

    tree = Treeview         # type: Treeview
    button = Button

    def __init__(self, parent):
        '''
        Constructor
        '''
        self.counter = 0
        AbstractWidgetPanel.__init__(self, parent)
        self.init_w_basic_widget_list(["tree", "button"], 2, 1)
        self.set_columns()

    def set_columns(self):
        # Set the treeview
        self.tree.config(columns=("first", "second"))  # this creates to seperate headings for treeview
        self.tree.heading('#0', text='Item')
        self.tree.heading('#1', text='Type')
        self.tree.heading('#2', text='Confidence')
        self.tree.column('#0', stretch=tkinter.YES)
        self.tree.column('#1', stretch=tkinter.YES)
        self.tree.column('#2', stretch=tkinter.YES)

    def insert_data(self):
        """
        Insertion method.
        """
        self.tree.insert('', 'end', text="Item_"+str(self.counter),
                         values=("stuff_" + str(self.counter).zfill(5), "things_" + str(self.counter).zfill(5)))
        # Increment counter
        self.counter = self.counter + 1
