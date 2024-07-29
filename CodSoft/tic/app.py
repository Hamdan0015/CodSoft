from flask import Flask, render_template, request, jsonify
from tic_tac_toe import ai_move, has_won, is_board_full

app = Flask(__name__)


board = [''] * 9
history = []
game_started = False  

@app.route('/')
def index():
    global board, history, game_started
    
    if not game_started:
        board = [''] * 9  
    return render_template('index.html', board=board, history=history)

@app.route('/move', methods=['POST'])
def move():
    global board, history, game_started
    if not game_started:
        game_started = True  

    move_index = int(request.form['move_index'])
    if board[move_index] == '':
        board[move_index] = 'X'
        if has_won(board, 'X'):
            result = 'You won!'
            history.append(result)
            board = [''] * 9  
            game_started = False  
            return render_template('index.html', board=board, message=result, history=history)
        elif is_board_full(board):
            result = 'It\'s a draw!'
            history.append(result)
            board = [''] * 9  
            game_started = False  
            return render_template('index.html', board=board, message=result, history=history)
        else:
            ai_index = ai_move(board)
            if ai_index is not None:
                board[ai_index] = 'O'
                if has_won(board, 'O'):
                    result = 'AI won!'
                    history.append(result)
                    board = [''] * 9  
                    game_started = False  
                    return render_template('index.html', board=board, message=result, history=history)
    return render_template('index.html', board=board, history=history)

@app.route('/reset', methods=['POST'])
def reset():
    global board, history, game_started
    board = [''] * 9
    history.clear()
    game_started = False
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)