# Farmers Market Checkout System
A checkout system to order items and apply discounts.

### Requirements
The Farmers Market Checkout system was designed to be used with Python 3, but should be runnable in a Python 2 environment.

### Running the program
Outside a container:
```bash
git clone https://github.com/benjaminjb/farmers_market.git && cd farmers_market
python src/interface.py
```

Inside a Docker container:
```bash
docker build -t <<TAG>> .
docker run -it <<TAG>>
```

### Using the checkout system
When running the interface.py script, a session starts automatically with an empty basket. A basket can be manually cleared by entering `clear`, which creates a new empty basket.

Items can be added with the command `add <<ITEM>>`. Items currently supported include apples, chai, coffee, milk, and oatmeal. Attempts to add unsupported items will result in an error message, though the current basket will still be usable.

Every successful action results in a print out of the current basket, including a running total. A printout can be manually generated with the `sum` command.

The checkout program can be terminated with the `checkout` command.

### Running Tests
The tests are kept in the "/tests" folder. Run them by running
```bash
python -m unittest discover tests
```

### Known Issues
1. When the BOGO discount is reached, it will apply to the first coffee bought.

### Possible To Do
1. Implement `remove <<ITEM>>`.

### Discussion topics
1. I implemented Basket as a very simple Class, but nothing else seemed like it required being a Class.
2. I never before shared a project simply with a Dockerfile, and while `ADD` and untarring the project seemed like the best way to do that, there might be a better way.
3. Discounts get recalculated after every addition to mimic a standard market checkout system. This would make it easier to add a hypothetical `remove <<ITEM>>` command, but it might not scale well for another sort of system. (For example, a system that was getting millions of `add` commands might work better with the discounts being calculated less frequently.)
4. The discounts.py is potentially fragile because it might seem unintuitive and it is the heart of the discount system. For an actual app, I would put more documentation to make sure that any users knew what the structure has to be.
5. I used tuples for the keys of a dictionary, because they're immutable and so able to be used as keys. However, the tuple structure leads to a lot of unclear references, so one potential improvement would be to use a namedTuple structure (an immutable tuple with key/value pairs).
