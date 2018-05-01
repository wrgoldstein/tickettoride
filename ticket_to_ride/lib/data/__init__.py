import os
import csv
from ..route import Route
from ..ticket import Ticket

routes = []
with open(os.path.dirname(__file__) + '/routes.csv', 'r') as f:
    csv_reader = csv.reader(f)
    next(csv_reader, None)
    for row in csv_reader:
        route = Route(*row)
        routes.append(route)

cities = sorted(set(sum([[r.from_city, r.to_city] for r in routes],[])))

tickets = []
with open(os.path.dirname(__file__) + '/tickets.csv', 'r') as f:
    csv_reader = csv.reader(f)
    next(csv_reader, None)
    for row in csv_reader:
        tickets.append(Ticket(*row))
