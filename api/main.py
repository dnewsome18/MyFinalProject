import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .routers import index as indexRoute
from .routers import users
from .models import model_loader
from .dependencies.config import conf
from .routers import analytics
from .routers import recipes
from .routers import promotions
from .routers import system_docs
#from .routers import Feedback
#from .routers import permissions
#from .routers import order_items
#from .routers import sandwiches


app = FastAPI()
app.router.redirect_slashes = False

app.include_router(analytics.router)
app.include_router(users.router)
app.include_router(recipes.router)
app.include_router(promotions.router)
app.include_router(system_docs.router)
#app.include_router(Feedback.router)
#app.include_router(permissions.router)
#app.include_router(order_items.router)
#app.include_router(sandwiches.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_loader.index()
indexRoute.load_routes(app)


if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)