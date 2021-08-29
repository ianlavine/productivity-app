from flask_login import UserMixin

from site import bcrypt, db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=False)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    events = db.relationship('Event', backref='owned_user', lazy=True)
    # need attribute for tasks/events/calendar data?

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)  #returns bool t/f

class Event(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(length=30), nullable=False, unique=False)
    description = db.Column(db.String(length=100), nullable=True, unique=False)
    date = db.Column(db.String(length=10), nullable=False, unique=False)
    start = db.Column(db.Integer(), nullable=False, unique=False)
    end = db.Column(db.Interger(), nullable=False, unique=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

