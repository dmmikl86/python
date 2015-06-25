"""
Cookie Clicker Simulator
"""

# Used to increase the timeout, if necessary
import math

import SimpleGUICS2Pygame.codeskulptor as codeskulptor

codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """

    def __init__(self):
        self._totalCookies = float(0.0)
        self._currentCookies = float(0.0)
        self._currentTime = float(0.0)
        self._currentCPS = float(1.0)
        self._history = [(0.0, None, 0.0, 0.0)]

    def __str__(self):
        """
        Return human readable state
        """
        return "Time: " + str(self._currentTime) + "\n\t\t" + \
               " Current Cookies: " + str(self._currentCookies) + "\n\t\t" + \
               " CPS: " + str(self._currentCPS) + "\n\t\t" + \
               " Total Cookies: " + str(self._totalCookies)

    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._currentCookies

    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._currentCPS

    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._currentTime

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
        time = (cookies - self._currentCookies) / self._currentCPS
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

        self._currentTime += time
        producedCookies = time * self._currentCPS
        self._currentCookies += producedCookies
        self._totalCookies += producedCookies

    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if cost > self._currentCookies: return False

        self._currentCookies -= cost
        self._currentCPS += additional_cps
        self._history.append((self._currentTime, item_name, cost, self._totalCookies))
        return True

def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """

    new_build_info = build_info.clone()
    clicker = ClickerState()
    while clicker.get_time() <= SIM_TIME:
        # 2
        # Call the strategy function with the appropriate arguments to determine
        # which item to purchase next. If the strategy function returns None,
        # you should break out of the loop, as that means no more items will be purchased.
        time_left = SIM_TIME - clicker.get_time()
        item_name = strategy(clicker.get_cookies(), clicker.get_cps(), clicker.get_history(), time_left, new_build_info)
        if item_name is None:
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
    return None

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    return None

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    return None

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
    run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)

    # clicker = ClickerState()

run()
    

