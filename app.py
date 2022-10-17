
import os
from flask import Flask, request, render_template, jsonify, session
from read_puzzle import export_result
from sudokuSolver import solveSudoku
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'static/images'
app.secret_key = "qh7djvl;3gffwkkdkkdwkhgsomdddd\\\\\\dcywk"

@app.route("/")
def index():
    return render_template("index.html")

# ==============================================
# To read the initial puzzle & return it to JS
@app.route("/read_puzzle", methods=["POST","GET"])
def read():
    # Read filepath & save it
    if request.method == "POST":
        enquired_file = request.files['file']
        file_name = secure_filename(enquired_file.filename)
        path = os.path.join(app.config['UPLOAD_PATH'], file_name)
        enquired_file.save(path)
        board = export_result(path)
        board_py = board.tolist()
        session["initial_puzzle"] = board_py
        session["saved_path"] = path
    return render_template("solution.html", data=board_py, path=path)

# ==============================================
# To read the modified input & solve puzzles & then return it to JS
@app.route("/solve_puzzle", methods=["POST","GET"])
def solve():
    board_py = session.get("initial_puzzle")
    path = session.get("saved_path")

    # get the input result
    if request.method == "POST":
        mo_data = request.form.get("modification")
    
    # modify board based on user's input
    try:
        if mo_data == "none":
            solution = solveSudoku(board_py_copy)
        else:
            board_py_copy = board_py
            modified_data = mo_data.split(";")
            for i in range(len(modified_data)):
                x = int(modified_data[i][0])-1 # -1 to account for different rule of start point in python
                y = int(modified_data[i][1])-1
                value = int(modified_data[i][2])
                board_py_copy[x][y] = value
            solution = solveSudoku(board_py_copy)
    except:
        solution = None
    
    if solution:    
        return render_template("solution_confirmed.html", data=solution, path=path)
    else: 
        return render_template("solution_confirmed.html", data=(board_py,[],False), path=path)

if __name__ == "__main__":
    app.run(debug=True)