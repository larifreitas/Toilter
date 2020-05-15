from app import db


# SqlAlchemy
class User(db.Model):
    __tablename__ = 'users'  # nome da tabela

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(30))
    name = db.Column(db.String(40))
    email = db.Column(db.String, unique=True)

    @property
    def is_authenticated(self):
        return True  # True se o usuário fornece credenciais válidas

    @property
    def is_active(self):
        return True  # Se o usuário estiver ativo

    @property
    def is_anonymous(self):
        return False  # Se o usuário estiver logado não esta anônimo. ÓBVIO

    def get_id(self):  # carrega exclusivamente o usuário com seu id a partir de user_loader
        return str(self.id)

    # Create do objeto usuário
    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    # Representação pelo username
    def __repr__(self):
        return f"User {self.username}"


# Dados do post c/ id do usuário(foreign)
class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=user_id)

    # Conteúdo de usuário
    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    # Representação
    def __repr__(self):
        return f"Post {self.id}"


# Esquema de seguidores
class Follow(db.Model):
    __tablename__ = 'follow'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=user_id)
    follower = db.relationship('User', foreign_keys=user_id)
