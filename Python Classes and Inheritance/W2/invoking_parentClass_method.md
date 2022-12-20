# Invoking the Parent Class’s Method

Sometimes the parent class has a useful method, but you just need to execute a little extra code when running the subclass’s method. You can override the parent class’s method in the subclass’s method with the same name, but also invoke the parent class’s method. Here’s how.

Say you wanted the Dog subclass of Pet to say “Arf! Thanks!” when the feed method is called, as well as executing the code in the original method.

Here’s the original Pet class again.
```
from random import randrange

# Here's the original Pet class
class Pet():
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 5
    hunger_threshold = 10
    sounds = ['Mrrp']
    def __init__(self, name = "Kitty"):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        # state += "Hunger %d Boredom %d Words %s" % (self.hunger, self.boredom, self.sounds)
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def teach(self, word):
        self.sounds.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)
```

And here’s a subclass that overrides feed() by invoking the the parent class’s feed() method; it then also executes an extra line of code. Note the somewhat inelegant way of invoking the parent class’ method. We explicitly refer to Pet.feed to get the method/function object. We invoke it with parentheses. However, since we are not invoking the method the normal way, with <obj>.methodname, we have to explicitly pass an instance as the first parameter. In this case, the variable self in Dog.feed() will be bound to an instance of Dog, and so we can just pass self: Pet.feed(self).
```
from random import randrange

class Dog(Pet):
    sounds = ['Woof', 'Ruff']

    def feed(self):
        Pet.feed(self)
        print("Arf! Thanks!")

d1 = Dog("Astro")

d1.feed()
```

### Note
There’s a better way to invoke a superclass’s method. In that alternative method, we would call super().feed(). This is nice because it’s easier to read, and also because it puts the specification of the class that Dog inherits from in just one place, class Dog(Pet). Elsewhere, you just refer to super() and python takes care of looking up that the parent (super) class of Dog is Pet.

This technique is very often used with the __init__ method for a subclass. Suppose that some extra instance variables are defined for the subclass. When you invoke the constructor, you pass all the regular parameters for the parent class, plus the extra ones for the subclass. The subclass’ __init__ method then stores the extra parameters in instance variables and calls the parent class’ __init__ method to store the common parameters in instance variables and do any other initialization that it normally does.

Let’s say we want to create a subclass of Pet, called Bird, and we want it to take an extra parameter, chirp_number, with a default value of 2, and have an extra instance variable, self.chirp_number. Then, we’ll use this in the hi method to make more than one sound.
```
class Bird(Pet):
    sounds = ["chirp"]
    def __init__(self, name="Kitty", chirp_number=2):
        Pet.__init__(self, name) # call the parent class's constructor
        # basically, call the SUPER -- the parent version -- of the constructor, with all the parameters that it needs.
        self.chirp_number = chirp_number # now, also assign the new instance variable

    def hi(self):
        for i in range(self.chirp_number):
            print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

b1 = Bird('tweety', 5)
b1.teach("Polly wanna cracker")
b1.hi()

chirp
Polly wanna cracker
Polly wanna cracker
Polly wanna cracker
Polly wanna cracker
```

What will print when print(b1.sounds) is run?
  
["chirp"]
The interpeter finds the value in the class variable for the class Bird.

  
For the Dog class defined in the earlier activecode window, what would happen when d1.feed() is run if the Pet.feed(self) line was deleted?

  The string would print but d1 would not have its hunger reduced.
Since we are no longer calling the parent Pet class's method in the Dog subclass's method definition, the class definition will override the parent method.
