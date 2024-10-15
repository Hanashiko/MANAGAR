from app.extensions import db

class finance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, index=True, nullable=False)
    actualTerm = db.Column(db.Integer, index=True, nullable=False)
    marriageTerm = db.Column(db.Integer, index=True, nullable=False)
    marriageNumber = db.Column(db.Integer, index=True, nullable=False)
    childrenNumber = db.Column(db.Integer, index=True, nullable=False)
    dependentsNumber = db.Column(db.Integer, index=True, nullable=False)
    estateAvailability = db.Column(db.String(64), index=True)

    def __repr__(self):
        return f"<ChooseClass {self.age}"