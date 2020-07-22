from extras.plugins import PluginConfig

class ServicesTypesConfig(PluginConfig):
    name = "netbox-services-types"
    verbose_name = "Services Types"
    description = "Extension providing services type section"

    version = "0.1"

    # Plugin author
    author = 'Tomasz Durda'
    author_email = 'tomekdur@wp.pl'

    # Configuration parameters that MUST be defined by the user (if any)
    required_settings = []

    # Default configuration parameter values, if not set by the user
    default_settings = {
    }

    # Base URL path. If not set, the plugin name will be used.
    base_url = 'ipam/services-types'

    # Caching config
    caching_config = {}


config = ServicesTypesConfig

