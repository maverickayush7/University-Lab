class Company:
    def __init__(self, companyName, turnover, revenue, noOfEmployees):
        self.companyName = companyName
        self.turnover = turnover
        self.revenue = revenue
        self.noOfEmployees = noOfEmployees

    def getProductivity(self):
        productivity = self.revenue / self.noOfEmployees
        return productivity


company = Company("MED",2000,5000,5)

print("productivity:" , company.getProductivity())