from card import *
import random

class Event:
	def __init__(self, time, event_type, bill):
		self.time = time
		self.event_type = event_type
		self.bill = bill
		# bill field is a card for release events and None for income events.

class Scheduling:
	def __init__(self, income_period, minimum_income, maximum_income):
		self.income_period = income_period
		self.minimum_income = minimum_income
		self.maximum_income = maximum_income
		self.events = []
		self.time = 0
		self.money = 0
		self.alert = False
	def update_time(self, new_time):
		self.time = new_time
	def add_event(self, event):
		self.events.append(event)
	def add_bill_event(self, bill):
		self.add_event(Event(bill.deadline, "2-deadline", bill))
		self.add_event(Event(bill.hard_deadline, "1-hard", bill))
	def get_money_from_a_friend(self, amount):
		self.money += amount
		self.alert = False
	def time_of_next_income(self):
		for event in self.events:
			if "income" in event.event_type:
				return event.time
		else:
			raise Exception("no income event found in events list!")
	def schedule(self):
		while True:
			self.events.sort(key=lambda x : (x.time, x.event_type))
			event = self.events.pop(0)
			if event.time != self.time:
				if event.time > self.time:
					self.events.append(event)
					self.events.sort(key=lambda x : (x.time, x.event_type))
					return self.events[0].time
				continue
			if "hard" in event.event_type:
				if event.bill.debt <= self.money:
					amount_payed, remained_debt = event.bill.pay_debt(self.money)
					assert(remained_debt == 0)
					self.money -= amount_payed
					assert(self.money >= 0)
				self.event.bill.pass_hard_deadline()
			elif "release" in event.event_type:
				self.add_event(Event(self.time + event.bill.bill_period, "3-release", event.bill))
				if event.bill.maximum_credit >= event.bill.minimum_paying_first + event.bill.get_total_debt():
					bill = event.bill.release_bill(self.time, random.uniform(event.bill.minimum_paying_first, event.bill.maximum_credit - event.bill.get_total_debt()))
					self.add_bill_event(bill)
			elif "income" in event.event_type:
				self.money += random.uniform(self.minimum_income, self.maximum_income)
				self.events.append(Event(self.time + self.income_period, "0-income", None))
				self.alert = False
			elif "deadline" in event.event_type:
				income_time = self.time_of_next_income()
				if event.bill.hard_deadline < income_time:
					amount_payed, remained_debt = event.bill.pay_debt(self.money)
					self.money -= amount_payed
					assert(self.money >= 0)
					if remained_debt > 0:
						self.alert = True
				else:
					amount_payed, remained_debt = event.bill.pay_debt(min(event.bill.card.minimum_paying_first, self.money))
					self.money -= amount_payed
					candidates = [event.bill]
					temp_money = self.money
					for temp_event in self.events:
						if "income" in temp_event.event_type:
							break
						elif "release" in temp_event.event_type:
							continue
						elif "hard" in temp_event.event_type:
							temp_money -= temp_event.bill.debt
							if temp_money < 0:
								self.alert = True
								break
						elif "deadline" in temp_event.event_type:
							if temp_event.bill.hard_deadline >= income_time:
								candidates.append(temp_event.bill)
						else:
							assert(False)
					if not self.alert:
						temp_money -= sum([candidate.card.minimum_paying_first for candidate in candidates])
						temp_money += event.bill.card.minimum_paying_first
						if temp_money < 0:
							self.alert = True
						else:
							candidates.sort(key=lambda x : x.card.penalty_percent, reverse=True)
							for candidate in candidates:
								if candidate is event.bill:
									amount_payed, remained_debt = event.bill.pay_debt(temp_money)
									self.money -= amount_payed
									assert(self.money >= 0)
									break
								else:
									temp_money -= candidate.debt - candidate.card.minimum_paying_first
									if temp_money < 0:
										self.alert = True
										break
				event.bill.pass_deadline()
			else:
				assert(False)