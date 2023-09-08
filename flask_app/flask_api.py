from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_app import selecteur as sl 
from flask_app.insert import ajout_page
from waitress import serve
def create_app():
    app = Flask(__name__)
    CORS(app)
    @app.route("/pages", methods=['GET'])
    def affich_pages():
        posts=sl.select_pages()
        return posts
    @app.route("/posts/<int:page_id>", methods=['GET'])
    def affich_post(page_id):
        posts=sl.select_posts(page_id)
        
        return posts

    @app.route("/posts/comments/<int:post_id>", methods=['GET'])
    def affich_comments(post_id):
        comments=sl.select_comments(post_id)
        return comments

    @app.route("/posts/reactions/<int:post_id>", methods=['GET'])
    def affich_reactions(post_id):
        reactions=sl.select_reactions(post_id)
        return reactions


    @app.route('/add/new_page', methods=['POST'])
    def create_page():
        try:
            page = request.json
            err= ajout_page(page['name'])
            return jsonify({"message": err}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    return app    
