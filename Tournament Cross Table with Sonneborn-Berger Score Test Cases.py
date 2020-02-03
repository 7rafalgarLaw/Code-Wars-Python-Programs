# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 17:15:18 2019

@author: simasurk
"""

def do_test(players, results, expected):
    actual = crosstable(players, results)
    if actual != expected:
        print("crosstable({!r}, {!r})\n\nactual:\n{}\n\nexpected:\n{}".format(players, results, actual, expected))
        test.assert_equals(actual.count('\n') + 1, expected.count('\n') + 1, "There should be {} lines".format(expected.count('\n') + 1))
        for i, (actual_line, expected_line) in enumerate(zip(actual.split('\n'), expected.split('\n')), 1):
            if actual_line != expected_line:
                print("actual line:\n{!r}".format(actual_line))
                print("expected line:\n{!r}".format(expected_line))
                test.assert_equals(actual_line, expected_line, "line {}".format(i))
    test.assert_equals(actual, expected)

d, _ = 0.5, None

do_test([
    "Emmett Frost", "Cruz Sullivan", "Deandre Bullock", "George Bautista", "Norah Underwood", "Renee Preston"], [
    [_, 1, 0, 0, d, 0],
    [0, _, d, 1, 0, 0],
    [1, d, _, d, d, d],
    [1, 0, d, _, d, d],
    [d, 1, d, d, _, d],
    [1, 1, d, d, d, _]],
    "#  Player           1 2 3 4 5 6  Pts   SB\n"
    "==========================================\n"
    "1  Renee Preston      = = = 1 1  3.5  7.25\n"
    "2  Deandre Bullock  =   = = = 1  3.0  6.75\n"
    "   Norah Underwood  = =   = 1 =  3.0  6.75\n"
    "4  George Bautista  = = =   0 1  2.5  6.25\n"
    "5  Cruz Sullivan    0 = 0 1   0  1.5  4.00\n"
    "6  Emmett Frost     0 0 = 0 1    1.5  3.00")

do_test([
    'Ana Gill', 'Alan Benitez', 'Lina Estes', 'Greta Kline', 'Simone Kelly', 'Quinn Sexton', 'India Cooper',
    'Ashton Richardson'], [
    [_, 0, 1, d, d, d, 0, 1],
    [1, _, 0, d, 1, d, 0, 0],
    [0, 1, _, d, 0, 1, 1, 1],
    [d, d, d, _, 1, 1, d, 0],
    [d, 0, 1, 0, _, d, d, d],
    [d, d, 0, 0, d, _, 1, d],
    [1, 1, 0, d, d, 0, _, d],
    [0, 1, 0, 1, d, d, d, _]],
    "#  Player             1 2 3 4 5 6 7 8  Pts   SB\n"
    "=================================================\n"
    "1  Lina Estes           = 0 1 1 0 1 1  4.5  15.00\n"
    "2  Greta Kline        =   = = 0 1 = 1  4.0  13.25\n"
    "3  Ana Gill           1 =   0 1 = 0 =  3.5  13.00\n"
    "4  India Cooper       0 = 1   = = 1 0  3.5  11.75\n"
    "   Ashton Richardson  0 1 0 =   = 1 =  3.5  11.75\n"
    "6  Simone Kelly       1 0 = = =   0 =  3.0  11.25\n"
    "7  Alan Benitez       0 = 1 0 0 1   =  3.0  10.00\n"
    "   Quinn Sexton       0 0 = 1 = = =    3.0  10.00")

do_test([
    'Trystan Randall', 'Pamela Glass', 'Coleman Serrano', 'Brycen Beasley', 'Wayne Allison', 'Natalia Powell',
    'Carlos Koch', 'Emilio Mejia', 'Lennon Rollins', 'Madilynn Huerta'], [
    [_, 1, 1, 0, 1, 1, d, d, 0, 1],
    [0, _, d, 0, d, d, 1, 0, 1, 0],
    [0, d, _, 0, 0, d, 0, 0, 1, 1],
    [1, 1, 1, _, d, 1, d, 1, 1, d],
    [0, d, 1, d, _, 0, d, 0, d, d],
    [0, d, d, 0, 1, _, 1, 1, 1, d],
    [d, 0, 1, d, d, 0, _, 0, d, d],
    [d, 1, 1, 0, 1, 0, 1, _, d, d],
    [1, 0, 0, 0, d, 0, d, d, _, 0],
    [0, 1, 0, d, d, d, d, d, 1, _]],
    " #  Player            1  2  3  4  5  6  7  8  9 10  Pts   SB\n"
    "==============================================================\n"
    " 1  Brycen Beasley       1  1  1  =  =  =  1  1  1  7.5  31.75\n"
    " 2  Trystan Randall   0     1  =  1  =  1  1  1  0  6.0  24.50\n"
    " 3  Natalia Powell    0  0     1  =  1  1  =  =  1  5.5  20.50\n"
    " 4  Emilio Mejia      0  =  0     =  1  1  1  1  =  5.5  20.00\n"
    " 5  Madilynn Huerta   =  0  =  =     =  =  1  0  1  4.5  18.75\n"
    " 6  Carlos Koch       =  =  0  0  =     =  0  1  =  3.5  15.00\n"
    " 7  Wayne Allison     =  0  0  0  =  =     =  1  =  3.5  13.75\n"
    " 8  Pamela Glass      0  0  =  0  0  1  =     =  1  3.5  12.00\n"
    " 9  Coleman Serrano   0  0  =  0  1  0  0  =     1  3.0  11.50\n"
    "10  Lennon Rollins    0  1  0  =  0  =  =  0  0     2.5  12.25")

do_test([
    'K. Kel', 'A. Vau', 'Z. Aya', 'J. Coc', 'M. Hue', 'A. Sim', 'C. Yan', 'J. Wal',
    'M. Hor', 'L. Ell', 'H. Mic', 'P. Bla', 'L. Lan', 'M. Rid', 'M. Bec', 'J. Gat'], [
    [_, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, _, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, _, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, _, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, _, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, _, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, _, 0, 0, 1, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, _, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, _, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, _, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, _, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, _, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _]],
    " #  Player   1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16  Pts     SB\n"
    "=========================================================================\n"
    " 1  J. Gat      1  1  1  1  1  1  1  0  1  1  1  1  1  1  1  14.0  100.00\n"
    " 2  M. Bec   0     1  1  1  1  1  1  1  1  1  1  1  1  1  1  14.0   92.00\n"
    " 3  M. Rid   0  0     1  0  1  1  1  1  0  1  1  1  1  1  1  11.0   65.00\n"
    " 4  L. Lan   0  0  0     1  1  1  1  0  1  1  1  1  1  1  1  11.0   64.00\n"
    " 5  M. Hor   0  0  1  0     0  1  0  1  1  1  1  1  1  1  1  10.0   53.00\n"
    " 6  H. Mic   0  0  0  0  1     0  1  1  1  1  1  1  1  0  1   9.0   50.00\n"
    " 7  P. Bla   0  0  0  0  0  1     1  0  1  1  1  1  1  1  1   9.0   45.00\n"
    " 8  L. Ell   0  0  0  0  1  0  0     1  1  1  1  1  1  1  1   9.0   43.00\n"
    " 9  M. Hue   1  0  0  1  0  0  1  0     0  0  1  0  0  1  1   6.0   43.00\n"
    "10  C. Yan   0  0  1  0  0  0  0  0  1     1  0  0  1  1  1   6.0   30.00\n"
    "11  J. Wal   0  0  0  0  0  0  0  0  1  0     1  1  1  1  1   6.0   21.00\n"
    "12  A. Sim   0  0  0  0  0  0  0  0  0  1  0     1  1  1  1   5.0   16.00\n"
    "13  K. Kel   0  0  0  0  0  0  0  0  1  1  0  0     0  0  1   3.0   14.00\n"
    "14  Z. Aya   0  0  0  0  0  0  0  0  1  0  0  0  1     1  0   3.0   11.00\n"
    "15  A. Vau   0  0  0  0  0  1  0  0  0  0  0  0  1  0     0   2.0   12.00\n"
    "16  J. Coc   0  0  0  0  0  0  0  0  0  0  0  0  0  1  1      2.0    5.00")

do_test([
    "Harry Pillsbury", "Mikhail Chigorin", "Emanuel Lasker", "Siegbert Tarrasch", "William Steinitz",
    "Emanuel Schiffers", "Curt Bardeleben", "Richard Teichmann", "Carl Schlechter", "Joseph Blackburne",
    "Carl Walbrodt", "David Janowski", "James Mason", "Amos Burn", "Isidor Gunsberg", "Henry Bird", "Adolf Albin",
    "Georg Marco", "William Pollock", "Jacques Mieses", "Samuel Tinsley", "Beniamino Vergani"], [
    [_, 0, 0, 1, 1, 1, 1, 1, 0, d, d, 1, 1, 1, 1, 1, 1, d, 1, 1, 1, 1],
    [1, _, 1, 1, 0, 0, 1, 1, 1, 1, d, 0, 1, 1, 1, d, d, 1, 1, d, 1, 1],
    [1, 0, _, 0, 1, 1, 0, 1, 1, 0, 1, 1, d, 1, 1, 1, d, 1, 1, d, 1, 1],
    [0, 0, 1, _, 1, 1, d, 0, d, 1, 1, 1, 0, 1, d, 1, 1, 1, 0, d, 1, 1],
    [0, 1, 0, 0, _, 1, 1, d, d, 1, 1, 0, 1, d, 1, 0, 1, 1, 0, d, 1, 1],
    [0, 1, 0, 0, 0, _, d, d, 0, 1, 1, 1, d, d, 1, 1, 0, d, 1, d, 1, 1],
    [0, 0, 1, d, 0, d, _, d, d, 0, 0, d, 1, 1, 1, d, d, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, d, d, d, _, d, 0, 0, d, 1, 1, 0, 1, d, 1, d, 1, 1, 1],
    [1, 0, 0, d, d, 1, d, d, _, d, d, 0, 1, 1, d, d, d, d, d, d, 1, 0],
    [d, 0, 1, 0, 0, 0, 1, 1, d, _, 0, 1, 0, 1, 0, d, 1, 0, 1, 0, 1, 1],
    [d, d, 0, 0, 0, 0, 1, 1, d, 1, _, 0, d, 0, d, d, 0, d, d, 1, 1, 1],
    [0, 1, 0, 0, 1, 0, d, d, 1, 0, 1, _, d, 0, 0, d, 0, 1, d, 1, 0, 1],
    [0, 0, d, 1, 0, d, 0, 0, 0, 1, d, d, _, 1, 0, 1, d, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, d, d, 0, 0, 0, 0, 1, 1, 0, _, 0, d, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, d, 0, 0, 0, 1, d, 1, d, 1, 1, 1, _, 0, 1, d, 0, 1, 0, 0],
    [0, d, 0, 0, 1, 0, d, 0, d, d, d, d, 0, d, 1, _, 1, d, 0, d, d, 1],
    [0, d, d, 0, 0, 1, d, d, d, 0, 1, 1, d, 0, 0, 0, _, 0, 0, 1, 1, d],
    [d, 0, 0, 0, 0, d, 0, 0, d, 1, d, 0, 1, 0, d, d, 1, _, 1, 1, 0, d],
    [0, 0, 0, 1, 1, 0, 0, d, d, 0, d, d, 0, 0, 1, 1, 1, 0, _, 0, 0, 1],
    [0, d, d, d, d, d, 0, 0, d, 1, 0, 0, 0, 0, 0, d, 0, 0, 1, _, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, d, 0, 1, 1, 0, _, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, d, d, 0, 0, 0, _]],
    " #  Player              1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22  Pts     SB\n"
    "======================================================================================================\n"
    " 1  Harry Pillsbury        0  0  1  1  1  1  1  0  =  =  1  1  1  1  1  1  =  1  1  1  1  16.5  157.50\n"
    " 2  Mikhail Chigorin    1     1  1  0  0  1  1  1  1  =  0  1  1  1  =  =  1  1  =  1  1  16.0  163.00\n"
    " 3  Emanuel Lasker      1  0     0  1  1  0  1  1  0  1  1  =  1  1  1  =  1  1  =  1  1  15.5  150.75\n"
    " 4  Siegbert Tarrasch   0  0  1     1  1  =  0  =  1  1  1  0  1  =  1  1  1  0  =  1  1  14.0  136.00\n"
    " 5  William Steinitz    0  1  0  0     1  1  =  =  1  1  0  1  =  1  0  1  1  0  =  1  1  13.0  125.75\n"
    " 6  Emanuel Schiffers   0  1  0  0  0     =  =  0  1  1  1  =  =  1  1  0  =  1  =  1  1  12.0  111.50\n"
    " 7  Curt Bardeleben     0  0  1  =  0  =     =  =  0  0  =  1  1  1  =  =  1  1  1  0  1  11.5  108.25\n"
    " 8  Richard Teichmann   0  0  0  1  =  =  =     =  0  0  =  1  1  0  1  =  1  =  1  1  1  11.5  105.25\n"
    " 9  Carl Schlechter     1  0  0  =  =  1  =  =     =  =  0  1  1  =  =  =  =  =  =  1  0  11.0  115.50\n"
    "10  Joseph Blackburne   =  0  1  0  0  0  1  1  =     0  1  0  1  0  =  1  0  1  0  1  1  10.5  102.75\n"
    "11  Carl Walbrodt       =  =  0  0  0  0  1  1  =  1     0  =  0  =  =  0  =  =  1  1  1  10.0   95.25\n"
    "12  David Janowski      0  1  0  0  1  0  =  =  1  0  1     =  0  0  =  0  1  =  1  0  1   9.5   93.75\n"
    "13  James Mason         0  0  =  1  0  =  0  0  0  1  =  =     1  0  1  =  0  1  1  0  1   9.5   89.25\n"
    "14  Amos Burn           0  0  0  0  =  =  0  0  0  0  1  1  0     0  =  1  1  1  1  1  1   9.5   79.50\n"
    "15  Isidor Gunsberg     0  0  0  =  0  0  0  1  =  1  =  1  1  1     0  1  =  0  1  0  0   9.0   88.25\n"
    "16  Henry Bird          0  =  0  0  1  0  =  0  =  =  =  =  0  =  1     1  =  0  =  =  1   9.0   84.25\n"
    "17  Adolf Albin         0  =  =  0  0  1  =  =  =  0  1  1  =  0  0  0     0  0  1  1  =   8.5   85.50\n"
    "18  Georg Marco         =  0  0  0  0  =  0  0  =  1  =  0  1  0  =  =  1     1  1  0  =   8.5   79.25\n"
    "19  William Pollock     0  0  0  1  1  0  0  =  =  0  =  =  0  0  1  1  1  0     0  0  1   8.0   77.50\n"
    "20  Jacques Mieses      0  =  =  =  =  =  0  0  =  1  0  0  0  0  0  =  0  0  1     1  1   7.5   74.25\n"
    "21  Samuel Tinsley      0  0  0  0  0  0  1  0  0  0  0  1  1  0  1  =  0  1  1  0     1   7.5   63.50\n"
    "22  Beniamino Vergani   0  0  0  0  0  0  0  0  1  0  0  0  0  0  1  0  =  =  0  0  0      3.0   28.50")
        