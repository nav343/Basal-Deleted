# Basal

#### A general purpose low level programming language written in Python. Basal is an easy mid level programming language compiling to C. It has an easy syntax, similar to Python, Rust etc.

# Contributors

- ### SnmLogic (suggested the idea and now we're doing it)
- ### Bunch-Of-Cells (The guy who decided the bad (obviously) name, I mean it sounds like Nasal!)
- ### Mochii (DetectiveCatt, random dude who is in love with cats, weirdo)

# Syntax

## Variables

```
let a = 20
```

## Functions

```
func a(xyz: int32) {
  // do something here
}
```

## For loop

```
for i in range(1, 21) {
  out(i)
}
```

## While loop

```
while 1 {
  out("this gonna go forevaaaaaaaaaa")
}
```

### Note: The syntax is not fixed and may change in the future.

# File Structure
```
/core
  |- lexer.py
  |- parser.py
  
/utils
  /create-basal-app
    /Test
      /src
        |- main.basl
      |- init.json
    |- create-basal-app.py
    |- requirements.txt
  |- error.py
  |- peekable.py
  |- token.py

basalc.py
Readme.md
```
~Mochii
