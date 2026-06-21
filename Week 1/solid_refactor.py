class Report:
    def __init__(self, content):
        self.content = content
class ReportPrinter:
    def print_report(self, report):
        print(report.content)
report = Report("Monthly Sales Report")
printer = ReportPrinter()
printer.print_report(report)