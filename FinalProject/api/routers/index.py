from . import orders, order_details, menu_items


def load_routes(app):
    print("Loading routes...")
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(menu_items.router)
    #app.include_router(Feedback.router)
    #app.include_router(order_items.router)
    #app.include_router(permissions.router)
    #app.include_router(promotions.router)
    print("Menu Items router added!")
