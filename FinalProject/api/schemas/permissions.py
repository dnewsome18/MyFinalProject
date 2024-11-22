from pydantic import BaseModel


class PermissionBase(BaseModel):
    role: str
    action: str


class PermissionCreate(PermissionBase):
    pass


class PermissionUpdate(BaseModel):
    role: Optional[str] = None
    action: Optional[str] = None


class Permission(PermissionBase):
    permission_id: int

    class Config:
        orm_mode = True
