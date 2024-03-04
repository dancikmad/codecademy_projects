from flask import Flask
from helper import pets

app = Flask(__name__)


@app.route("/")
def index():
    return """
  <h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend: </p>
  <ul>
    <li><a href="/animals/dogs">Dogs</a></li>
    <li><a href="/animals/cats">Cats</a></li>
    <li><a href="/animals/rabbits">Rabbits</a></li>
  """


@app.route("/animals/<pet_type>")
def animals(pet_type):
    if pet_type not in pets:
        return f"<h1>{pet_type} not found</h1>"

    html = f"<h1>List of {pet_type}</h1>"
    html += "<ul>"
    for pet_id, pet in enumerate(pets[pet_type]):
        html += f"<li><a href='/animals/{pet_type}/{pet_id}'>{pet['name']}</a></li>"

    html += "</ul>"

    return html


@app.route("/animals/<pet_type>/<int:pet_id>")
def pet(pet_type, pet_id):
    pet = pets[pet_type][pet_id]
    name = pet["name"]
    src = pet["url"]
    description = pet["description"]
    breed = pet["breed"]
    age = pet["age"]

    return f"""<h1>{name}</h1>
  <img src={src}>
  <p>{description}</p>
  <ul>
    <li>Breed: {breed}</li>
    <li>Age: {age}</li>
  </ul>
  """


if __name__ == "__main__":
    app.run(debug=True)
