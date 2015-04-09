from flask import Flask
from flask.ext.orientdb import OrientDB

app = Flask(__name__)
app.debug = True
client = OrientDB(app=app, server_pw="B0FC9CF1CBEAD07351C4C30197C43BE2D611E94AFAFA7EF4B4AAD3262F7907DB")

@app.route("/")
def cheese_eating_animals():
    client.set_current_db('animal')
    client.query("select * from Animal")
    animal_list = []
    cheese_eaters = client.command("select expand( in( Eat )) from Food where name = 'pea'")
    return ','.join([cheese_eaters[0].name, cheese_eaters[0].specie])

if __name__ == "__main__":
        app.run()