def play(MAX_RUNS, show_games=False):

    from random import randint as r

    # Random
    player1_wins = 0

    # Knows how to play
    player2_wins = 0

    player1_win = False

    for i in range(MAX_RUNS):
        sticks = 10

        if show_games:
            print ("\n")
            print "Game: {}".format(i + 1)

        while sticks >= 0:

            # Player 1

            player1_move = r(1, 2)
            if sticks < player1_move:
                player1_move = 1

            if show_games:
                print "Player 1 Available: {}, Took: {}, Left: {}".format(sticks, player1_move, (sticks - player1_move))
                print("\n")

            sticks -= player1_move

            if sticks == 0:
                player1_win = True
                if show_games:
                    print("Player 1 Wins")
                break

            # Player 2

            if sticks % 3 == 0:
                player2_move = 1
            else:
                player2_move = sticks % 3

            if show_games:
                print "Player 2 Available: {}, Took: {}, Left: {}".format(sticks, player2_move, (sticks - player2_move))
                print("\n")

            sticks -= player2_move

            if sticks == 0:
                player1_win = False
                if show_games:
                    print("Player 2 Wins")
                break

        if player1_win:
            player1_wins += 1
        else:
            player2_wins += 1

    if show_games:
        print('\n\n')

    print "Player 1 (Random) Won: {}/{} ({}%)".format(player1_wins, MAX_RUNS, (float(player1_wins) / MAX_RUNS * 100))
    print "Player 2 (Strategy) Won: {}/{} ({}%)".format(player2_wins, MAX_RUNS, (float(player2_wins) / MAX_RUNS * 100))

play(1000, True)