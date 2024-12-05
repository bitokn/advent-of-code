def main():
    with open("input5.txt", "r") as file:
        reading_rules = True
        rules = []
        while reading_rules:
            rule = file.readline()
            if "\n" == rule:
                reading_rules = False
            rules.append(rule.strip())

        rules.pop()
        reading_reports = True
        reports = []
        while reading_reports:
            report = file.readline()
            if "" == report:
                reading_reports = False
            reports.append(report.strip())

        reports.pop()
        sum = 0
        invalid_reports = []
        for report in reports:
            report = report.split(",")
            # print(report)
            report_valid = True
            for i, num in enumerate(report):
                before_rules = []
                after_rules = []
                for rule in rules:
                    if int(num) == int(rule[0:2]):
                        # print(f"{rule} rule is relevant (before rule)")
                        before_rules.append(int(rule[3:]))
                    if int(num) == int(rule[3:]):
                        # print(f"{rule} rule is relevant (after rule)")
                        after_rules.append(int(rule[0:2]))
                # print(before_rules, after_rules)
                for j in range(i + 1, len(report)):
                    if int(report[j]) in before_rules:
                        # print("we found a rule that lets us keep going")
                        pass
                    else:
                        # print(f"{report[j]} report invalid")
                        report_valid = False
                        break
                # print(f"{i} number in report {report} valid")
            if report_valid:
                # print(f"report {report} valid")
                middlenumber = report[((len(report) + 1) // 2) - 1]
                # print(middlenumber)
                sum += int(middlenumber)
            else:
                invalid_reports.append(report)
        sum2 = 0
        for invalid_report in invalid_reports:
            store = []
            for k in range(len(invalid_report)):
                if k != 0:
                    store.insert(0, invalid_report.pop())

                for i, num in enumerate(invalid_report):
                    before_rules = []
                    after_rules = []
                    for rule in rules:
                        if int(num) == int(rule[0:2]):
                            # print(f"{rule} rule is relevant (before rule)")
                            before_rules.append(int(rule[3:]))
                        if int(num) == int(rule[3:]):
                            # print(f"{rule} rule is relevant (after rule)")
                            after_rules.append(int(rule[0:2]))
                    print(before_rules, after_rules)
                    for j in range(i + 1, len(invalid_report)):
                        if int(invalid_report[j]) in before_rules:
                            # print("we found a rule that lets us keep going")
                            pass
                        elif int(invalid_report[j]) in after_rules:
                            print(f"number {invalid_report[j]} is in the wrong spot")
                            temp = invalid_report[i]
                            invalid_report[i] = invalid_report[j]
                            invalid_report[j] = temp

            print(f"fixed report {invalid_report}")
            print(store)

            gurbaksdjhfasl = invalid_report + store

            print(invalid_report + store)

            middlenumber2 = gurbaksdjhfasl[((len(gurbaksdjhfasl) + 1) // 2) - 1]
            # print(middlenumber2)
            sum2 += int(middlenumber2)

        print(sum)
        print(sum2)
        print("done")


main()
