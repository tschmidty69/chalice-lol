import random
from botocore.vendored import requests
import cassiopeia as cass
from chalice import Chalice

app = Chalice(app_name='chalice-new')

# https://github.com/aws/chalice/
@app.route('/')
def index():
    return get_summ('Fodder1969', 'NA')

# https://github.com/meraki-analytics/cassiopeia
def get_summ(summ="Fodder1969", region="NA"):
    cass.set_riot_api_key("RGAPI-18f8d037-17c8-4add-b6b5-0eac3011adb0")  # This overrides the value set in your configuration/settings.
    cass.set_default_region("NA")

    output = {}
    summoner = cass.get_summoner(name=summ)
    output['summoner']="{name} is a level {level} summoner on the {region} server.".format(name=summoner.name,
                                                                              level=summoner.level,
                                                                              region=summoner.region)

    champions = cass.get_champions()
    mastery_champions = summoner.champion_masteries.filter(lambda cm: cm.level >= 6)
    output['champ']="He enjoys playing champions such as {name}.".format(name=[cm.champion.name for cm in mastery_champions])

    return output
