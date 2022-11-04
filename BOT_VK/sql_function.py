import sqlalchemy as sq
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Users(Base):
    __tablename__ = "users"
    user_id = sq.Column(sq.Integer, primary_key=True)
    # - Id (из VK)
    vk_id = sq.Column(sq.Integer)
    # - Имя
    name = sq.Column(sq.String)
    # - Возраст
    age = sq.Column(sq.Integer)
    # - Пол
    gender = sq.Column(sq.Integer)
    # - Город
    city = sq.Column(sq.String)
    relationlist = relationship('RelationList', back_populates='user')


class Сhallengers(Base):
    __tablename__ = "challengers"
    challengers_id = sq.Column(sq.Integer, primary_key=True)
    # объявление таблицы challengers
    # - Id (из VK)
    vk_id = sq.Column(sq.Integer)
    # - Имя
    name = sq.Column(sq.String)
    # -  Фамилия
    last_name = sq.Column(sq.String)
    # - Ссылка на профиль
    link_profile = sq.Column(sq.String)
    relationlist = relationship('RelationList', back_populates='challenger')

class RelationList(Base):
    __tablename__ = "relation_lists"
    relationlist_id = sq.Column(sq.Integer, primary_key=True)
    # объявление таблицы relation_lists
    # - id_user (ссылка на users)
    # - Id_challenger (ссылка на challengers)
    # - Дата внесения записи
    date_added = sq.Column(sq.String)
    # - Наличие в избранном (логический тип)
    favorites = sq.Column(sq.Boolean)
    # - Наличие в черном списке
    black_list = sq.Column(sq.Boolean)
    user_id = sq.Column(sq.Integer, sq.ForeignKey('users.user_id'), nullable=False)
    user = relationship('Users', back_populates='relationlist')
    challengers_id = sq.Column(sq.Integer, sq.ForeignKey('challengers.challengers_id'), nullable=False)
    challenger = relationship('Сhallengers', back_populates='relationlist')


def insert_challenger(id_challenger, name_challenger, surname_challenger, link):
    new_challenger = Сhallengers(vk_id=id_challenger, name= name_challenger, last_name=surname_challenger, link_profile=link)
    # не успела
    # new_relationList = RelationList(date_added=datetime.now().date(), )
    session.add(new_challenger)
    session.commit()
    # Загружает информацию о кандидате в таблицу challengers

    # return True/False

def create_tables(engine):
    # создаются все таблицы
    Base.metadata.create_all(engine)
    # return True/False
    try:
        Base.metadata.create_all(engine)
        return True
    except:
        return False


def connect(localhost, user, pwd):
    # Создет новое соединение
    engine = sq.create_engine(f"postgresql://postgres:{pwd}@localhost:{localhost}/{user}")
    create_tables(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # return экземпляр класса Session
    return session


session = connect(localhost="5432", pwd="5240", user="users")


def select_date_from_table(connect, table_name):
    # Получает данные из таблицы table_name
    # return список
    return connect.query(table_name).all()


def insert_user(vk_id, name_user, sex_user, age_user, city_user):
    # Загружает данные в таблицу user
    user = Users(vk_id=vk_id, name=name_user, age=age_user, gender=sex_user, city=city_user)
    session.add(user)
    session.commit()
    return user.user_id


def check_user(id_user):
    pass
    # Проверяет наличие пользователя в таблице users

    # return True/False


def check_and_update_param_user(id_user, name_user, sex_user, age_user, city_user):
    pass
    # Проверяет соответствие информации о пользователе в таблице users, полученным на вход. Обновляет данные в таблице
    # при несоответсвии

    # return [id_user, name_user, sex_user, age_user, city_user]




def check_challenger(id_challenger):
    pass
    # Проверяет наличие кандидата в таблице challenger

    # return True/False


def check_and_update_param_challenger(id_challenger, name_challenger, surname_challenger, link):
    pass
    # Проверяет соответствие информации о пользователе в таблице users, полученным на вход. Обновляет данные в таблице
    # при несоответсвии

    # return [id_challenger, name_challenger, surname_challenger, link]


def insert_relation(id_user, id_challenger, recording_date, favorite_list=False, black_list=False):
    pass
    # Загружает данные в таблицу relation_lists

    # return True/False


def check_relation(id_user, id_challenger):
    pass
    # По id_user, id_challenger проверяет наличие записи в таблице relation_lists

    # return True/False


def get_last_challenger(id_user):
    pass
    # Получает информацию о последнем кандидате добавленным пользователем(id_user) из таблиц relation_list и challengers

    # return [id_challenger, name_challenger, surname_challenger, link, favorite_list, black_list]


def insert_challenger_in_favorite_list(id_user, id_challenger):
    pass
    #  Устанавливает True в таблице relation_lists для строки с комибинацией id_user и id_challenger

    # return True/False


def select_favorite_list(id_user):
    pass
    # Получвет выборку записей из таблицы relation_list где столбец id_user = id_user и наличие  favorite_list = true

    # return список с вложенным списком [[id_challenger, name_challenger, surname_challenger, link],[...]] список
    # отсортирован по дате внесения пользователей в лист избранных
