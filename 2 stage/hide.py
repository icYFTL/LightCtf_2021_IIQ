INPUT_FILE = 'Cat.jpg'
OUTPUT_FILE = 'StegoCat.jpg'

with open(INPUT_FILE, 'rb') as f:
    cat = f.read()
    cat += open('Xexe.zip', 'rb').read()
    open(OUTPUT_FILE, 'wb').write(cat)
