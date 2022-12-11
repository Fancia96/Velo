import json
import unittest
from assertpy import assert_that

from classes.statement import statement


class StatemetTest(unittest.TestCase):

    def setUp(self):
        with open('../data/Invoice.json', 'r') as f:
            self.invoice = json.load(f)

        with open('../data/Plays.json', 'r') as f:
            self.plays = json.load(f)

    def testAmountOfCreditsInstance(self):
        stmnt = statement(self.invoice, self.plays)
        print(stmnt)
        assert_that(stmnt).contains_ignoring_case("You earned 47 credits")

    def testAmountOfMoney(self):
        stmnt = statement(self.invoice, self.plays)
        print(stmnt)
        assert_that(stmnt).contains_ignoring_case("Amount owed is $1,730.00")

    def testException(self):
        self.invoice["performances"].append({"playID": "test", "audience": 15})
        self.plays['test'] = ({"name": "test", "type": "drama"})
        try:
            assert_that(statement(self.invoice, self.plays)).raises(ValueError)
        except ValueError:
            assert True

    def testAppendNewDataException(self):
        self.invoice["performances"].append({"playID": "test", "audience": 15})
        self.plays['test'] = ({"name": "test", "type": "comedy"})

        assert_that(statement(self.invoice, self.plays)).contains_ignoring_case("Amount owed is $2,075.00")

    def tearDown(self):
        self.invoice = None
        self.plays = None