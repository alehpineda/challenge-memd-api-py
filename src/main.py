import constants

from fastapi import FastAPI

from controllers import member_controller, status_controller

# fastapi starting and config
app = FastAPI()

# add endpoints to app path
app.include_router(status_controller.router)
app.include_router(
    member_controller.router,
    prefix=constants.MEMBER_PREFIX,
)
