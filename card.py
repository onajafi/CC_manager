class Card:

	def __init__(self, name, bill_period, bill_relative_deadline, minimum_paying_first, maximum_credit, penalty_percent, bill_relative_hard_deadline):
		self.name = name
		self.bill_period = bill_period
		self.bill_relative_deadline = bill_relative_deadline
		self.minimum_paying_first = minimum_paying_first
		self.maximum_credit = maximum_credit
		self.penalty_percent = penalty_percent
		self.bill_relative_hard_deadline = bill_relative_hard_deadline
		self.bills = []

	def release_bill(self, time, debt):
		if self.get_total_debt() + debt > self.maximum_credit:
			raise Exception("maximum credit error!")
		bill = Bill(self, time, debt)
		self.bills.append(bill)
		return bill

	def get_total_debt(self):
		return sum([bill.debt for bill in self.bills])


class Bill:
	def __init__(self, card, release_time, debt):
		self.card = card
		self.release_time = release_time
		self.deadline = release_time + card.bill_relative_deadline
		self.hard_deadline = release_time + card.bill_relative_hard_deadline
		self.debt = debt
		self.payed_amount = 0

	def pay_debt(self, paying_amount):
		if paying_amount > self.debt:
			return self.pay_debt(self.debt)
		else:
			self.debt -= paying_amount
			self.payed_amount += paying_amount
			return paying_amount, self.debt

	def add_penalty(self):
		self.debt *= (1 + self.card.penalty_percent / 100)

	def pass_hard_deadline(self):
		if self.debt != 0:
			raise Exception("deadline miss error!")
		self.card.bills.remove(self)
		
	def pass_deadline(self):
		if self.payed_amount < self.card.minimum_paying_first:
			raise Exception("deadline miss error!")
		self.add_penalty()