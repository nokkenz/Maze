from colorama import init, Fore

wall = 'w'
free = 'f'
unvisited = 'u'
H = 10
W = 30

init() #colorama

def init_maze(W,H):
    maze = []

    for i in range(0, H):
        row = []
        for j in range(0, W):
            row.append('u')
            maze.append(row)
    return maze

def print_maze(maze):

    for i in range(0,len(maze)):
        for j in range(0, len(maze[0])):
            if maze[1] == 'u':
                print(Fore.WHITE,f'{maze[i][j]}', end='')
            elif maze[i][j] == 'f':
                print(Fore.CYAN,f'{maze[i][j]}', end='')
            else:
                print(Fore.RED,f'{maze[i][j]}', end='')

        print('\n')


if __name__ == '__main__':
    init_maze(1)


