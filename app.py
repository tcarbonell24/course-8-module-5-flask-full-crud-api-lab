from flask import Flask, jsonify, request 

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    # TODO: Task 2 - Design and Develop the Code
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Missing 'title' field"}), 400

    # TODO: Task 3 - Implement the Loop and Process Each Element
    new_id = max([event.id for event in events], default=0) + 1
    new_event = Event(new_id, data["title"])
    events.append(new_event)

    # TODO: Task 4 - Return and Handle Results
    return jsonify(new_event.to_dict()), 201

# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    event = next((e for e in events if e.id == event_id), None)
    if not event:
        return jsonify({"error": "Event not found"}), 404

    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Missing 'title' field"}), 400

    # TODO: Task 3 - Implement the Loop and Process Each Element
    event.title = data["title"]

    # TODO: Task 4 - Return and Handle Results
    return jsonify(event.to_dict()), 200

# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    event = next((e for e in events if e.id == event_id), None)
    if not event:
        return jsonify({"error": "Event not found"}), 404

    # TODO: Task 3 - Implement the Loop and Process Each Element
    events.remove(event)

    # TODO: Task 4 - Return and Handle Results
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
