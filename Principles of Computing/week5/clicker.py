"""
Cookie Clicker Simulator
"""

# Used to increase the timeout, if necessary
import math

# import SimpleGUICS2Pygame.codeskulptor as codeskulptor
# import SimpleGUICS2Pygame.simpleplot as simpleplot
# import matplotlib.pyplot as plot
import codeskulptor

codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """

    def __init__(self):
        self._total_cookies = float(0.0)
        self._current_cookies = float(0.0)
        self._current_time = float(0.0)
        self._current_cps = float(1.0)
        self._history = [(0.0, None, 0.0, 0.0)]

    def __str__(self):
        """
        Return human readable state
        """
        return "\n\t\t Time: " + str(self._current_time) + "\n\t\t" + \
               " Current Cookies: " + str(self._current_cookies) + "\n\t\t" + \
               " CPS: " + str(self._current_cps) + "\n\t\t" + \
               " Total Cookies: " + str(self._total_cookies)

    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_cookies

    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._current_cps

    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_time

    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return list(self._history)

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        time = (cookies - self._current_cookies) / self._current_cps
        if time <= 0:
            time = float(0)
        else:
            time = float(math.ceil(time))
        return time

    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time <= 0.0:
            return

        self._current_time += time
        produced_cookies = time * self._current_cps
        self._current_cookies += produced_cookies
        self._total_cookies += produced_cookies

    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if cost > self._current_cookies:
            return False

        self._current_cookies -= cost
        self._current_cps += additional_cps
        self._history.append((self._current_time, item_name, cost, self._total_cookies))
        return True

def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """

    new_build_info = build_info.clone()
    clicker = ClickerState()
    while clicker.get_time() <= duration:
        # 2
        # Call the strategy function with the appropriate arguments to determine
        # which item to purchase next. If the strategy function returns None,
        # you should break out of the loop, as that means no more items will be purchased.
        time_left = duration - clicker.get_time()
        item_name = strategy(clicker.get_cookies(), clicker.get_cps(), clicker.get_history(), time_left, new_build_info)
        if item_name is None:
            clicker.wait(time_left)
            break

        # 3
        # Determine how much time must elapse until it is possible to purchase the item.
        # If you would have to wait past the duration of the simulation to purchase the item,
        # you should end the simulation.
        item_cost = new_build_info.get_cost(item_name)
        time_until_purchase = clicker.time_until(item_cost)
        if time_left < time_until_purchase:
            clicker.wait(time_left)
            break

        # 4
        # Wait until that time.
        clicker.wait(time_until_purchase)

        # 5
        # Buy the item.
        item_cps = new_build_info.get_cps(item_name)
        purchase_result = clicker.buy_item(item_name, item_cost, item_cps)

        # 6
        # Update the build information
        if purchase_result:
            new_build_info.update_item(item_name)

    return clicker

def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """

    items = build_info.build_items()
    min_item_cost = float("inf")
    cheaper_item = None
    for item_name in items:
        item_cost = build_info.get_cost(item_name)
        time_until_purchase = item_cost / cps
        if item_cost < min_item_cost and time_until_purchase <= time_left:
            min_item_cost = item_cost
            cheaper_item = item_name

    return cheaper_item

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """

    items = build_info.build_items()
    max_item_cost = float("-inf")
    expensive_item = None
    for item_name in items:
        item_cost = build_info.get_cost(item_name)
        time_until_purchase = item_cost / cps
        if item_cost > max_item_cost and (time_until_purchase <= time_left or cookies > item_cost):
            max_item_cost = item_cost
            expensive_item = item_name

    return expensive_item

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    best_item = None
    items_cps_cost, min_cps_cost = get_min_cps_cost(build_info)

    best_items = []
    for item_name in items_cps_cost:
        if items_cps_cost[item_name] == min_cps_cost:
            best_items.append((item_name, build_info.get_cost(item_name)))

    cheaper_best_item_cost = float('inf')
    for item in best_items:
        if item[1] < cheaper_best_item_cost:
            cheaper_best_item_cost = item[1]
            best_item = item[0]

    return best_item

def get_min_cps_cost(build_info):
    """
    return items with minimal cps cost
    """
    items = build_info.build_items()
    items_cps_cost = {}
    for item_name in items:
        item_cost = build_info.get_cost(item_name)
        item_cps = build_info.get_cps(item_name)
        item_cps_cost = int(item_cost / item_cps)
        items_cps_cost[item_name] = item_cps_cost
    min_cps_cost = min(items_cps_cost.values())
    return items_cps_cost, min_cps_cost

def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """
    # run_strategy("Cursor", SIM_TIME, strategy_none)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best", SIM_TIME, strategy_best)

    # clicker = ClickerState()

# print strategy_expensive(500000.0, 1.0, [(0.0, None, 0.0, 0.0)], 5.0, provided.BuildInfo({'A': [5.0, 1.0], 'C': [50000.0, 3.0], 'B': [500.0, 2.0]}, 1.15))
# run()
# plot.show()
