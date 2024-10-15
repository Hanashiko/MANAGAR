from app.extensions import db

class FinanceState(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    KDN = db.Column(db.Integer, index=True, nullable=False)
    KKD = db.Column(db.Integer, index=True, nullable=False)
    stability = db.Column(db.Integer, index=True, nullable=False)

    def __repr__(self):
        return f"<FinanceState {self.id}, {self.KDN}, {self.KKD}, {self.stability}"