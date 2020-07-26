from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        permissions = ['netbox_intellectual_property.view_softwareprovider'],
        link='plugins:netbox_intellectual_property:software_providers_list',
        link_text='Software Providers',
        buttons=(
            PluginMenuButton('home', 'Button A', 'fa fa-info', ButtonColorChoices.BLUE),
            PluginMenuButton('home', 'Button B', 'fa fa-warning', ButtonColorChoices.GREEN),
        )
    ),
)
