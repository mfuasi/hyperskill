class Puppy:
    n_puppies = 0  # number of created puppies

    # define __new__
    def __new__(cls):
        while cls.n_puppies < 10:
            object.__new__(cls)
            cls.n_puppies += 1
