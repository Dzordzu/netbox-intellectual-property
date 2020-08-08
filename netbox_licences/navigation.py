from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices
from .utilities.navigation import plugin_item

menu_items = (
    plugin_item("SoftwareProvider"),
    plugin_item("SoftwareType"),
    PluginMenuItem(
        permissions = ['netbox_licences.view_licence'],
        link='plugins:netbox_licences:licences_list',
        link_text='Licences',
    ),
)
