def hello(to="world"):#giving an parameter to the function
    print("hello,",to)
hello()#if no value is passed to the parameter to, it will take the default value "world"
name=input("enter your name:")
hello(name)# copies the value of name to the parameter to in the function hello
