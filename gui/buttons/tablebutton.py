from kivy.app import App
from kivy.uix.listview import ListItemButton
from lib import rpclib


class TableListItemButton(ListItemButton):

    def select(self):
        # setting active channel id after button release
        self.background_color = [1., 0., 0., 1]
        application = App.get_running_app()
        application.active_table_id = str(self.text)
        application.root.ids.userpage.ids.tableinformation.text = str(rpclib.dice_info(application.rpc_connection,
                                                                        application.active_table_id))

    def deselect(self):
        application = App.get_running_app()
        # on deselect set active channel id as blank and clear info text
        application.active_table_id = ""
        application.root.ids.userpage.ids.tableinformation.text = ""
        self.background_color = [0., 1., 0., 1]
