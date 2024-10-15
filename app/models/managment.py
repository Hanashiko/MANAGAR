from app.extensions import db

class Managment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    knowledge = db.Column(db.String(64), index=True)
    experience = db.Column(db.String(64), index=True)

    def __repr__(self):
        return f"<FinanceState {self.id}, {self.knowledge}, {self.experience}"