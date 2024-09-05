import traceback
from typing import (
    List,
    Optional,
)
import ast

from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session
# import dateutil.parser
import models
import tables
from services.auth import  get_session
# from services.UserProfile import  UserProfileServices
from fastapi.encoders import jsonable_encoder
# from database import get_current_user
#
# print(get_current_user)
class TaskServices:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session
    #
    # def createTask_S(self,TechTaskDATA: models.UserTask,user: tables.User,) -> tables.TaskForm:
    #     try:
    #         operation = tables.TaskForm(
    #             NameTechTask=TechTaskDATA.NameTechTask,
    #             TechTaskClient=TechTaskDATA.TechTaskClient,
    #             NameTechAdres=TechTaskDATA.NameTechAdres,
    #             TechTaskProject=TechTaskDATA.TechTaskProject,
    #             # TechTaskPPR=TechTaskDATA.TechTaskPPR,
    #             TechTaskOverhead=TechTaskDATA.TechTaskOverhead,
    #             TechTaskDateKP=TechTaskDATA.TechTaskDateKP,
    #             TechTaskDateEndWork=TechTaskDATA.TechTaskDateEndWork,
    #             TechTaskPrice=TechTaskDATA.TechTaskPrice,
    #             TechTaskLeaderKP=TechTaskDATA.TechTaskLeaderKP,
    #             # TechTask_plan=TechTaskDATA.TechTask_plan,
    #             # TechTask_sketch=TechTaskDATA.TechTask_sketch,
    #             user_name=user.username,
    #         )
    #         self.session.add(operation)
    #         self.session.commit()
    #         operation = (
    #             self.session
    #             .query(tables.TaskForm)
    #             .filter(
    #                 tables.TaskForm.NameTechTask == TechTaskDATA.NameTechTask
    #             )
    #             .first()
    #         )
    #         if not operation:
    #             raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
    #         # return jsonable_encoder(operation)
    #         return jsonable_encoder(operation)
    #     except:
    #         print(traceback.format_exc())
    #         raise HTTPException(status.HTTP_409_CONFLICT, detail="Запись с таким именем уже существует запись")
    #         # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})
    #
    #
    #     # return "operation"
    #
    # def update_value(self, TechTaskDATA: models.UserTask) -> tables.TaskForm:
    #     try:
    #         # operation = tables.TaskForm(
    #         #     NameTechTask=TechTaskDATA.NameTechTask,
    #         #     TechTaskClient=TechTaskDATA.TechTaskClient,
    #         #     TechTaskProject=TechTaskDATA.TechTaskProject,
    #         #     TechTaskPPR=TechTaskDATA.TechTaskPPR,
    #         #     TechTaskOverhead=TechTaskDATA.TechTaskOverhead,
    #         #     TechTaskDateKP=TechTaskDATA.TechTaskDateKP,
    #         #     TechTaskDateEndWork=TechTaskDATA.TechTaskDateEndWork,
    #         #     TechTaskPrice=TechTaskDATA.TechTaskPrice,
    #         #     TechTaskLeaderKP=TechTaskDATA.TechTaskLeaderKP,
    #         # )
    #
    #         # existing_row = self.session.query(tables.TaskForm).filter(tables.TaskForm.NameTechTask == TechTaskDATA.NameTechTask).first()
    #         # existing_row.column1 = 'new_value1'
    #         # existing_row.column2 = 'new_value2'
    #         # existing_row.TechTaskClient = TechTaskDATA.TechTaskClient,
    #         # self.session.commit()
    #
    #         self.session.query(tables.TaskForm).filter(
    #             tables.TaskForm.NameTechTask == TechTaskDATA.NameTechTask).update(dict(TechTaskDATA))
    #         self.session.commit()
    #         operation = (
    #             self.session
    #             .query(tables.TaskForm)
    #             .filter(
    #                 tables.TaskForm.NameTechTask == TechTaskDATA.NameTechTask
    #             )
    #             .first()
    #         )
    #         if not operation:
    #             raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
    #         # return jsonable_encoder(operation)
    #         return jsonable_encoder(operation)
    #     except:
    #         print(traceback.format_exc())
    #         raise HTTPException(status.HTTP_409_CONFLICT, detail="Запись с таким именем уже существует запись")
    #         # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})
    #
    # def getAllTask_S(self) :#-> tables.TaskForm
    #     try:
    #         operation = (
    #             self.session
    #             .query(tables.TaskForm)
    #             .all()
    #         )
    #         # if not operation:
    #         #     raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ошибка повторите еще раз")
    #         # return jsonable_encoder(operation)
    #         lisr_tech_tasks=jsonable_encoder(operation)
    #         save_val_fio = {}
    #
    #         for i,lisr_tech_task in enumerate(lisr_tech_tasks):
    #             operation = (
    #                 self.session
    #                 .query(tables.ListUserTask)
    #                 .filter(
    #                     # tables.ListUserTask.connection.ilike('%"TechTask":'+str(lisr_tech_task["id"])+'%')
    #                     tables.ListUserTask.connection == '{"TechTask":'+str(lisr_tech_task["id"])+'}'
    #                 )
    #                 .all()
    #             )
    #             lisr_tech_tasks[i]["ListUserTask"] = jsonable_encoder(operation)
    #             for j, ListUserTask in enumerate(lisr_tech_tasks[i]["ListUserTask"]):
    #
    #                 if not save_val_fio.get(ListUserTask["user_create"],False):
    #                     save_val_fio[ListUserTask["user_create"]]=UserProfileServices.get_UserProfile(self,ListUserTask["user_create"])
    #
    #                 lisr_tech_tasks[i]["ListUserTask"][j]["UserPfofile_create"] = save_val_fio[ListUserTask["user_create"]]
    #                 save_executor = []
    #                 for user_executor_val in ast.literal_eval(lisr_tech_tasks[i]["ListUserTask"][j]["user_executor"]):
    #                     if not save_val_fio.get(user_executor_val, False):
    #                         save_val_fio[user_executor_val] = UserProfileServices.get_UserProfile(self,user_executor_val)
    #                     save_executor.append(save_val_fio[user_executor_val])
    #
    #                 lisr_tech_tasks[i]["ListUserTask"][j]["UserPfofile_executor"] = save_executor
    #
    #
    #         return lisr_tech_tasks
    #     except:
    #         print(traceback.format_exc())
    #         raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)
    #         # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})
    #
    #
    #     # return "operation"
    #
    #
    # def getTechTaskNameTechTask_S(self,NameTechTask: models.UserTask): #-> tables.TaskForm:
    #     try:
    #         print("NameTechTaskNameTechTask",NameTechTask)
    #         operation = (
    #             self.session
    #             .query(tables.TaskForm)
    #             .filter(
    #                 tables.TaskForm.NameTechTask == NameTechTask
    #             )
    #             .first()
    #         )
    #         if not operation:
    #             raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Нет такого NameTechTask")
    #         lisr_tech_tasks = jsonable_encoder(operation)
    #         save_val_fio = {}
    #
    #         # for i, lisr_tech_task in enumerate(lisr_tech_tasks):
    #         operation = (
    #             self.session
    #             .query(tables.ListUserTask)
    #             .filter(
    #             tables.ListUserTask.connection.ilike('%"TechTask":' + str(lisr_tech_tasks["id"]) + '%')
    #
    #         )
    #             .all()
    #         )
    #         lisr_tech_tasks["ListUserTask"] = jsonable_encoder(operation)
    #         for j, ListUserTask in enumerate(lisr_tech_tasks["ListUserTask"]):
    #
    #             if not save_val_fio.get(ListUserTask["user_create"], False):
    #                 save_val_fio[ListUserTask["user_create"]] = UserProfileServices.get_UserProfile(self,
    #                                                                                                 ListUserTask[
    #                                                                                                     "user_create"])
    #
    #             lisr_tech_tasks["ListUserTask"][j]["UserPfofile_create"] = save_val_fio[
    #                 ListUserTask["user_create"]]
    #             save_executor = []
    #             for user_executor_val in ast.literal_eval(lisr_tech_tasks["ListUserTask"][j]["user_executor"]):
    #                 if not save_val_fio.get(user_executor_val, False):
    #                     save_val_fio[user_executor_val] = UserProfileServices.get_UserProfile(self,
    #                                                                                           user_executor_val)
    #                 save_executor.append(save_val_fio[user_executor_val])
    #
    #             lisr_tech_tasks["ListUserTask"][j]["UserPfofile_executor"] = save_executor
    #         lisr_tech_tasks["TechTaskDateSrokStart"]= dateutil.parser.isoparse(lisr_tech_tasks["TechTaskDateSrokStart"]).strftime("%Y-%m-%d")
    #         lisr_tech_tasks["TechTaskDateSrokEnd"]= dateutil.parser.isoparse(lisr_tech_tasks["TechTaskDateSrokEnd"]).strftime("%Y-%m-%d")
    #         return lisr_tech_tasks
    #     except:
    #         print(traceback.format_exc())
    #         raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)
    #         # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})
    #
    #
    #     # return "operation"
    #
    #
    # def getTechTaskIDTechTask_S(self,IDTechTask: models.BaseTask) -> tables.TaskForm:
    #     try:
    #         operation = (
    #             self.session
    #             .query(tables.TaskForm)
    #             .filter(
    #                 tables.TaskForm.id == IDTechTask
    #             )
    #             .first()
    #         )
    #         if not operation:
    #             raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Нет такого NameTechTask")
    #         return jsonable_encoder(operation)
    #     except:
    #         print(traceback.format_exc())
    #         raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)
    #         # raise JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': "Уже существует запись"})
    #
    #
    #     # return "operation"


    #
    # def update(
    #     self,
    #     user_id: int,
    #     operation_id: int,
    #     operation_data: models.OperationUpdate,
    # ) -> tables.Operation:
    #     operation = self._get(user_id, operation_id)
    #     for field, value in operation_data:
    #         setattr(operation, field, value)
    #     self.session.commit()
    #     return operation
    #
    # def delete(
    #     self,
    #     user_id: int,
    #     operation_id: int,
    # ):
    #     operation = self._get(user_id, operation_id)
    #     self.session.delete(operation)
    #     self.session.commit()

