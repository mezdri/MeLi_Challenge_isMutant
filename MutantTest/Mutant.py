from flask import (Blueprint, request, jsonify)
from isMutant import IsMutant
import hashlib
from .Model import MutantTests
from main import db

bp = Blueprint('MutantTest', __name__, url_prefix='/')


@bp.route('mutant/', methods=['POST'])
def mutantTest():
    dna = request.json['dna']
    valueToHash = ''.join(dna)
    hashToken = hashlib.new('sha256', valueToHash.encode('utf-8')).hexdigest()
    queryResult = MutantTests.query.filter_by(dna_token=hashToken).first()
    #queryResult = db.session.query(MutantTests).filter_by(dna_token=hashToken).scalar()
    print(queryResult)
    if queryResult is None:
        result = IsMutant().isMutant(dna)
        mutantObject = MutantTests(dna=str(dna).replace("'", '"'), dna_token=hashToken, is_mutant=1 if result else 0)
        db.session.add(mutantObject)
        db.session.commit()
    else:
        result = True if queryResult.is_mutant == 1 else False
    if result:
        return jsonify({'result': result})
    else:
        return jsonify({'result': result}), 403


@bp.route('stats/', methods=['POST'])
def stats():
    queryResults = db.session.execute(
        "select count(case when is_mutant = 1 then 1 end) as count_mutant, "
        "count(case when is_mutant = 0 then 1 end) as count_human from mutant_tests"
    ).fetchone()
    print(queryResults)
    ratio = (int(queryResults.count_mutant) / int(queryResults.count_human)) if int(
        queryResults.count_human) > 0 else int(queryResults.count_mutant)
    return jsonify({'count_mutant_dna': queryResults.count_mutant, 'count_human_dna': queryResults.count_human,
                    'ratio': ratio})
