from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from minimal.services.system.login import *
from minimal.services.system.register import *
from minimal.schemas.system import *
from utils.db_utils import get_db


systemRouter = APIRouter(prefix="/system")


@systemRouter.post("/login", response_model=TokenOut)
async def login(request: Request,
                form_data: CustomOAuth2PasswordRequestForm = Depends(),
                login_service: ILoginService = Depends(LoginService.instance),
                query_db: Session = Depends(get_db)):
    
    return await login_service.login(request, form_data, query_db)


@systemRouter.post("/logout")
async def logout(request: Request,
                 login_service: ILoginService = Depends(LoginService.instance),
                 token: Optional[str] = Depends(oauth2_scheme)):
    # print('logout')
    return await login_service.logout(request, token)



@systemRouter.post("/register")
async def register(request: Request,
                   register_user: RegisterUserIn,
                   register_service: IRegisterService = Depends(RegisterService.instance),
                   query_db: Session = Depends(get_db)):
    print('-------- resgister controller --------')
    
    return await register_service.register(request, register_user, query_db)