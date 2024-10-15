from app.extensions import db

class SalesFigures(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    salesGeography = db.Column(db.Integer, index=True, nullable=False)
    enterperualActivity = db.Column(db.Integer, index=True, nullable=False)
    deliveryConcentration = db.Column(db.Integer, index=True, nullable=False)
    salesConcentration = db.Column(db.Integer, index=True, nullable=False)

    def __repr__(self):
        return f"<SalesFigures {self.id}, {self.salesGeography}, {self.enterperualActivity}, {self.deliveryConcentration}, {self.salesConcentration}"