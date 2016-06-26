import flag


env = flag.string("env", "production", "The environment to use")
workers = flag.int("workers", 4, "The number of workers")

if __name__ == '__main__':
    flag.parse()

    print(env.upper())
    print (workers + 3)
