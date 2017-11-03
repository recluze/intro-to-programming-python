## IMPORTS GO HERE

## END OF IMPORTS



### YOUR CODE FOR line_count() FUNCTION GOES HERE ###

#### End OF MARKER



### YOUR CODE FOR character_count() FUNCTION GOES HERE ###

#### End OF MARKER



### YOUR CODE FOR move_lines() FUNCTION GOES HERE ###

#### End OF MARKER



if __name__ == '__main__':
    print line_count('.', 'essay.txt')
    print line_count('.', 'essay.txt', True)

    print character_count('.', 'essay.txt')
    print character_count('.', 'essay.txt', True)

    move_lines('essay.txt', 'out.txt', 3)

    pass
