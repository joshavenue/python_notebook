count = 0      # A global count variable

def remember():
    global count
    count += 1  # Count this invocation
    print(str(count))


remember()
remember()
remember()
remember()
remember()
