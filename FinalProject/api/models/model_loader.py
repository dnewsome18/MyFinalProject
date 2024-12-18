from . import orders, order_details, recipes, sandwiches, resources, users, permissions, menu_items, order_items, \
   feedback, promotions, analytics, system_docs

#menu_items, order_items, feedback, promotions, analytics, system_docs

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    sandwiches.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    users.Base.metadata.create_all(engine)
    permissions.Base.metadata.create_all(engine)
    menu_items.Base.metadata.create_all(engine)
    order_items.Base.metadata.create_all(engine)
    feedback.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    analytics.Base.metadata.create_all(engine)
    system_docs.Base.metadata.create_all(engine)
