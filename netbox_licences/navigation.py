from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        permissions = ['netbox_licences.view_softwareprovider'],
        link='plugins:netbox_licences:software_providers_list',
        link_text='Software Providers',
        buttons=(
            PluginMenuButton(
                'plugins:netbox_licences:software_providers_add',
                'Add Software Provider',
                'fa fa-plus',
                ButtonColorChoices.GREEN
            ),
        )
    ),
    PluginMenuItem(
        permissions = ['netbox_licences.view_softwaretype'],
        link='plugins:netbox_licences:software_types_list',
        link_text='Software Types',
        buttons=(
            PluginMenuButton(
                'plugins:netbox_licences:software_types_add',
                'Add Software Type',
                'fa fa-plus',
                ButtonColorChoices.GREEN
            ),
        )
    ),
    PluginMenuItem(
        permissions = ['netbox_licences.view_licence'],
        link='plugins:netbox_licences:licences_list',
        link_text='Licences',
    ),
)
