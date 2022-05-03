from main import api_calls
from flask import Flask, request
import main
import json
from index_comparison import indexComparison
from swot_analysis import swotAnalysis
from moving_avg import movingAverage
from moving_avg import chartMovingAverage
from year_on_year_profit_growth import yoyprofitgrowth
from pivot_level import pivot_level
from pe_ratio import peAnalysis
from Analyzer import analyse

app = Flask(__name__)


@app.route('/metaData', methods=['GET'])
def meta():
    args = request.args
    name = args.get("name", default="", type=str)
    x = main.aboutTheCompany(name)
    print(x)
    metaData = {"Name": x["name"], "Description": x["description"]}

    return json.dumps(metaData)


@app.route('/search', methods=['GET'])
def search():
    args = request.args
    name = args.get("name", default="", type=str)
    strength, weak, oppurtunity, threat = swotAnalysis(name)
    r1, r2, r3, s1, s2, s3 = pivot_level(name)

    risk_ana, sent_ana, stockTelAnalysis, fundamental, technical = analyse(name)
    thisdict = {"ticker": name, "index Comparison": indexComparison(name), "Strength": strength, "Weakness": weak,
                "Opportunity": oppurtunity, "Threat": threat, "Moving Average": movingAverage(name, 7),
                "Chart Moving Average": chartMovingAverage(name, 4), "Y-O-Y growth": yoyprofitgrowth(name),
                "S1": s1, "S2": s2, "S3": s3, "R1": r1, "R2": r2, "R3": r3, "pe_ratio": peAnalysis(name),
                "RisK": risk_ana, "Sentimental": sent_ana, "Recommendation": stockTelAnalysis,
                "fundamental": fundamental, "Technical": technical}
    return json.dumps(thisdict)


@app.route('/forex')
def currency():
    return json.dumps(main.forex())


app.run()
