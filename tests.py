import unittest

class Test1(unittest.TestCase):
    
    def setUp(self):
        # Set up a simulation with no initial queue
        # Process with single activity
        # Simulate for 1 day, receiving 100 cases
        # Single resource able to process 120 cases/day
        pass

    def test_Backlog(self):
        # Backlog at the end of the day should be 0
        pass

class Test2(unittest.TestCase):
    
    def setUp(self):
        # Set up a simulation with 100 initial cases waiting
        # Process with single activity
        # Simulate for 1 day, receiving 0 cases
        # Single resource able to process 100 cases/day
        pass

    def test_Backlog(self):
        # Backlog at the end of the day should be 0
        pass

class Test3(unittest.TestCase):
    
    def setUp(self):
        # Set up a simulation with 100 initial cases waiting
        # Process with single activity
        # Simulate for 1 day, receiving 0 cases
        # 2 resources able to process 100 cases/day
        pass

    def test_FinalBacklog(self):
        # Backlog at the end of the day should be 0
        pass

    def test_HalfDayBacklog(self):
        # Backlog half way through the day should be 0 from there on
        pass

class Test4(unittest.TestCase):
    
    def setUp(self):
        # Set up a simulation with 100 initial cases waiting
        # Process with single activity
        # Simulate for 1 day, receiving 100 cases
        # Single resource able to process 100 cases/day
        pass

    def test_FinalBacklog(self):
        # Backlog at the end of the day should be 100
        pass

class Test5(unittest.TestCase):
    
    def setUp(self):
        # Set up a simulation with 100 initial cases waiting
        # Process with single activity
        # Simulate for 1 day, receiving 100 cases
        # Single resource able to process 200 cases/day
        pass

    def test_FinalBacklog(self):
        # Backlog at the end of the day should be 0
        pass

if __name__ == "__main__":
    unittest.main()