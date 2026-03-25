from flask import Flask , jsonify , request

app = Flask(__name__)
#the flask class will act as the wsgi to process request from server and send reply to it by app
items = [
    {"id":1 , "name":"item1" , "description":"this is item 1", "completed": False},
    {"id":2 , "name":"item2" , "description":"this is item 2" , "completed":False}
]

@app.route("/")
def home():
    return "Welcome to sample todo list"

#retrive the list 
@app.route('/items' , methods = ['GET'])
def get_items():
    return jsonify(items) , 200




#retrieve a specific element by id
@app.route('/items/<int:item_id>' , methods = ['GET'])
def id(item_id):
    item = next((item for item in items if item["id"] == item_id) , None)
    if item is None:
        return jsonify( {"error":"id not found" }), 404
    return jsonify(item) , 200

#post : create a new task by adding a new dict into list

@app.route('/items' , methods =['POST'])
def add():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"item not found"}) , 404
    #add the new item
    new_item = {
        "id":items[-1]["id"]+1 , "name":request.json['name'] , "description":request.json['description'] , "completed":False
    }
    items.append(new_item)
    return jsonify(new_item) , 201


@app.route('/items/<int:item_id>' , methods = ['PUT'])
def update(item_id):
    item = next((item for item in items if item["id"] == item_id) , None)
    if item is None:
        return jsonify({"error":"no id found"}) , 404
    item['name'] = request.json.get('name' , item['name'])
    item['description'] = request.json.get('description' , item['description'])
    item['completed']  =request.json.get('completed' , item['completed'])
    return jsonify(item) , 200

#delete an item

@app.route('/items/<int:item_id>' , methods = ['DELETE'])
def delete(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"done"}) , 200

@app.route('/health')
def health():
    return jsonify({'error':'Page is running'}) , 200





if __name__ == "__main__":
    app.run(debug = True)