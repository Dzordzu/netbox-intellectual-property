from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

def plugin_item(camel_case_name):
    return PluginMenuItem(
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
    )
