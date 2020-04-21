try:
    import Tkinter
    import ttk
except ImportError:  # Python 3
    import tkinter as Tkinter
    import tkinter.ttk as ttk

from tkinter_gui_builder.panel_templates.widget_panel.widget_panel import AbstractWidgetPanel
from tkinter_gui_builder.widgets.basic_widgets import Treeview


class TreeviewPanel(AbstractWidgetPanel):

    tree = Treeview

    def __init__(self, parent):
        '''
        Constructor
        '''
        AbstractWidgetPanel.__init__(self, parent)
        self.init_w_basic_widget_list(["tree"], 1, 1)
        self.set_columns()

    def set_columns(self):
        # Set the treeview
        self.tree.config(columns=("first", "second"))  # this creates to seperate headings for treeview
        self.tree.heading('#0', text='Item')
        self.tree.heading('#1', text='Dose')
        self.tree.heading('#2', text='Modification Date')
        self.tree.column('#0', stretch=Tkinter.YES)
        self.tree.column('#1', stretch=Tkinter.YES)
        self.tree.column('#2', stretch=Tkinter.YES)
        # Initialize the counter
        self.i = 0
        self.tree.pack()
        self.pack()

    def insert_data(self):
        """
        Insertion method.
        """
        self.tree.insert('', 'end', text="Item_"+str(self.i),
                             values=(self.dose_entry.get() + " mg",
                                     self.modified_entry.get()))
        # Increment counter
        self.i = self.i + 1
