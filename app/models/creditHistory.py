from app.extensions import db

class CreditHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bankDept = db.Column(db.Integer, index=True, nullable=False)
    vexelDept = db.Column(db.Integer, index=True, nullable=False)
    deptRightNow = db.Column(db.String(64), index=True)

    def __repr__(self):
        return f"<FinanceState {self.id}, {self.KDN}, {self.KKD}, {self.stability}"