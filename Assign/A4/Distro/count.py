if __name__ == "__main__":
    f = open("train4c.txt", 'r')
    total_line = 0
    win = 0
    for line in f:
        total_line += 1
        if "cheese" in line:
            win += 1
 
    print "Total runs: ", total_line
    print "Mouse win: ", win
    print "Ratio: ", (float(win) / total_line)