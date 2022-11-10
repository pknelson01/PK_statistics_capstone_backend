from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os

app = Flask(__name__)

CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Basketball_stat(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date_of_game = db.Column(db.String(100), unique=False)
  points = db.Column(db.Integer, unique=False)
  assists = db.Column(db.Integer, unique=False)
  rebounds = db.Column(db.Integer, unique=False)
  steals = db.Column(db.Integer, unique=False)
  blocks = db.Column(db.Integer, unique=False)
  turn_overs = db.Column(db.Integer, unique=False)
  fouls = db.Column(db.Integer, unique=False)
  minutes = db.Column(db.Integer, unique=False)


  def __init__(self, date_of_game, points, assists, rebounds, steals, blocks, turn_overs, fouls, minutes):
    self.date_of_game = date_of_game
    self.points = points
    self.assists = assists
    self.rebounds = rebounds
    self.steals = steals
    self.blocks = blocks
    self.turn_overs = turn_overs
    self.fouls = fouls
    self.minutes = minutes

class Basketball_statSchema(ma.Schema):
  class Meta:
    fields = ('id', 'date_of_game', 'points', 'assists', 'rebounds', 'steals', 'blocks', 'turn_overs', 'fouls', 'minutes')

basketball_stat_schema = Basketball_statSchema()
basketball_stats_schema = Basketball_statSchema(many=True)


class Football_stat(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date_of_game = db.Column(db.String(100), unique=False)
  touchdowns = db.Column(db.Integer, unique=False)
  receiving_yards = db.Column(db.Integer, unique=False)
  rushing_yards = db.Column(db.Integer, unique=False)
  tackles = db.Column(db.Integer, unique=False)
  completions = db.Column(db.Integer, unique=False)
  interceptions = db.Column(db.Integer, unique=False)
  sacks = db.Column(db.Integer, unique=False)
  passing_yards = db.Column(db.Integer, unique=False)

  def __init__(self, date_of_game, touchdowns, receiving_yards, rushing_yards, tackles, completions, interceptions, sacks, passing_yards):
    self.date_of_game = date_of_game
    self. touchdowns = touchdowns
    self.receiving_yards = receiving_yards
    self.rushing_yards = rushing_yards
    self.tackles = tackles
    self.completions = completions
    self.interceptions = interceptions
    self.sacks = sacks
    self.passing_yards = passing_yards

class Football_statSchema(ma.Schema):
  class Meta:
    fields = ('id', 'date_of_game', 'touchdowns', 'receiving_yards', 'rushing_yards', 'tackles', 'completions', 'interceptions', 'sacks', 'passing_yards')

football_stat_schema = Football_statSchema()
football_stats_schema = Football_statSchema(many=True)


class Soccer_stat(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date_of_game = db.Column(db.String(100), unique=False)
  goals = db.Column(db. Integer, unique=False)
  assists = db.Column(db. Integer, unique=False)
  pks = db.Column(db. Integer, unique=False)
  shots_on_goal = db.Column(db. Integer, unique=False)
  yellow_cards = db.Column(db. Integer, unique=False)
  red_cards = db.Column(db. Integer, unique=False)
  goals_allowed = db.Column(db. Integer, unique=False)
  minutes = db.Column(db.Integer, unique=False)

  def __init__(self, date_of_game, goals, assists, pks, shots_on_goal, yellow_cards, red_cards, goals_allowed, minutes):
    self.date_of_game = date_of_game
    self.goals = goals
    self.assists = assists
    self.pks = pks
    self.shots_on_goal = shots_on_goal
    self.yellow_cards = yellow_cards
    self.red_cards = red_cards
    self.goals_allowed = goals_allowed
    self.minutes = minutes

class Soccer_statSchema(ma.Schema):
  class Meta:
    fields = ('id', 'date_of_game', 'goals', 'assists', 'pks', 'shots_on_goal', 'yellow_cards', 'red_cards', 'goals_allowed', 'minutes')

soccer_stat_schema = Soccer_statSchema()
soccer_stats_schema = Soccer_statSchema(many=True)


# Endpoints to POST a new entry

@app.route('/api/basketball_stat', methods=["POST"])
def add_basketball_stat():
  date_of_game = request.json['date_of_game']
  points = request.json['points']
  assists = request.json['assists']
  rebounds = request.json['rebounds']
  steals = request.json['steals']
  blocks = request.json['blocks']
  turn_overs = request.json['turn_overs']
  fouls = request.json['fouls']
  minutes = request.json['minutes']

  new_basketball_stat = Basketball_stat(date_of_game, points, assists, rebounds, steals, blocks, turn_overs, fouls, minutes)

  db.session.add(new_basketball_stat)
  db.session.commit()

  # return jsonify('Created'), 201

  basketball_stat = Basketball_stat.query.get(new_basketball_stat.id)

  return basketball_stat_schema.jsonify(basketball_stat)


@app.route('/api/football_stat', methods=["POST"])
def add_football_stat():
  date_of_game = request.json['date_of_game']
  touchdowns = request.json['touchdowns']
  receiving_yards = request.json['receiving_yards']
  rushing_yards = request.json['rushing_yards']
  tackles = request.json['tackles']
  completions = request.json['completions']
  interceptions = request.json['interceptions']
  sacks = request.json['sacks']
  passing_yards = request.json['passing_yards']

  new_football_stat = Football_stat(date_of_game, touchdowns, receiving_yards, rushing_yards, tackles, completions, interceptions, sacks, passing_yards)

  db.session.add(new_football_stat)
  db.session.commit()

  # return jsonify('Created'), 201

  football_stat = Football_stat.query.get(new_football_stat.id)

  return football_stat_schema.jsonify(football_stat)


@app.route('/api/soccer_stat', methods=["POST"])
def add_soccer_stat():
  date_of_game = request.json['date_of_game']
  goals = request.json['goals']
  assists = request.json['assists']
  pks = request.json['pks']
  shots_on_goal = request.json['shots_on_goal']
  yellow_cards = request.json['yellow_cards']
  red_cards = request.json['red_cards']
  goals_allowed = request.json['goals_allowed']
  minutes = request.json['minutes']

  new_soccer_stat = Soccer_stat(date_of_game, goals, assists, pks, shots_on_goal, yellow_cards, red_cards, goals_allowed, minutes)

  db.session.add(new_soccer_stat)
  db.session.commit()

  # return jsonify('Created'), 201

  soccer_stat = Soccer_stat.query.get(new_soccer_stat.id)

  return soccer_stat_schema.jsonify(soccer_stat)


# Endpoint to GET all stats
@app.route("/api/basketball_stats", methods=["GET"])
def get_basketball_stats():
  all_basketball_stats = Basketball_stat.query.all()
  result = basketball_stats_schema.dump(all_basketball_stats)
  
  return jsonify(result)


@app.route("/api/football_stats", methods=["GET"])
def get_football_stats():
  all_football_stats = Football_stat.query.all()
  result = football_stats_schema.dump(all_football_stats)
  
  return jsonify(result)


@app.route("/api/soccer_stats", methods=["GET"])
def get_soccer_stats():
  all_soccer_stats = Soccer_stat.query.all()
  result = soccer_stats_schema.dump(all_soccer_stats)
  
  return jsonify(result)

#Endpoint for GETing a single item
@app.route("/api/basketball_stat/<id>", methods=["GET"])
def get_basketball_stat(id):
  basketball_stat = Basketball_stat.query.get(id)
  
  return basketball_stat_schema.jsonify(basketball_stat)


@app.route("/api/football_stat/<id>", methods=["GET"])
def get_football_stat(id):
  football_stat = Football_stat.query.get(id)
  
  return football_stat_schema.jsonify(football_stat)


@app.route("/api/soccer_stat/<id>", methods=["GET"])
def get_soccer_stat(id):
  soccer_stat = Soccer_stat.query.get(id)
  
  return soccer_stat_schema.jsonify(soccer_stat)
  
# Endpoint for UPDATING an item
@app.route("/api/basketball_stat/<id>", methods=["PUT"])
def basketball_stat_update(id):
  basketball_stat = Basketball_stat.query.get(id)
  date_of_game = request.json['date_of_game']
  points = request.json['points']
  assists = request.json['assists']
  rebounds = request.json['rebounds']
  steals = request.json['steals']
  blocks = request.json['blocks']
  turn_overs = request.json['turn_overs']
  fouls = request.json['fouls']
  minutes = request.json['minutes']

  basketball_stat.date_of_game = date_of_game
  basketball_stat.points = points
  basketball_stat.assists = assists
  basketball_stat.rebounds = rebounds
  basketball_stat.steals = steals
  basketball_stat.blocks = blocks
  basketball_stat.turn_overs = turn_overs
  basketball_stat.fouls = fouls
  basketball_stat.minutes = minutes

  db.session.commit()
  return basketball_stat_schema.jsonify(basketball_stat)


@app.route("/api/football_stat/<id>", methods=["PUT"])
def football_stat_update(id):
  football_stat = Football_stat.query.get(id)
  date_of_game = request.json['date_of_game']
  touchdowns = request.json['touchdowns']
  receiving_yards = request.json['receiving_yards']
  rushing_yards = request.json['rushing_yards']
  tackles = request.json['tackles']
  completions = request.json['completions']
  interceptions = request.json['interceptions']
  sacks = request.json['sacks']
  passing_yards = request.json['passing_yards']

  football_stat.date_of_game = date_of_game
  football_stat.touchdowns = touchdowns
  football_stat.receiving_yards = receiving_yards
  football_stat.rushing_yards = rushing_yards
  football_stat.tackles = tackles
  football_stat.completions = completions
  football_stat.interceptions = interceptions
  football_stat.sacks = sacks
  football_stat.passing_yards = passing_yards

  db.session.commit()
  return football_stat_schema.jsonify(football_stat)


@app.route("/api/soccer_stat/<id>", methods=["PUT"])
def soccer_stat_update(id):
  soccer_stat = Soccer_stat.query.get(id)
  date_of_game = request.json['date_of_game']
  goals = request.json['goals']
  assists = request.json['assists']
  pks = request.json['pks']
  shots_on_goal = request.json['shots_on_goal']
  yellow_cards = request.json['yellow_cards']
  red_cards = request.json['red_cards']
  goals_allowed = request.json['goals_allowed']
  minutes = request.json['minutes']

  soccer_stat.date_of_game = date_of_game
  soccer_stat.goals = goals
  soccer_stat.assists = assists
  soccer_stat.pks = pks
  soccer_stat.shots_on_goal = shots_on_goal
  soccer_stat.yellow_cards = yellow_cards
  soccer_stat.red_cards = red_cards
  soccer_stat.goals_allowed = goals_allowed
  soccer_stat.minutes = minutes

  db.session.commit()
  return soccer_stat_schema.jsonify(soccer_stat)

# Endpoint for DELETING a record
@app.route("/api/basketball_stat/<id>", methods=["DELETE"])
def basketball_stat_delete(id):
  basketball_stat = Basketball_stat.query.get(id)
  db.session.delete(basketball_stat)
  db.session.commit()

  return basketball_stat_schema.jsonify(basketball_stat)


@app.route("/api/football_stat/<id>", methods=["DELETE"])
def football_stat_delete(id):
  football_stat = Football_stat.query.get(id)
  db.session.delete(football_stat)
  db.session.commit()

  return football_stat_schema.jsonify(football_stat)


@app.route("/api/soccer_stat/<id>", methods=["DELETE"])
def soccer_stat_delete(id):
  soccer_stat = Soccer_stat.query.get(id)
  db.session.delete(soccer_stat)
  db.session.commit()

  return soccer_stat_schema.jsonify(soccer_stat)


if __name__ == '__main__':
  app.run(debug = True)