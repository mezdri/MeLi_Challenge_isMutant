from flask import (Blueprint, request, jsonify, )
from .isMutant import IsMutant
from .Model import get_db
import hashlib

bp = Blueprint('MutantTest', __name__, url_prefix='/')


@bp.route('mutant/', methods=['POST'])
def mutantTest():
    db = get_db()
    dna = request.json['dna']
    valueToHash = str(dna[0]) + str(dna[1])
    hashToken = hashlib.new('sha256', valueToHash.encode('utf-8')).hexdigest()
    queryResult = db.execute(
        "select * from mutantTests where dna_token = '%s'" % hashToken
    ).fetchall()
    if len(queryResult) > 0:
        result = True if queryResult[0]['is_mutant'] == 1 else False
    else:
        result = IsMutant().isMutant(dna)
        print("Query ", "insert into mutantTests(dna, dna_token, is_mutant) values ('%s', '%s', %s)" % (
            str(dna), hashToken, 1 if result else 0))
        queryResult = db.execute(
            "insert into mutantTests(dna, dna_token, is_mutant) values ('%s', '%s', %s)" % (
                str(dna).replace("'", '"'), hashToken, 1 if result else 0)
        )
        db.commit()
        print(queryResult)
    if result:
        return jsonify({'result': result})
    else:
        return jsonify({'result': result}), 403


@bp.route('stats/', methods=['POST'])
def stats():
    db = get_db()
    queryResults = db.execute(
        "select count(case when is_mutant = 1 then 1 end) as count_mutant, "
        "count(case when is_mutant = 0 then 1 end) as count_human from mutantTests"
    ).fetchone()
    print(queryResults['count_mutant'])
    ratio = int(queryResults['count_mutant']) / int(queryResults['count_mutant'])
    return jsonify({'count_mutant_dna': queryResults['count_mutant'], 'count_human_dna': queryResults['count_mutant'], 'ratio': ratio})
