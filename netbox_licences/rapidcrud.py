from netbox_rapid_crud import RapidCRUD
from . import config

config_text = open("config.json","r").read()

rapidcrud = RapidCRUD(
    plugin_name=config.name,
    config=config_text
)

rapidcrud\
    .prepare_models()
#     .prepare_filters()\
#     .prepare_forms()\
#     .prepare_tables()\
#     .prepare_views()\
#     .prepare_api()\
#     .prepare_admin()
#     .finish_preparation()

# Or just use
# rapidcrud.full_prepare()

