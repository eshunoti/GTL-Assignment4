from Flask import Flask, jsonify,requests
from bs4 import BeautifulSoup
import requests


def findinfo(cname):
    totalresult = []
    country = cname
    url = "https://www.worldmeters.info/coronavirus/country/{countryname}/".format(countryname = country)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        result = soup.find_all('div',class_="maincounter-number")
        for i in result:
            totalresult.append(i.find("span").text)
    else:
        totalresult.append("No Result")
    return totalresult 



app = Flask(__name__)



@app.route('/', methods = ["GET"])
def case():
    country = request.args.get('country')

    try:
        return jsonify({"total Cases": findinfo(country)[0],"Total Death": findinfo(country)[1], "Total Recovered": findinfo(country)[2]})
    except:
            return jsonify({"Not Available":" "})


if __name__=='__main':
    app.run(debug=True)            





