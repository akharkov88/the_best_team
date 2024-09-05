from pydantic import BaseModel



class UserTask(BaseModel):
    NameTechTask: str  # Наименование обекта
    TechTaskClient: str  # Наименование заказчика
    NameTechAdres: str  # Местонахождение объекта
    TechTaskProject: str # Проект/чертеж
    # TechTaskPPR: str  # Проект/чертеж
    TechTaskOverhead: str  # Накладные расходы
    TechTaskDateKP: str # Срок подготовки КП
    TechTaskDateEndWork: str # Срок выполнение работ
    TechTaskPrice: str  # Условия оплаты
    TechTaskLeaderKP: str  # Отвественный
    TechTaskDateSrokStart: str
    TechTaskDateSrokEnd: str
class BaseTask(UserTask):
    id: int
    class Config:
        orm_mode = True


# class TaskCreate(BaseTask):
#     pass
