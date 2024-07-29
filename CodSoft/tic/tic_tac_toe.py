import random

def minimax(board, depth, is_maximizing, alpha, beta):
    """
    Minimax algorithm with Alpha-Beta Pruning
    """
    if has_won(board, 'X'):
        return -10 + depth
    elif has_won(board, 'O'):
        return 10 - depth
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == '':
                board[i] = 'O'
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ''
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == '':
                board[i] = 'X'
                score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ''
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score

def has_won(board, player):
    """
    Check if a player has won
    """
    winning_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def is_board_full(board):
    """
    Check if the board is full
    """
    return all(cell != '' for cell in board)

def ai_move(board):
    """
    Make a move using Minimax algorithm
    """
    best_score = -float('inf')
    best_move = None
    
    
    if all(cell == '' for cell in board):
        return random.randint(0, 8)
    
    for i in range(9):
        if board[i] == '':
            board[i] = 'O'
            score = minimax(board, 0, False, -float('inf'), float('inf'))
            board[i] = ''
            if score > best_score:
                best_score = score
                best_move = i
    
    return best_move
