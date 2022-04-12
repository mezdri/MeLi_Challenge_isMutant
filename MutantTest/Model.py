from main import db, ma
import datetime


class MutantTests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.TIMESTAMP, default=datetime.datetime.utcnow())
    dna = db.Column(db.TEXT)
    dna_token = db.Column(db.TEXT)
    is_mutant = db.Column(db.INTEGER)

    def __init__(self, dna, dna_token, is_mutant):
        self.dna = dna
        self.dna_token = dna_token
        self.is_mutant = is_mutant


class MutantTestSchema(ma.Schema):
    class Meta:
        fields = ('dna', 'dna_token', 'is_mutant')


mutantSchema = MutantTestSchema()
mutantsSchema = MutantTestSchema(many=True)

db.create_all()
