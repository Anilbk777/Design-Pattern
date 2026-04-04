from abc import ABC, abstractmethod

class FitnessDataObserver(ABC):

    @abstractmethod
    def update(self, subejct:"FitnessDataSubject"):
        pass

class FitnessDataSubject(ABC):

    @abstractmethod
    def register_observer(self, observer: FitnessDataObserver):
        pass

    @abstractmethod
    def remove_observer(self, observer: FitnessDataObserver):
        pass

    @abstractmethod
    def notify(self):
        pass

class FitnessData(FitnessDataSubject):
    def __init__(self):
        self.steps = 0
        self.active_minutes = 0
        self.calories = 0.0
        self.observers :list[FitnessDataObserver] = []

    def register_observer(self, observer:FitnessDataObserver):
        if not isinstance(observer, FitnessDataObserver):
            raise ValueError("Give observer is not an instance of FitnessDataObserver")

        self.observers.append(observer)

    def remove_observer(self,observer:FitnessDataObserver):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def new_fitness_data_pushed(self, steps:int, active_minutes:int,calories:float):
        self.steps = steps
        self.active_minutes = active_minutes
        self.calories = calories

        print(f"\nFitnessData: New data received – Steps: {steps}, "
            f"Active Minutes: {active_minutes}, Calories: {calories}")

        self.notify()

    def daily_reset(self):
        self.steps = 0
        self.active_minutes = 0
        self.calories = 0.0

        print("\nFitnessData: Daily reset performed.")
        self.notify()

    def get_steps(self):
        return self.steps
    
    def get_active_minutes(self):
        return self.active_minutes
    
    def get_calories(self):
        return self.calories


class LiveActivityDisplay(FitnessDataObserver):

    def update(self, sub: FitnessData):
        print(
            f"Live Display -> Steps: {sub.get_steps()},"
            f"| Active Minutes: {sub.get_active_minutes()} "
            f"| Calories: {sub.get_calories()}"
        )

class ProgressLogger(FitnessDataObserver):
    def update(self, subejct: FitnessData):
        print(
            f"Logger → Saving to DB: Steps={subejct.get_steps()}, "
            f"ActiveMinutes={subejct.get_active_minutes()}, "
            f"Calories={subejct.get_calories()}"
        )
