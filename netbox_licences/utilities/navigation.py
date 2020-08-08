from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices
import inflection

def plugin_item(name):
    return PluginMenuItem(
        permissions = [f"netbox_licences.view_{name.lower()}"],
        link=f"plugins:netbox_licences:{inflection.tableize(name)}_list",
        link_text=f"{inflection.titleize(inflection.pluralize(name))}",
        buttons=(
            PluginMenuButton(
                f"plugins:netbox_licences:{inflection.tableize(name)}_add",
                f"Add {inflection.titleize(name)}",
                'fa fa-plus',
                ButtonColorChoices.GREEN
            ),
        )
    )
