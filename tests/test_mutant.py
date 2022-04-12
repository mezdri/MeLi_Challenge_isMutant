import unittest, hashlib, os

from main import app, db

from MutantTest.Model import MutantTests
from MutantTest.Mutant import bp
app.register_blueprint(bp)

class MutantTest(unittest.TestCase):
    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'dbtest.sqlite3')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.app_context().push()
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        db.drop_all()
        self.app = None
        self.client = None

    def test_mutantTest_human(self):
        dna_test = ["CCAGTG", "CCAGGC", "TAAGCA", "CACTGC", "CCTCTT", "TACTGC"]
        response = self.client.post('/mutant', json=dict(dna=dna_test), follow_redirects=True)
        self.assertEqual(response.status_code, 403)

    def test_mutantTest_mutant(self):
        dna_test = ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
        response = self.client.post('/mutant', json=dict(dna=dna_test), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_mutantStats(self):
        self.chargeData()
        response = self.client.post('/stats/', json={})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['count_mutant_dna'], 1)
        self.assertEqual(response.json['count_human_dna'], 1)
        ratio = int(response.json['count_mutant_dna']) / int(response.json['count_human_dna'])
        self.assertEqual(response.json['ratio'], ratio)

    def chargeData(self):
        dna_test = [(["CCAGTG", "CCAGGC", "TAAGCA", "CACTGC", "CCTCTT", "TACTGC"], 0), (["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"],1)]
        for dna in dna_test:
            dna_token = hashlib.new('sha256', ''.join(dna[0]).encode('utf-8')).hexdigest()
            mutantObj = MutantTests(dna=str(dna[0]), dna_token=dna_token, is_mutant=dna[1])
            db.session.add(mutantObj)
        db.session.commit()


if __name__ == '__main__':
    unittest.main()
