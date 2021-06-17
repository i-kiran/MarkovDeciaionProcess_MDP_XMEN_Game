
import time
import tkinter as Mazegame
from tkinter import ttk, Canvas, Label

#make the window to display
def make_screen(n):
    size = 500

    cell_width = int(size/n)
    cell_height = int(size/n)

    screen = Mazegame.Tk()
    screen.title("prey and predator")
    grid = Canvas(screen, width = cell_width*n, height = cell_height*n, highlightthickness=0)
    grid.pack(side="top", fill="both", expand="true")

    rect = {}
    for col in range(n):
        for row in range(n):
            x1 = col * cell_width
            y1 = row * cell_height
            x2 = x1 + cell_width
            y2 = y1 + cell_height
            rect[row, col] = grid.create_rectangle(x1,y1,x2,y2, fill="red", tags="rect")
    return grid, rect, screen, cell_width

# update window with repect to given positions
def redraw_maze(grid, rect, screen, n, maze, delay, wid):
    grid.itemconfig("rect", fill="green")
    
    for i in range(n):
        for j in range(n):
            item_id = rect[i,j]
            if maze[i][j] == 0:                      
                grid.itemconfig(item_id, fill="dark grey")
            elif maze[i][j] == 1:                      
                grid.itemconfig(item_id, fill="light green")	#magneto
            elif maze[i][j] == 2:                        
                grid.itemconfig(item_id, fill="cyan")	#wolverine
            elif maze[i][j] == 3:
                grid.itemconfig(item_id, fill="grey")	#jean
    grid.itemconfig(rect[2,3], fill="black")
    screen.update_idletasks()
    screen.update()
    time.sleep(delay)
    return
	
