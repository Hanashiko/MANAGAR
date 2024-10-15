from app.extensions import db

class Reputation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    criminalCases = db.Column(db.String(64), index=True)
    familyCriminalCases = db.Column(db.String(64), index=True)
    arestFacts = db.Column(db.String(64), index=True)
    misbehaviourFacts = db.Column(db.String(64), index=True)

    def __repr__(self):
        return f"<FinanceState {self.id}, {self.criminalCases}, {self.familyCriminalCases}, {self.arestFacts}, {self.misbehaviourFacts}"